to run program :
python filename # you might use python3


# format string
```
name = input()
print(f"hello, {name}!")
```
it will print:
```
hello, yourname
```
```
"{} square is {}".format(i,square(i))
```

# data types
```
integer = 1
float = 2.8
boolean = True
n = None
no need to specify the datatype
```
# if statement
```
if x > 0 :
  print("positive)
elif x < 0 :
  print("negative")
else:
print("zero")
```
# String
```
name = "maradona"
name[0]
```


# tuples
```
coordinates = (10,20)
coordinates[0]
```
# list
```
verbs = ["play","use","read"]
verbs[0]
```
# loops
```
for i in range(5):
  print(i)
it will print from 0 to 4

verbs = ["play","use","read"]
for verb in verbs:
  print (verb)
it will print each verb
```
# set

```
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(1) # will give error. it must be unique
print(s) # will print {1,2,3}
```
# dictionaries
```
playersnumbers = {"pele":10,"maradona":10,"majed":9}
playersnumbers["vandarsar"] = 1
print (playernumbers) #{'pele': 10, 'maradona': 10, 'majed': 9}
playersnumbers["duaia"] = 1
print (playernumbers) # {'pele': 10, 'duaia': 1, 'maradona': 10, 'majed': 9}
```
# function
```
def test(x):
  return 2 * x 

for in rage(5)
  print test(i)
```

# import
functions.py
```
def square(x):
  retrun x * x
```  
module.py
```
from functions import square
print square(10)
```

# class
```
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

p = Point(5,4)
```
