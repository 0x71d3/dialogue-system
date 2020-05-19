import random
import sys
from tqdm import tqdm

from pyknp import Juman

with open(sys.argv[1], encoding='utf-8') as f:
    data = [tuple(line.strip().split('\t')) for line in f]

jumanpp = Juman()

wakati_data = []
for src, tgt in tqdm(data):
    try:
        result = jumanpp.analysis(src)
        wakati_src = ' '.join(mrph.midasi for mrph in result.mrph_list())
        result = jumanpp.analysis(tgt)
        wakati_tgt = ' '.join(mrph.midasi for mrph in result.mrph_list())
        wakati_pair = (wakati_src, wakati_tgt)
        wakati_data.append(wakati_pair)
    except:
        pass

random.shuffle(wakati_data)
data_size = len(wakati_data)

# train_size = 10000
val_size = 5000
test_size = 5000

test_data = wakati_data[:test_size]
with open('src-test.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(src for src, tgt in test_data))

val_data = wakati_data[test_size:test_size+val_size]
with open('src-val.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(src for src, tgt in val_data))
with open('tgt-val.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(tgt for src, tgt in val_data))

train = wakati_data[test_size+val_size:]
with open('src-train.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(src for src, tgt in train))
with open('tgt-train.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(tgt for src, tgt in train))
