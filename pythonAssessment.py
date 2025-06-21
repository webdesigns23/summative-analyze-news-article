from text_analysis_manager.validation import validate_task_word
from collections import Counter

# Read article in to string variable      

def string_article(file_path):
    with open(file_path, 'r') as file:
        return file.read()
     

# file_path = 'article.txt'

# with open(file_path, 'r') as file:
#   text = file.read()



#Count Specific Word
def word_occurance_count(text, word):
    try:
        validate_task_word(word)

        if not text.strip():
            print(f"The word '{word}' occurs 0 time(s) in the article.")
            return 0

        words = text.lower().split()
        word_count = Counter(words)
        if word.lower() in words:
            number = word_count[word.lower()]
            print(f"The word '{word}' occurs {number} time(s) in the article.")
            return number
        else:
            print(f"The word '{word}' does not occur in the article.")
            return 0
    except ValueError as e:
        print(e)
        return 0

#Identify Most Common Word
def most_common_word(text):
	words = text.split()
	word_count = Counter(words)
	most_common = max(word_count, key=word_count.get)
	print(most_common)

#Calculate Average Word Length
def average_word_length(text):
	words = text.split()
	total_length = sum(len(word) for word in words)
	num_words = len(words)

	if num_words > 0:
		average_length = total_length / num_words
		print(f"The average word length is: {average_length:.2f}")
	else:
		print("No words in article")
	
#Count Number of Paragraphs
def num_of_paragraphs(text):
	paragraphs = [p for p in text.split('\n\n') if p.strip()]
	paragraph_count = len(paragraphs)
	print(f"Number of paragraphs: {paragraph_count}")

#Count Number of Sentences
def num_of_sentences(text):
    sentence_endings = {".", "!", "?"}
    count = 0 
    for index in range(len(text)):
        if text[index] in sentence_endings:
             if index == len(text) - 1 or text[index + 1] == " ":
                  count += 1
    print(f"Number of sentences in article: {count}")    	

# Main Text Analysis Function
def main():
    file_path = 'article.txt'
    text = string_article(file_path)

    while True:
        print("Text Analysis System")
        print("1. Count Specific Word Occurance")
        print("2. Identify Most Common Word")
        print("3. Calculate Average Word Length")
        print("4. Count Number of Paragraphs")
        print("5. Count Number of Sentences")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            word = input("What would would you like to search the occurance of: ")
            word_occurance_count(text, word)             
        elif choice == "2":     
            most_common_word(text)
        elif choice == "3":
            average_word_length(text)
        elif choice == "4":
            num_of_paragraphs(text)
        elif choice == "5":
            num_of_sentences(text)
        elif choice == "6":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()

