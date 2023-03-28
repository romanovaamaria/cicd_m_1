

with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2:
    f1_lines = f1.readlines()
    f2_lines = f2.readlines()

def find_same():
    same_lines = list(set(f1_lines) & set(f2_lines))
    with open('same.txt', 'w') as same_file:
        same_file.writelines(same_lines)