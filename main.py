#Jaunel Deans 
#October 24, 2023 
#Time Reminder 

time = int(input("Enter a time between 0 and 23: "))#asks user for time 

if time < 8:#if time is less than 8 the following code will run
  print("TOO EARLY TO GET UP!!!")#prints "TOO EARLY TO GET UP!!!"
elif time >= 8 and time < 12:#if time is greater than or equal to 8 and less than 12 the following code will run. This will run if the previous condition is false. 
  print("Good Morning")#prints "Good Morning" is the statement is true
elif time >= 12 and time < 14:#if time is greater than or equal to 12 and less than 14 the following code will run. This will run if the previous condition is false.
  print("Lunch time!")#prints "Lunch time!" is the statement is true
elif time >= 14 and time < 18:#if time is greater than or equal to 14 and less than 18 the following code will run. This will run if the previous condition is false.
  print("Good afternoon")#prints "Good afternoon" is the statement is true
elif time == 18:#if time is equal to 18 the following code will run
  print("Tea Time")#prints "Tea Time" is the statement is true
elif time >= 18 and time <= 19:#if time is greater than or equal to 18 and less than or equal to 19 the following code will run. This will run if the previous condition is false.
  print("Good evening")#prints "Good evening" is the statement is true
elif time > 19 and time <= 22:#if time is greater than 19 and less than 22 the following code will run. This will run if the previous condition
  print("Nearly bedtime")#prints "Nearly bedtime" is the statement is true
elif time == 23:#if time is equal to 23 the following code will run if everything is false
  print("Good night!")
else:
  print("Sorry, I don’t recognise that")#if the previous conditions are false, the following code will run

