#ITERATOR : gives values one by one by next(iterator_object)
l=[6,4,7,9,0]

it = iter(l) #creating iterator object of list

print(next(it)) #next is function to go to next element
print(next(it))

for i in it: #loop with iterator object
 print(i)


'''output:- (6 and 4 printed only once)
6
4
7
9
0
[Program finished]'''



#GENERATOR : by yield keyword
#yield generators a iterator and stores the values in the iterator object


def gen(n): #square of 10 natural number
 i=1
 while i<11:
  yield i*i
  i+=1

val=gen(10)
print(next(val))
print(next(val))
for i in val:
 print(i)
 
'''output:-
1
4
9
16
25
36
49
64
81
100

[Program finished]'''