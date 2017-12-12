#!/usr/bin/python
'''
    A B C D E F G H I J K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
    -------------------------------------------------------------------
    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
'''

def helper(message, shift):
	message = message.lower()
	secret = ""
	for c in message:
		if c in "abcdefghijklmnopqrstuvwxyz":
			num = ord(c)
			num += shift
			if num > ord("z"):     # wrap if necessary
				num -= 26
			elif num < ord("a"):
				num += 26
			secret = secret + chr(num)
		else:
			# don't modify any non-letters in the message; just add them as-is
			secret = secret + c
	return secret

# Encrypts the given string using a Caesar cipher and returns the result.
def encrypt(message):
	return helper(message, 3)

# Decrypts a string that was previously encrypted using a Caesar cipher and returns the result.
def decrypt(message):
	return helper(message, -3)


# main program
msg = "ramin" #input("Your message to encode? ")
if len(msg) > 0:
	# wants to encrypt
	secret = encrypt(msg)
	print("The encoded message is:", secret)
	if len(secret) > 0:
		msg = decrypt(secret)
		print("The decoded message is:", msg)
