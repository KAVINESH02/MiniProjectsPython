print('Welcome to the quiz show! ')

var = input('Are you intrested in my show! ').lower()

if var != 'yes':
    print('Thank you')
    quit ()
else:
    print('Lets get started! ')
    
score = 0

answer = input('What is a cpu? ').lower()
if answer == 'central processing unit' :
    print('Correct!! ')
    score +=1
else:
    print('Incorrect')
    
answer = input('What is a gpu? ').lower()
if answer == 'graphics processing unit' :
    print('Correct!! ')
    score +=1
else:
    print('Incorrect')
    
answer = input('What is a psu? ').lower()
if answer == 'power supply unit' :
    print('Correct!! ')
    score +=1
else:
    print('Incorrect')

answer = input('What is a ram? ').lower()
if answer == 'random access memory' :
    print('Correct!! ')
    score +=1
else:
    print('Incorrect')
    
answer = input('What is a gb? ').lower()
if answer == 'giga byte' :
    print('Correct!! ')
    score +=1
else:
    print('Incorrect')
    
answer = input('What is a tb? ').lower()
if answer == 'tera byte' :
    print('Correct!! ')
    score +=1
else:
    print('Incorrect')
    
answer = input('What is a rtx 4090 called? ').lower()
if answer == 'graphics card' :
    print('Correct!! ')
    score +=1
else:
    print('Incorrect')
    
print("You got " + str(score) + " questions correct!!")
print("You got a percentage of " + str((score/7)*100) + " %.")
    
