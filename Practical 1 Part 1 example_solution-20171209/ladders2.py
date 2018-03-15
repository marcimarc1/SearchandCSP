import string
import sys
import collections
def write_solution(solution):
    realwordsolution = ([])
    for i in solution:
        if i == solution[-1]:
            realwordsolution.append(goali)
            break
        for words in realWordList:
            if i == solution[0]:
                realwordsolution.append(starti)
                break
            if compare(i, words):
                realwordsolution.append(words)
                break
    with open('output.txt','w') as f:
        for i in realwordsolution:
            f.write(i+"\n")
    f.close()

def verbleibend(word, remove):
    remainingchars = StringtoChar(word)
    for i in remove:
        buchstabe = 0
        for j in range(len(remainingchars)):
            if i in remainingchars[j]:
                buchstabe += 1
        if buchstabe < 2:
            if i in remainingchars:
                remainingchars.remove(i)
        else:
            remainingchars.remove(i)
            #remainingchars.append(i)
    return remainingchars

def solution( currentNode, GoalWord):
    goalPath = []
    goalPath.insert(0, GoalWord)

    while currentNode is not None:
        if currentNode.Pred is None:
            goalPath.insert(0, currentNode.word)
            break
        for words in WordList:
            WordsSorted = StringtoChar(words)
            WordsSorted.sort()
            WordsSorted = ''.join(WordsSorted)

            if WordsSorted == currentNode.word:
                goalPath.insert(0, WordsSorted)
                break

        currentNode = currentNode.Pred
    write_solution(goalPath)


class Node():
    def __init__(self, word, Pred = None):
        self.Pred = Pred
        self.word = word

    def setPred(self, pred):
        self.Pred = pred

def compare(string1, string2):
    '''Returns if the word has the same letters (not necessarily the same sequence'''
    return (collections.Counter(string1) == collections.Counter(string2))

alphabet = string.ascii_lowercase

def generateletterlists(startword, goalword):
    # compare total difference in letters
    letterremove = []
    letterapp = []
    for i in startword:
        if i not in goalword:
            letterremove.append(i)
    for i in goalword:
        if i not in startword:
            letterapp.append(i)
    return letterapp, letterremove

def StringtoChar(string):
    chars = []
    chars.extend(string)
    return chars

def createNode(chars, currentNode, append, GoalWord):
    global comingNodes
    global computedWords
    char = chars.pop(0)
    word = StringtoChar(currentNode.word)
    #global comingNodes
    #global computedWords
    if append:
        word.append(char)
    else:
        word.remove(char)

    word.sort()
    word = ''.join(word)

    if word == GoalWord:
        solution(currentNode, GoalWord)
        return True

    if word in WordList:
        if word in computedWords:
            return False
        comingNodes.append(Node(word, currentNode))
        computedWords.add(word)
        return False
    return False

def nodouble(liste):
    newlist = []
    for i in liste:
        liste.remove(i)
        if i not in liste:
            newlist.append(i)
    return newlist

def ladders(StartWord,GoalWord):
    while True:
        global comingNodes
        global computedWords
        if len(comingNodes)<= 0:
            print("no solution")
            break


        currentNode = comingNodes.pop(0)
        #first list of chars one have to remove
        _, removechars = generateletterlists(currentNode.word, GoalWord)

        remainingchars = verbleibend(currentNode.word, removechars)#list(set(StringtoChar(currentNode.word)) - set(removechars))
        #remainingchars.sort()
        removechars += remainingchars
        #generate a list with no double entrys
        #removechars = nodouble(removechars)

        #list of chars one have to add
        addchars, _ = generateletterlists(currentNode.word, GoalWord)
        #remaining characters in the alphabet that are not included adding
        remainingchars = verbleibend(alphabet, addchars)
        addchars += remainingchars
        #addchars = nodouble(addchars)

        if len(currentNode.word) >= len(GoalWord):
            # the current word is longer than the goal --> remove characters first


            for i in range(len(removechars)):
                if createNode(removechars, currentNode, False, GoalWord)==True:
                    return #comingNodes = createNode(removechars, currentNode, False, GoalWord, comingNodes, computedWords)

            for i in range(len(addchars)):
                if createNode(addchars, currentNode, True, GoalWord)==True:
                    return  #comingNodes = createNode(addchars, currentNode, True, GoalWord, comingNodes, computedWords)
        else:

            for i in range(len(addchars)):
                if createNode(addchars, currentNode, True, GoalWord)==True:
                    return  #comingNodes = createNode(addchars, currentNode, True, GoalWord, comingNodes, computedWords)

            for i in range(len(removechars)):
                if createNode(removechars, currentNode, False, GoalWord)==True:
                    return  #comingNodes = createNode(removechars, currentNode, False, GoalWord, comingNodes, computedWords)






#imports the word list and transform the strings
with open('wordList.txt') as f:
    WordList = set()
    realWordList = ([])
    for line in f:
        real = line[:-1]
        realWordList.append(real)
        temp = StringtoChar(line[:-1])
        temp.sort()
        WordList.add(''.join(temp))
f.close()


#getting start word and goal word
StartWord = sys.argv[1]
GoalWord = sys.argv[2]
goali = GoalWord
starti = StartWord
StartWord = (StringtoChar(StartWord))
GoalWord = (StringtoChar(GoalWord))
StartWord.sort()
GoalWord.sort()
StartWord = ''.join(StartWord)
GoalWord = ''.join(GoalWord)
a, b = generateletterlists(StartWord, GoalWord)

computedWords = set()
computedWords.add(''.join(StartWord))
comingNodes = [Node(StartWord)]


ladders(StartWord,GoalWord)