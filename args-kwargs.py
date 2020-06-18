#we can use any name for *args and **kwargs
#just the * and ** is important in function argument


#1) simple function
def myself(name, age, place):
	print(f"My name is {name} and my age is {age} and i live in {place}")
	
myself("Shubham",22,"Uttarakhand")


#2) *args create the tuple
# can pass list or tuple by *
def myself1(*args):
	print(args)
	print(type(args)) #<class 'tuple'>
	print(f"My name is {args[0]} and my age is {args[1]} and i live in {args[2]}")
	
myself1("Shubham",22,"Uttarakhand")
list=["shubham",22,"Uttarakhand"]
myself1(*list) #can pass list with * to *args


#3) **kwargs create the dictionary
# can pass dict only by **
def myself2(**kwargs):
	print(type(kwargs))
	for key,value in kwargs.items():
		print(key,value)

d={"Name":"Shubham", "Age":22,"Place":"Uttarakhand"}
myself2(**d)



'''  OUTPUT:-
My name is Shubham and my age is 22 and i live in Uttarakhand

('Shubham', 22, 'Uttarakhand')
<class 'tuple'>
My name is Shubham and my age is 22 and i live in Uttarakhand
('shubham', 22, 'Uttarakhand')
<class 'tuple'>
My name is shubham and my age is 22 and i live in Uttarakhand

<class 'dict'>
Name Shubham
Age 22
Place Uttarakhand

[Program finished] '''
