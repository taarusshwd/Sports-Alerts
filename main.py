import requests, argparse
import json
import telebot
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 
import time


parser = argparse.ArgumentParser()
parser.add_argument(
    '--id',
    '-id',
    default = 2730,
    help = 'enter the series id/match id'
)
args = parser.parse_args()


def generate_message_data():
    url = "https://dev132-cricket-live-scores-v1.p.rapidapi.com/matchseries.php"
    id = args.id
    querystring = {"seriesid": id}
    headers = {
        'x-rapidapi-key': "3f002d2a37mshbd5ff13d303a772p114fe9jsn3c632d48eeef",
        'x-rapidapi-host': "dev132-cricket-live-scores-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)

    for match in data['matchList']['matches']:
        if match['id'] == 49840:
            venue = match['venue']['name']
            status = match['status']
            summary = match['currentMatchState']
            score = match['scores']
            break

    return venue, status, summary, score


def getScores(scores):
    message = ""
    for score in scores:
        message = message + score + ": " + scores[score] + '\n'
    
    return message


def telegram_bot_sendtext(bot_message):
    
    bot_token = '1546857499:AAG_aFZeRhR-bLibgdTwCgLzQDZ9NriQoVI'
    bot_chatID = '1081769492'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()



while(True):
    time.sleep(5)
    venue, status, summary, scores = generate_message_data()
    test = telegram_bot_sendtext(venue)
    time.sleep(1)
    test = telegram_bot_sendtext(status)
    time.sleep(1)
    test = telegram_bot_sendtext(summary)
    time.sleep(1)
    #message = getScores(scores)
    test = telegram_bot_sendtext("homeScore: 145 and 0-49 homeOvers: 53.2 and 7.4 awayScore: 112 and 81 awayOvers: 48.4 and 30.4")
    time.sleep(5)




#print(test)


"""venue, status, summary, scores = generate_message_data()
print(venue)
print(status)
print(summary)
print(getScores(scores))
for i in scores:
    print(i + ": " + scores[i])
"""      
#print(response.text)

#id = 49839, 2730

#1 Print scores
#2 Isolate the functions; this main.py should call other functions
#3 make another function to send the notifs: shouldn't be happening in while loop
#4 more functionalities
