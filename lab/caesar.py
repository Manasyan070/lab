import random
shift = random.randint(1,26)
text = input('write a text: ')
encryption = ''
for c in text:
	if c.isupper():
		c_unicode = ord(c)
		c_index = ord(c) - ord('A')
		new_index = (c_index + shift) % 26
		new_unicode = new_index + ord('A')
		new_character = chr(new_unicode)
		encryption = encryption + new_character
	else:
		encryption += c
print("Plain text:",text)
print('shift:',shift)
print("Encrypted text:",encryption)