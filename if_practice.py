user_age = int(input('what is your age? '))
if user_age > 30:
    print('You are over 30 years old')
    print('Sorry, you do not qualify')
elif user_age == 30:
    print('You are exactly 30 years old')
    print('You must provide additional details to qualify')
else:
    print('You are younger than 30 years old')
    print("Congrats! You qualify")

