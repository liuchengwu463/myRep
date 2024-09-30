origin_file = "origin.txt"
out_file = "striped.txt"

with open(origin_file, 'r', encoding='utf-8') as f:
    origin_content = f.read()
origin_list = origin_content.splitlines()

with open(out_file, 'r', encoding='utf-8') as f:
    out_content = f.read()
out_list = out_content.splitlines()

diff_list = list(set(origin_list) - set(out_list))

with open("diff.txt", 'w', encoding='utf-8') as f:
    f.write('')
for diff in diff_list:
    with open("diff.txt", 'a', encoding='utf-8') as f:
        f.write(f'{diff}\n')

