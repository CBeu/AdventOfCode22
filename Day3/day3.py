import os

def loadData(path):
    with open(path,'r') as f:
        f_contents = f.read().splitlines()
        return f_contents

class Group:
    def __init__(self, r1, r2, r3):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.shared = self.shared()
    
    def shared(self):
        r12 = ''.join(set(self.r1.shared).intersection(self.r2.shared))
        r123 = ''.join(set(r12).intersection(self.r3.shared))

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
    
    def __str__(self):
        return f"shared:{self.sharedComp}"

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

# Part 2
def findBadge(path):
    f = loadData(path)
    groups = []
    group = []
    i = 0
    for line in f:
        if i <=2:
            i = i + 1
            group.append(Rucksack(line))
        else:
            groups.append(group)
            group = []
            i = 0
    return groups


print("Part1:\t",rucksackReorg('Day3/input.txt'))
print("Part1:\t",findBadge('Day3/test.txt')[0])