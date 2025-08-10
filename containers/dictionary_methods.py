# get --> to get the value of the key

profile={
    "name":"Abhishek Kumar",
    "class":"BTech",
    "Roll No.":2201006,
}
print(profile.get('class'))

# keys

print(list(profile.keys()))

# values

print(list(profile.values()))

# items

print(list(profile.items()))

# pop
popped=profile.pop('name') # customizable pop

print(popped)

# popitems
new_popped=profile.popitem()
print(new_popped)
print(profile)

# clear
profile.clear()
print(profile)