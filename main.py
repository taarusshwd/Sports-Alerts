import argparse 
import time
from helper import validMessage, sendMessage, getScores, generateMessageData


parser = argparse.ArgumentParser()
parser.add_argument(
    '--id',
    '-id',
    default = 2730,
    help = 'enter the series id/match id'
)
args = parser.parse_args()

while(True):
    time.sleep(5)
    venue, status, summary, scores = generateMessageData(args)
    test = sendMessage(venue)
    time.sleep(1)
    test = sendMessage(status)
    time.sleep(1)
    test = sendMessage(summary)
    time.sleep(1)
    message = getScores(scores)
    test = sendMessage(validMessage(message))


#test_id = 49839, 2730

#1 Print scores^
#2 Isolate the functions; this main.py should call other functions^
#3 make another function to send the notifs: shouldn't be happening in while loop*
#4 more functionalities
