
def main():
	filepath = "books/frankenstein.txt"
	file_contents = get_book_text(filepath)
	word_count = get_book_words(file_contents)
	book_chars = get_chars_in_book(file_contents)

	print(book_chars)

def get_book_text(path):
	with open(path) as f:
		return f.read()
	
def get_book_words(book_text):
	word_counter = 0
	words = book_text.split()
	for word in words:
		word_counter += 1
	return word_counter
	# instead of looping through the list of words,
	# i can just return len(string_of_seperated_words)

def get_chars_in_book(book_text):
	char_count = {}
	book_lower = book_text.lower()
	for word in book_lower:
		if word not in char_count:
			char_count[word] = 1;
		else:
			char_count[word] += 1
	return char_count
	#instead of turning whole book to lowercase, I can
	#turn each character lower in the loop. 
	#Looping through a string is looping through characters

main()