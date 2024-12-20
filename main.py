from api import fetch_seasons, fetch_gamedays, fetch_games_for_gameday

def main():
    print("STAT EXPLORER")
    print("*************\n")

    # Fetch available seasons
    seasons = fetch_seasons()
    if not seasons:
        print("No available seasons found. Exiting.")
        return

    # User input: Year
    print("Available seasons:", ", ".join(seasons))
    year = input("Enter year: ").strip()
    if year not in seasons:
        print(f"Invalid year. Choose from: {', '.join(seasons)}")
        return

    # Fetch gamedays for the year
    gamedays = fetch_gamedays(year)
    if not gamedays:
        print(f"No gamedays found for year {year}. Exiting.")
        return

    # User input: Scores
    try:
        home_score = int(input("Home score: ").strip())
        away_score = int(input("Away score: ").strip())
    except ValueError:
        print("Invalid scores. Please enter integers.")
        return

main()