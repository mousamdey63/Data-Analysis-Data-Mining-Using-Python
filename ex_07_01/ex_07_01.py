fh = open('words.txt')
for line in fh:   # loop
     print (line.upper().rstrip())
