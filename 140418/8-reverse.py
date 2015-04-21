arr = [1,2,8,5,4]

# reverse
arr = [1,2,8,5,4]
arr.reverse()
print arr

arr = [1,2,8,5,4]
arr = arr[::-1]
print arr

arr = [1,2,8,5,4]
arr_re = []
while len(arr) > 0:
    arr_re.append(arr.pop())
print arr_re
