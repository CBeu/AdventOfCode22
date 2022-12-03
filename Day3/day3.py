import os

def loadData(path):
    with open(path,'r') as f:
        f_contents = f.read().splitlines()
        return f_contents

class Rucksack:
    def __init__(self, items):
        self.firstHalf = items[:len(items)//2]
        self.secondHalf = items[len(items)//2:]
        self.firstComp = self.fillComp(self.firstHalf)
        self.secondComp = self.fillComp(self.secondHalf)
        self.shared = ''.join(set(self.firstHalf).intersection(self.secondHalf))
        self.sharedComp = self.fillComp(self.shared)
        self.sharedSum = sum(self.sharedComp.values())

    def getCharPriority(self,char):
        if char.isupper():
            return((ord(char)-38))
        else:
            return((ord(char)-96))
    
    def fillComp(self, items):
        dic = {}
        for item in items:
            dic[item] = self.getCharPriority(item)
        return dic

# Part 1
def rucksackReorg(path):
    f = loadData(path)
    rucksacks = []
    for line in f:
        r = Rucksack(line)
        rucksacks.append(r)
    
    sums = 0
    for r in rucksacks:
        sums = sums + r.sharedSum
    return sums


print("Part1:\t",rucksackReorg('Day3/input.txt'))