arr = [1,2,'a',3,5,1,56,45,234,6,7,234]

# index
print arr.index('a')

i = 0
for n in arr:
    if n == 'a':
        break
    i += 1 
print i

arr = [1,2,2,2]
print arr.index(2)
