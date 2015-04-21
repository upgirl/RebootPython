arr = [1,2,3,4,43,3,1,2,3]

# count
print arr.count(2)
print [1,2,3,4,43,3,1,2,3].count(2)

count = 0
for n in arr:
    if n == 2:
        count += 1
print count


