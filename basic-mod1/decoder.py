import sys

def mod37(val):
	charSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

	return (charSET[val%37])


msg = ""

with open('message.txt', 'r') as file:
	c = file.read()
	nums = [int(val) for val in c.split()]		

for num in nums:
	msg += mod37(num)


print (msg)