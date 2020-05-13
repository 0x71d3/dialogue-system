import sys
import re
from pyknp import Juman

jumanpp = Juman()

id_pairs = []
with open('../data/twitter_id_str_data.txt', 'r') as f:
    for line in f:
        id_pair = tuple(map(int, line.split()))
        id_pairs.append(id_pair)

break_sub = ' '
reply_pattern = re.compile(r'^@+[ \n　]?[a-zA-Z0-9_]+[ \n　]*')

id2tweet = {}
with open('../data/twitter_tweet_data.txt', 'r') as f:
    id_ = -1
    tweet = ''
    for line in f:
        line = line.rstrip('\n')
        if '\t' in line:
            id2tweet[id_] = tweet.replace('\\n', break_sub)
            id_, tweet = line.split('\t')
            id_ = int(id_)
            while reply_pattern.match(tweet):
                tweet = reply_pattern.sub('', tweet)
        else:
            tweet += break_sub + line
    id2tweet[id_] = tweet

tweet_pairs = []
for id_pair in id_pairs:
    if id_pair[0] in id2tweet and id_pair[1] in id2tweet:
        tweet_pair = (id2tweet[id_pair[0]], id2tweet[id_pair[1]])
        tweet_pairs.append(tweet_pair)

with open('../data/twitter_data.tsv', 'w') as f:
    f.write('\n'.join('\t'.join(tweet_pair) for tweet_pair in tweet_pairs))