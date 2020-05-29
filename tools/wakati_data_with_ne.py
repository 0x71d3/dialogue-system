import gc
import re
import sys
from tqdm import tqdm

import timeout_decorator
from pyknp import KNP

data = []
for line in iter(sys.stdin.readline, ''):
    data.append(line.strip().split('\t'))

timeout_seconds = 10

@timeout_decorator.timeout(timeout_seconds)
def wakati(text, knp):
    result = knp.parse(text)
    midasis = []
    for mrph in result.mrph_list():
        ne = re.search(r'<NE:(.*?):(.*?)>', mrph.fstring)
        if ne:
            tag = ne[1]
            position = ne[2]
            if position in ['tail', 'single']:
                midasis.append('<{}>'.format(tag))
        else:
            midasis.append(mrph.midasi)
    return ' '.join(midasis)

def init_knp():
    return KNP(option='-ne-crf -tab')

batch_size = 100
knp = init_knp()

for i in tqdm(range(0, len(data), batch_size)):
    for src, tgt in data[i:i+batch_size]:
        try:
            src_seq = wakati(src, knp)
            tgt_seq = wakati(tgt, knp)
            print(src_seq, tgt_seq, sep='\t')
        except:
            del knp
            gc.collect()
            knp = init_knp()
    del knp
    gc.collect()
    knp = init_knp()
