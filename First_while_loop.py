answer_1 = int(input('When was Python 1.0 released? '))
while(answer_1 != 1994):
    if answer_1 < 1994:
        print('It was later than that!')
    elif answer_1 > 1994:
        print('It was earlier than that!')
    answer_1 = int(input('When was Python 1.0 released? '))
print('Correct!')
