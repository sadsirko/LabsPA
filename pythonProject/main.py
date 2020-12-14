import random
import plCl

plM = compM = -1
pl1 = plCl.Player('player')
pl2 = plCl.Player('player')

while plM == compM:
    plM = random.randint(1, 6)
    compM = random.randint(1, 6)

if plM > compM:
    print('first turn will do man')
    pl2 = plCl.Player('computer')
else:
    print('first turn will do computer ')
    pl1 = plCl.Player('computer')

print('player first roll', plM)
print('PC first roll', compM)

def turn(first, second):
    print('--------------Round--------------')
    tryRoll = 1
    rollFive = plCl.Roll()
    arrOfReRoll = []
    print('Turn of ', first.selfIs)
    rollFive.roll()
    while (tryRoll < 4):
        for i in range(len(arrOfReRoll)):
            arrOfReRoll[i] = int(arrOfReRoll[i])
        rollFive.reroll(arrOfReRoll)
        print(rollFive.arr)
        locRes = rollFive.check_roll()
        print(locRes)
        a = 'n'
        if tryRoll < 3:
            print('want again? y/n')
            if first.selfIs == 'computer':
                a = 'y'
                if locRes > 22 and tryRoll == 1:
                    a = 'n'
            else:
                a = input()
        if a == 'y':
            if first.selfIs == 'computer':
                print('input arr what you want to change ?')
                test = plCl.CompDecision(rollFive.arr, 3 - tryRoll, 18, 18, 1)
                locloc = test.analizeWhatToDo()
                print(locloc)
                if type(locloc) == int:
                    arrOfReRoll = [locloc]
                else:
                    arrOfReRoll = locloc.split()
                tryRoll += 1
            else:
                print('input arr what  you want to change ?')
                arrOfReRoll = input().split()
                tryRoll += 1
        else:
            break
    first.turnSum = rollFive.sum
    first.addtoAvgSum()
    print('--------------')
    tryRoll2 = 1
    print('turn of ', second.selfIs)
    rollFive.roll()
    while (tryRoll2 <= tryRoll):
        for i in range(len(arrOfReRoll)):
            arrOfReRoll[i] = int(arrOfReRoll[i])
        rollFive.reroll(arrOfReRoll)
        print(rollFive.arr)
        print(rollFive.check_roll())
        a = 'n'
        if tryRoll2 < tryRoll:
            print('want reroll? y/n')
            if second.selfIs == 'computer':
                a = 'y'
                if locRes > 22 and tryRoll2 == 1:
                    a = 'n'
            else:
                a = input()
        if a == 'y':
            if second.selfIs == 'computer':
                print('input arr what you want to change ?')
                test = plCl.CompDecision(rollFive.arr, 3 - tryRoll, 18, 18, 1)
                locloc = test.analizeWhatToDo()
                print(locloc)
                if type(locloc) == int:
                    arrOfReRoll = [locloc]
                else:
                    arrOfReRoll = locloc.split()
                tryRoll2 += 1
            else:
                print('input arr what you want to change ? ')
                arrOfReRoll = input().split()
                tryRoll2 += 1
        else:
            break
    second.turnSum = rollFive.sum
    second.addtoAvgSum()

# a = plCl.Roll()
# a.roll()
# print(a.arr)
# test = plCl.CompDecision(a.arr, 3, 18, 18, 1)
# print(test.analizeWhatToDo())

turn(pl1, pl2)
turn(pl2, pl1)
turn(pl1, pl2)
#
print(pl1.selfIs, pl1.averageSum)
print(pl2.selfIs, pl2.averageSum)

# check count of percent
# result = []
# for j in range(0, 51):
#     result.append(0)
#
# for i in range(1, 1000):
#     tmp = turn(0, 0)
#     #print(turn(0, 0))
#     result[tmp] += 1
# print(result)
