# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

n1 = name1.lower()
n2 = name2.lower()



t= n1.count("t") + n2.count("t")
r= n1.count("r") + n2.count("r")
u= n1.count("u") + n2.count("u")
e= n1.count("e") + n2.count("e")

true= t+r+u+e

l= n1.count("l") + n2.count("l")
o= n1.count("o") + n2.count("o")
v= n1.count("v") + n2.count("v")
e= n1.count("e") + n2.count("e")


love= l+o+v+e

love_score= str(true)+str(love)
love_score= int(love_score)

if love_score <= 10 or love_score >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")



