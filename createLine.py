import os
import QuickS
import checkMem
import createFile


def createSeries(fName1,fName2):
    countOfSeries = 0
    with open(fName1, "r") as fileS, open (fName2, "w") as file1 :
        sc = 1
        fi = fileS.readline()[:-1]
        sc = fileS.readline()[:-1]
        while sc != '':
            if fi == '':
                fi = sc
                sc = fileS.readline()[:-1]
            elif int(fi) > int(sc) :
                file1.write(fi + '\n')
                countOfSeries += 1
                #print(fi)
                fi = sc 
                sc = fileS.readline()[:-1]
            else:
                #fi[:-1]
                a = fi 
                while int(fi) < int(sc):  
                    fi = sc
                    sc[:-1]
                    a = a + sc 
                    sc = fileS.readline()[:-1]
                    if(sc == '') : 
                        break
                # threr
                file1.write(a + '\n')
                countOfSeries += 1
                #print(a )
                #stop fi for first if
                fi = ''
            if(sc == '') : 
                break
    print(countOfSeries)            
createFile.createF('file1.txt',100)
createSeries('file1.txt','fileOut.txt')
