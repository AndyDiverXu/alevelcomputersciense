#Question1,a1
def IterativeVowels(Value):
    Total = 0 
    for X in range(0, len(Value)): 
        FirstCharacter = Value[0] 
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u': 
            Total = Total + 1 
        Value = Value[1:len(Value)]  
    return Total


#str1 = "hellooooooo"
#totalNumber = IterativeVowels(str1)
#print(totalNumber)
#T2 = "QHo"
#print(IterativeVowels(T2))


print(IterativeVowels("houseeee")) 



def RecursiveVowels(Value):  
    if len(Value) == 0: 
        return 0  
    else: 
        FirstCharacter = Value[0] 
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u': 
            return 1 + RecursiveVowels(Value[1:len(Value)])  
        else: 
            return RecursiveVowels(Value[1:len(Value)])
        
        
        
        
print(RecursiveVowels("houseeee")) 