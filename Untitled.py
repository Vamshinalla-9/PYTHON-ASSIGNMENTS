#!/usr/bin/env python
# coding: utf-8

# In[1]:


#hare krishna hare krishna krishna krishna hare hare
#hare rama hare rama rama rama hare hare


# In[2]:


def sayhello():
    """ This is the function docstrings """
    return "hello world"


# In[4]:


sayhello.__doc__


# In[5]:


dir (__builtin__)


# In[11]:


def __init__(self,x,y):
    self.x = x
    self.y = y


# In[12]:


def __repr__(self):
    
    return "Represent(x={},y=\"{}\")".format(self.x, self.y)


# In[13]:


def __str__(self):
            "Representing x as {} and y as {}".format(self.x, self.y)


# In[14]:


def hellow(name):
    """ jf;ajkfdf;;a fkldlfja;l fjd afjkda;fjkdajfkljakjkkljk  
    kjkd;jkal;jkl
    fjkdjkl;a
    jlkdjak;;jfkla;kl;;ja"""
    print("hellow"+name)


# In[15]:


import datetime
dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")


# In[16]:


print(dt)


# In[17]:


import dateutil.parser
dt = dateutil.parser.parse("2016-04-15T08:27:18-0500")


# In[18]:


dt


# In[19]:


today = datetime.date.today()
print('Today:', today)


# In[20]:


yesterday = today - datetime.timedelta(days=1)
print('Yesterday:', yesterday)


# In[21]:


import datetime


# In[23]:


today = datetime.date.today()
print("today date is : ", today)


# In[24]:


tommorow = today-datetime.timedelta(days = 3)
print("date is the ",tommorow)


# In[26]:


date = today+datetime.timedelta(days = 7)
print("after a week date is : ",date)


# In[27]:


import enum


# In[28]:


from enum import Enum


# In[29]:


class colour(Enum):
    red = 2
    green = 1
    blue = 4
print(colour.red)    


# In[30]:


print(colour(1))


# In[31]:


print(colour['red'])


# In[33]:


seta = ['a','b','b','c','d','e','e','f','k']


# In[34]:


seta = set(seta)


# In[35]:


type(seta)


# In[38]:


dir(__collections__)


# In[39]:


help(collections)


# In[40]:


help(len)


# In[42]:


from collections import counter
counterA = counter(['a','b','b','c','d','e','e','f','k'])
print(counterA)


# In[43]:


from collections import Counter
counterA = Counter(['a','b','b','c'])
counterA


# In[44]:


a = 3
b = 2


# In[45]:


a/b


# In[46]:


a//b


# In[47]:


a|b


# In[48]:


b =4


# In[49]:


a | b


# In[50]:


a&b


# In[57]:


a % b


# In[56]:


a = 9


# In[2]:


~-2


# In[3]:


~ 3


# In[5]:


~8


# In[6]:


~~8


# In[7]:


~-2


# In[8]:


~-3


# In[9]:


bin(60^30)


# In[10]:


(60 ^ 30)


# In[11]:


bin(10 ^ 30)


# In[14]:


(60 & 30)   # symbol represents the LOGICAL AND


# In[15]:


bin(60 & 30) # bin is the function used to convert the numerical value to binary format


# In[16]:


(60 | 30) # symbol represents the LOGICAL OR


# In[17]:


bin(60|30)


# In[21]:


2 << 3 #bitwise left shift


# In[20]:


bin(2<<3) # instially one 1 is at the 2^0 = 2 then it shifted to 3 place left to it i.e.,2^4 = 16


# In[24]:


32>>4 #Bitwise Right shift


# In[23]:


bin(32>>4)


# In[25]:


3<<2


# In[26]:


7<<2


# In[29]:


9<<3


# In[30]:


9<<7


# In[31]:


7<<4


# In[32]:


1>>3


# In[33]:


23>>50


# In[36]:


a = 0b010


# In[37]:


a <<= 3


# In[38]:


a


# In[44]:


x = float(input("enter the x value"))
if 3.14<x<3.142:
    print("x is the between value of limits")
else:
    print("not it is not between value of limits")


# In[45]:


x = "vamshi"
def names():
    global x
    x = "vamshi krishna"
    print(x)
    


# In[47]:


names()


# In[53]:


def foo():
    c = 5
    print(c)


# In[55]:


print(c)


# In[56]:


def foo():
    if True:
        a = 5
        print(a)


# In[57]:


foo


# In[58]:


foo()


# In[62]:


b = 3
def foo1():
    if False:
        b = 5


# In[63]:


foo1()


# In[64]:


class A:
    pass


# In[65]:


a = A()


# In[66]:


a.x = 4


# In[67]:


print(a.x)


# In[68]:


del a.x


# In[69]:


print(a.x)


# In[73]:


x = {'vamshi':'krishna','kiran':'deshpande'}


# In[74]:


x


# In[75]:


del x['kiran']


# In[76]:


print(x)


# In[77]:


del x['kiran']
print(x)


# In[78]:


x = [1,2,3,4,5,6,7,8,9]


# In[79]:


del x[1:4]


# In[80]:


print(x)


# In[82]:


del x[1:2]
print(x)


# In[83]:


del x[-1]


# In[84]:


print(x)


# In[89]:


del x[::-1]


# In[90]:


print(x)


# In[91]:


a = 'global'
class Fred:
    a = 'class' # class scope
    b = (a for i in range(10)) # function scope
    c = [a for i in range(10)] # function scope
    d = a # class scope
    e = lambda: a # function scope
    f = lambda a=a: a # default argument uses class scope


# In[92]:


print(Fred.a)


# In[95]:


print(next(Fred.b))


# In[96]:


print(Fred.c[1])


# In[97]:


a = 42
b = list(a + i for i in range(10))


# In[98]:


print(b)


# In[ ]:




