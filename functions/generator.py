def count_down(num):
    while num>0:
        yield num
        num-=1

for number in count_down(5):
    print(number)