import re
import sys

with open(sys.argv[1], encoding='utf-8') as f:
    data = [line.strip().split('\t') for line in f]

symbol = re.compile(r'‘.*?’|\[.*?\]|《.*?》|=|【【|】】|\(.*?\)|<.*?>|(<.*?>)')

for i in range(len(data) - 1):
    if data[i][2] == '/' or data[i+1][2] == '/':
        continue
    if data[i][3] == data[i+1][3]:
        continue
    if '{<}' in data[i][4] or '{>}' in data[i][4] \
            or '{<}' in data[i+1][4] or '{>}' in data[i+1][4]:
        continue
    if '#' in data[i][4] or '#' in data[i+1][4]:
        continue

    src = symbol.sub('', data[i][4])
    tgt = symbol.sub('', data[i+1][4])

    if src == '。' or tgt == '。':
        continue
    print(src, tgt, sep='\t')
