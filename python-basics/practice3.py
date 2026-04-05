name=input("enter your name: ")
print(f"good after noon {name}") # "f" string lets you use variables in a string
a=10
print(F"ten {a}")

# chaining of replace function
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
nam=input("enter your name: ")


print(letter.replace("<|Name|>",nam).replace("<|Date|>","24 sept 2090"))

#program to detect double space
cha="the python is  easy to understand"
print(f"double space is at ", cha.find("  "))

#to format
letter = "Dear Harry,\n\tThis python course is nice. \nThanks!" 
print(letter)
