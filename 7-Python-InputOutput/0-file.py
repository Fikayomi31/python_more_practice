import os

with open("tests/mydata.txt", "w", encoding="utf-8") as myfile:
    myfile.write("Some rsndon text\nMore random file\nAnd some more")

with open("tests/mydata.txt", encoding="utf-8") as myfile:
    print(myfile.read())

print(myfile.close)
