import random
import sys

with open(sys.argv[1], encoding='utf-8') as f:
    data = [line.strip().split('\t') for line in f]

random.seed(0)
random.shuffle(data)

data_size = len(data)

val_size = 5000
test_size = 5000

test = data[:test_size]
val = data[test_size:test_size+val_size]
train = data[test_size+val_size:]

with open('src-test.txt', 'w', encoding='utf-8') as f:
    for src, tgt in test:
        f.write(src + '\n')

with open('src-val.txt', 'w', encoding='utf-8') as f, \
        open('tgt-val.txt', 'w', encoding='utf-8') as g:
    for src, tgt in val:
        f.write(src + '\n')
        g.write(tgt + '\n')

with open('src-train.txt', 'w', encoding='utf-8') as f, \
        open('tgt-train.txt', 'w', encoding='utf-8') as g:
    for src, tgt in train:
        f.write(src + '\n')
        g.write(tgt + '\n')
