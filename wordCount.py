import re  # Regular Expression tools
import sys  # Command line arguments


# splitting text into a list of words
def split(text):
    if text is not None:
        for char in '"-.,\'\n':
            text = text.replace(char, ' ')
            text = text.lower()
        words = text.split()
        return words
    else:
        return None


# Creating dictionary based on list of words
def createDict(wordList):
    myDict = {}
    if wordList is not None:
        for element in wordList:
            # Cleaning characters from words
            word = re.sub(r'[^\w\s]', '', element)
            # If it exists, increment counter
            if word in myDict:
                myDict[word] += 1
            # new word into dictionary
            else:
                myDict[word] = 1
        return myDict
    else:
        return None


def main():
    # User Input
    inputFname: int = sys.argv[1]
    outputFname = sys.argv[2]

    inFile = open(inputFname, "r")
    text = inFile.read()
    # Writing to file
    outFile = open(outputFname, "w+")

    words = split(text)
    newDict = createDict(words)

    # Sorting, then writing to output file
    for key, val in sorted(newDict.items()):
        toFile = key + " " + str(val)
        outFile.write(toFile + '\n')
    outFile.close()


if __name__ == "__main__":
    main()
