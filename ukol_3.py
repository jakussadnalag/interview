import urllib.request as requests
import re


def scrape_results():
    url = "https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089"
    response = requests.urlopen(url).read().decode('utf-8')

    pattern = re.compile(r'"@type":"SportsEvent",.*?"name":"(.*?)",.*?'
                         r'<div class="datetime-container">(.*?)</div>.*?'
                         r'<div class="score">(.*?)</div>', re.DOTALL)
    matches = re.findall(pattern, response)

    results = []
    for match in matches:
        home_team, away_team = match[0].strip().split(" vs. ")
        date_time = re.sub('[^0-9.: ]+', '', match[1]).split(' ')
        score = re.sub('[^0-9:]', "", match[2].strip()).split(':')
        results.append((date_time, home_team, away_team, score))
    return results


def filter_winning_matches(my_team, matches):
    matches_won = []
    for date_time, home_team, away_team, score in matches:
        if home_team == my_team and score[0] > score[1]:
            matches_won.append((date_time[0], away_team))
        elif away_team == my_team and score[0] < score[1]:
            matches_won.append((date_time[0], home_team))
    return matches_won


# Test the functions
favorite_team = "Brno"  # Replace with your favorite team's name

all_matches = scrape_results()
winning_matches = filter_winning_matches(favorite_team, all_matches)

for date, opponent in winning_matches:
    print(f"{date} jsme porazili {opponent}")
