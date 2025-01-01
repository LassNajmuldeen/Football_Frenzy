from api import fetch_seasons, fetch_gamedays, fetch_games_for_gameday

def main():
    print("STAT EXPLORER")
    print("*************\n")

    # Fetch and display available seasons
    seasons = fetch_seasons()
    if not seasons:
        print("No available seasons found. Exiting.")
        return
    print(f"Available seasons: {seasons[0]}-{seasons[-1]}")

    # User input for year
    year = input("Enter year: ").strip()
    if year not in seasons:
        print(f"Invalid year. Please choose a year between {seasons[0]} and {seasons[-1]}.")
        return

    # Fetch gamedays for the selected year
    gamedays = fetch_gamedays(year)
    if not gamedays:
        print(f"No gamedays found for year {year}. Exiting.")
        return

    # User input for scores
    try:
        home_score = int(input("Home score: ").strip())
        away_score = int(input("Away score: ").strip())
    except ValueError:
        print("Invalid score input. Please enter integers.")
        return

    print("\n" + "-" * 53 + "\n")

    # Fetch and filter games
    matching_games = []
    for gameday in gamedays:
        games = fetch_games_for_gameday(year, gameday)
        for game in games:
            home_team = game.get("home", {}).get("team")
            away_team = game.get("away", {}).get("team")
            home_goals = game.get("home", {}).get("goals")
            away_goals = game.get("away", {}).get("goals")

            if home_goals == home_score and away_goals == away_score:
                matching_games.append((gameday, home_team, away_team))

    # Display results
    if matching_games:
        for gameday, home_team, away_team in matching_games:
            game_date = gameday.split("/")[-1]  # Extract date part
            print(f"[{game_date}]  ({home_score})  {home_team.center(15)}- {away_team.center(15)}({away_score})")
    else:
        print("No games found with the specified scores.")

    print("\n" + "-" * 53)


main()