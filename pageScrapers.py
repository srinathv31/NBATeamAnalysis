'''
Srinath Venkatesh 4/28/2022
'''

def rosterPageScraper(rosterPageSoup):
    rosterTable = rosterPageSoup.find("table", id="advanced")
    rosterList = rosterTable.find("tbody").find_all("tr")
    player_entries = {}
    for playerObj in rosterList:
        playerStats = playerObj.find_all("td")
        for i in playerStats:
            match i.get('data-stat'):
                case 'player':
                    playerName = i.text
                case 'g':
                    playerGP = i.text
                case 'per':
                    playerPER = i.text
                case 'ts_pct':
                    playerTS = i.text
                case 'ws':
                    playerWS = i.text
        player_entries = player_entries | ({
            f'{playerName}': {
                'G': playerGP,
                'PER': playerPER,
                'TS%': playerTS,
                'WS': playerWS,
            }
        })

    try:
        rosterTablePlayoffs = rosterPageSoup.find("table", id="playoffs_advanced")
        rosterListPlayoffs = rosterTablePlayoffs.find("tbody").find_all("tr")
        for playerObjPlayoffs in rosterListPlayoffs:
            playerStatsPlayoffs = playerObjPlayoffs.find_all("td")
            playerName = playerObjPlayoffs.find_next("td").text
            for j in playerStatsPlayoffs:
                match j.get('data-stat'):
                    case 'g':
                        player_entries[playerName]["P_G"] = j.text
                    case 'per':
                        player_entries[playerName]["P_PER"] = j.text
                    case 'ts_pct':
                        player_entries[playerName]["P_TS%"] = j.text
                    case 'ws':
                        player_entries[playerName]["P_WS"] = j.text
    except (AttributeError, KeyError) as e:
        try:
            player_entries[playerName].update({
                'P_G': "None",
                'P_PER': "None",
                'P_TS%': "None",
                'P_WS': "None",
            })
        except KeyError:
            print(playerName)
            print("WHO ARE YOU!")

    return player_entries

def schedulePageScraper(schedulePageSoup, team_name):
    try:
        regularSeasonGamesTable = schedulePageSoup.find("table", id="games").find_next("tbody")
        regularSeasonGameList = regularSeasonGamesTable.find_all("tr")

        game_entries = {}
        for game in regularSeasonGameList:
            if (game.find_next("th").text != 'G'):
                gameNumber = game.find_next("th").text
                gameDetails = game.find_all("td")
                for details in gameDetails:
                    match details.get('data-stat'):
                        case 'date_game':
                            gameDate = details.text
                        case 'game_start_time':
                            gameStart = details.text
                        case 'box_score_text':
                            gameBoxScore = "https://www.basketball-reference.com/"+details.find_next("a")['href']
                        case 'game_location':
                            gameLocation = details.find_next_sibling("td").text if details.text == "@" else team_name
                        case 'opp_name':
                            gameOpp = details.text
                        case 'game_result':
                            gameResult = details.text
                        case 'pts':
                            gamePtsFor = details.text
                        case 'opp_pts':
                            gamePtsOpp = details.text
                        case 'game_streak':
                            gameStreak = details.text
                        case 'wins':
                            gameWins = details.text
                        case 'losses':
                            gameLosses = details.text
            try:
                game_entries = game_entries | ({
                    f'{gameNumber}': {
                        'Date': gameDate,
                        'Start (ET)': gameStart,
                        'Box Score': gameBoxScore,
                        'Location': gameLocation,
                        'Opponent': gameOpp,
                        'Result': gameResult,
                        'PtsFor': gamePtsFor,
                        'PtsOpp': gamePtsOpp,
                        'W': gameWins,
                        'L': gameLosses,
                        'Streak': gameStreak
                    }
                })
            except UnboundLocalError:
                game_entries = game_entries | ({
                    f'{gameNumber}': {
                        'Date': gameDate,
                        'Start (ET)': "N/A",
                        'Box Score': gameBoxScore,
                        'Location': gameLocation,
                        'Opponent': gameOpp,
                        'Result': gameResult,
                        'PtsFor': gamePtsFor,
                        'PtsOpp': gamePtsOpp,
                        'W': gameWins,
                        'L': gameLosses,
                        'Streak': gameStreak
                    }
                })

        playoffGamesTable = schedulePageSoup.find("table", id="games_playoffs").find_next("tbody")
        playoffGameList = playoffGamesTable.find_all("tr")
        for game in playoffGameList:
            if (game.find_next("th").text != 'G'):
                    gameNumber = f'P_{game.find_next("th").text}'
                    gameDetails = game.find_all("td")
                    for details in gameDetails:
                        match details.get('data-stat'):
                            case 'date_game':
                                gameDate = details.text
                            case 'game_start_time':
                                gameStart = details.text
                            case 'box_score_text':
                                gameBoxScore = "https://www.basketball-reference.com/"+details.find_next("a")['href']
                            case 'game_location':
                                gameLocation = details.find_next_sibling("td").text if details.text == "@" else team_name
                            case 'opp_name':
                                gameOpp = details.text
                            case 'game_result':
                                gameResult = details.text
                            case 'pts':
                                gamePtsFor = details.text
                            case 'opp_pts':
                                gamePtsOpp = details.text
                            case 'game_streak':
                                gameStreak = details.text
                            case 'wins':
                                gameWins = details.text
                            case 'losses':
                                gameLosses = details.text
            try:
                game_entries = game_entries | ({
                    f'{gameNumber}': {
                        'Date': gameDate,
                        'Start (ET)': gameStart,
                        'Box Score': gameBoxScore,
                        'Location': gameLocation,
                        'Opponent': gameOpp,
                        'Result': gameResult,
                        'PtsFor': gamePtsFor,
                        'PtsOpp': gamePtsOpp,
                        'W': gameWins,
                        'L': gameLosses,
                        'Streak': gameStreak
                    }
                })
            except UnboundLocalError:
                game_entries = game_entries | ({
                    f'{gameNumber}': {
                        'Date': gameDate,
                        'Start (ET)': "N/A",
                        'Box Score': gameBoxScore,
                        'Location': gameLocation,
                        'Opponent': gameOpp,
                        'Result': gameResult,
                        'PtsFor': gamePtsFor,
                        'PtsOpp': gamePtsOpp,
                        'W': gameWins,
                        'L': gameLosses,
                        'Streak': gameStreak
                    }
                })
    except AttributeError:
        pass

    return game_entries

if __name__ == '__main__':
    rosterPageScraper()
