
def main():
	filepath = "books/frankenstein.txt"
	file_contents = get_book_text(filepath)
	word_count = get_book_words(file_contents)

	print(word_count)

def get_book_text(path):
	with open(path) as f:
		return f.read()
	
def get_book_words(book_text):
	word_counter = 0
	words = book_text.split()
	for word in words:
		word_counter += 1
	return word_counter


main()