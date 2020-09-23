import os

def toStr(arr):
    str1 = " "
    return(str1.join(arr))

def merge2ser(str1,str2):
    
    str1 = str(str1)[:-1].split(' ')
    str2 = str(str2)[:-1].split(' ')
    if str1[len(str1) - 1] == '':
        str1.pop(len(str1) - 1)
    if str2[len(str2) - 1] == '':
        str2.pop(len(str2) - 1)
        

    strRes = []
    Ind1, Ind2 = 0, 0
    #print( str1)
    #print( str2)
    if str1 == ['']: 
        return toStr(str2)
    elif str2 == ['']:
        return toStr(str1)        
    a = len(str1) >= 1 or len(str2) >= 1
    while a :
        if   len(str1) == 0 :
            strRes = strRes + str2
            break
        elif  len(str2) == 0 :
            strRes = strRes + str1
            break
        f = str(str1[0])
        s = str(str2[0])
        if int(f) < int(s):
            strRes.append(f)
            str1.pop(0)
        elif int(s) < int(f):
            strRes.append(s)
            str2.pop(0)
        a = len(str1) >= 1 or len(str2) >= 1
    return toStr(strRes)       
        

    
    
def merge2filesto3(fName1,fName2,fName3):
    with open(fName1, "r") as file1, open (fName2, "r") as file2, open (fName3, "w") as fileOut:
        arr1 = file1.readlines()
        arr2 = file2.readlines()
        Ind1 = 0
        Ind2 = 0
        a = Ind1 < len(arr1) and Ind2 < len(arr2)
        while  a :
           
            fileOut.write(merge2ser(arr1[Ind1],arr2[Ind2]) + '\n')    
            Ind1 += 1 
            Ind2 += 1
            a = Ind1 < len(arr1) and Ind2 < len(arr2)        
        
    # deleting of used series
    f = open(fName1).readlines()
    g = open(fName2).readlines()
    for i in range(0,Ind1):
        f.pop(0)
        g.pop(0)
    with open(fName1,'w') as F1, open(fName2,'w') as F2:
        F1.writelines(f)
        F2.writelines(g)
   
#merge2filesto3('ser1.txt','ser2.txt','serJoined.txt')
