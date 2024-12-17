import requests

BASE_URL = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api"

def fetch_gamedays(year):
    """
    Fetch all gamedays for a given season.
    Args:
        year (str): The year of the season (e.g., '2006').
    Returns:
        list: A list of gameday dates if successful, otherwise None.
    """
    try:
        response = requests.get(f"{BASE_URL}/{year}")
        response.raise_for_status()
        data = response.json()
        return data.get("gamedays", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching gamedays for year {year}: {e}")
        return None

def fetch_games_for_gameday(year, gameday):
    """
    Fetch games for a specific gameday in a season.
    Args:
        year (str): The year of the season (e.g., '2006').
        gameday (str): The date of the gameday (e.g., '2006/03/19').
    Returns:
        list: A list of games if successful, otherwise None.
    """
    try:
        response = requests.get(f"{BASE_URL}/{year}/{gameday}")
        response.raise_for_status()
        data = response.json()
        return data.get("games", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching games for gameday {gameday} in {year}: {e}")
        return None