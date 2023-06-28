date = int(input('How many days ago have you purchased the item? '))
answer_a = input('Have you used the item at all y/n? ')
answer_c = input('Has the item broken down on its own y/n? ')
# If the purchase date is less than or equal to 10 days
# If the item has been not been used
# If the item broke on it's own
# If the purchase date is more than 10 days
if answer_c == 'y':
    print('You can get a refund!')
elif date <= 10 and answer_a == 'n':
    print('You can get a refund!')
else:
    print('You cannot get a refund.')
