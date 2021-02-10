print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

t = (name1 + name2).count("t")
r = (name1 + name2).count("r")
u = (name1 + name2).count("u")
e = (name1 + name2).count("e")
l = (name1 + name2).count("l")
o = (name1 + name2).count("o")
v = (name1 + name2).count("v")

true = t + r + u + e
love = l + o + v + e

love_score = str(true) + str(love) 

if int(love_score) < 10 or int(love_score) > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) > 40 and int(love_score) < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
