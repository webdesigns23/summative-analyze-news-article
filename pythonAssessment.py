import re
from collections import Counter

# Read article in to string variable      
def load_article(file_path):
    with open(file_path, 'r') as file:
        return file.read()
     
#Count Specific Word
def count_specific_word(text, word):
    if not text.strip():
          return 0
    words = re.findall(r'\b\w+\b', text.lower())
    count = words.count(word.lower())
    return count

#Identify Most Common Word
def identify_most_common_word(text):
	words = text.split()
	word_count = Counter(words)
	most_common = max(word_count, key=word_count.get)
	return most_common

#Calculate Average Word Length
def calculate_average_word_length(text):
    words = text.split()
    if not words:
        return 0

    total_length = sum(len(word.strip(".,!?;:")) for word in words)
    average_lenth = total_length / len(words)
    return round(average_lenth , 2)

#Count Number of Paragraphs
def count_paragraphs(text):
    if not text.strip():
        return 1
    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    paragraph_count = len(paragraphs)
    return paragraph_count

#Count Number of Sentences
def count_sentences(text):
    if not text.strip():
        return 1
    sentence_endings = {".", "!", "?"}
    count = 0 
    for index in range(len(text)):
        if text[index] in sentence_endings:
             if index == len(text) - 1 or text[index + 1] == " ":
                  count += 1
    return count  	

# Main Text Analysis Function
def main():
    file_path = 'article.txt'
    text = load_article(file_path)
    
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
            count = count_specific_word(text, word)
            print(f"{count}")            
        elif choice == "2":
            word = identify_most_common_word(text)
            print(f"{word}")
        elif choice == "3":
            word_length = calculate_average_word_length(text)
            print(f"{word_length}")
        elif choice == "4":
            number_of_p = count_paragraphs(text)
            print(f"{number_of_p}")
        elif choice == "5":
            number_of_s = count_sentences(text)
            print(f"{number_of_s}")
        elif choice == "6":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()

