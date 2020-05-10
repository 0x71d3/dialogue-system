import os
import re

pair_data = []

nucc_path = '../data/nucc'
for data_name in os.listdir(nucc_path):
    data_path = nucc_path + '/' + data_name
    with open(data_path, 'r') as f:
        prev_text = ''
        text = ''
        for line in f:
            if line[0] == '＠' or line[0] == '％':  # 2) or 11)
                continue
            line = line.rstrip('\n')

            if '：' in line:
                if re.search(r'＜中略＞|＊|＜間＞|[FM][0-9]{3}', text):  # 3), 9) or etc.
                    text = ''
                else:
                    text = re.sub(r'（.*?）', '', text)  # 4)
                    text = re.sub(r'＜.*?＞', '', text)  # 7)
                    text = re.sub(r'【.*?】', '', text)  # 10)
                    text = text.replace('\t', ' ')
                if prev_text and text:
                    text_pair = (prev_text, text)
                    pair_data.append(text_pair)

                prev_text = text
                text = ''
                line_code, line_text = line.split('：', maxsplit=1)
            else:
                line_text = line

            text += line_text

        if re.search(r'＜中略＞|＊|＜間＞|[FM][0-9]{3}', text):  # 3), 9) or etc.
            text = ''
        else:
            text = re.sub(r'（.*?）', '', text)  # 4)
            text = re.sub(r'＜.*?＞', '', text)  # 7)
            text = re.sub(r'【.*?】', '', text)  # 10)
            text = text.replace('\t', ' ')
        if prev_text and text:
            text_pair = (prev_text, text)
            pair_data.append(text_pair)

with open(nucc_path + '_data.tsv', 'w') as f:
    f.write('\n'.join('\t'.join(pair) for pair in pair_data))