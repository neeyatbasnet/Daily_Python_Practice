#parse a file and extract all numbers from the file and find their sum 
import re

sum=0
try:
    with open("textfile.txt","r") as f:
        for line in f:
            lst=re.findall('[0-9]+' ,line)
            if lst:
                for num in lst:
                    num1=int(num)
                    sum+=num1
        print(sum)
except(FileNotFoundError):
    print("File Not Found")