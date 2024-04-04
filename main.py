from helpers.api_calls import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


username = input("Input Riot username: ")

tagline = input("Input user region: ")


account_data = get_account_data(username, tagline)

puuid = account_data["puuid"]

number_of_matches = 0

print(puuid)

while number_of_matches <= 0:
    number_of_matches = input("Please input number of matches: ")
    if not isinstance(number_of_matches, int):
        number_of_matches = 20


matches = get_match_data(puuid, number_of_matches)

# todo - iterate through list of matches to present match data
