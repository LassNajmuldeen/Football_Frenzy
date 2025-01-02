import requests

URL = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api"

def list_seasons():
    """Fetch all available seasons."""
    response = requests.get(URL)
    data = response.json()
    return data['seasons']

def list_gamedays(year):
    """Fetch all games for a specific season."""
    response = requests.get(f"{URL}/{year}")
    return response.json()

def list_games(year, gameday):
    """Fetch all games for a specific gameday in a season."""
    response = requests.get(f"{URL}/{year}/{gameday}")
    return response.json()
