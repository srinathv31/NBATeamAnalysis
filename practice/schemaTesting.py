'''
Srinath Venkatesh

This file was used only to "TEST" python functions and potential data schema.

NOT USED IN PRODUCTION
'''

from random import randint, random
import pandas as pd
import numpy as np
from webScraper.teamDataInitializers import generateTeamURLs

team_list = ["ATLANTA HAWKS", "BOSTON CELTICS", "BROOKLYN NETS", "CHARLOTTE HORNETS", "CHICAGO BULLS", "CLEVELAND CAVALIERS", "DALLAS MAVERICKS", "DENVER NUGGETS", "DETROIT PISTONS", "GOLDEN STATE WARRIORS", "HOUSTON ROCKETS", "INDIANA PACERS", "LOS ANGELES CLIPPERS", "LOS ANGELES LAKERS", "MEMPHIS GRIZZLIES", "MIAMI HEAT", "MILWAUKEE BUCKS", "MINNESOTA TIMBERWOLVES", "NEW ORLEANS PELICANS", "NEW YORK KNICKS", "OKLAHOMA CITY THUNDER", "ORLANDO MAGIC", "PHILADELPHIA 76ERS", "PHOENIX SUNS", "PORTLAND TRAIL BLAZERS", "SACRAMENTO KINGS", "SAN ANTONIO SPURS", "TORONTO RAPTORS", "UTAH JAZZ", "WASHINGTON WIZARDS"]

url_big = generateTeamURLs("TOR", "TORONTO RAPTORS")
df_url = pd.DataFrame(d for d in url_big)
df_url.to_csv("gobblyGuuid.csv", encoding="utf-8", index_label="index")


all_data = {}
for i in team_list:
    all_data[f'{i}'] = {
        "TeamYr": {
            "Players": [
                {"John": {
                    "ws": round(randint(1,10)+random(), 2),
                    "playoffs_ws": round(randint(1,10)+random(), 2)
                }},
                {"Barry": {
                    "ws": round(randint(1,10)+random(), 2),
                    "playoffs_ws": round(randint(1,10)+random(), 2)
                }}
            ],
            "Schedule": [
                {
                    "date": "Fri, Dec 14, 2007",
                    "outcome": "W",
                    "opponent": "Lakers",
                    "margin": "4",
                    "playoff_status": False,
                    "location": "Los Angeles"
                },
                {
                    "date": "Sat, Dec 15, 2007",
                    "outcome": "W",
                    "opponent": "Bulls",
                    "margin": "14",
                    "playoff_status": False,
                    "location": "Chicago"
                },
                {
                    "date": "Wed, May 16, 2007",
                    "outcome": "L",
                    "opponent": "Knicks",
                    "margin": "-2",
                    "playoff_status": True,
                    "location": "Boston"
                }
            ],
        }
    }

all_data["BOSTON CELTICS"]["TeamYr"]["Players"].append({ "Bird": { "ws": round(randint(1,10)+random(), 2), "playoffs_ws": round(randint(1,10)+random(), 2) }})
all_data["BOSTON CELTICS"]["TeamYr"]["Schedule"].append({
                    "date": "Fri, May 18, 2007",
                    "outcome": "W",
                    "opponent": "Knicks",
                    "margin": "5",
                    "playoff_status": True,
                    "location": "New York"
                })

df = pd.DataFrame(all_data)

# Grabbing Roster in csv format
roster_tmp = np.array([])
for i in df["BOSTON CELTICS"]["TeamYr"]["Players"]:
    for j in i.items():
        roster_tmp = np.append(roster_tmp, { "name": j[0], "ws": j[1]["ws"], "playoffs_ws": j[1]["playoffs_ws"]})
roster_df = pd.DataFrame(d for d in roster_tmp)
roster_df.to_csv("../testData/testingRoster.csv", encoding="utf-8", index_label="index")

# Grabbing Schedule in csv format
sch_tmp = np.array([])
for i in df["BOSTON CELTICS"]["TeamYr"]["Schedule"]:
    sch_tmp = np.append(sch_tmp, { "date": i["date"], "outcome": i["outcome"], "opponent": i["opponent"], "margin": i["margin"], "playoff_status": i["playoff_status"], "location": i["location"]})

sch_df = pd.DataFrame(d for d in sch_tmp)
sch_df.to_csv("../testData/testingSch.csv", encoding="utf-8", index_label="game_number")

df.to_json("testingFormat.json")
