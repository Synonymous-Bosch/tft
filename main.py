import requests
from api_key import key


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

puuid = "fim3v7XndQ81afZ9hStzRoJKi-fNiYxZgmTw3PVpOvL_NajGErBPZIMCWAZm09ZvjSWu8gLTPEafeA"

match_data_url = "https://europe.api.riotgames.com/tft/match/v1/matches/by-puuid/" + puuid + "/ids?start=0&count=20"

account_data_url = "https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/Anonymous%20Bosch/euw"

headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept-Language": "en-GB,en;q=0.5",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    # "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": key
}

req = requests.get(account_data_url, headers=headers)

print(req.json())

