'''
very simple program for beginners to convert Fahrenheit to celsius with Python programming language.

0 degrees Celsius is 32 degrees Fahrenheit. 
So to convert Fahrenheit to degrees Celsius, we just need to subtract 32 from the temperature Fahrenheit.
'''

def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c

print(convert(100))

# 37.77777777777778

