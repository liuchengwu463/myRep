import os
import xlsxwriter as xw
import datetime


now = datetime.datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")
out_path = os.path.join(month, day, "receive_info", "receive_info.txt")
# out_path = os.path.join('output', 'receive_info.txt')
with open(out_path, 'r', encoding='utf-8') as f:
    bill_info_str = f.read()
bill_info_list = bill_info_str.splitlines()
data = []
for bill_info in bill_info_list:
    result = bill_info.split()
    data.append(result)

now = datetime.datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")

#workbook = xw.Workbook(f'{month}月{day}号-472.xls')  # 创建工作簿
workbook = xw.Workbook(f'打印单-53.xls')  # 创建工作簿
worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表

cell_format_A = workbook.add_format({'font_size': 11, 'border': 1})
worksheet1.set_column('A:A', cell_format=cell_format_A)

cell_format_B = workbook.add_format({'bold': True, 'font_size': 11, 'border': 1})
worksheet1.set_column('C:C', width=20, cell_format=cell_format_B)

cell_format = workbook.add_format()
cell_format.set_border(1)

worksheet1.print_area(f'A1:B{len(data)+1}')
worksheet1.set_print_scale(95)
worksheet1.set_paper('A4')
worksheet1.set_footer('&CPage &P of &N')

worksheet1.activate()  # 激活表
title = ['单号', '姓名', '手机']  # 设置表头
# title = ['单号', '姓名', '手机', '地址']  # 设置表头
worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
i = 2  # 从第二行开始写入数据
for j in range(len(data)):
    # insertData = [data[j][1], data[j][2]]
    # data[j][2] = data[j][2][13:]
    insertData = [data[j][0], data[j][1], data[j][2]]
    # insertData = [data[j][0], data[j][1], data[j][2], data[j][3]]
    row = 'A' + str(i)
    worksheet1.set_row(j, 25)
    worksheet1.write_row(row, insertData)
    i += 1
worksheet1.set_row(j+1, 25)
workbook.close()  # 关闭表