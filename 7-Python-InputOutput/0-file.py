import os

with open("tests/mydata.txt", "w", encoding="utf-8") as myfile:
    myfile.write("Some randon text\nMore random file\nAnd some more")

with open("tests/mydata.txt", encoding="utf-8") as myfile:
    print(myfile.read())


    # seek used to omit a given character
    print(myfile.seek(1))
    print()
    print(myfile.seek(2))
    print()
    print(myfile.seek(3))
    print()
    print(myfile.read())


print(myfile.close())
