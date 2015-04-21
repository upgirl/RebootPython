arr = [1,3,4,2,8,8,0,-5]

arr_t = arr[:]
for i in range(3):
    m = max(arr_t)
    arr_t.remove(m)
    print m

print arr_t
print arr
