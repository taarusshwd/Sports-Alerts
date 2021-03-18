import requests
import json

url = "https://dev132-cricket-live-scores-v1.p.rapidapi.com/scorecards.php"

querystring = {"seriesid":"2141","matchid":"43431"}

headers = {
    'x-rapidapi-key': "3f002d2a37mshbd5ff13d303a772p114fe9jsn3c632d48eeef",
    'x-rapidapi-host': "dev132-cricket-live-scores-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)

batsmen = data["fullScorecardAwards"]["mostRunsAwardPlayerResults"][0]
bowler = data["fullScorecardAwards"]["mostWicketsAwardPlayerResults"][0]
manOfTheMatch = data["fullScorecardAwards"]["manOfTheMatchName"]
#batsmenOfTheMatch = data["fullScorecardAwards"]["mosRunsAward"]["name"]

print(batsmen["name"])
print(bowler["name"])
print(manOfTheMatch)