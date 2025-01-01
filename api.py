import requests

BASE_URL = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api"

def fetch_seasons():
    """
    Fetch available seasons from the API.
    Returns:
        list: A list of available seasons.
    """
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        data = response.json()
        return data.get("seasons", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching seasons: {e}")
        return []

def fetch_gamedays(year):
    """
    Fetch all gamedays for a given year.
    Args:
        year (str): The year to fetch gamedays for.
    Returns:
        list: A list of gamedays.
    """
    try:
        response = requests.get(f"{BASE_URL}/{year}")
        response.raise_for_status()
        data = response.json()
        return data.get("gamedays", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching gamedays for year {year}: {e}")
        return []

def fetch_games_for_gameday(year, gameday):
    """
    Fetch games for a specific gameday in the given year.
    Args:
        year (str): The year of the season.
        gameday (str): The gameday date (e.g., "2000/03/19").
    Returns:
        list: A list of games played on the gameday.
    """
    try:
        response = requests.get(f"{BASE_URL}/{year}/{gameday}")
        response.raise_for_status()
        data = response.json()
        return data.get("games", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching games for gameday {gameday}: {e}")
        return []
