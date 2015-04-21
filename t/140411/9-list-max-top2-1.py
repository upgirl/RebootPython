arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,65555]

max_one = arr[0]
max_two = arr[0]
max_index = 0

# get max_one
i = 0
for num in arr:
    if num > max_one:
        max_one = num
        max_index = i
    i += 1

# get max_two
i = 0
for num in arr:
    if num > max_two and i != max_index:
        max_two = num
    i += 1

print max_one,max_two

