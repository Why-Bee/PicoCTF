# grab the enc file

encoded = open('enc').read()

#''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

flag = ""

for i in encoded:
	letter1 = chr(ord(i) >> 8)
	letter2 = chr(ord(i) & 255)
	flag += letter1 + letter2

print(flag)
