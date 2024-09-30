import datetime
import os


now = datetime.datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")
express_num_file = f"{day}.txt"
file_path = os.path.join(month, express_num_file)

with open(f'{os.path.join(month, f"{day}num.txt")}', 'w', encoding='utf-8') as f:
    f.write('')
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()
wait_split_list = content.splitlines()
for index, wait_split in enumerate(wait_split_list):
    if '@' in wait_split:
        wait_split_list[index] = wait_split[1:]

lst = list(set(wait_split_list))
for i in lst:
    if i == '快递单号':
        continue
    if len(i) < 14:
        continue
    if len(i) > 15:
        continue
    ii = i[:14]
    with open(f'{os.path.join(month, f"{day}num.txt")}', 'a', encoding='utf-8') as f:
        f.write(f'{ii}\n')
