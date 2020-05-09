import random

src = []
with open('../data/src.txt', 'r') as f:
    for line in f:
        src.append(line.rstrip('\n'))

tgt = []
with open('../data/tgt.txt', 'r') as f:
    for line in f:
        tgt.append(line.rstrip('\n'))

src_tgt = list(zip(src, tgt))
random.shuffle(src_tgt)

# train_size = 10000
val_size = 3000
test_size = 3000

test = src_tgt[:test_size]
with open('../data/src-test.txt', 'w') as f:
    f.write('\n'.join(s for s, t in test))

val = src_tgt[test_size:test_size+val_size]
with open('../data/src-val.txt', 'w') as f:
    f.write('\n'.join(s for s, t in val))
with open('../data/tgt-val.txt', 'w') as f:
    f.write('\n'.join(t for s, t in val))

train = src_tgt[test_size+val_size:]
with open('../data/src-train.txt', 'w') as f:
    f.write('\n'.join(s for s, t in train))
with open('../data/tgt-train.txt', 'w') as f:
    f.write('\n'.join(t for s, t in train))