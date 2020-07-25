filename = input ("Enter The File Name: ")
fhand = open(filename, 'r')

email_addresses = {}
for line in fhand:
    if line.startswith("From "):
        email = (line.split()[1])
        email_addresses[email] = email_addresses.get(email,0)+1

print(email_addresses)
