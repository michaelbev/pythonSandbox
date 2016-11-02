def printBreak(title):
    """Prints a dotted line"""
    print("------" + title + "------")


def printWords(theWords):
    """Prints the passed array with word length and word"""
    for w in theWords:
        print(len(w), w)


def sortWordsByLength(theWords):
    """Word array sorted by length"""
    for w in theWords:
        for i in range(len(wordsSortedByLength)):
            if len(w) > len(wordsSortedByLength[i]):
                wordsSortedByLength.insert(i, w)
                break
        else:
            wordsSortedByLength.append(w)

def sortWordsByReverseAlphabet(theWords):
    """Word array sorted by reverse alphabet"""
    for word in theWords:
        for i in range(len(wordsSortedByReverseAlphabet)):
            for letter in range(len(word)):
                print(word[letter] + " : " + wordsSortedByReverseAlphabet[i][0])
                if word[letter] > wordsSortedByReverseAlphabet[i][0]:
                     wordsSortedByReverseAlphabet.insert(i, word)
                     break
                else:
                     wordsSortedByReverseAlphabet.append(word)
                     break


def main():
    printBreak("Initial word array")
    printWords(words)
    printBreak(sortWordsByLength.__doc__)
    sortWordsByLength(words[1:])
    printWords(wordsSortedByLength)
    printBreak(sortWordsByReverseAlphabet.__doc__)
    sortWordsByReverseAlphabet(words[1:])
    printWords(wordsSortedByReverseAlphabet)


# Sort some strings
words = ['happy', 'cats', 'window', 'appetizers'] #, 'gophery', 'cat', 'widow', 'it', 'perky']
wordsSortedByLength = [words[0]]
wordsSortedByReverseAlphabet = [words[0]]
main()
