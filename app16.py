guess_count = 0
secret_number = 7
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess # 0-9: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!!')
        break
else:
    print('Sorry, you lost :(')