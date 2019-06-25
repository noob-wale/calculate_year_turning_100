#import datetime module 
import datetime
now = datetime.datetime.now()
print(now.year, now.month, now.day)
#request for the user's name
user_name = input('Hi. Please enter your name:')
#request for the user's age
print('Hello, ' , user_name)
user_age = int(input('Please enter your age: '))
#print and calculate year they are turning 100
print('You will turn 100 in the year,' , ((now.year-user_age+100)))
