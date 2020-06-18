from time import time

startTime = time() #get initial time, time() gives current time

n1 = "Shubham"
n2 = "Rawat"

#   by default {0}   then             {1}         0   1
m="First name is {} and second name is {}".format(n1,n2)
n=f"First name is {n1} and second name is {n2}"
print(m)
print(n)


''''
Multiple Line comments
'''

#LIST
l=[11,2,3,4]
del(l[2]) # [11,2,4]

#del(l) - #delete the list

l.remove(11) # [2,4]
print(l)
l.clear() # clear the list

#TUPLE : same as list but is immutable
t=(1,3,5,7,"ghh",9,9)

#SET :  repeated elements are considered only once
s={2,2,4,5,6,7,8,8}
s.add(9)
s.remove(5) # gives error if not found in set
s.discard(5) # no error if not found
print(s)

print(time()-startTime) #get the program execution time


''' OUTPUT:-
First name is Shubham and second name is Rawat
First name is Shubham and second name is Rawat
[2, 4]
{2, 4, 6, 7, 8, 9}
0.0004172325134277344

[Program finished]
'''
