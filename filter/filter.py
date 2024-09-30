import requests
import os
import time
import re
import datetime
import common


cookie_file_path = os.path.join("../cookie", "cookie1.txt")
with open(cookie_file_path, 'r') as f:
    cookie = f.read()

now = datetime.datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")
file_path = os.path.join(month, day, "num1.txt")
with open(file_path, 'r') as f:
    bill_id_str = f.read()

wait_decrypt_path = os.path.join(month, day, "wait_decrypt")
if not os.path.exists(wait_decrypt_path):
    os.system(f"mkdir {wait_decrypt_path}")

question_billid_path = os.path.join(month, day)

bill_id_list = bill_id_str.splitlines()

for index, bill_id in enumerate(bill_id_list):
    print(index, bill_id)
    # seconds = random.randint(1, wait_second)
    time.sleep(2)
    list_rendered_url = "https://waybill-service.zt-express.com/bill-tracing/list-rendered"
    list_rendered_data = {
        "billCodes": [bill_id],
        "billHide": False,
        "controlSet": [],
        "deCodebillCodes": [bill_id],
        "hideCarInfo": False,
        "hideForm": False,
        "showData": False,
        "showDataColumn": [],
        "useArchive": False,
    }
    list_rendered_response = requests.post(list_rendered_url, headers=common.waybill_head(cookie), json=list_rendered_data).json()
    list_rendered_result = list_rendered_response['result']

    complaint_find_result = re.findall("客诉保障部", list_rendered_result)
    if len(complaint_find_result) > 0:
        with open(os.path.join(wait_decrypt_path, "conplained_bill_id.txt"), 'a', encoding='utf-8') as f:
            f.write(f'{bill_id}\n')
        print(f'{bill_id} 存在投诉')
        continue

    back_find_result = re.findall("退回发件网点", list_rendered_result)
    if len(back_find_result) > 0:
        with open(os.path.join(wait_decrypt_path, "back_bill_id.txt"), 'a', encoding='utf-8') as f:
            f.write(f'{bill_id}\n')
        print(f'{bill_id} 退回发件网点')
        continue

    sign_find_result = re.findall("派件已签收|派件进站", list_rendered_result)
    if len(sign_find_result) == 0:
        with open(os.path.join(wait_decrypt_path, "unsign_bill_id.txt"), 'a', encoding='utf-8') as f:
            f.write(f'{bill_id}\n')
        print(f'{bill_id} 未签收')
        continue

    with open(os.path.join(wait_decrypt_path, "num1.txt"), 'a', encoding='utf-8') as f:
        f.write(f'{bill_id}\n')
