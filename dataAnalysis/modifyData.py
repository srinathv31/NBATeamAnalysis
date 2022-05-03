import pandas as pd
from datetime import datetime

def grabTeamWinsPerMonth():
    df_team_data = pd.read_json('../collectedData/allTeamData.json')
    df_schedule = pd.DataFrame(df_team_data["LOS ANGELES LAKERS"][2001]["Schedule"]["games"])
    
    # Turn string dates (Wed, Nov 15, 2000) from schedule into datetime objects (2000-11-15) to compare time
    date_str_list = []
    for i in df_schedule.items():
        date_str_list.append(f'{i[1]["Date"]}')
        i[1]["Date"] = datetime.strptime(f'{i[1]["Date"]}', '%a, %b %d, %Y')

    # Add total number of wins/losses per month into object:
    # {
    #   'Month#': { W: #, L: # }
    # }
    month_win_totals = {}
    for i in df_schedule.items():
        try:
            month_win_totals[i[1]["Date"].month][i[1]["Result"]] += 1
        except KeyError:
            month_win_totals[i[1]["Date"].month] = { 'W': 0, 'L': 0 } 
            month_win_totals[i[1]["Date"].month][i[1]["Result"]] = 1

    # Append each month (with total wins/losses) into a list of months (month_df)
    month_df = []
    for i in month_win_totals.items():
        game_entry = {
            'month': i[0],
            'W': i[1]['W'],
            'L': i[1]['L'],
        }
        month_df.append(game_entry)

    # Convert month_df into a Dataframe:
    #   month  W  L
    # 0    10  1  0
    # 1    11 10  5
    # ...
    print(pd.DataFrame(month_df))
    return(pd.DataFrame(month_df))

if __name__ == '__main__':
    grabTeamWinsPerMonth()
