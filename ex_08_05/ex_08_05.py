filename = input("Enter The File Name: ")
count = 0
fhand = open(filename, 'r')


for line in fhand:
    if line.startswith('From:'):
       print(line.split()[1])
       count += 1                   # short form of (count = count + 1)
print("There were",count,"lines in the file with From as the first word")
