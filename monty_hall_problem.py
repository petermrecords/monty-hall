import random

def monty_hall_problem():
    winning_door = random.randint(1,3)
    first_choice = random.randint(1,3)
    hosts_choice = [i for i in [1,2,3] if i not in [first_choice, winning_door]][0]
    second_choice = [i for i in [1,2,3] if i not in [first_choice, hosts_choice]][0]
    if second_choice == winning_door:
        return True
    else:
        return False

def run_trials(trials):
    wins = 0
    for i in range(trials):
        if monty_hall_problem():
            wins += 1
    return wins

description = """THE MONTY HALL PROBLEM:
Suppose you're on a game show, and you're given the choice of three doors.
Behind one door is a car; behind the others, goats.
You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.
He then says to you, 'Do you want to pick door No. 2?'
Is it to your advantage to switch your choice?
----------------------------------------------
THE SOLUTION:
In a word, yes.  Switching doors will raise your chances of winning from 1 in 3 to 2 in 3.
Doubt it?  Try for yourself:"""

print(description)
trials = input('How many trials would you like to run? ')
while type(trials) != int:
    try:
        trials = int(trials)
    except(ValueError):
        trials = input('This must be an integer! Try again: ')
print('Running trials (this can take a few seconds for high numbers)...')
wins = run_trials(trials)
print('You won the car '+str(wins)+' out of '+str(trials)+' times, or '+str((wins/trials)*100)+'% of the time!')
