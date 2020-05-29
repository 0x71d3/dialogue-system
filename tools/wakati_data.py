import sys
from pyknp import Juman

jumanpp = Juman()

for line in iter(sys.stdin.readline, ''):
    src, tgt = line.strip().split('\t')
    try:
        result = jumanpp.analysis(src)
        src_seq = ' '.join(mrph.midasi for mrph in result.mrph_list())
        result = jumanpp.analysis(tgt)
        tgt_seq = ' '.join(mrph.midasi for mrph in result.mrph_list())
        print(src_seq, tgt_seq, sep='\t')
    except:
        pass
