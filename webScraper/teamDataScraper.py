'''
Srinath Venkatesh
'''

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
from webScraper.teamDataInitializers import generateTeamURLs, generateInitTeamDataObject
from webScraper.pageScrapers import rosterPageScraper, schedulePageScraper
from multiprocessing import Pool
import json

'''
generateURLRequest() - Used to scrape data from the URLs
parameters:
    teamUrl - Used to access the [year] Team's roster and W/L schedule
    {
        "year": number,
        "roster_url": URL,
        "schedule_url": URL,
        "team_key": string
    }
return:
    team_season_data - an object that contains { "team_key", "year", "data" } to add to the master dictionary
'''
def generateURLRequest(teamUrl):
    rosterPageRequest = requests.get(teamUrl["roster_url"])
    rosterPageSoup = BeautifulSoup(rosterPageRequest.content, "html.parser")
    roster_stats = rosterPageScraper(rosterPageSoup)
    
    schedulePageRequest = requests.get(teamUrl["schedule_url"])
    schedulePageSoup = BeautifulSoup(schedulePageRequest.content, "html.parser")
    schedule_stats = schedulePageScraper(schedulePageSoup, teamUrl["team_key"])

    team_season_data = {
        'team_key': teamUrl["team_key"],
        'year': teamUrl["year"],
        'data': {
            'Roster': {
                'url': f'{teamUrl["roster_url"]}'
            },
            'Schedule': {
                'url': f'{teamUrl["roster_url"]}'
            }
        }
    }

    team_season_data["data"]["Roster"]["players"] = roster_stats
    team_season_data["data"]["Schedule"]["games"] = schedule_stats

    print(f'{teamUrl["team_key"]}: {teamUrl["year"]}')
    return (team_season_data)

'''
main() - Scrape NBA Team Data from 1977 (Post NBA-ABA merger) to 2022 including every team's roster and W/L schedule
return:
    The data will be used to find coorelations between weather and team performance.
    More studies will be done with this data.
'''
def main():
    # Initialize master dictionary
    all_team_data = generateInitTeamDataObject()

    # Create URLs
    team_list = ["ATLANTA HAWKS", "BOSTON CELTICS", "BROOKLYN NETS", "CHARLOTTE HORNETS", "CHICAGO BULLS", "CLEVELAND CAVALIERS", "DALLAS MAVERICKS", "DENVER NUGGETS", "DETROIT PISTONS", "GOLDEN STATE WARRIORS", "HOUSTON ROCKETS", "INDIANA PACERS", "LOS ANGELES CLIPPERS", "LOS ANGELES LAKERS", "MEMPHIS GRIZZLIES", "MIAMI HEAT", "MILWAUKEE BUCKS", "MINNESOTA TIMBERWOLVES", "NEW ORLEANS PELICANS", "NEW YORK KNICKS", "OKLAHOMA CITY THUNDER", "ORLANDO MAGIC", "PHILADELPHIA 76ERS", "PHOENIX SUNS", "PORTLAND TRAIL BLAZERS", "SACRAMENTO KINGS", "SAN ANTONIO SPURS", "TORONTO RAPTORS", "UTAH JAZZ", "WASHINGTON WIZARDS"]
    team_abv_list = ["ATL", "BOS", "BRK", "CHO", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]
    all_team_urls = np.array([])
    for abv, full_name in zip(team_abv_list, team_list):
        all_team_urls = np.append(all_team_urls, generateTeamURLs(abv, full_name))

    # Run the scraping function with multiprocessing and store return values into a list (results[])
    results = []
    p = Pool(10)  # Pool tells how many at a time
    results.append(p.map(generateURLRequest, all_team_urls))
    p.terminate()
    p.join()

    # Since multiprocessing doesn't share memory, grab each return value from results[] and add it to
    # the all_team_data (master dictionary) given the Team (team_key) and Team's Year ("year")
    for i in results:
        for j in i:
            all_team_data[j["team_key"]][j["year"]] = j["data"]

    # Print out each team object's values length to double check for any missing data
    # (Not all teams have 46 seasons worth of data)
    for key, value in all_team_data.items(): print(key, len(value), sep=" | ")

    df_master = pd.DataFrame(all_team_data)
    df_master.to_csv("../collectedData/allTeamData.csv", encoding="utf-8", index_label="index")
    with open("../collectedData/allTeamData.json", "w+") as f:
        json.dump(df_master.to_dict(), f)

if __name__=="__main__":
    main()
