import os

#part 1
def getMaxCals():
    with open('Day1\input.txt','r') as f:
        f_contents = f.readlines()
        totals = []
        sum = 0
        for line in f_contents:
            if (len(line) ==1):
                totals.append(sum)
                sum = 0
            else:
                sum = sum + int(line)
        return(sorted(totals,key=int,reverse=True))

#part 2

def main():
    print("Part 1: ", getMaxCals()[0])
    print("Part 2: ", sum(getMaxCals()[0:3]))

if __name__ == '__main__':
    main()