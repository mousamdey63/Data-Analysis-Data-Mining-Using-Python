import re

filename = input("Enter The File Name : ")
filehand = open(filename, 'r')
nums = list()

for line in filehand:
    line = line.rstrip()
    numlist = re.findall("[0-9]+",line)
    nums = nums + numlist

sum = 0
for value in nums:
    sum = sum + int(value)
print(sum)
