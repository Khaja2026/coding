#1)STRING CREATION, INDEXING, SLICING:
s="python"
print(s[0])   #p
print(s[-1]) #n

print(s[0:2]) #py
print(s[:-1]) #pytho
print(s[::-1]) #nohtyp

#2)STRING IMMUTABILITY
'''s="mits" 
s[0]="a" #error str does not support item assignment 
print(s)'''

s="mats"
s=s.replace("a","i")
print(s)      #mits

#3)LENGTH AND TRAVERSAL
s="hussain"
print(len(s))     #7
for ch in s:
    print(ch)      #prints all characters line by line

#4)CONCATENATION(+) AND REPETITION(*)

a="mits"
b="deemed to be university"
print(a+" ",b)    #mits deemed to be university
print(a*3)        #mitsmitsmits

#5)STRING METHODS

##case conversion
a="pytHoN LanguaGE"
print(a.upper())        #PYTHON LANGUAGE
print(a.lower())        #python language
print(a.capitalize())   #Python language
print(a.title())        #Python Language

##stripping
s="   khaja   "
print(s.strip())    #khaja (removes all extra spaces)
print(s.rstrip())   #   khaja(removes only right spaces)
print(s.lstrip())   #khaja    (removes only left spaces)

##search and count
s="Madanapalle"
print(s.find("a"))              #1
print(s.find("a",4,6))        #returns the first occurence of a from 4 to 6 index
print(s.count('a'))            #4
print(s.count('a',4,10))       #2

##replace
s="abcdefgh"
print(s.replace("a","z"))     #zbcdefgh

##split and join
s="abc,def,ghi"
print(s.split(','))         #['abc','def','ghi']
print('-'.join(['a','b','c'])) #a-b-c
'''print('.'.join('khaja','hussain')) '''# error str.join takes only one argument

##string formatting
name="khaja"
print(f"His name is {name}")      #His name is khaja
print("His name is {}".format("hussain"))   #His name is hussain

##Membership(in,not in) and comparision(==,<,> for lexicographic comparisions)
s="mango"
print('a' in s)                     #True
print('g' not in s)                 #False

##Character classification methods
ch="6"
print(ch.isdigit())       #True
print('abc123'.isalnum()) #True
print("hello".isalpha())  #True

##counting and frequency analysis
from collections import Counter
freq=Counter("aabbccd")
print(freq)             #Counter({'a':2,'b':2,'c':2,'d':1})

##string sorting
s='dabc'
print(''.join(sorted(s))) #abcd

##palindrome detection
s="dad" 
print(s==s[::-1])     #True

##Regular expressions(Regex)
import re
email="test123@gmail.com"
pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
print(bool(re.match(pattern,email)))   #True

##Handling special and escape characters
import string
s="Hello, world!"
s=''.join(c for c in s if c not in string.punctuation)
print(s)           #Hello world

##Recursion and advanced algorithms
def rec_rev(s):
    return s if len(s)<=1 else rec_rev(s[1:])+s[0]
print(rec_rev("abc"))    #cba

##Set operations
s1,s2="apple","plum"
print(set(s1) & set(s2)) #{'l','p'} (find intersections or remove duplicates)

