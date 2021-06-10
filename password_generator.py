#password generator
import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols= "!@#$%&*"
all = lower+upper+number+symbols
length= 10
password="".join(random.sample(all,length))
print(password)
