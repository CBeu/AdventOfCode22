import os


def loadData(path):
    with open(path,'r') as f:
        f_contents = f.read().splitlines()
        return f_contents

class Rucksack:
    def __init__(self, items):
        self.items = items
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
        return f"self:{self.firstHalf}{self.secondHalf} shared:{self.sharedComp}\n"

class Group:
    def __init__(self, g):
        self.r1 = Rucksack(g[0])
        self.r2 = Rucksack(g[1])
        self.r3 = Rucksack(g[2])
        self.shared = self.shared()
        self.sharedSum = self.getCharPriority(self.shared)

    def getCharPriority(self, items):
        sums = 0
        for i in items:
            if i.isupper():
                sums = sums + ((ord(i)-38))
            else:
                sums = sums +((ord(i)-96))
        return sums
    
    def shared(self):
        r123 = ''.join(set(set(self.r1.items).intersection(self.r2.items)).intersection(self.r3.items))
        return r123
    
    def __str__(self):
        return f"shared:{self.r1} {self.r2} {self.r3}"

# Part 1
def rucksackReorg(path):
    f = loadData(path)
    sums = 0
    for line in f:
        r = Rucksack(line)
        sums = sums + r.sharedSum
    return sums

# Part 2
def findBadge(path):
    f = loadData(path)
    split = [f[i * 3:(i + 1) * 3] for i in range((len(f) + 3 - 1) // 3 )]
    sums = 0
    for i in split:
        g = Group(i)
        sums = sums + g.sharedSum
    return sums


print("Part1:\t",rucksackReorg('Day3/input.txt'))
print("Part2:\t",(findBadge('Day3/input.txt')))