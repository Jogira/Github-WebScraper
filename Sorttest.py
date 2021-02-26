import itertools

epicDict = {}
counter = 0
while counter != 4:
    username = input("\nKey ")
    epicDictionary = int(input("\nValue "))
    epicDict[username] = epicDictionary
    counter = counter+1


def sortByValue():
    print(epicDict)
    sortedByKeyDict = dict(sorted(epicDict.items(),
                              key=lambda item: item[1],
                              reverse=True))
    print(sortedByKeyDict)
    D2 = dict(itertools.islice(sortedByKeyDict.items(), 2))
    print(D2)
    print('\n'.join("{}, {}".format(k,v) for k, v in D2.items()))


if __name__ == '__main__':
    sortByValue()