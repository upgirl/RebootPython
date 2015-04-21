demo_list = [-2,65555,1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,45,33,45]

# len
print len(demo_list)

len = 0
for demo in demo_list:
    len +=1
print len

# max
print max(demo_list)

max = demo_list[0]
for demo in demo_list:
    if demo > max:
        max = demo
print max

# min
print min(demo_list)

min = demo_list[0]
for demo in demo_list:
    if demo < min:
        min = demo
print min

# del
print demo_list
del demo_list[0]
print demo_list

# multi
l = ['aa','bb']
print l*2

# add
l = ['aa','bb']
print demo_list+l

# cut [i,j)
demo_list = [0,1,2,3,4,5]
print demo_list[0:3]
print demo_list[:3]
print demo_list[1:3]
print demo_list[1:]
print demo_list[-1:]
print demo_list[-1:-3]  # x
print demo_list[-1:0] # x
print demo_list[-3:-1]
print demo_list[:]
print demo_list[1:5]
print demo_list[1:5:1]
print demo_list[1:5:2]


# change
print demo_list[0]
demo_list[0] = '111'
print demo_list
print demo_list[0:0]
demo_list[0:0] = 'insert'
print demo_list
demo_list[0:2] = ['ti','huan']
print demo_list
demo_list[0:2] = ['h','e','l','l','o']
print demo_list
print demo_list[:4]
# add new after second element
demo_list[2:2] = [10]
print demo_list
# delete second element
demo_list[2:3] = []
print demo_list

demo_list = [0,1,2,3,4,5,6,7,8,9]
print demo_list
print demo_list[::2]
print demo_list[1:4]
demo_list[1:4:2]='ab'
print demo_list
demo_list = demo_list+[1]
print demo_list
demo_list = [0,1,2,3,4,5,6,7,8,9]
print demo_list
print demo_list[0:2]
print demo_list[2:0]
print demo_list[2:0:-1]













