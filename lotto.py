import random
listnumber = input(print("Enter three numbers between 1 and 10 and separate by a space"))
print("\n")
user_list = listnumber.split()
#print list
print("list", user_list)
#convert the strings into integers
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])
    
print("The numbers that you chose are", user_list)

#This generates three random numbers between 1 and 10
randomList = random.sample(range(1, 10), 3)
print("Our winning numbers are", randomList)
