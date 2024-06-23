#create a string
word="COMPUTER SCIENCE"
print(word)

#acess characters in a string
word="ARIYALUR"
print("the wordc is:",word)
letter=word[7]
print("the letter is:",letter)

#find length of a string
word="ARIYALUR"
print(word)
length=len(word)
print("the length of the string is:",length)

#split a string
word="computer science"
text=word.split()
print(text)

# count the no of space
mystr="count,the number of spaces"
print("the string is:",mystr)
character="     "
position=mystr.count(character)
print("the no of spaces in the string is:",position)

#check
word="computerscience"
start=word.startswith("e")
end=word.endswith("c")
print(start,end)

#repeat string
word="Ariyalur"
t=word*5
print(t)

#replace sub string
word="computer science"
print("before replace:",word)
replace=word.replace("computer","social")
print("after replaced :",replace)

#concutenate string
str1="computer"
str2="science"
str3=str1+str2
print(str3)
