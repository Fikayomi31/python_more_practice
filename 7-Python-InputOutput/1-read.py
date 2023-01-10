with open('mydata.txt', encoding="utf-8") as f:
    read_data = f.read()
    for line in read_data:

        print(line, end='')
        

with open('tests/my_file_0.txt', encoding="utf-8") as e_file:
    read_file = e_file.read()
    print(read_file)
