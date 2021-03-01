import requests, argparse
import json
import telebot
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 


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

data = json.loads(response.text)
#matches = data['matchList']
#print(type(data['matches']))

for match in data['matchList']['matches']:
    if match['id'] == 49840:
        venue = match['venue']['name']
        status = match['status']
        summary = match['currentMatchState']
        score = match['scores']
        break

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1546857499:AAG_aFZeRhR-bLibgdTwCgLzQDZ9NriQoVI'
    bot_chatID = '1081769492'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

test = telegram_bot_sendtext(venue)
print(test)


"""api_id = '3664885'
api_hash = '597eb2483c1e172e8e52d40461444f40'
token = '1546857499:AAG_aFZeRhR-bLibgdTwCgLzQDZ9NriQoVI'

phone = '+919886882121'

client = TelegramClient('session', api_id, api_hash)

client.connect() 

if not client.is_user_authorized(): 
   
    client.send_code_request(phone) 
      
    # signing in the client 
    client.sign_in(phone, input('Enter the code: ')) 

try: 
    # receiver user_id and access_hash, use 
    # my user_id and access_hash for reference 
    receiver = InputPeerUser('user_id', 'user_hash') 
  
    # sending message using telegram client 
    client.send_message(receiver, message = venue, parse_mode='html') 
except Exception as e: 
      
    # there may be many error coming in while like peer 
    # error, wwrong access_hash, flood_error, etc 
    print(e)
  
# disconnecting the telegram session  
client.disconnect() 
"""



"""print(venue)
print(status)
print(summary)
for i in score:
    print(i + ": " + score[i])
        
#print(response.text)

#id = 49839, 2730"""