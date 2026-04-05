Marks={
    "tushar":100,
    "Raman":20,
    "rohan":56,
    1:"rahul"
    #keys : keys value
}

# print(Marks,type(Marks))
print(Marks[1])
print(Marks.items())
print(Marks.keys())
print(Marks.values())
Marks.update({"tushar":99})
print(Marks)

print(Marks.get("ajay")) #gives none
print(Marks["ajay"]) #gives error

d={}#empty dictionary