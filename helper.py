import requests
import urllib.parse
import json
import telebot
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 


def validMessage(message):
    return urllib.parse.quote_plus(message)


def generateMessageData(args):
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


def sendMessage(bot_message):
    
    bot_token = '1546857499:AAG_aFZeRhR-bLibgdTwCgLzQDZ9NriQoVI'
    bot_chatID = '1081769492'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def trialMatch3rdT20(args):
    url = "https://dev132-cricket-live-scores-v1.p.rapidapi.com/match.php"
    seriesId = args.seriesId
    matchId = args.matchId
    querystring = {"seriesid":seriesId,"matchid":matchId}
    headers = {
    'x-rapidapi-key': "3f002d2a37mshbd5ff13d303a772p114fe9jsn3c632d48eeef",
    'x-rapidapi-host': "dev132-cricket-live-scores-v1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    data = json.loads(response.text)

    summary = data['match']['matchSummaryText']

    return summary