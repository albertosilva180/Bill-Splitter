# write your code here
import random

print('Enter the number of friends joining (including you):')
number_of_friends = int(input())
if number_of_friends > 0:
    friends = {}
    print('Enter the name of every friend (including you), each on a new line')
    for i in range(number_of_friends):
        name_friend = input()

        friends[name_friend] = 0
    # print(friends)
    print()
    print('Enter the total bill value:')
    total_bill = float(input())
    lucky_one = ''
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    use_feature = input()
    if use_feature == 'Yes':
        lucky_one = random.choice(list(friends.keys()))
        print(lucky_one, 'is the lucky one!')
        number_of_friends -= 1
    else:
        print('No one is going to be lucky')
    one_part = round(total_bill / number_of_friends, 2)
    for i in friends:
        friends[i] = one_part
    if use_feature == 'Yes':
        friends[lucky_one] = 0
    print(friends)
else:
    print('No one is joining for the party')
