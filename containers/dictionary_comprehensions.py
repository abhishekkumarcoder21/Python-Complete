squares={x:x**2 for x in range(1,11,1)}
print(squares)

for k in squares:
    print(k,end=' ')

print('\n')
for k in squares.values():
    print(k,end=' ')