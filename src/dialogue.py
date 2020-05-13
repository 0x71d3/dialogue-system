from onmt.translate.translator import build_translator
import onmt.opts as opts
from onmt.utils.parse import ArgumentParser

from pyknp import Juman

jumanpp = Juman()

parser = ArgumentParser()
opts.config_opts(parser)
opts.translate_opts(parser)

model_path = '../data/model/stcj-model_step_50000.pt'
opt = parser.parse_args([
    '-model',
    model_path,
    '-src',
    '../data/src-test.txt',
    '-replace_unk',
    ])

ArgumentParser.validate_translate_opts(opt)
translator = build_translator(opt, report_score=False)

translator.translate(
    src=[[]],
    tgt=None,
    src_dir=opt.src_dir,
    batch_size=opt.batch_size,
    batch_type=opt.batch_type,
    attn_debug=opt.attn_debug,
    align_debug=opt.align_debug
    )

print('system ready')
src_input = input('> ')

while src_input:
    result = jumanpp.analysis(src_input)

    src_shard = [[mrph.midasi for mrph in result.mrph_list()]]
    tgt_shard = None

    _, all_predictions = translator.translate(
        src=src_shard,
        tgt=tgt_shard,
        src_dir=opt.src_dir,
        batch_size=opt.batch_size,
        batch_type=opt.batch_type,
        attn_debug=opt.attn_debug,
        align_debug=opt.align_debug
        )

    print(all_predictions[0][0].replace(' ', ''))
    print()
    src_input = input('> ')