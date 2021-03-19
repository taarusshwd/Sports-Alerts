import argparse 
import time
from helper import trialMatch3rdT20, sendMessage, scorecardDetails


parser = argparse.ArgumentParser()
parser.add_argument(
    '--seriesId',
    '-seriesId',
    default = 2731,
    help = 'enter the series id'
)
parser.add_argument(
    '--matchId',
    '-matchId',
    default = 49845,
    help = 'enter the match id'
)

args = parser.parse_args()

while(True):
    time.sleep(5)
    summary = trialMatch3rdT20(args)
    batsmen, bowler, MOTM = scorecardDetails(args)
    test = sendMessage(summary)
    test = sendMessage("Best Batsmen: {} \nBest Bowler: {} \nMan ff The Match: {}".format(batsmen, bowler, MOTM))
    time.sleep(1)
    
#test_id = 49839, 2730
#test_id_3rd_T20 = 49844, 2731
