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
main()