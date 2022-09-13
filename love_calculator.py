# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combo = name1 + name2
combo = combo.lower()

t = combo.count("t")
r = combo.count("r")
u = combo.count("u")
e = combo.count("e")

true = t + r + u + e

l = combo.count("l")
o = combo.count("o")
v = combo.count("v")
e = combo.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
love_score = int(love_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


