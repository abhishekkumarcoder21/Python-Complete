# key value pairs in dictionary
# dictionary is mutable and dynamic

my_dict={
    "Name":"Abhishek Kumar",
    "Roll No":2201006,
    "age":24,
    "marks":[1,2,3,4],
    'marks':100 # overwrite the previous marks
}
print(my_dict)
my_dict['class']="BTech"
print(my_dict)
del my_dict["Roll No"]
print(my_dict)