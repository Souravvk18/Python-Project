'''
This quiz game uses a function; a block of code with a name that performs a specific task.
 A function allows you to use the same code several times, without having to type everything each time. 

Now is the time to create your quiz! First, I’ll create the questions and the answer verification mechanism. Next,
 I’ll add the code that gives the player three attempts to answer each question:
'''

def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again ")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Guess the Animal")
guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the larget animal? ")
check_guess(guess3, "Blue Whale")
print("Your Score is "+ str(score))


'''
Output-
Guess the Animal
Which bear lives at the North Pole? polar bear
Correct Answer
Which is the fastest land animal? cheetah
Correct Answer
Which is the larget animal? elephant
Sorry Wrong Answer, try again Blue Whale
Correct Answer
Your Score is 3

Mix up your quiz! Make it longer or harder, use different types of questions, or even change the subject of the quiz.

'''