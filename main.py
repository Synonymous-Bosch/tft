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

print(account_data)

puuid = account_data["puuid"]

number_of_matches = 0

print(puuid)

while number_of_matches <= 0:
    try:
        number_of_matches = int(input("Please input number of matches: "))
    except ValueError:
        print("not a number")
    if number_of_matches > 0:
        break


matches = get_match_data(puuid, number_of_matches)

print(matches)

# todo - iterate through list of matches to present match data
match_details_list = []

for match in matches:
    match_details_list.append(get_match_details(match))

for match in match_details_list:
    print(match['metadata']['participants'])


