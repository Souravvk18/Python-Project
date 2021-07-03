'''
you will learn how to create a very basic text-based game with Python.
 Here I will show you the basic idea of how you can create this game and then you can modify or 
 increase the size of this game with more situations and user inputs to suit you.
'''

name = str(input("Enter Your Name: "))
print(f"{name} you are stuck at work")
print(" You are still working and suddenly you you saw a ghost, Now you have two options")
print("1.Run. 2.Jump from the window")
user = int(input("Choose 1 or 2: "))
if user == 1:
    print("You did it")
elif user == 2:
    print("You are not that smart")
else:
    print("Please Check your input")



'''
output-
 Enter Your Name: sourav
sourav you are stuck at work
 You are still working and suddenly you you saw a ghost, Now you have two options
1.Run. 2.Jump from the window
Choose 1 or 2: 2
You are not that smart
'''