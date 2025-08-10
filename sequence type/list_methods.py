# append

lst1=[1,2,3]
print(lst1)
lst1.append(100)
print(lst1)

# copy

lst2=lst1.copy()
print(lst2)
lst2[2]=300
print(lst2)
print(lst1)

# count

fruits=['apple','mango','apple','mango','orange']
print(fruits.count('mango'))

# extend

list1=[100,200,300]
list2=[400,500,600]
list1.extend(list2)
print(list1)

# index

print(list1.index(600))




# insert
list1.insert(0,"bitturaja")
print(list1)

# pop

popped=list2.pop(1)
print(popped)

# remove
list1.remove("bitturaja")
print(list1)

# reverse

num_list=[1,2,3,4,5,6]
num_list.reverse()
print(num_list)

# sort
list2.sort()
print(list2)

# clear
list2.clear()
print(list2)
