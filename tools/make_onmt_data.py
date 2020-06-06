import random
import sys

data = []
for line in iter(sys.stdin.readline, ''):
    data.append(line.strip().split('\t'))

random.seed(0)
random.shuffle(data)

data_size = len(data)

val_size = 5000
test_size = 5000

test = data[:test_size]
val = data[test_size:test_size+val_size]
train = data[test_size+val_size:]

with open('src-test.txt', 'w', encoding='utf-8') as f, \
        open('tgt-test.txt', 'w', encoding='utf-8') as g:
    for src, tgt in test:
        f.write(src + '\n')
        g.write(tgt + '\n')

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
