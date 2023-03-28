with open('file1.txt', 'r',encoding="utf8") as f1, open('file2.txt', 'r', encoding="utf8") as f2:
    f1_lines = f1.readlines()
    f2_lines = f2.readlines()

def find_same(file_list1, file_list2):
    same_lines = list(set(file_list1) & set(file_list2))
    with open('same.txt', 'w') as same_file:
        same_file.writelines(same_lines)

def find_diff(file_list1, file_list2):
    same_lines = list(set(file_list1) ^ set(file_list2))
    with open('diff.txt', 'w') as same_file:
        same_file.writelines(same_lines)


find_same(f1_lines, f2_lines)
find_diff(f1_lines, f2_lines)