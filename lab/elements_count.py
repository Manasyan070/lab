def encode(sentence):
	count = 0
	final_sentence = ''
	letter_check = sentence[0]
	for letter in sentence:
		if letter_check == letter:
			count += 1
		else:
			final_sentence += letter_check
			final_sentence += str(count)
			count = 1
		letter_check = letter
	final_sentence += letter_check
	final_sentence += str(count)
	return final_sentence

def decode(encoded):
	final_decoded_sentence = ''
	for index in range(0,len(encoded),2):
		letter = encoded[index]
		count = int(encoded[index + 1])
		final_decoded_sentence += count * letter

	return final_decoded_sentence

if __name__ == '__main__':
	sentence = input('write a sentence: ')
	encoded = encode(sentence)
	print(encoded)
	# print(len(encoded))
	decoded = decode(encoded)
	print(decoded)


