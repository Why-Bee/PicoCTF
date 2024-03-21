




with open('message.txt', 'r') as f:
	contents = f.read()
	nums = [int(val) for val in contents.split()] 

message = ""
chars = " ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

for i in nums:
	print(pow((i%41), -1, 41))
	message += chars[pow((i%41), -1, 41)]
print(message)