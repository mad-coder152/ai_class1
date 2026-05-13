print("Hello! I'm AI bot! What's your name?")
name = input("Please enter here...")

print(f"Nice to meet you, {name}!")
print("How are you feeling today? (good/bad)")
mood = input("Please enter here..").lower()

if "good" in mood:
    print("I'm glad to hear that.")
elif "bad" in mood:
    print("I'm sorry to hear that. Hope things get better soon.")
else:
    print("I see sometimes its hard to put feelings to words.")

print(f"it was nice chatting with you, {name}. Goodbye!")