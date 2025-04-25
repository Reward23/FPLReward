import requests

FPL_BOOTSTRAP_URL = "https://fantasy.premierleague.com/api/bootstrap-static/"
FPL_TEAM_URL_TEMPLATE = "https://fantasy.premierleague.com/api/entry/{fpl_id}/event/{gw}/picks/"

def fetch_bootstrap_data():
    response = requests.get(FPL_BOOTSTRAP_URL)
    response.raise_for_status()
    return response.json()

def fetch_team_picks(fpl_id, gw):
    url = FPL_TEAM_URL_TEMPLATE.format(fpl_id=fpl_id, gw=gw)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()