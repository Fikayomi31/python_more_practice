import os

with open("mydata.txt", mode="w", encoding="utf-8") as myfile:
    myfile.write("Some rsndon text\nMore random file\nAnd some more")

with open("mydata.txt", encoding="utf-8") as myfile:
    print(myfile.read())
