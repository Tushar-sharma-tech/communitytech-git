a="name"

# a string can be sliced from indexes int char
s=a[0:3] #start from 0 all the way to 3 index (excluding 3)
print(s)

char1=a[1]
print(char1)

#skip valus
name="0123456789"
n=name[1:9:2]
print(n) 

#string functions
name2="rahul"
l=len(name2)
print(l)

#endwith and startswith (these functions are case sensitive)
print(name2.endswith("ul"))
print(name2.startswith("ra"))

#capatalize first world of string
print(name2.capitalize())
name3="rohan are"
print(name3.capitalize())

#replace world
nam="i am a good good good boy"
print(nam.replace("good","bad"))

#explore more of such functions on ai and chatgpt