import requests
import time
import re
import datetime
import os
import random
import yaml
from mime import common

with open('../config.yaml', 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
wait_second = config['wait_second']
is_need_virtual = config['is_need_virtual']

cookie_file_path = os.path.join("../cookie", "cookie2.txt")
with open(cookie_file_path, 'r') as f:
    cookie = f.read()

now = datetime.datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")
# file_path = os.path.join('..', month, day, "wait_decrypt", "num2.txt")
file_path = os.path.join('..', month, day, "wait_decrypt", "sign_num2.txt")
with open(file_path, 'r') as f:
    bill_id_str = f.read()
bill_id_list = bill_id_str.splitlines()

receive_info_path = os.path.join('..', month, day, "receive_info")
if not os.path.exists(receive_info_path):
    os.system(f"mkdir {receive_info_path}")
question_billid_path = os.path.join('..', month, day)

get_orderinfo_url = "https://ydzx-web.gw.zt-express.com/order/orderInfoList"
get_fullphone_url = "https://order-query-center.gw.zt-express.com/orderQuery/mobileQueryByCode"
for index, bill_id in enumerate(bill_id_list):
    print(index, bill_id)
    seconds = random.randint(1, wait_second)
    time.sleep(seconds)

    get_ticket_url1 = f'https://sso.zto.com/security-services/billtrack/billinfo-query-preauth?bill_id={bill_id}&type=A014&archive=false'
    ticket_type1 = 'A014'
    ticket_response1 = requests.get(get_ticket_url1, headers=common.ticket_head(cookie)).json()
    print(ticket_response1)
    ticket1 = ticket_response1['ticket']
    print(ticket1)

    orderinfo_post_data = {
        "billCode": bill_id,
        "billHide": "false",
        "useArchive": False
    }
    orderinfo_response = requests.post(
        get_orderinfo_url,
        headers=common.orderinfo_head(cookie, bill_id, ticket1, ticket_type1, '67'),
        json=orderinfo_post_data
    ).json()
    orderinfo_result = orderinfo_response['result'][0]
    receivePrivacyNum = orderinfo_result['receivePrivacyNum']
    orderCode = orderinfo_result['orderCode']
    receive_info = orderinfo_result['receiveInfo']
    receive_name = receive_info[:receive_info.find(" ")]
    receive_address = re.sub('<button.*', "", orderinfo_result['receiveAddress'], flags=re.S)
    time.sleep(1)

    fullphone_post_data = {
        "bizScenario": {"useCase": "mobile_query_real_case"},
        "orderMobileCO": {
            "extValues": {"order_code": orderCode},
            "mobileQueryCode": bill_id,
            "mobileQueryCodeType": 0,
            "needQuerySixMonthBefore": False,
            "sceneCode": "kjgz_view_receive_scene",
        },
        "secureCheckCO": {
            "pageUrl": "https://www.zt-express.com/e-static/billtracing-web/default/prod/index.html?esingle=y&esinglefull=y&eiframe=1&emicroAppId=billtracing-web&eportalRoleCode=PORTAL_ROLE_002&esuffixUrl=prod%2Findex.html%3Fesingle%3Dy%26esinglefull%3Dy",
            "secureToken": "token-from-otc-sdk"
        },
        "orderCode": orderCode,
        "phoneType": "2"
    }

    response = requests.post(
        get_fullphone_url,
        headers=common.order_query_head(cookie, '595'),
        json=fullphone_post_data
    ).json()
    print(response)
    result = response['result']
    phone = result['data']['mobileQueryResCO']['suggestMobile']
    if len(phone) != 11 and is_need_virtual == 0:
        with open(os.path.join(question_billid_path, "virtual_bill_id.txt"), 'a', encoding='utf-8') as f:
            f.write(f'{bill_id}\n')
        print(f'{bill_id} 虚拟号')
        continue

    if phone[4] == '*':
        with open(os.path.join(question_billid_path, "secret_bill_id.txt"), 'a', encoding='utf-8') as f:
            f.write(f'{bill_id}\n')
        print(f'{bill_id} 加密号')
        continue

    with open(os.path.join(receive_info_path, "receive_info2.txt"), 'a', encoding='utf-8') as f:
        f.write(f'{bill_id} {receive_name} {phone} {receive_address}\n')