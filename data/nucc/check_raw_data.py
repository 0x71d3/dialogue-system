import os
from collections import Counter

code_counter = Counter()

dir_path = 'nucc'
for file_name in os.listdir(dir_path):
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            if line[0] in ['＠', '％']:
                continue
            if '：' in line:
                code, _ = line.strip().split('：', maxsplit=1)
                code_counter[code] += 1

print(code_counter)
