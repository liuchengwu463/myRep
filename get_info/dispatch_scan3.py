import requests
import time
import re
import datetime
import os
import random
import yaml
import pyautogui as pg
import pyperclip

with open('../config.yaml', 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
wait_second = config['wait_second']

now = datetime.datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")
# file_path = os.path.join('..', month, day, "wait_decrypt", "num1.txt")
file_path = os.path.join('..', month, day, "wait_decrypt", "sign_num3.txt")
with open(file_path, 'r') as f:
    bill_id_str = f.read()
bill_id_list = bill_id_str.splitlines()

for index, bill_id in enumerate(bill_id_list):
    time.sleep(1)
    pyperclip.copy(bill_id)
    pg.click(x=549, y=174)
    pg.doubleClick()
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'v')
    pg.press('enter')




