
def main():
	filepath = "books/frankenstein.txt"
	file_contents = get_book_text(filepath)
	word_count = get_book_words(file_contents)
	book_chars = get_chars_in_book(file_contents)
	char_list = dict_into_char_list(book_chars)

	char_list.sort(key=sort_on, reverse=True)

	generate_report(filepath, word_count, char_list)
	
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

def dict_into_char_list(char_dict):
	char_list = []
	for k, v in char_dict.items():
		new_dict = {"char":k,"val":v}
		if new_dict["char"].isalpha():
			char_list.append(new_dict)
	return char_list

def sort_on(dict):
	return dict["val"]

def generate_report(book_name, num_words, sorted_chars):
	print(f"-- Begin report of {book_name} ---")
	print(f"{num_words} words found in the document")
	print()
	for item in sorted_chars:
		print(f"The '{item["char"]}' character was found {item["val"]} times")
	print("--- End report ---")
	pass

main()