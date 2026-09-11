friends = ["Jelio", "Drago", "Vasil"]
for friend in friends:
    print(f"{friend}, you are invited for dinner!")
print(f"{friends[0]} can't make it because he is in the Netherlands.")
friends[0] = "Petar"
print()
for friend in friends:
    print(f"{friend} you are still invited for dinner")

print("\nI found a bigger table!\n")
friends.insert(0, "Alex")
friends.insert(2, "George")
friends.append("Ivan")

for friend in friends: 
    print(f"{friend} is invited to the table")

print("\nI can invite only two people!\n")

frend = friends.pop()
print(f"Sorry {frend} i can't invite you.")
frend = friends.pop() 
print(f"Sorry {frend} i can't invite you.")
frend = friends.pop()
print(f"Sorry {frend} i can't invite you.")
frend = friends.pop() 
print(f"Sorry {frend} i can't invite you.")

print(f"\n{friends[0]} you are still invited")
print(f"{friends[1]} you are still invited")

del friends[1]
del friends[0]
print(friends)