import requests
from api_key import key


# username = input("input username: ")

account_data_url = f'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'

headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept-Language": "en-GB,en;q=0.5",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    # "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": key
}

# req = requests.get(account_data_url, headers=headers)


def get_account_data(username, tagline):
    try:
        r = requests.get(account_data_url+f'{username}/{tagline}', headers=headers)
    except requests.exceptions.RequestException as err:
        return repr(err)
    else:
        return r.json()

# puuid = account_data["puuid"]


match_data_url = f'https://europe.api.riotgames.com/tft/match/v1/matches/by-puuid/'

match_details_url = "https://europe.api.riotgames.com/tft/match/v1/matches/"


def get_match_data(puuid, number_of_games):
    try:
        r = requests.get(f'{match_data_url}{puuid}/ids?start=0&count={number_of_games}', headers=headers)
    except requests.exceptions.RequestException as err:
        return repr(err)
    else:
        return r.json()


def get_match_details(match_id):
    try:
        r = requests.get(f'{match_details_url}{match_id}', headers=headers)
    except requests.exceptions.RequestException as err:
        return repr(err)
    else:
        return r.json()

