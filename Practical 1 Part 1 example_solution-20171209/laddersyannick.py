import sys
#import characters
import string

def charDifference(current, goal):
    """
    Generates a list of characters that are present in current but not in goal

    :param current:     list of characters in current word
    :param goal:        list of characters in goal word
    :return:            list of characters that appear in current but not in goal
    """

    diff = current

    for c in goal:
        if c in diff:
            diff.remove(c)

    return diff


def stringToList(word):
    """
    Generates a list of characters that represent the given string

    :param word:        the string to be represented as a list
    :return:            the list representation of the string
    """

    chars = []
    chars.extend(word)
    return chars


class Node:
    def __init__(self, word, pred=None):
        self.__word = word
        self.__pred = pred

    def setPred(self, pred):
        self.__pred = pred

    def getPred(self):
        return self.__pred

    def getWord(self):
        return self.__word


realStartWord = 'croissant'#sys.argv[1]
realGoalWord = 'baritone'#sys.argv[2]

# start word in alphabetical order
startWord = stringToList(realStartWord)
startWord.sort()
startWord = ''.join(startWord)
# goal word in alphabetical order
goalWord = stringToList(realGoalWord)
goalWord.sort()
goalWord = ''.join(goalWord)

computedWords = set()
computedWords.add(startWord)
comingNodes = [Node(realStartWord)]

f = open("Practical 1 Part 1 example_solution-20171209/wordList.txt")
words = set()
realWords = []
for line in f:
    lineList = stringToList(line[:-1])
    lineList.sort()
    words.add(''.join(lineList))
    realWords.append(line[:-1])


def uniqueList(l):
    res = []
    seen = set()

    for elem in l:
        if elem not in seen:
            res.append(elem)
            seen.add(elem)

    return res


def createNewNode(chars, currentNode, remove):
    char = chars.pop(0)
    newWord = stringToList(currentNode.getWord())

    if remove:
        newWord.remove(char)
    else:
        newWord.append(char)

    newWord.sort()

    newWord = ''.join(newWord)

    if newWord == goalWord:
        # goal word has been found
        goalPath = []
        goalPath.insert(0, realGoalWord)
        while currentNode is not None:
            if currentNode.getPred() is None:
                # write the real start word, not the alphabetically ordered one
                goalPath.insert(0, currentNode.getWord())
                break

            # find a real word to the given alphabetically ordered word
            for possibleWord in realWords:
                possibleWordSorted = stringToList(possibleWord)
                possibleWordSorted.sort()
                possibleWordSorted = ''.join(possibleWordSorted)

                if possibleWordSorted == currentNode.getWord():
                    goalPath.insert(0, possibleWord)
                    break

            currentNode = currentNode.getPred()

        f = open('output.txt', 'w')
        for node in goalPath:
            f.write(node + "\n")
        f.close()

        return True

    if newWord in words:
        # newWord is a valid word
        if newWord in computedWords:
            # newWord has already been computed
            return False
        comingNodes.append(Node(newWord, currentNode))
        computedWords.add(newWord)
        return False

    # newWord is not valid
    return False


def main():
    while len(comingNodes) > 0:
        currentNode = comingNodes.pop(0)

        # characters that appear in the current word but not in the goal word.
        # list(set(charDifference)) makes unique list
        charsToBeRemoved = list(set(charDifference(stringToList(currentNode.getWord()), stringToList(goalWord))))

        remainingChars = list(set(charDifference(stringToList(currentNode.getWord()), charsToBeRemoved)))

        charsToBeRemoved += remainingChars

        charsToBeRemoved = uniqueList(charsToBeRemoved)


        # characters that appear in the goal word but not in the current word
        charsToBeAdded = list(set(charDifference(stringToList(goalWord), stringToList(currentNode.getWord()))))

        remainingChars = list(set(charDifference(set(string.ascii_lowercase), charsToBeAdded)))
        charsToBeAdded += remainingChars
        charsToBeAdded = uniqueList(charsToBeAdded)


        if len(currentNode.getWord()) >= len(goalWord):
            # the current word is longer than the goal --> remove characters first

            # create new words by removing characters
            while (len(charsToBeRemoved) > 0):
                if createNewNode(charsToBeRemoved, currentNode, True):
                    return

            # create new words by adding characters
            while (len(charsToBeAdded) > 0):
                if createNewNode(charsToBeAdded, currentNode, False):
                    return
        else:
            # the current word is shorter than the goal --> add characters first

            # create new words by adding characters
            while (len(charsToBeAdded) > 0):
                if createNewNode(charsToBeAdded, currentNode, False):
                    return

            # create new words by removing characters
            while (len(charsToBeRemoved) > 0):
                if createNewNode(charsToBeRemoved, currentNode, True):
                    return

    # no solution was found
    open('output.txt', 'w').close()

main()
