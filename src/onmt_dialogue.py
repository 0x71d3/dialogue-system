import sys

from onmt.translate.translator import build_translator
import onmt.opts as opts
from onmt.utils.parse import ArgumentParser

from pyknp import Juman

jumanpp = Juman()

parser = ArgumentParser()
opts.config_opts(parser)
opts.translate_opts(parser)

opt = parser.parse_args([
    '-model',
    sys.argv[1],
    '-src',
    'dummy.txt',
    '-output',
    'dummy.txt',
    '-replace_unk',
])

ArgumentParser.validate_translate_opts(opt)
translator = build_translator(opt, report_score=False)

def answer(translator, utterance):
    result = jumanpp.analysis(utterance)
    src_shard = [[mrph.midasi for mrph in result.mrph_list()]]
    tgt_shard = [['']]
    _, all_predictions = translator.translate(
        src=src_shard,
        tgt=tgt_shard,
        src_dir=opt.src_dir,
        batch_size=opt.batch_size,
        batch_type=opt.batch_type,
        attn_debug=opt.attn_debug,
        align_debug=opt.align_debug
    )
    return all_predictions[0][0].replace(' ', '')

answer(translator, ' ')
print()

print('system ready')
print()

user_utterance = input('> ')
while user_utterance:
    system_answer = answer(translator, user_utterance)
    print(system_answer)
    print()
    user_utterance = input('> ')
