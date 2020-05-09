import sys
import re
from pyknp import Juman

jumanpp = Juman()

id_pairs = []
with open('../data/twitter_id_str_data.txt', 'r') as f:
    for line in f:
        id_pair = tuple(map(int, line.split()))
        id_pairs.append(id_pair)

reply_pattern = re.compile(r'^@+[ \n　]?[a-zA-Z0-9_]+[ \n　]*')
break_sub = ' '

output_map = {}
with open('../data/twitter_data.txt', 'r') as f:
    id_ = -1
    tweet = ''
    for line in f:
        line = line.rstrip('\n')
        if '\t' in line:
            output_map[id_] = tweet.replace('\\n', break_sub)
            id_, tweet = line.split('\t')
            id_ = int(id_)
            while reply_pattern.match(tweet):
                tweet = reply_pattern.sub('', tweet)
        else:
            tweet += break_sub + line
    output_map[id_] = tweet

wakati_map = {}
for id_, tweet in output_map.items():
    try:
        result = jumanpp.analysis(tweet)
        wakati_tweet = ' '.join(mrph.midasi for mrph in result.mrph_list())
        wakati_map[id_] = wakati_tweet
    except IndexError:
        print('IndexError in', id_, file=sys.stderr)
    except ValueError:
        print('ValueError in', id_, file=sys.stderr)

wakati_pairs = []
for id_a, id_b in id_pairs:
    if id_a in wakati_map and id_b in wakati_map:
        wakati_a = wakati_map[id_a]
        wakati_b = wakati_map[id_b]
        wakati_pair = (wakati_a, wakati_b)
        wakati_pairs.append(wakati_pair)

with open('../data/src.txt', 'w') as f:
    f.write('\n'.join(wakati_pair[0] for wakati_pair in wakati_pairs))
    
with open('../data/tgt.txt', 'w') as f:
    f.write('\n'.join(wakati_pair[1] for wakati_pair in wakati_pairs))