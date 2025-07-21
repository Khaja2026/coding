
#count no of vowels,consonants and spaces in a string

def count(s):
    vow_count=0
    con_count=0
    space_count=0
    
    for char in s:
        if char in "aeiouAEIOU":
            vow_count+=1
            
        elif char.isalpha():
            con_count+=1
        
        elif char==" ":
            space_count+=1
        
            
    return vow_count,con_count,space_count
    
v,c,sp=count("shaik khaja hussain")
print("vowels",v)
print("consonants",c)
print("space_count",sp)