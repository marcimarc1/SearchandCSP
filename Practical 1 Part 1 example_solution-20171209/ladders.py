import collections
import queue as q
import string
import pickle
import os
def compare(string1, string2):
    '''Returns if the word has the same letters (not necessarily the same sequence'''
    return (collections.Counter(string1) == collections.Counter(string2))


def possibleWords(startword, letterremove, letterapp, WordList):
    '''computation of possible words of wordlist, maybe we need to append this function by some variable append/remove
    letter'''
    listofWords = ([])
    for i in letterremove:
        for words in WordList:  # TODO: nur 1 buchstabe wird remove, auch wenn 2 im wort sind
            buchstabe = 0
            for j in range(len(startword)):
                if i in startword[j]:
                    buchstabe += 1
            if buchstabe < 2:
                if compare(startword.replace(i, ""), words) and words not in listofWords:
                    listofWords.append(words)
                    break
            else:
                if compare(startword.replace(i, "") + (buchstabe - 1) * i, words) and words not in listofWords:
                    listofWords.append(words)
    for i in letterapp:
        for words in WordList:
            if compare(startword + i, words) and words not in listofWords:
                listofWords.append(words)
                break
    for Words in listofWords:
        for i in letterremove:
            for words in WordList:
                buchstabe = 0
                for j in range(len(words)):
                    if i in words[j]:
                        buchstabe += 1
                if buchstabe < 2:
                    if compare(Words.replace(i, ""), words) and words not in listofWords:
                        listofWords.append(words)
                        break
                else:
                    if compare(Words.replace(i, "") + (buchstabe - 1) * i, words) and words not in listofWords:
                        listofWords.append(words)
                        break

        for i in letterapp:
            for words in WordList:
                if compare(Words + i, words) and words not in listofWords:
                    listofWords.append(words)
                    break

    return listofWords


def BuildingMatrix(WordList):
    WordMatrix = {}
    Alphabet = string.ascii_lowercase
    for words in WordList:
        WordMatrix[words] = ([])
        for characters in Alphabet:  # check addition
            for change in WordList:
                if compare(words + characters, change):
                    WordMatrix[words].append(change)
                    break

    return WordMatrix


def BuildingaGraph(append, remove, listofWords, WordList):
    '''Builds the graph's adjacency list'''
    graph = ([])

    return graph


def bfs(graph, start, goal):
    ''' needs a dictionary (an adjacency list)'''
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def ladders(startword, goalword, WordList):
    # compare total difference in letters
    letterremove = ([])
    letterapp = ([])
    for i in startword:
        if i not in goalword:
            letterremove.append(i)
    for i in goalword:
        if i not in startword and i not in letterapp:
            letterapp.append(i)

    listofWords = possibleWords(startword, letterremove, letterapp, WordList)

    graph = BuildingaGraph(letterapp, letterremove, listofWords, WordList)

    return graph


def save_obj(obj, name):
    with open(os.getcwd() + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(os.getcwd() + name + '.pkl', 'rb') as f:
        return pickle.load(f)

with open('wordList.txt') as f:
    WordList = set()
    for line in f:
        temp = line[:-1]
        WordList.add(temp)
f.close()

ladders("croissant", "baritone", WordList)
#liste = BuildingMatrix(WordList)

#d = {"a":1,"b":2}
#save_obj(d, 'liste')
#e = load_obj( 'liste' + '.pkl')

#print(e)