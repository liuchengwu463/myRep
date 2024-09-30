import yaml
import os
import random
import datetime

with open('config.yaml', 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
max_express_num = config['max_express_num']  # 平均每人最多查询记录
people_num = config['people_num']  # 总查询人数

now = datetime.datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")

express_num_file = f"{day}num.txt"
file_path = os.path.join(month, express_num_file)

with open(file_path, 'r') as f:
    content = f.read()
wait_split_list = content.splitlines()

print(len(wait_split_list))

os.system(f'mkdir {os.path.join(month, day)}')
while 1 == 1:
    total_num = 0
    last_num = 0
    split_num_list = []
    for i in range(0, people_num):
        if i < people_num - 1:
            random_num = random.randint(1, max_express_num)
            split_num_list.append(random_num)
            total_num += random_num
        elif i == people_num - 1:
            last_num = len(wait_split_list) - total_num
    if max_express_num > last_num > 0:
        split_num_list.append(last_num)
        print(split_num_list)
        first_index = 0
        second_index = 0
        for index, express_num in enumerate(split_num_list):
            file_name = f'num{index+1}.txt'
            second_index += express_num
            first_index = second_index - express_num
            print(f'first_index {first_index}')
            print(f'second_index {second_index}')
            write_list = wait_split_list[first_index:second_index]
            for ii in write_list:
                with open(f'{os.path.join(month, day, file_name)}', 'a', encoding='utf-8') as f:
                    f.write(f'{ii}\n')
            print(write_list)
        break
