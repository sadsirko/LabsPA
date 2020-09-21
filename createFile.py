import random
import os

def createF(fName,size):
    def file_size(fPath):
        fInfo = os.stat(fPath)
        return round(fInfo.st_size / 1048576)


    with open(fName, "w") as file:
        a = 0
        strok = ' '
        while True:
            for i in range(1,7):
                b = str(random.randint(0, 1000000)) 
                c = ' \n'
                strok = strok +  b + c 
              #  print (strok)
            file.write(strok )
            strok = ''
            if a != file_size(fName):
                print(file_size(fName))
                a = file_size(fName)
                if a == size:
                    break


