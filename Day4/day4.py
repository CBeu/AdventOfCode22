import os


def loadData(path):
    with open(path,'r') as f:
        f_contents = f.read().splitlines()
        return f_contents

class Elf:
    def __init__(self, low, high):
        self.range = set(list(range(low,high+1)))
    
    def __str__(self):
        return f"Range: {self.range}"

class ElfPair:
    def __init__(self, elfA, elfB):
        self.elfA = elfA.range
        self.elfB = elfB.range
        self.overlap = self.rangeOverlap()
        self.fullOverlap = True if self.overlap == self.elfA or self.overlap == self.elfB else False
    
    def rangeOverlap(self):
        return self.elfA.intersection(self.elfB)


# Part 1
def fullContain(path):
    f = loadData(path)
    total = 0
    for line in f:
        ranges = line.split(",")
        pair = None
        for i in range(0,len(ranges),2):
            a = Elf(int(ranges[i].split("-")[0]),int(ranges[i].split("-")[1]))
            b = Elf(int(ranges[i+1].split("-")[0]),int(ranges[i+1].split("-")[1]))
            pair = ElfPair(a,b)
        
        total = total + 1 if pair.fullOverlap else total
    print(total)

# Part 2
def totalOverlaps(path):
    f = loadData(path)
    total = 0
    for line in f:
        ranges = line.split(",")
        pair = None
        for i in range(0,len(ranges),2):
            a = Elf(int(ranges[i].split("-")[0]),int(ranges[i].split("-")[1]))
            b = Elf(int(ranges[i+1].split("-")[0]),int(ranges[i+1].split("-")[1]))
            pair = ElfPair(a,b)
        total = total + 1 if len(pair.overlap) > 0 else total
    print(total)

fullContain('Day4/input.txt')
totalOverlaps('Day4/input.txt')