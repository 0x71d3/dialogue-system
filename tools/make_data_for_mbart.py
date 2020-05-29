import random
import sys

with open(sys.argv[1], encoding='utf-8') as f:
    data = [line.strip().split('\t') for line in f]

random.seed(0)
random.shuffle(data)

data_size = len(data)

val_size = 10000
test_size = 10000

test = data[:test_size]
valid = data[test_size:test_size+val_size]
train = data[test_size+val_size:]

with open('test.ja_src', 'w', encoding='utf-8') as f, \
        open('test.ja_tgt', 'w', encoding='utf-8') as g:
    for src, tgt in test:
        f.write(src + '\n')
        g.write(tgt + '\n')

with open('valid.ja_src', 'w', encoding='utf-8') as g, \
        open('valid.ja_tgt', 'w', encoding='utf-8') as f:
    for src, tgt in valid:
        f.write(src + '\n')
        g.write(tgt + '\n')

with open('train.ja_src', 'w', encoding='utf-8') as f, \
        open('train.ja_tgt', 'w', encoding='utf-8') as g:
    for src, tgt in train:
        f.write(src + '\n')
        g.write(tgt + '\n')
