import datetime
import os

now = datetime.datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")

merge_type = input()
if merge_type == '1':
    file_name = 'receive_info'
    merge_path = os.path.join(month, day, 'receive_info')
    file_path = os.path.join(month, day, 'receive_info', 'receive_info.txt')
    print('merge receive_info')
elif merge_type == '2':
    file_name = 'sign'
    merge_path = os.path.join(month, day, 'wait_decrypt')
    file_path = os.path.join(month, day, 'wait_decrypt', 'sign_num.txt')
    print('merge num')
elif merge_type == '3':
    file_name = 'unsign'
    merge_path = os.path.join(month, day, 'wait_decrypt')
    file_path = os.path.join(month, day, 'wait_decrypt', 'unsign_bill_id.txt')
    print('merge unsign')
files = os.listdir(merge_path)
# if not os.path.exists("output"):
#     os.system(f"mkdir output")
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('')
for file in files:
    print(file)
    if merge_type == '2' and file.find('sign') != 0:
        continue
    if merge_type == '3' and file.find('unsign') != 0:
        continue
    with open(f"{os.path.join(merge_path, file)}", 'r', encoding='utf-8') as f:
        cotent = f.read()
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(cotent)
