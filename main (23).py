import random

print('GHOST GAME')
feel_brave = True
score = 1
ghost_position = random.randint(1, 3)

while feel_brave:
    choice = int(input('choose room '))
    if choice == ghost_position:
        print('you lost')
        feel_brave = False 
    else:
        print('you survived!')
        score += 1
        ghost_position = random.randint(1, 3)  

print(f'Your score: {score}')
