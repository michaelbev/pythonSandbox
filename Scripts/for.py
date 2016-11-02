def printBreak():
	print("------------")

def printWords(theWords):
    for w in theWords:
	    print(w,len(w))

def sortWordsByLength(theWords):
	for w in theWords:
		for i in range(len(wordsSortedByLength)):
			if len(w) > len(wordsSortedByLength[i]):
				wordsSortedByLength.insert(i,w)
				break
		else:
			wordsSortedByLength.append(w)


def main():
	printWords(words)
	printBreak()
	sortWordsByLength(words[1:])
	printWords(wordsSortedByLength)


# Measure some strings
words = ['happy','cat', 'window', 'defensive', 'gophery']
wordsSortedByLength = [words[0]]
main()