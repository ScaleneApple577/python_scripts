import random
import sys

# Create empty dictionary
country_capital = {}

# File containing countries and capitals
f = open("country_list.txt", "r")
for line in f:
  (key, val) = line.split(":")
  country_capital[key] = val

print(country_capital)
length = len(country_capital)
print ("Number of countries in this quiz " + str(length))
question_num = 0
score = 0
while question_num < 20:
  question_num += 1
  print("#" + str(question_num),  end =" ")
  index = random.randint(0,length-1)
  key = list(country_capital)[index]
  answer = input("What is the capital of " + key + ": ")   
  correct_answer = country_capital[key]
  print("Your answer is " + answer)
  if answer.lower().strip() == correct_answer.lower().strip():
    print(answer + " is correct")
    score += 1
  else:
    print("Incorrect, the correct answer is: " + correct_answer.strip())
  print ("Score: " + str(score) + "/" + str(question_num))

print("Final Score: " + str(score) + "/" + str(question_num))
