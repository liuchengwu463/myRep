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

cookie_file_path = os.path.join("../cookie", "cookie3.txt")
with open(cookie_file_path, 'r') as f:
    cookie = f.read()

now = datetime.datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")
# file_path = os.path.join('..', month, day, "wait_decrypt", "num3.txt")
file_path = os.path.join('..', month, day, "wait_decrypt", "sign_num3.txt")
with open(file_path, 'r') as f:
    bill_id_str = f.read()
bill_id_list = bill_id_str.splitlines()

receive_info_path = os.path.join('..', month, day, "receive_info")
if not os.path.exists(receive_info_path):
    os.system(f"mkdir {receive_info_path}")
question_billid_path = os.path.join('..', month, day)

get_orderinfo_url = "https://ydzx-web.gw.zt-express.com/order/orderInfoList"
get_fullphone_url = "https://ydzx-web.gw.zt-express.com/order/getFullPhoneNum"
for index, bill_id in enumerate(bill_id_list):
    print(index, bill_id)
    seconds = random.randint(1, wait_second)
    time.sleep(seconds)

    get_ticket_url1 = f'https://sso.zto.com/security-services/billtrack/billinfo-query-preauth?bill_id={bill_id}&type=A014&archive=false'
    ticket_type1 = 'A014'
    ticket_response1 = requests.get(get_ticket_url1, headers=common.ticket_head(cookie)).json()
    print(ticket_response1)
    ticket1 = ticket_response1['ticket']

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
    receive_phone = receive_info[receive_info.find("1"):]
    if len(receive_phone) == 11:
        length = '123'
    else:
        length = '128'
    receive_address = re.sub('<button.*', "", orderinfo_result['receiveAddress'], flags=re.S)
    time.sleep(1)

    get_ticket_url2 = f'https://sso.zto.com/security-services/billtrack/billinfo-query-preauth?bill_id={bill_id}&type=A028&archive=false'
    ticket_type2 = 'A028'
    ticket_response2 = requests.get(get_ticket_url2, headers=common.ticket_head(cookie)).json()
    print(ticket_response2)
    ticket2 = ticket_response2['ticket']

    fullphone_post_data = {
        "billCode": bill_id,
        "manName": receive_name,
        "normalPhone": receivePrivacyNum,
        "orderCode": orderCode,
        "phoneType": "2"
    }

    phone_response = requests.post(
        get_fullphone_url,
        headers=common.orderinfo_head(cookie, bill_id, ticket2, ticket_type2, length),
        json=fullphone_post_data
    ).json()
    print(phone_response)
    phone_result = phone_response['result']
    phone = phone_result[phone_result.find("1"):]
    if len(phone) != 11 and is_need_virtual == 0:
        with open(os.path.join(question_billid_path, "virtual_bill_id.txt"), 'a', encoding='utf-8') as f:
            f.write(f'{bill_id}\n')
        print(f'{bill_id} 虚拟号')
        continue

    with open(os.path.join(receive_info_path, "receive_info3.txt"), 'a', encoding='utf-8') as f:
        f.write(f'{bill_id} {receive_name} {phone} {receive_address}\n')
