#!/usr/bin/env python
# coding: utf-8

# In[ ]:


if 5 > 5:
  print("Five is greater than two!")
else:
    print("u")


# In[ ]:


if 5 > 2:
 print("Five is greater than two!") 
print("Five is greater than two!")


# In[ ]:


"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")


# In[ ]:


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# In[ ]:


x = "Python is "
y = "awesome"
z =  x + y
print(z)


# In[ ]:


# "Global variable within a fxn"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# In[ ]:


x = range(6)
print(x)


# In[ ]:


x = ["apple", "banana", "cherry"]

y= list(("apple", "banana", "cherry"))

# type(x)
type(y)


# In[ ]:


x=int("3")
x


# In[ ]:


a = "Hello, World!"
print(a[7])

print(len(a))

print(a[-1])


# In[ ]:


a = "He llo Wo rl d  qw ere  aqe q e qw w!"
print(a.replace("H", "J"))


# In[ ]:


a = "He llo Wo rl d  qw ere  aqe q e qw w!"
b= a.split(" ")

print(type(a))
print(b)


# In[ ]:


txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)


# In[ ]:


txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) 


# In[ ]:


a = "Hello"
b = "World"
c = a + " " +  b
print(c)


# In[ ]:


txt = "We are the so-called \"Vikings\" from the north."


# In[ ]:


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# In[ ]:


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# In[ ]:


thislist = ["appfle", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
    print("No Apples")


# In[ ]:


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# In[ ]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# In[ ]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


# In[ ]:


print(list1[1])


# In[ ]:


thistuple = ["apple", "banana", "cherry"]
thistuple[2] = "orange" # This will raise an error
print(thistuple)


# In[ ]:


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)


# In[ ]:


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


# In[ ]:


dic={"Brand" :"Toyota", "Year" :2016, "Owner" : "Mike"}
print(dic)
type(dic)


# In[ ]:


x=dic["Year"]
x


# In[ ]:


dic['Year']=2000
dic


# In[ ]:


for x in dic:
  print(x)


# In[ ]:


for x in dic:
  print(dic[x])


# In[ ]:


for x in dic.values():
  print(x)


# In[ ]:


for x, y in dic.items():
  print(x, y)


# In[ ]:


if "Brand" in dic:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# In[ ]:


if "Model" in dic:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
else:
    print("Does not exist")


# In[ ]:


print(len(dic))


# In[ ]:


# f = open("df.txt", "r")
# print(f.read())


# In[ ]:


a = 330
b = 330
print("A") if a > b else print("they are equal") if a == b else print("B")


# In[ ]:


# to avoid some elements say 3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# In[ ]:


# To stop at 3
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# In[ ]:


i = 1
while i < 6:
  print(i)
  i= i+1
    


# In[ ]:


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# In[ ]:


for x in "banana":
  print(x)


# In[ ]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


# In[ ]:


# Skip
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# In[ ]:


for x in range(2, 30, 3):
  print(x)


# In[ ]:


for x in range(6):
  print(x)
else:
  print("Finally finished!")


# In[ ]:


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# In[ ]:


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# In[ ]:


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# In[ ]:


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Mike")


# In[ ]:


x = lambda a : a + 10
print(x(5))


# In[ ]:


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


# In[ ]:


cars = ['Ford', 'BMW', 'Volvo']

cars.sort()
cars


# In[ ]:


cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)
cars


# In[ ]:


cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=False)
cars


# In[ ]:


# A function that returns the length of the value:
# sort accordign to lenth
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)
cars


# In[ ]:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# In[ ]:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name  + "  aged"  )

p1 = Person("John", 36)
p1.myfunc()


# In[ ]:


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


# In[ ]:


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# In[ ]:


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


# In[1]:


import datetime

x = datetime.datetime.now()
print(x)


# In[2]:


import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


# In[3]:


import datetime

x = datetime.datetime(2020, 5, 17)

print(x)


# In[4]:


import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


# In[5]:


import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


# In[6]:


import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


# In[12]:


try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


# In[23]:


import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 5)
plt.show()


# In[20]:


import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()


# In[24]:


import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()


# In[33]:


from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r**2)
print(p)


# In[29]:


# predict new values using regression 
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

speed10 = myfunc(10)

print(speed10)


# In[32]:


# bad fit

import matplotlib.pyplot as plt
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

print(r*r)


# In[47]:


import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("C:/Users/user/Desktop/dat.csv")

X = df[['V1', 'V2']]

scaledX = scale.fit_transform(X)

print(scaledX)


# In[50]:


df2 = pd.DataFrame(scaledX) 
df2.head()
df.head()


# In[51]:


df2.head()


# In[15]:


print('Enter Your name')
name = input()

if name != "":
    print("Thank your for your facking name")
else:
    print("You are stupid")
    
    
    


# In[21]:


def my_function(*kids):
  print("The youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus", 'Kama')


# In[22]:


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# In[23]:


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# In[26]:


food = ["apple", "banana", "cherry"]
for x in food:
    print(x)



# In[ ]:





# In[ ]:




