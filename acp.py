#Name
print("Hello! I'm AI bot! What's your name?")
name = input("")
print(f"Nice to meet you, {name}!")

#Mood
print("How are you feeling today? (good/bad)")
mood = input("").lower()
if "good" in mood:
    print("I'm glad to hear that.")
elif "bad" in mood:
    print("I'm sorry to hear that. Hope things get better soon.")
else:
    print("I see sometimes its hard to put feelings to words.\n")

#Age
print(f"How old are you, {name}?")
age = int(input(""))

if age>=18:
    print("Oh, you're an adult. You have a right to vote and drive.")
elif age < 18:
    print("Oh, you're quite young! You can't use various websites, drive or vote.")
else:
    print("I understand you can't share some data with me and I respect your privacy.")

#Season
print("Do you enjoy summers or winters more?")
season = input("").lower()

if "summer" in season:
    print("Summers are the best! Beaches, juices and MANGOES, lovely choice!")
elif "winter" in season:
    print("Amidst sweaters, heaters and mountain trips, winters are full of coziness and joy!")
else:
    print("It seems you're unable to make a definite choice.")

#Book ya movie
print("What do you prefer: books or movies?")
enjoy = input("").lower()
if "book" in enjoy:
    print("A cozy corner, and a few aesthetic lightings are what you need to read and enjoy a great novel!")
elif "movie" in enjoy:
    print("Nice sound, great picture quality and a couple bags of popcorn and infinite thrill!")
else:
    print("Seems like you're unable to decide.")

#coffee ya tea
print("What you prefer: coffees or teas?")
drink = input("")
if "coffee" in drink:
    print("So, you like coffee.")
    brand = input("Barista or Starbucks?").lower()
    if brand == "barista":
        print("Barista is a nice one!")
    elif brand == "starbucks":
        print("Starbucks is wonderful if you crave good coffee.")
    else:
        print("Oh, I couldn't quite get that")
elif "tea" in drink:
    print("So, you like coffee.")
    brand2 = input("Chaayos or local tea?").lower()
    if brand2 == "chaayos":
        print("Chaayos is a wonderful area for chaat and tea!")
    elif brand2 == "local tea":
        print("Whatever anyone might say, local teas hit different.")
    else:
        print("Oh, I couldn't quite get that")
else:
    print("I respect your choice to not answer")
    
#Ending
print(f"It was nice chatting with you, {name}. Goodbye!")

