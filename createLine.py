import os
import QuickS
import checkMem
import createFile
import fibo
import merge2file
import createFile

# create file with series in it - fName2
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
    return countOfSeries           
#createFile.createF('file1.txt',100)


# There we distribute one file on two with fib numbers
def create2Files(fNameIn,fNameI,fNameII,series):
    firsrtF , secF, summ = fibo.fibonacci(series)
    #print(firsrtF , secF, summ)
    f = open(fNameIn).readlines()
    s = open(fNameIn).readlines()
    length = len(f)
    while len(f) > secF:
        f.pop(len(f) - 1)
    for i in range(0,secF):    
        s.pop(0)
    #add empty elements    
    while len(s) < firsrtF:
        s.append('\n')
    with open(fNameI,'w') as F1, open(fNameII,'w') as F2:
        F1.writelines(f)
        F2.writelines(s)


series = (createSeries('test.txt','fileOut.txt'))
create2Files('fileOut.txt','ser1.txt','ser2.txt',series)

def fibMerge(fName1,fName2,fName3):
    with open(fName1, "r") as file1, open (fName2, "r") as file2, open (fName3, "r") as file3 :
        merge2file.merge2filesto3(fName1, fName2, fName3)
        a = file1.read() == ''
        b = file2.read() == ''
        c = file3.read() == ''
        while not ((a and b) or (a and c) or (b and c)):
            if a :
                merge2file.merge2filesto3(fName3, fName2, fName1 )
            elif b :
                merge2file.merge2filesto3(fName3, fName1, fName2 )
            elif c :
                merge2file.merge2filesto3(fName1, fName2, fName3 )
            a = file1.read() == ''
            b = file2.read() == ''
            c = file3.read() == ''
            print(a,b,c)

fibMerge('ser1.txt','ser2.txt','serJoined.txt')
#for i in range(0,10):
 #   print('merge')
#merge2file.merge2filesto3('ser1.txt','ser2.txt','serJoined.txt' )
#merge2file.merge2filesto3('serJoined.txt','ser1.txt','ser2.txt' )
#merge2file.merge2filesto3('ser2.txt','serJoined.txt','ser1.txt' )
with open('serJoined.txt', "r") as file1:
    print(file1.read() == '')

#merge2file.merge2filesto3('ser1.txt','ser2.txt','serJoined.txt' )
#merge2file.merge2filesto3('serJoined.txt','ser1.txt','ser2.txt' )
#merge2file.merge2filesto3('ser2.txt','serJoined.txt','ser1.txt' )
     
#merge2file.merge2filesto3('ser1.txt','ser2.txt','serJoined.txt' )
#merge2file.merge2filesto3('serJoined.txt','ser1.txt','ser2.txt' )

       