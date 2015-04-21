# List
# list is keyword, cannot be name, split string
# use [index] get value
# index 0 1 -1 -2

demo_list = [1,2,'a','b',[3,'c'],{'name':'upgirl'}]

print '==== get value by index ===='
print demo_list[0]
print demo_list[4]
print demo_list[4][1]
print demo_list[-1]
print demo_list[-1]['name']

print '==== bianli list ===='
for demo in demo_list:
    print demo

print '==== in or not ===='
print 1 in demo_list
print 0 in demo_list

print '==== bianli string ===='
string = 'hello'
print string[-1]

string = '[3,4,5]'
print string[-1]

print '==== ERROR, use list as name ===='
print list('123')
list = [1,2,3]
print list('hello')


