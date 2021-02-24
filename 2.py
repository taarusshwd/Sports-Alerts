import requests

url = "https://dev132-cricket-live-scores-v1.p.rapidapi.com/matchdetail.php"

querystring = {"seriesid":"2730","matchid":"49839"}

headers = {
    'x-rapidapi-key': "3f002d2a37mshbd5ff13d303a772p114fe9jsn3c632d48eeef",
    'x-rapidapi-host': "dev132-cricket-live-scores-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)