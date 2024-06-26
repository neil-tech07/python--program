What is python??

- python is simple,easy & portable.
- python is free & open source.
- python is high level , interpreted language.
- python is developed by guido van rosum.


python is interpreted language means when we write python code its executed the code line by line thats why we called python is interpreted language. 

- print is function to output statement in python. simply we can tell "print" is output function.

character set of python language :
1. letter -> A-Z , a-z
2. Digits -> 0-9
3. soecial character -> -,+,/,* etc..
4. whitespace -> Blank space , Tab , newline

VARIABLES :->

What is variable in python :- a variable is a name given to a memory location in a program or else we can simply say variable is a container to store some data.

example->
name = "shrada" 
age = 23
salary = 23000.56

variable names = name , age , salary
variable values = "shrada" , 23 , 23000.56

Rules for identifires:->
1. identifiers  - names of the variables 
2. identifiers can be combinations of uppercase and lowercase lettter , digits or an underscore(_). ex- myVariable , variable_1 .
3. an identifiers can't start with digit. so while variable1 is valid but 1variable is not valid.
4. we can't use special character or symbols like !, #, @, %etc ...
5. identifiers can be of length.
6. variables names should be small and meaningful like -  when we give our age in that case we take the variable as "myAge".
7. here myAge is camel case letter

- type is a operator to show the datatype name in our variables like which  datatypes we use in our variables.

DATATYPES:->

- mainly datatypes are 5 types in python :
- These datatypes are unmutable or build-in datatypes.
1. integer - +ve value , 0 , -value (int)
2. string - "hello" , "shradha" etc... (str)
3. float - 3.91 , 6.37, etc ... (float)
4. boolean - true , false (boolean)
5. None - not assign

Comments in python:->

- when we write some code but we don"t want to execute it then we give a commentline to that place so that line of code will not executed .
- comments are of 2 types .

1. single line comment:-
- when we the single line comments in python we did it on "#". 
ex- #single line comment
    #this is a comment

2. multiline comment:-
- when we it a multiline comment we did it through """_""" .
ex- 
"""
multiline 
comments
"""

TYPES OF OPERATORS :->
- simply we can say operator is a symbol that performs a certain operation between operands .
ex-
a+b
Here, 
a,b -> operands 
+ -> operator

- There are 4 types of operators in python 

1. Arithmatic Operator - (+, -, /, *, %)
2. Retational Operator - (==, !=, <, >,<=,>=)
3. Assignment Operator - (=, +=, -=, *=, /=, %=)
4. Logical operator - (and, or, not)

Input in python :-

- Input() statement is used to accept values (use keyword) from the user. 


STRINGS:->

- String is a datatype that stores a sequence of characters

str1 = "This is a good guy"
str2 = 'this is a good guy'
str3 = """this is a good guy"""

- All these strings are real strings . because in python , it sopports all these syntax like - "" , ' , """


- \n(newLine)- when we want to break our line in to a new line then we can give the new line symbol in that place so the line get breaked automatically. 

Basic operations of string:

concatenation ->
"Hello" + "World" = HelloWorld

Lentgh of string ->
len(str)


INDEXING OF STRING :->

- WEBBOCKET -> 012345678(indexing)
- Always indexing starts from '0'.

SLICING OF STRING :->

- Accessing parts of a string.
- ending index is not counting.
- syntax - str[starting_index : ending_index]

str = "webbocket"
str[0:3] - web
str[1:3] - eb
str[:3] - web


FUNCTIONS OF STRING :->

EX-
str = "i am a coder."

1. str.endswith("er.") - returns true if string ends with substring
2. str.capitalize() - returns first char is capital
3. str.replace(old , new) - replace all occurences of old with new 
4. str.find(word) - returns 1st index of 1st occurence 
5. str.count("am") - counts the occurence of substring in string 


CONDITIONAL STATEMENT:->

- used to handle the condition in your program . 
- syntax (if-elif-else)
- elif means else-if

if(cond):
    statement 1
elif(cond):
    statement 2 
else:
    statement(default)

LISTS IN PYTHON :->

- Lists is a built-in data type that stores set of values.
- it can store elements of different types like integer, float, & string etc... 
- in list we can make indexing.
- in list we can find length of the list also.

- in list we can also do the slicing activity.
ex- 
marks = [87, 45, 67, 83, 45] - array and list
student = ["Neil", 85, "Bhubneswar"] - list


LIST SLICING :->

- it similar to starting slicing .
- syntax - list_name[starting_idx : ending_idx]
- ending index is not included 

marks = [23 , 25 , 34 , 47, 46 , 78]
marks[1:4]-> [25 , 34 , 47]
marks[:3] -> [23 , 25 , 34]
marks[2:] -> [34 , 47 , 46 , 78]

List methods :->

list = [9, 4, 6, 7, 8 ,2]
list.append(6) - adds one element at the end of the list - [9, 4, 6, 7, 8, 2, 6]
list.sort() - sort the elements in assending order - [2,4,6,7,8,9,]
list.sort(reverse=True) - sorts the element in decending order - [9,8,7,6,4,2]
list.reverse() - reversing the list - [2,8,7,6,4,9]
list.insert(idx,el) - insert the element at index
list.remove(1) - remove the first occurence of element - [9,6,7,8,2]
list.pop(idx) - remove element at index 


GIT ->

- it is a open source repository system where we can save , manipulate , colaborate our code with anyone else .
- in our software era, everyone can use git system for their software development . 
- we also call git is a version control system. 
- git provides some tools to use their functionlity and fratures ex- github , gitlab etc...


#git init
#git add -A
#git commit -m "first commit"
#git branch -M main
#git remote add origin https://github.com/neil-tech07/python--program.git
#git push -u origin main


TUPLE IN PYTHON :->

- Tuple is a build in datatype that lets us create immutable (the value can't be changeble) sequence of values .
- ex. tup = (87 , 67 , 98 , 34 , 45)
- tup[0] -> 87
- tup[1] -> 67
- we can do the tuple as 
1. tup1 = () -> empty tuple
2. tup2 = (1,) -> a tuple
3. tup3 = (34 , 67 , 89 , 20) -> tuple
- tuple has also satisfy the slicing property.


- tup.index(element) = returns index of first occurence 
- tup.count(element) = returns the count total occurence 
 
ex. tup = (2,1,3,1)
tup.index(2) -> 3
tup.count(1) -> 2


DICTIONARY IN PYTHON :->

- Dictionary are used to store the data values in key-values pair. 
- They are unordered , mutable(changeble) & don't allow duplicate key .
- ex -
dict = {
    "name" : "shradha"
    "cgpa" = 9.8,
    "marks" = [98 , 96, 95]
}

- the left part of the dictionary are the keys and right side part in their values so dictionary contains key:value pair structure. 


NESTED DICTOIARY :->

- Dictionary also satisfy the nested property.
- dictoinary under dictoinary is called nested dictonary.
- ex- 
student : {
    "name" : "Neil"
    "score" : {
    "chem" : 98,
    "math" : 87,
    "phy" : 79
    }
}


DICTIONARY METHODS :->

1. myDict.keys() = it returns all keys .
2. myDict.values() = it returns all values .
3. myDict.items() = it will return all key:value pair as tuple.
4. myDict.get("key") = returns the key according to values .
5. myDict.update(newDict) = insert the specified items to the dictionary.


SET IN PYTHON :->

- Set is the collection of the unordered items .
- Each elements of the set must be unique & immutable (can't change).
- ex -

set1 = {1,2,3,4,5}
set2 = {5,8,9,4}

SET METHOD :->

1. set1.add(element) - adds an element
2. set1.remove(element) - remove an element
3. set1.clear() - clear all the elements
4. set1.pop() - Remove random values of set
5. set1.union(set2) - combine both set values and returns a new set
6. set1.intersection(set2) - combines the common values and returns a nnew set

ex-

set1 = {1,2,3,4,5}
set2 = {4,5,6,7}
set1.union(set2) -> {1,2,3,4,5,6,7}
set1.intersecton(set2) - {4,5}


LOOPS IN PYTHON :->

- Loops are used to repeat instruction.
- in python there are 2 loops -> 'while loop' & 'for loop'
1. WHILE LOOP :-
   syntax - 

   initialization
   while condition : 
     statement
     increament/decreament

break & continue :-

- break: break is used to terminate the loop encountered.
- continue: terminates execution in the current iteration $ continue execution of the loop 
with the iteration.


FOR LOOP :->

- For loop are use for sequential transversal . for traversing list , string , tuple etc . 
- syntax ->

   for value in list:
   statement..


RANGE() :->

- range function returns a sequence of numbers , starting from 0 by default , and increaments by 1 (by default) , and stops before a specified number .

- syntax ->
range(start , stop , step)


FUNCTIONS IN PYTHON :->

- Functions is a block of statements that performs a specific task .
- syntax :-
def func_name(parameter1 , parameter2 ...):
returns val

func_name(arg1 , arg2) #function call


- functions are of 2 types in python
1. buld-in function - print(), len(), type(), range() ... etc
2. user defined function - user can develop the function.

OOPS in python (OBJECT ORIENTED PROGRAMMING):->

- to map with real world scenarios , we started using objects in code . this is called object oriented programming .

1st concept -> procedual programming.
2nd concept -> functional programming.
3rd concept -> object oriented programming. 

CLASS & OBJECT IN PYTHON :->

- class is a blueprint of creating objects .

ex -> creating a class - 
class Student:
name = "web bocket"

ex -> creating an object(instance)
s1 = student()
print(s1.name) #web bocket


__init__ function (constructor) :->

- All class have a function called __init__() , which is always executed when the class is being initiated.

ex.-> creating a class 
class student:
def __init__(self , fullname):
self.name = fullname

ex.-> creating a object
s1 = student("webbocket")
print(s1.name)

note :-> The self parameter is the reference to the current instance of the class ,  and is used to access variable that belongs to the class .


CLASS & INSTANCE ATTRUBURES :->

university -> college1 , college2 , college3 , college4
              student1 , student2 , student3 , student4

- colleges and students are the attributes of university.

METHODS IN PYTHON :->

- methods are the function that belongs to objects.

ex, -> creating a class 

class student:
   def __init__ (self , fullname):
       self.name = fullname 
   def heello(self):
   print("hello" , self.name)


ex. -> creating object

s1 = student("rohan")
s1.hello()
/
/
/
/
/


private(like) Attributes & Methods :->

- private attributes and methods are meant to be used only within the class and are not accessible from outside the class .
- the private class attributes are written in __(attributes) so that we call it private attributes of a class.



INHERITANCE :->

- when one class(child class) derives the properties & methods of another class(parent class).

- syntax - 
class Car:
----------
class Toyotacar(car):
----------

- in python inheritance are of 3 types :
1. single inheritance 
2. multi-level inheritance 
3. multiple inheritance 


-------- geeksforgeeks --------


POLYMORPHISM :-> OPERATOR OVERLOADING :->
- when the same operator is allowed to have different meaning meaning accordingly to the context.
- in that polymorphism we can use duner functions.

1. a + b -> __add__
2. a - b -> __sub__
3. a * b -> __mul__
4. a / b -> __truediv__
5. a % b -> __mod__

ex - (+)

print(1 + 2) #3 (addition)
print("web" + "bocket") #web bocket (concatination)
print([1,2,3] + [4,5,6]) #[1,2,3,4,5,6] (merged)





















