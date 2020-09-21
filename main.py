import os
import QuickS
import checkMem
import createFile

def createSeries(fName1,fName2):
     with open(fName1, "r") as fileS, open (fName2, "w") as file1 :
        sc = 1
        fi = fileS.readline()[:-1]
        sc = fileS.readline()[:-1]
        while sc != '':
            if fi == '':
                fi = sc
                sc = fileS.readline()[:-1]
            elif int(fi) > int(sc) :
                file1.writelines(fi)
                print(fi)
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
                # threr
                file1.writelines(a)
                print(a)
                #stop fi for first if
                fi = ''
            #sc = fileS.readline()[:-1]
createFile.createF('file1.txt',1)
createSeries('file1.txt','fileOut.txt')