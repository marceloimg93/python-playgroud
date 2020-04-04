friends = ["Kevin", "Karen", "Jim", "James", "Adams"]
numbers = [0,5,87,4,5,6,9,8,7,7,7,75,6]

# print(friends)

# print(friends[0])
# print(friends[-1])
# print(friends[-2])
# print(friends[1:])
# print(friends[1:3])

# print("------------------------")

# friends.extend(numbers)

friends.append("Added on end")

friends.insert(1, "Add on second position")

friends.remove("Jim")

friends.pop() # remove last user

# order in alphabetically order
friends.sort()

print(friends)

# find index
print(friends.index("Kevin"))

numbers.reverse() # reverse the order of list
print(numbers)

# friends2 = friends.copy() # not avaiable on this version ... maybe on python 3

# print(friends2)
