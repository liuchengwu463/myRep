origin_file = "origin.txt"
out_file = "striped.txt"

with open(origin_file, 'r', encoding='utf-8') as f:
    origin_content = f.read()
origin_list = origin_content.splitlines()

with open(out_file, 'r', encoding='utf-8') as f:
    out_content = f.read()
out_list = out_content.splitlines()

intersection_list = list(set(origin_list) & set(out_list))

with open("intersection.txt", 'w', encoding='utf-8') as f:
    f.write('')
for intersection in intersection_list:
    with open("intersection.txt", 'a', encoding='utf-8') as f:
        f.write(f'{intersection}\n')

