import urllib.parse

initial = "homeScore: 145 & 0-49\nhomeOvers: 53.2 & 7.4\nawayScore: 112 & 81\nawayOvers: 48.4 & 30.4"

message = urllib.parse.quote_plus(initial)
print(message)