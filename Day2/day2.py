import os
class Move:
    # Decodes the encrypted move and assigns point values of move
    def __init__(self,move):
        switcher = {
            "A" : ["Rock", 1],
            "B" : ["Paper",2],
            "C" : ["Scissors",3],
            "X": ["Rock", 1],
            "Y": ["Paper",2],
            "Z": ["Scissors",3],
        }
        self.move = switcher.get(move)[0]
        self.movePts = switcher.get(move)[1]
    
    def __str__(self):
        return f"Move Made: {self.move}, Move Points: {self.movePts}, Wins: {self.findWin().move}, Loses: {self.findLoss().move}, Draws: {self.findDraw().move}"
    
    # Returns pts for self versus antoerh Move 
    def versus(self,oppMove):
        if self.findWin().move == oppMove.move:
            return 6
        elif self.findLoss().move == oppMove.move:
            return 0
        else:
            return 3

    # Creates a Move that will lose to self
    def findWin(self):
        match self.move:
            case "Rock":
                return Move("C")
            case "Scissors":
                return Move("B")
            case "Paper":
                return Move("A")

    # Creates a Move that will win to self
    def findLoss(self):
        match self.move:
            case "Rock":
                return Move("B")
            case "Scissors":
                return Move("A")
            case "Paper":
                return Move("C")
    
    #return a Move that will darw to self
    def findDraw(self):
        return self

def loadData(path):
    with open(path,'r') as f:
        f_contents = f.read().splitlines()
        return f_contents

#part 1
#Col 1
# A = Rock
# B = Paper
# C = Scissors
#Col 2
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

# Using pure switch cases to determine score
def strategyGuide(path):
    score = []
    for line in loadData(path):
        score.append(roundResult(line.split()[0],line.split()[1]))
    return sum(score)

# Using Class Objects to determine score
def strategyGuideObjs(path):
    score = []
    for line in loadData(path):
        oppMove, myMove = Move(line.split()[0]), Move(line.split()[1])
        roundPts  = myMove.movePts + myMove.versus(oppMove)
        score.append(roundPts)
    return sum(score)

# Part 2 - Second Column how round needs to end
#Col 1
# A = Rock
# B = Paper
# C = Scissors
#Col 2
# X - Need to Loose
# Y - Need to Draw
# Z - Need to Win
#Results
# 0 = Lost
# 3 = Draw
# 6 = Win

def needsToEnd(path):
    score = []
    for line in loadData(path):
        oppMove = Move(line.split()[0])

        pass
    return (score)

print("Part 1:",strategyGuide('Day2/input.txt'))
print("Part 1:",strategyGuideObjs('Day2/input.txt'))
print("Part 2:",needsToEnd('Day2/test.txt'))





# def determineMove(oppMove, result):
#     score = 0
#     match result:
#         case "X":
#             score = 0
#             match oppMove:
#                 case "A":
#                     score = score + 
#                 case "B":
#                 case "C":
#         case "Y":
#             score = 3
#             match oppMove:
#                 case "A":
#                 case "B":
#                 case "C":
#         case "Z":
#             score = 6
#             match oppMove:
#                 case "A":
#                 case "B":
#                 case "C":
#     return score
