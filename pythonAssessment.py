with open('article.txt', 'r') as file:
	text = " ".join(line.rstrip() for line in file)

print(text)

	