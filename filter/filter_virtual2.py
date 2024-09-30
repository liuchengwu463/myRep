import requests
import os
import time
import re
import datetime
import random
import yaml
import json
from mime import common


with open('../config.yaml', 'r', encoding='UTF-8') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
wait_second = config['wait_second']


cookie_file_path = os.path.join("../cookie", "cookie2.txt")
with open(cookie_file_path, 'r') as f:
    cookie = f.read()

now = datetime.datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")
file_path = os.path.join('..', month, day, 'wait_decrypt', "sign_num2.txt")
with open(file_path, 'r') as f:
    bill_id_str = f.read()

wait_decrypt_dir = os.path.join('..', month, day, "wait_decrypt")
if not os.path.exists(wait_decrypt_dir):
    os.system(f"mkdir {wait_decrypt_dir}")

question_billid_path = os.path.join('..', month, day)
bill_id_list = bill_id_str.splitlines()
url = "https://order-query-center.gw.zt-express.com/orderQuery/mobileQueryByCode"

for index, bill_id in enumerate(bill_id_list):
    print(index, bill_id)
    seconds = random.randint(1, wait_second)
    time.sleep(seconds)

    query_result = common.get_query_result()
    post_data = {
        "bizScenario": {"useCase": "mobile_query_desensitizate_case"},
        "orderMobileCO": {
            "extValues": {},
            "mobileQueryCode": bill_id,
            "mobileQueryCodeType": 0,
            "needQuerySixMonthBefore": False,
            "sceneCode": "kjgz-query-record-receive-scene",
        },
        "secureCheckCO": {
            "pageUrl": "",
            "secureToken": "token-from-otc-sdk"
        }
    }
    response = requests.post(url, headers=common.order_query_head(cookie, '297'), json=post_data).json()
    print(response)
    result = response['result']

    if result['data']['mobileQueryResCO']['virtualNumberFlag']:
        with open(os.path.join(question_billid_path, "virtual_bill_id.txt"), 'a', encoding='utf-8') as f:
            f.write(f'{bill_id}\n')
        print(f'{bill_id} 虚拟号')
        continue
    else:
        with open(os.path.join(wait_decrypt_dir, "num2.txt"), 'a', encoding='utf-8') as f:
            f.write(f'{bill_id}\n')
