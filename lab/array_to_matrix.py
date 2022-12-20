import numpy as np
import math

def getting_key(sentence,len_sentence):
	size_matrix = math.sqrt(len_sentence)
	size_matrix = math.ceil(size_matrix)
	sentence += (size_matrix**2 - len_sentence) * '-'
	current_sentence = np.empty(size_matrix**2, dtype = str)	
	index = 0
	for letter in sentence:
		current_sentence[index] = letter
		index += 1
	sentence_for_encode = np.reshape(current_sentence, (size_matrix, size_matrix))
	return sentence_for_encode


def encode(key):
	encoded_sentence = ''
	for row in range(0,len(key)):
		for col in range(0,len(key)):
			encoded_sentence += key[col][row]
	return encoded_sentence


if __name__ == '__main__':
	sentence = input('write a sentence: ')
	len_sentence = len(sentence)
	key = getting_key(sentence,len_sentence)
	print('key:\n ',key)
	encrypted_sentence = encode(key)
	print('encrypted sentence: ',encrypted_sentence)