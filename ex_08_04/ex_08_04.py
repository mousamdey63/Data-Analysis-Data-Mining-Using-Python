words = []

fname = input("Enter File Name: ")
fhand = open(fname)

for line in fhand:
    line = line.rstrip()

    for word in line.split(' '):    # nested loop
        if word not in words:         # words in not in alphabetical order
            words.append(word)

print(sorted(words))
