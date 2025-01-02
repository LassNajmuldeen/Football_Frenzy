import api
from api import list_seasons, list_gamedays, list_games


def main():
    print("STAT EXPLORER")
    print("*************")

    # Take user input
    year = str(input("Enter year: "))
    if year not in api.list_seasons():
        print('Year is not available')
        return
    home_score = int(input("Home score: "))
    away_score = int(input("Away score: "))

    # Fetch all data for the given season
    season_data = list_gamedays(year)

    # List to store games that match the criteria
    games = []

    # Iterate through each gameday and extract games with the required score
    for gameday in season_data['gamedays']:
        gameday_data = list_games(year, gameday)
        for game in gameday_data['games']:
            # Check if the game score matches the user's input
            if game['score']['home']['goals'] == home_score and  game['score']['away']['goals'] == away_score:
                date = gameday_data['date']
                home_team = game['score']['home']['team']
                away_team = game['score']['home']['team']
                games.append(f"[{date}]  ({home_score}) {home_team} - {away_team} ({away_score})")

    # Display the results
    if games:
        print("\n-----------------------------------------------------")
        for game in games:
            print(game)
    else:
        print("No games found with the specified score.")


if __name__ == "__main__":
    main()
