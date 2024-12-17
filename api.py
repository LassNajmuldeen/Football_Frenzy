import requests

BASE_URL = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api"

def fetch_seasons():
    """Fetch available seasons from the API."""
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        data = response.json()
        return data.get("seasons", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching seasons: {e}")
        return []

def fetch_gamedays(year):
    """Fetch gamedays for a given season."""
    try:
        response = requests.get(f"{BASE_URL}/{year}")
        response.raise_for_status()
        data = response.json()
        return data.get("gamedays", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching gamedays for year {year}: {e}")
        return []

def fetch_games_for_gameday(year, gameday):
    """Fetch games for a specific gameday in a season."""
    try:
        response = requests.get(f"{BASE_URL}/{year}/{gameday}")
        response.raise_for_status()
        data = response.json()
        return data.get("games", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching games for gameday {gameday} in {year}: {e}")
        return []