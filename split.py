import sys

file = input("Enter the file name : ")

try:
    handle = open(file)
except:
    print("File Name Error")
    quit()

for line in handle:
    line = line.strip()
    if '*.' in line:
        with open('All_Wildcard.txt', 'a') as f:
            sys.stdout = f
            print(line)
            sys.stdout = sys.__stdout__ 


    else:

        with open('All_Subdomans.txt', 'a') as f:
            sys.stdout = f
            print(line)
            sys.stdout = sys.__stdout__ 



