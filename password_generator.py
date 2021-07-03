#password generator
'''
To create a password with Python, we need to create a program that takes 
the length of the password and generates a random password of the same length.
'''

import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols= "!@#$%&*"
all = lower+upper+number+symbols
length= 10
password="".join(random.sample(all,length))
print(password)

'''
Output- EiApHg!XPj   Z&Q76CP*xj   
'''