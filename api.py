import requests

BASE_URL = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com"

def fetch_games(year: int):
    """
    Fetch all games for a given year from the Football Frenzy API.

    Args:
        year (int): The year to fetch games for.

    Returns:
        list: A list of games if the request is successful, otherwise None.
    """
    url = f"{BASE_URL}/games/{year}.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching games for {year}: {e}")
        return None