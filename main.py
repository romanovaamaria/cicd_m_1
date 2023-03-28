def read_files(filename1, filename2):
    with open(filename1, 'r',encoding="utf8") as f1, open(filename2, 'r', encoding="utf8") as f2:
        f1_lines = f1.readlines()
        f2_lines = f2.readlines()
    return f1_lines, f2_lines

def find_same(file_list1, file_list2):
    same_lines = list(set(file_list1) & set(file_list2))
    with open('same.txt', 'w') as same_file:
        same_file.writelines(same_lines)

def find_diff(file_list1, file_list2):
    same_lines = list(set(file_list1) ^ set(file_list2))
    with open('diff.txt', 'w') as same_file:
        same_file.writelines(same_lines)

f1_lines, f2_lines = read_files('file1.txt', 'file2.txt')
find_same(f1_lines, f2_lines)
find_diff(f1_lines, f2_lines)