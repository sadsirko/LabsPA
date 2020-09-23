import random
import os

def file_size(fPath):
        fInfo = os.stat(fPath)
        return round(fInfo.st_size / 1048576)
        
def createF(fName,size):

    with open(fName, "w") as file:
        a = 0
        strok = ''
        while True:
            for i in range(1,7):
                b = str(random.randint(0, 1000000)) 
                c = ' \n'
                strok = strok +  b + c 
              #  print (strok)
            file.write(strok )
            strok = ''
            if a != file_size(fName):
                a = file_size(fName)
                if a % 10 == 0:
                    print(a)
                if a == size:
                    break


#createF('test.txt',1)

