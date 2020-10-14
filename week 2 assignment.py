# Assignment 1

Electirc guitar = {
  "brand": "Ibanez",
  "location": "storage room",
  "strings": 6,
  "color": "white"
  "handle": True
  }

Apple laptop = {
  "Brand": "Apple",
  "location": "living room",
  "Color": "Silver",
  }

Broken nail clippers == {
  "material": "metal",
  "location": "trash",
  "broke": True,
  }

Breakfast = {
  "ingredient1": "egg",
  "ingredient2": "Toast",
  "drink": "coffee",
  }

#assignment 2
myDog = {
  "name": "Jack",
  "location": "home",
  "legnumber": 4,
  "furry": False
  }
print myDog

#Assignment 3

# let the user know what's going on
print ("Welcome to MadLibs!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables 
adjective1 = raw_input("Enter an adjective that describe yourself: ")
name1 = raw_input("Enter your name:")
color1 = raw_input("What is your favorite color?: ")
location1 = raw_input("Name a place: ")
object1 = raw_input("An object from your home: ")
famousPerson1 = raw_input("A famous person you don't really like: ")
famousPerson2 = raw_input("A famous person you that is you're favorite: ")
countryName = raw_input("Which country favorite country?: ")
adjective2 = raw_input("Desribe the object from your home: ")

# story

story = "Hello, I am " + adjective1 + " " + name1 + "  I love things that contain color " + color1 + " I currently live in " + location1 + ", " \
"I am carrying a " + object1 + " for my friend " + famousPerson1 + ". " \
"This is a " + adjective2 +  object1 + " made in " + countryName + " It is really expensive. " \
"" + famousPerson1 + " collected it then goes home to where ever he came from. " \
"One autumn afternoon " + famousPerson1 + " is sent by " + famousPerson2 + " " \
"to take some cash back to " + countryName + "."

print (story)
