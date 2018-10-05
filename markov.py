"""Generate Markov text from text files."""

import sys
from random import choice
input_path = sys.argv[1]


def open_and_read_file(file_path):
	"""Take file path as string; return text as string.
	Takes a string that is a file path, opens the file, and turns
	the file's contents as one string of text.
	"""
	text = open(file_path,"r")
	text_string = text.read()
	return text_string


def make_chains(text_string):
	"""Take input text as string; return dictionary of Markov chains.
	A chain will be a key that consists of a tuple of (word1, word2)
	and the value would be a list of the word(s) that follow those two
	words in the input text.
	For example:
		>>> chains = make_chains("hi there mary hi there juanita")
	Each bigram (except the last) will be a key in chains:
		>>> sorted(chains.keys())
		[('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]
	Each item in chains is a list of all possible following words:
		>>> chains[('hi', 'there')]
		['mary', 'juanita']
		
		>>> chains[('there','juanita')]
		[None]
	"""
	chains = {}
	text_string_list = text_string.rstrip().split()
	n_gram_length = int(input("How long do you want your keys to be? (ints only plz kthxbai)"))
	for i in range(len(text_string_list) - n_gram_length):
		# bigram = (text_string_list[i], text_string_list[i + 1])
		n_gram = tuple(text_string_list[i:i+n_gram_length])
		next_word = text_string_list[i+n_gram_length]
		# if not bigram in chains:
		# 	chains[bigram] = []
		# chains[bigram].append(next_word)
		if not n_gram in chains:
			chains[n_gram] = []
		chains[n_gram].append(next_word)
	return chains
	


def make_text(chains):
	
	"""Return text from chains."""

	# keys_list=list(chains.keys())
	# random_first_key = choice(keys_list)
	# words = list(random_first_key)

	# n = 0
	# while True:
	# 	link = words[n], words[1 + n]
	# 	if chains.get(link, False):
	# 		link_value = choice(chains[link])
	# 		words.append(link_value)
	# 		n += 1
	# 	else:
	# 		return " ".join(words)

	keys_list=list(chains.keys())
	while True:
		random_first_key = choice(keys_list)
		if random_first_key[0][0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			break
		
	n_gram_length = len(random_first_key)
	words = list(random_first_key)

	n = 0
	while True:
		link = tuple(words[n: n + n_gram_length])
		if chains.get(link, False):
			link_value = choice(chains[link])
			words.append(link_value)
			n += 1
		else:
			return " ".join(words)


# input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

# print(chains)