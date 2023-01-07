number = 10
print(f"Variable number: {number}, {id(number)}")
number +=2
print(f"Variable number: {number}, {id(number)}")

text = "Africa"
print(f"Variable number: {text}, {id(text)}")
text += " is hot"
print(f"Variable number: {text}, {id(text)}")

list = [1,2,3]
print(f"List variables: {list}, {id(list)}")
list.append(4)
print(f"List variables: {list}, {id(list)}")

list2 = list
print(f"Variable list2: {list2}, {id(list2)}")
list2.append(5)
print(f"Variable list2: {list2}, {id(list2)}")
print(f"Variable list: {list}, {id(list)}")

list3 = list.copy()
print(f"Variable list: {list}, {id(list)}")
print(f"Variable list2: {list2}, {id(list2)}")
print(f"Variable list3: {list3}, {id(list3)}")

list3.append(6)
print(f"Variable list: {list}, {id(list)}")
print(f"Variable list2: {list2}, {id(list2)}")
print(f"Variable list3: {list3}, {id(list3)}")
