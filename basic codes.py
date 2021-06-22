# how to get  dict with default values as 0 or 1
# https://medium.com/swlh/python-collections-defaultdict-dictionary-with-default-values-and-automatic-keys-305540540d2a

from collections import defaultdict
d = defaultdict(int)    # all zeros as default
d = defaultdict(float)  # all 0.0 as defalut

# how to change  string to upper
# let any string = string
string.upper()

# to print any variale or some variables we have a different method
print("{} some dataa we want to show as output".format(varible))
# let varible x =5 then
print("{} i know that value".format(x))  # output is "5 i know that value"
print("{} i know that value {}".format(x, x))  # output is"5 i .......5"

# let us go for
args and kwargs
# we know that when we want  to write a def function and we want to send dict or func to it
# from main function when we directly send it like this"let func is "do(x)" amd dict is "tect" then"
# writing in "do(tect)" doesnt send dict but it send it as a array or total one element
# so we want to write as"do(**x)" and call as "do(**tect)"

# let try for random value to take  bye computer
import random
random value = random.choice(fro m which you want to get random value)

# comprehensions
{
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # I want 'n' for each 'n' in nums
    my_list = []
    for n in nums:
    my_list.append(n)
    print my_list

    print[n for n in nums]

    # I want 'n*n' for each 'n' in nums
    # my_list = []
    # for n in nums:
    #   my_list.append(n*n)
    # print my_list

    # Using a map + lambda
    # my_list = map(lambda n: n*n, nums)
    # print my_list

    # I want 'n' for each 'n' in nums if 'n' is even
    # my_list = []
    # for n in nums:
    #   if n%2 == 0:
    #     my_list.append(n)
    # print my_list

    # Using a filter + lambda
    # my_list = filter(lambda n: n%2 == 0, nums)
    # print my_list

    # I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
    # my_list = []
    # for letter in 'abcd':
    #   for num in range(4):
    #     my_list.append((letter,num))
    # print my_list

    # Dictionary Comprehensions
    names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
    heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
    # print zip(names, heros)

    # I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
    # my_dict = {}
    # for name, hero in zip(names, heros):
    #     my_dict[name] = hero
    # print my_dict



    # If name not equal to Peter

    # Set Comprehensions
    # nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
    # my_set = set()
    # for n in nums:
    #     my_set.add(n)
    # print my_set


    # Generator Expressions
    # I want to yield 'n*n' for each 'n' in nums
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # def gen_func(nums):
    #     for n in nums:
    #         yield n*n

    # my_gen = gen_func(nums)

    # for i in my_gen:
    #     print i
}
# string formatting
{
    person = {'name': 'Jenn', 'age': 23}

    # sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
    # print(sentence)


    # sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
    # print(sentence)


    # sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
    # print(sentence)
    # sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
    # print = sentence

    # if you know how to unpack the dict then u can use below method
    #sentence  = 'My name is {name} and I am {age} years old.'.format(**person)
    # print(sentence)

    # tag = 'h1'
    # text = 'This is a headline'

    # sentence = '<{0}>{1}</{0}>'.format(tag, text)
    # print(sentence)


    sentence = 'My name is {0} and I am {1} years old.'.format(
        person['name'], person['age'])
    print(sentence)


    # class Person():

    # def __init__(self, name, age):
    self.name = name
    self.age = age

    p1 = Person('Jack', '33')

    sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
    print(sentence)

    # sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
    # print(sentence)

    # sentence = 'My name is {name} and I am {age} years old.'.format(**person)
    # print(sentence)

    # for i in range(1, 11):
    #     sentence = 'The value is {}'.format(i)
    #     print(sentence)

    # if u want to get num like 01,02,03,.....,10
    # for i in range(1, 11):
    #     sentence = 'The value is {:02}'.format(i)  (02 means it always print 3 digits if num hasless then 3 digits it fill them by 0)
    #     print(sentence)


    # pi = 3.14159265

    # sentence = 'Pi is equal to {}'.format(pi)

    # print(sentence)


    sentence = '1 MB is equal to {} bytes'.format(1000**2)
    print(sentence)

    sentence = '1 MB is equal to {:,} bytes'.format(1000**2)
    print(sentence)

    sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
    print(sentence)

    #import datetime

    my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

    # print(my_date)

    # March 01, 2016

    sentence = '{:%B %d, %Y}'.format(my_date)

    print(sentence)

    # March 01, 2016 fell on a Tuesday and was the 061 day of the year.

    sentence = '{:%B %d, %Y} fell on a {} and was the {} day of the year'.format(
        my_date)
    # if u want  these type of standerd libery func go to link
    "docs.python.org/3/library"


    print(sentence)
}
# f-string
{
    person = {'name': 'Jenn', 'age': 23}

    sentence = f'my name is {name} and my age is {age}'
    print(sentence)

    # when we want upper case
    sentence = f'my name is {name.upper()} and my age is {age}'
    print(sentence)
}
# generetors
{
    # def square_numbers(nums):
    for i in nums:
    yield(i * i)
    my_nums = square_numbers([1, 2, 3, 4, 5])
    print(my_nums)  # no output u will get .....to get output we nedd to call them
    print (next(my_nums))  # output is 1
    print (next(my_nums))  # output is 4
    print (next(my_nums))  # output is 9
    print (next(my_nums))  # output is 16
    print (next(my_nums))  # output is 25

    # or  u can do it by for loops
    for num in my_nums:
        print (1num)

    #or u can use this ...which convert gen to list
    print(list(my_nums))

    # the above codes give same output
}
#namedtuples
{
    #from collections import nampedtuple
    Color = nampedtuple('color',['red','green','blue'])
    color = Color(55,125,255)
    white = color(255,255,255)
    print(color.red) #output is 55
    print(white.green) #output is 255
}
