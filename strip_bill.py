import datetime
import os

express_num_file = "strip.txt"

with open(express_num_file, 'r', encoding='utf-8') as f:
    content = f.read()
wait_split_list = content.splitlines()
for index, wait_split in enumerate(wait_split_list):
    if '@' in wait_split:
        wait_split_list[index] = wait_split[1:]

#lst = list(set(wait_split_list))
with open("striped.txt", 'w', encoding='utf-8') as f:
    f.write('')
for i in wait_split_list:
    ii = i[0:14]
    # ii = i[4:]
    #ii = i[3:17]
    if ii[:2] == 'SF':
        continue
    if ii[:2] == 'JT':
        continue
    if ii[:2] == 'YT':
        continue
    if ii[:2] == '46':
        continue
    if ii[:2] == 'JD':
        continue
    if len(ii) < 14:
        continue
    with open("striped.txt", 'a', encoding='utf-8') as f:
        f.write(f'{ii}\n')
