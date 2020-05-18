import html
import json
import sys
import time

from requests_oauthlib import OAuth1Session

from settings import *

RESOURCE_URL = 'https://api.twitter.com/1.1/statuses/lookup.json'
ID_STEP = 100
SLEEP_SECS = 3
BR_SUB = ' '

oauth = OAuth1Session(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
)

id_str_list = []
for line in iter(sys.stdin.readline, ''):
    id_str_list.append(line.strip())

for i in range(0, len(id_str_list), ID_STEP):
    params = {'id': ','.join(id_str_list[i:i+ID_STEP])}
    
    r = oauth.get(RESOURCE_URL, params=params)
    statuses = json.loads(html.unescape(r.text))

    for status in statuses:
        id_str = status['id_str']
        text = status['text'].replace('\n', BR_SUB)
        print(id_str, text, sep='\t')

    time.sleep(SLEEP_SECS)