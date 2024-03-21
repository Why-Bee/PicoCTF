# Script to decode the password of user 'cultiris'

usernames = []
passwords = []

with open ('usernames.txt', 'r') as f:
	usernames = f.read().split()

with open ('passwords.txt', 'r') as f:
	passwords = f.read().split()

pwd = passwords[usernames.index('cultiris')]
print(pwd)