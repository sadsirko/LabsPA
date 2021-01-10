import random


class Player:
    def __init__(self, who):
        self.selfIs = who
        self.averageSum = 0
        self.turnSum = 0

    def addtoAvgSum(self):
        self.averageSum += self.turnSum
        self.turnSum = 0


class Roll:
    def __init__(self):
        self.arr = []
        self.dices = 5
        self.sum = 0

    def create(self):
        self.arr = []
        for i in range(0, self.dices):
            self.arr.append(0)

    def roll(self):
        self.create()
        for i in range(0, self.dices):
            self.arr[i] = random.randint(1, 6)

    def reroll(self, arrRel):
        if len(arrRel) == 0:
            arrRel = []
        else:
            for i in arrRel:
                self.arr[i - 1] = random.randint(1, 6)

    def check_roll(self):
        repeat = []
        para = [False, False]
        twoPara = False
        house = False
        three = False
        four = False
        five = False
        for i in range(6):
            repeat.append(0)
        for i in self.arr:
            repeat[i - 1] += 1
        # print(repeat)
        for i in repeat:
            if i == 5:
                self.sum = 50
                return 50
            if i == 4:
                self.sum = 40
                return 40
            if i == 3:
                three = True
            if i == 2:
                if not para[0]:
                    para[0] = True
                else:
                    para[1] = True
        if para[0] and three:
            self.sum = 30
            return 30
        if three:
            self.sum = 22
            return 22
        if para[0] and para[1]:
            self.sum = 18
            return 18
        if para[0] and not para[1]:
            self.sum = 12
            return 12
        return 0

class CompDecision:
    def __init__(self, arrRol, rollsLeft, yourScore = 0, enemyScore = 0, round = 0 ):
        self.arrRol = arrRol
        self.rollsLeft = rollsLeft
        self.yourScore = yourScore
        self.enemyScore = enemyScore
        self.round = round

    def analizeWhatToDo(self):
        rollLoc = Roll()
        rollLoc.create()
        rollLoc.arr = self.arrRol
        tmp = rollLoc.check_roll()
        if tmp == 0:
            return '1 2 3 4 5'
        maxChanceImprove = 0
        def checkOneDiceChange():
            arrOfChanges = []
            for i in range(len(self.arrRol)):
                arrOfChanges.append(0)
                for j in range(1,6):
                    loc = rollLoc.arr[i]
                    rollLoc.arr[i] = j
                    tmproll = rollLoc.check_roll()
                    rollLoc.arr[i] = loc
                    if tmproll > tmp:
                        arrOfChanges[i] += tmproll * 1/6

            return arrOfChanges

        def checkTwoDiceChange():
            arrOfChanges = []
            for i in range(len(self.arrRol)):
                arrOfChanges.append([])
                for j in range(len(self.arrRol)):
                    arrOfChanges[i].append(0)
                    if i < j:
                        for k in range(1, 6):
                            for l in range(1, 6):
                                    loc1 = rollLoc.arr[i]
                                    loc2 = rollLoc.arr[j]
                                    rollLoc.arr[i] = k
                                    rollLoc.arr[j] = l
                                    tmpRoll = rollLoc.check_roll()
                                    rollLoc.arr[i] = loc1
                                    rollLoc.arr[j] = loc2
                                    if tmpRoll > tmp:
                                        arrOfChanges[i][j] += tmpRoll * 1/36
            print(arrOfChanges)
            return arrOfChanges

        def checkThreeChange():
            arrOfChanges = []
            for i in range(len(self.arrRol)):
                arrOfChanges.append([])
                for j in range(len(self.arrRol)):
                    arrOfChanges[i].append(0)
                    if i < j:
                        for k in range(1, 6):
                            for l in range(1, 6):
                                loc1 = rollLoc.arr[i]
                                loc2 = rollLoc.arr[j]
                                rollLoc.arr[i] = k
                                rollLoc.arr[j] = l
                                tmpRoll = rollLoc.check_roll()
                                rollLoc.arr[i] = loc1
                                rollLoc.arr[j] = loc2
                                if tmpRoll > tmp:
                                    arrOfChanges[i][j] += tmpRoll * 1 / 36


        def maxInDoudleArr(arr):
            #print(arr)
            locmax = 0
            x = 0
            y = 0
            maxX = 0
            maxY = 0
            for i in arr:
                y += 1
                x = 0
                for j in i:
                    x +=1
                    if x > y:
                        if j > locmax:
                            locmax = j
                            maxX = x
                            maxY = y
            return locmax, maxY, maxX

        a = checkOneDiceChange()
        a1 = max(a)
        b = checkTwoDiceChange()
        b1, b2, b3 = maxInDoudleArr(b)
        #print(a)
        #print(b)
        #print('one change', a1)
        #print('two change', b1)
        tmptmp = str(b2) + ' ' + str(b3)
        #print(tmptmp)
        if a1 > b1:
            return a.index(a1)
        else:
            return tmptmp