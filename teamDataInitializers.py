'''
Srinath Venkatesh
'''

import numpy as np

'''
generateTeamURLs() - Used to generate all working URLs, primarily made to practice using 'match-case'
parameters:
    team - team abv ie. ATL, NYK, BOS, etc. for URL
    full_team_name - used as a key for each URL object to easily write data from the URL to local dictionary variable
return:
    team_urls - list of all URLs needed to scrape the necessary data (listOfAllURLs.csv)
'''
def generateTeamURLs(team, full_team_name):
    team_urls = np.array([])
    
    match team:
        case "BRK":
            team_url = {
                "year": 1977,
                "roster_url": 'https://www.basketball-reference.com/teams/NYN/1977.html',
                "schedule_url": 'https://www.basketball-reference.com/teams/NYN/1977_games.html',
                "team_key": full_team_name
            }
            team_urls = np.append(team_urls, team_url)
            for j in range(1978, 2013):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/NJN/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/NJN/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
            for j in range(2013, 2023):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/{team}/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/{team}/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
        case "LAC":
            for j in range(1977, 1979):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/BUF/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/BUF/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
            for j in range(1979, 1985):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/SDC/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/SDC/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
            for j in range(1985, 2023):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/{team}/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/{team}/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
        case "MEM":
            for j in range(1996, 2002):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/VAN/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/VAN/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
            for j in range(2002, 2023):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/{team}/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/{team}/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
        case "NOP":
            for j in range(2003, 2006):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/NOH/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/NOH/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
            for j in range(2006, 2008):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/NOK/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/NOK/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
            for j in range(2008, 2014):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/NOH/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/NOH/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
            for j in range(2014, 2023):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/{team}/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/{team}/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
        case "OKC":
            for j in range(1977, 2009):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/SEA/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/SEA/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
            for j in range(2009, 2023):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/{team}/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/{team}/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
        case "SAC":
            for j in range(1977, 1986):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/KCK/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/KCK/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
            for j in range(1986, 2023):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/{team}/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/{team}/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
        case "UTA":
            for j in range(1977, 1980):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/NOJ/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/NOJ/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
            for j in range(1980, 2023):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/{team}/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/{team}/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
        case "WAS":
            for j in range(1977, 1998):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/WSB/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/WSB/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
            for j in range(1998, 2023):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/{team}/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/{team}/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
        case "TOR":
            for j in range(1996, 2023):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/{team}/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/{team}/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
        case "CHO":
            for j in range(1996, 2003):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/CHH/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/CHH/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
            for j in range(2005, 2015):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/CHA/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/CHA/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
            for j in range(2015, 2023):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/{team}/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/{team}/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
        case "MIN" | "ORL":
            for j in range(1990, 2023):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/{team}/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/{team}/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
        case "DAL":
            for j in range(1981, 2023):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/{team}/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/{team}/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
        case "MIA":
            for j in range(1989, 2023):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/{team}/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/{team}/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
        case _:
            for j in range(1977, 2023):
                team_url = {
                    "year": j,
                    "roster_url": f'https://www.basketball-reference.com/teams/{team}/{j}.html',
                    "schedule_url": f'https://www.basketball-reference.com/teams/{team}/{j}_games.html',
                    "team_key": full_team_name
                }
                team_urls = np.append(team_urls, team_url)
    return team_urls

# def generateTeamURLs(team, full_team_name):
#     team_urls = np.array([])
    
#     for j in range(1977, 2023):
#                 team_url = {
#                     "year": j,
#                     "roster_url": f'https://www.basketball-reference.com/teams/{team}/{j}.html',
#                     "schedule_url": f'https://www.basketball-reference.com/teams/{team}/{j}_games.html',
#                     "team_key": full_team_name
#                 }
#                 team_urls = np.append(team_urls, team_url)
#     return team_urls

'''
generateInitTeamDataObject() - Used to initialize the master dictionary to store the scraped data into
return:
    all_data - a dictionary with each key being the full name of a NBA Franchise
'''
def generateInitTeamDataObject():
    team_list = ["ATLANTA HAWKS", "BOSTON CELTICS", "BROOKLYN NETS", "CHARLOTTE HORNETS", "CHICAGO BULLS", "CLEVELAND CAVALIERS", "DALLAS MAVERICKS", "DENVER NUGGETS", "DETROIT PISTONS", "GOLDEN STATE WARRIORS", "HOUSTON ROCKETS", "INDIANA PACERS", "LOS ANGELES CLIPPERS", "LOS ANGELES LAKERS", "MEMPHIS GRIZZLIES", "MIAMI HEAT", "MILWAUKEE BUCKS", "MINNESOTA TIMBERWOLVES", "NEW ORLEANS PELICANS", "NEW YORK KNICKS", "OKLAHOMA CITY THUNDER", "ORLANDO MAGIC", "PHILADELPHIA 76ERS", "PHOENIX SUNS", "PORTLAND TRAIL BLAZERS", "SACRAMENTO KINGS", "SAN ANTONIO SPURS", "TORONTO RAPTORS", "UTAH JAZZ", "WASHINGTON WIZARDS"]
    all_data = {}
    for i in team_list:
        all_data[f'{i}'] = {}
    return all_data

if __name__ == '__main__':
    generateTeamURLs()
