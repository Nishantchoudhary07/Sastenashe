import random

from time import time,ctime
t = time()
n = ctime(t)
print(n)
print('Please enter your name here:')
m = input()

score,rounds = 0, 10

def guessGame():
    global score,rounds
    number = random.randint(1, 4)
    try:
        guess = int(input('Guess a number between 1 and 4:'))
        if guess == number:
            score+=1
            print('\n CORRECT \n your score is now: '+str(score)+'\n')
        else:
            score+=0
        rounds-=1
    except:
        print('\n you need to enter a whole numberbetween 1 and 4 \n')
    if rounds<1 or rounds<1 and score<1:
        print('\n your total score is: '+str(score))
        print('Goodbye')
    else:
        guessGame()
guessGame()
d = (m, ctime(t),str(score))
print(d)



with open('test.txt','a') as filecope:
    for leadset in d:
        filecope.write('%s\n'% leadset)



g = open('test.txt', 'r')
print(g.readlines())
g.close()


with open('test.txt','r')as z:
    h = z.readlines()
    i = 0
    num_users = len(h)/3
    print('total number of players: ')
    print(num_users)
    all_users = []
    for user in range(int(num_users)):
        u = []
        u.sort()
        for x in range(3):
            u.append(h[i+x])
        i+=3
        all_users.append(u)
    print(all_users)

def Sort(all_users):
    all_users.sort(key = lambda x:x[2], reverse = True)
    return all_users
print(Sort(all_users))
print(m,'your rank is:')

print(all_users.index(u)+1)

