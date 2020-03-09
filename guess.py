import random

random_number = random.randrange(1, 10)
print(random_number)
user_input = int(input('Guess the number: '))
count = 1
while random_number != user_input:
    count += 1
    if random_number > user_input:
        print('Your guess is low. Try again!')
        user_input = int(input('Guess the number: '))
    elif random_number < user_input:
        print('Your guess is high. Try again!')
        user_input = int(input('Guess the number: '))
    else:
        print('You got it! ')


print('It took you, ', count)
