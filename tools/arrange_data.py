import sys
from pyknp import Juman

jumanpp = Juman()

data = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        data.append(tuple(line.split('\t')))

wakati_data = []
for src, tgt in data:
    try:
        src_result = jumanpp.analysis(src)
        src_wakati = ' '.join(mrph.midasi for mrph in src_result.mrph_list())
        tgt_result = jumanpp.analysis(tgt)
        tgt_watati = ' '.join(mrph.midasi for mrph in tgt_result.mrph_list())
        wakati = (src_wakati, tgt_watati)
        wakati_data.append(wakati)
    except:
        pass

with open('../data/src.txt', 'w') as f:
    f.write('\n'.join(wakati[0] for wakati in wakati_data))
    
with open('../data/tgt.txt', 'w') as f:
    f.write('\n'.join(wakati[1] for wakati in wakati_data))