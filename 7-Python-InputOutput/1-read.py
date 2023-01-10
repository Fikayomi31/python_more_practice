with open('mydata.txt', encoding="utf-8") as f:
    read_data = f.read()
    for line in read_data:

        print(line, end='')
