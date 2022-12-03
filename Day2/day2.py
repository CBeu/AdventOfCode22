import os

#part 1
#Col 1
# A = Rock
# B = Paper
# C = Scissors
#Col 1
# X = Rock
# Y = Paper
# Z = Scissors
#Results
# 0 = Lost
# 3 = Draw
# 6 = Win

def roundResult(oppMove,myMove):
    score = 0
    match myMove:
        case "X":
            score = 1
            match oppMove:
                case "A":
                    score = score + 3
                case "B":
                    score = score + 0
                case "C":
                    score = score + 6
        case "Y":
            score = 2
            match oppMove:
                case "A":
                    score = score + 6
                case "B":
                    score = score + 3
                case "C":
                    score = score + 0
        case "Z":
            score = 3
            match oppMove:
                case "A":
                    score = score + 0
                case "B":
                    score = score + 6
                case "C":
                    score = score + 3
    return score

# Part 2 - Second Column how round needs to end
# X - Need to Loose
# Y - Need to Draw
# Z - Need to Win

def strategyGuide(path):
    score = []
    with open(path,'r') as f:
        f_contents = f.read().splitlines()
        for line in f_contents:
            score.append(roundResult(line.split()[0],line.split()[1]))
    return score

#part 2

print(sum(strategyGuide('Day2/input.txt')))
