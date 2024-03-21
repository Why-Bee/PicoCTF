import sys

# grab the file from the netcat output

f = open('ncOut.txt')


string = ""
for line in f:
	string += chr(int(line))

print(string)