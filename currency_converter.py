# To create a realtime currency converter with Python.,
#  we first need to install the forex-python library which can be easily installed by using the pip command;
#   pip install forex-python.

from forex_python.converter import CurrencyRates
c = CurrencyRates()
amount = int(input("Enter the amount: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()
print(from_currency, " To ", to_currency, amount)
result = c.convert(from_currency, to_currency, amount)
print(result)


''' Output-
Enter the amount: 500
From Currency: USD
To Currency: INR
USD  To  INR 500
37344.79404550453'''