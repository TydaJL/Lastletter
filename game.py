print("Welcome to Lastletter!")
print("Please Pick a Mode:")
print("1: 10000 Most Common English Words")


words = open("text_samples/english_10000_words.txt", "r")
wordsString = words.read()
print(wordsString)