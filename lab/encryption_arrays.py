def encrypt(sentence):
	for_search = ['a','b','c','d','e','f','g','h','i','j','k','l','q','t','w','z']
	key = ['k','x','g','h','v','c','q','y','a','b','t','s','d','i','z','u']
	encrypted_sentence = ''
	for letter in sentence:
		if letter in for_search:
			index_ecrypted_letter = for_search.index(letter)
			encrypted_letter = key[index_ecrypted_letter]
			encrypted_sentence += encrypted_letter
		else:
			encrypted_sentence += letter
	return encrypted_sentence

if __name__ == '__main__':
	sentence_for_encrypt = input('write a sentence: ')
	result = encrypt(sentence_for_encrypt)
	print(result)
