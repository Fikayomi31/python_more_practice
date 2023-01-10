line_number = 0
with open("tests/my_file_0.txt", encoding="utf-8") as f:
    for line in f:
        line_number += 1
        print('{:>4} {}'.format(line_number, line.rstrip()))
