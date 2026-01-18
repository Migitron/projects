#Migitron
#Magic eight ball project
#1/16/2026

#using the random module 
import random

#variable for who will be asking the question
name = input('enter you name:')

#variable for question
question = input('What is your question?')

#variable to store the answer in 
answer = ''

#variable to store random number
random_number = random.randint(1,11)

#setting up answers based on random number generated
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "I am not sure right now"
elif random_number == 3:
  answer = "Without a doubt YES!"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "I can not tell you now"
elif random_number == 7:
  answer = "My sources say NO"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Yes"
else:
  answer = "Yup"

#printing an error message if not question is asked
if question == "":
  print("ERROR: you need to ask a question")
# if no name is provided
elif name == "":
  print("Question:", question)
  print("Magic 8-Ball's answer:", answer) 
#standard message
else:
  print(name, "asks:", question)
  print("Magic 8-Ball's answer:", answer)

