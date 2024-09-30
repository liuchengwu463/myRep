from collections import Counter


express_num_file = "origin.txt"

with open(express_num_file, 'r', encoding='utf-8') as f:
    content = f.read()
wait_split_list = content.splitlines()


# 使用Counter来计数
counter = Counter(wait_split_list)

# 找出出现次数大于1的元素
duplicates = [item for item, count in counter.items() if count > 1]

with open("repeat.txt", 'w', encoding='utf-8') as f:
    f.write('')
for duplicate in duplicates:
    with open("repeat.txt", 'a', encoding='utf-8') as f:
        f.write(f'{duplicate}\n')
print(duplicates)


