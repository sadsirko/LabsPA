import os

def merge2ser(str1,str2):
    str1 = str(str1)[:-2].split(' ')
    str2 = str(str2)[:-2].split(' ')
    strRes = []
    #arr1 = str1.split(' ')
    #arr2 = str2.split(' ')
    Ind1, Ind2 = 0, 0
    print(str1)
    print(str2)
    a = len(str1) > 1 or len(str2) > 1
    while a :
        if str1 == []:
            strRes = strRes + str2
            break
        elif str2 == []:
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
        a = len(str1) > 1 or len(str2) > 1
    return strRes       
        

    
    
def merge2filesto3(fName1,fName2,fName3):
    with open(fName1, "r") as file1, open (fName2, "r") as file2, open (fName3, "w") as fileOut:
        arr1 = file1.readlines()
        arr2 = file2.readlines()
        Ind1 = 0
        Ind2 = 0
        a = Ind1 < len(arr1) and Ind2 < len(arr2)
        while  a :
            print (merge2ser(arr1[Ind1],arr2[Ind2]))
            Ind1 += 1 
            Ind2 += 1
            a = Ind1 < len(arr1) and Ind2 < len(arr2)

merge2filesto3('ser1.txt','ser2.txt','serJoined.txt')

