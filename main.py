import requests, argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument(
    '--id',
    '-id',
    default = 2730,
    help = 'enter the series id/match id'
)

args = parser.parse_args()

url = "https://dev132-cricket-live-scores-v1.p.rapidapi.com/matchseries.php"
id = args.id
querystring = {"seriesid": id}
headers = {
    'x-rapidapi-key': "3f002d2a37mshbd5ff13d303a772p114fe9jsn3c632d48eeef",
    'x-rapidapi-host': "dev132-cricket-live-scores-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.txt)
matches = data['matchList']
print(matches)

#print(response.text)

#id = 49839, 2730