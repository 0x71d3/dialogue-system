import os
import re

symbols = re.compile(r'（.*?）|＜.*?＞|（＜.*?＞）|【.*?】')
codes = re.compile(r'[FM][0-9]{3}|Ｘ')

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
            try:
                code, temp_text = line.strip().split('：', maxsplit=1)
                text = symbols.sub('', temp_text)

                try:
                    if not codes.match(code) or not codes.match(prev_code):
                        raise Exception
                    if prev_code == code:
                        raise Exception
                    if not prev_text or not text:
                        raise Exception
                    if '＊' in text or '＊' in prev_text:
                        raise Exception
                    data.append([prev_text, text])
                except:
                    pass
                finally:
                    prev_code = code
            except:
                text = symbols.sub('', line.strip())
            finally:
                prev_text = text

for src, tgt in data:
    print(src, tgt, sep='\t')
