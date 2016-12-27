import random

def monty_hall_problem():
    a = False
    b = False
    c = False
    #place the car
    door = random.randint(1,3)
    if door == 1:
        a = True
    elif door == 2:
        b = True
    else:
        c = True
    #player's 1st choice
    door = random.randint(1,3)
    if door == 1:
        first_choice = 'a'
    elif door == 2:
        first_choice = 'b'
    else:
        first_choice = 'c'
    #host's choice
    if first_choice == 'a':
        if b:
            hosts_choice = 'c'
        else:
            hosts_choice = 'b'
    elif first_choice == 'b':
        if a:
            hosts_choice = 'c'
        else:
            hosts_choice = 'a'
    else:
        if a:
            hosts_choice = 'b'
        else:
            hosts_choice = 'a'
    #player switches doors
    available_doors = ['a','b','c']
    picked_doors = [hosts_choice, first_choice]
    second_choice = [i for i in available_doors if i not in picked_doors][0]
    #winner?
    if second_choice == 'a' and a:
        winner = True
    elif second_choice == 'b' and b:
        winner = True
    elif second_choice == 'c' and c:
        winner = True
    else:
        winner = False
    return winner

def run_trials(trials):
    wins = 0
    for i in range(trials):
        if monty_hall_problem():
            wins += 1
    return wins

print('THE MONTY HALL PROBLEM:')
print("Suppose you're on a game show, and you're given the choice of three doors.")
print("Behind one door is a car; behind the others, goats.")
print("You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.")
print("He then says to you, 'Do you want to pick door No. 2?'")
print("Is it to your advantage to switch your choice?")
print('----------------------------------------------')
print('THE SOLUTION:')
print('In a word, yes.  Switching doors will raise your chances of winning from 1 in 3 to 2 in 3.')
print('Doubt it?  Try for yourself:')
trials = input('How many trials would you like to run? ')
while type(trials) != int:
    try:
        trials = int(trials)
    except(ValueError):
        trials = input('This must be an integer! Try again: ')
print('Running trials (this can take a few seconds for high numbers)...')
wins = run_trials(trials)
print('You won the car '+str(wins)+' out of '+str(trials)+' times, or '+str((wins/trials)*100)+'% of the time!')
