import random

with open("high_scores.py", "r") as hs:
    print("The current High Scores:")
    hs_contents = hs.read()
    print(hs_contents)

print()
num = random.randint(1,100)
guess = 0
i = 0
while guess != num:
    guess = int(input("Guess a number! 1-100: "))
    i += 1
    if guess > num:
        print("Too high")
    if guess < num:
        print("Too low")
    if guess == num:
        print("Great Job!")

print("It took you "  + str(i) + " guesses")
print()
print("Here is an updated list of the sorted High Scores.")

with open("high_scores.py", 'a') as hs:
    hs_addscores = hs.write("\n" + str(i))

#https://www.tutorialspoint.com/python_text_processing/python_sorting_lines.htm
file = open("high_scores.py", "r+")

#FileName = ("high_scores.py")
data = file.readlines()
data.sort()
for i in range(len(data)):
    print(data[i])

file.close()


#need to do /n to somewhere to make sure the new thing appended is on a list. 
#somehow make the work from high_scores into a list so I can sort it

# When the program is started, it should read the current high scores list from a file called "high_scores.txt" if the file exists.
# If the file doesn't exist, the program should create a new empty list.
# The program should then generate a random number between 1 and 100 and prompt the user to guess the number.
# After each guess, the program should provide feedback to the user (e.g., "Too high!" or "Too low!") and keep track of the number of guesses made.
# Once the user has guessed the number correctly, the program should display the number of guesses it took and add the score to the high scores list.
# The high scores list should be sorted in ascending order, and only the top 10 scores should be saved to the "high_scores.txt" file for future use.
# Finally, the program should display the current high scores list to the user.
