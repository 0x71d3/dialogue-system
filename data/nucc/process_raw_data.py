import os
import re

data = []

dir_path = 'nucc'
for file_name in os.listdir(dir_path):
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, encoding='utf-8') as f:
        prev_code = ''
        prev_text = ''
        code = ''
        text = ''
        for line in f:
            if line[0] in ['＠', '％']:
                continue
            if '：' in line:
                text = re.sub(r'（.*?）|＜.*?＞|（＜.*?＞）|【.*?】', '', text)
                try:
                    if not re.match(r'[FM][0-9]{3}|Ｘ', code):
                        code = ''
                    if '＊' in text:
                        text = ''
                    if not (prev_code and code):
                        raise Exception
                    if prev_code == code:
                        raise Exception
                    if not (prev_text and text):
                        raise Exception
                    data.append([prev_text, text])
                except:
                    pass
                finally:
                    prev_code = code
                    prev_text = text
                code, text = line.strip().split('：', maxsplit=1)
            else:
                code = ''
                text = ''

for src, tgt in data:
    print(src, tgt, sep='\t')
