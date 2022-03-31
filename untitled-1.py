def product(x,y):
    '''Returns the product of the given arguments.'''
    return x*y

x = 4
y = 3

print("{} x {} = {}".format(x,y,product(x,y)))

### how to print out a docstring wiht the attribute __doc__
print(product.__doc__)

mylist = [0] * 5
print(mylist) 
mylist1 = [1,2,4,5,6,7]



for i in range(len(mylist1)):
    item = mylist1.pop()
    print(mylist1 + [item]) 
    
    
def remove_item(l):
    if l == []:
        return None 
    else:
        print(l)
        remove_item(l[:len(l)-1])
        
l = [1,2,4,5,6,7,8]
remove_item(l)

### SPLICING 
splice_list = l[::2]
print(splice_list) # prints [1, 4, 6, 8]




#### make a triangle 
## hw 
## start with recursion 
def triangle(line, New_line, ws):
    if line == []:
        return None 
    elif line != New_line:
        space = [0]*ws
        print(space + line + space)
        triangle(line[:len(line)-1], New_line, ws+1)
    else:
        print(line)
        triangle(line[:len(line)-1], New_line, ws+1)
print("triangle")   
print(triangle([1,2,3,4,5], [1,2,3,4,5], 0))
      
      
## LIST COMPHRENSION 
## a fast way to make a new list from a prev list 
a = [1, 2, 3, 4, 5]
b = [i*i for i in a]
print(b)

## TUPLES 
mytuple = ("Max", "MK")
mytuple1 =("Max",)

## covert tuple into list 
my_list = list(mytuple)
print(my_list)

my_tuple = "Max", 23, "Boston"

name, age, city = my_tuple 
print(name)
print(age)
print(city)

## how to unpack tuple 
example = (1,2,4,5)
i, *j, l = example 
print(i)
print(j)
print(l)

##Dictionary: key-Value pairs, Unordered, Mutable 
mydict= {"name": "max", "age": 28, "city": "New york"}
## we can also use the dic function 
print(mydict)

mydict2 = dict(name="mary", age=24, city="LA")
print(mydict2)

values = mydict.values()
print(values)

for key, value in mydict.items():
    print(key, value)

## building an actual copy of a dict
mydict_copy = mydict.copy()
## this way the original one will not be changed 
## or you can do it this way 
mydict_copy2 = dict(mydict) 

## to overwrite a dict
mydict_copy2.update(mydict2)
print(mydict_copy2)


## SETS
## unorganize, mutable, and no duplicates 
myset= {1,2,3,1,2}
print(myset)
