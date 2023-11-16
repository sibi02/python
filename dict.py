alphabets = {'a','b','c'}
numbers = 1
dictionary = dict.fromkeys(alphabets,numbers)
print(dictionary)
print("----------------------------------------")

keys = {'a','e','i','o','u'}
values = [1]
camp = dict.fromkeys(keys,values)
print(camp)
values.append([2,3])
values.append(4)
values.append("five")
print(camp)

