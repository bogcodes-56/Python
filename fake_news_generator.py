import random

names = ["President", "Alien", "CEO", "Robot", "Teenager", "SRK"]
actions = ["discovers", "destroys", "launches", "hacks", "saves"]
places = ["New York", "Mars Base", "Secret Lab", "Tech Summit", "Ocean Floor"]

while True:
    subject = random.choice(names)
    action = random.choice(actions)
    place = random.choice(places)

    headlines = f"BREAKING NEWS : {subject} {action} at {place}!"
    print("\n",headlines)

    user_input = input("\n Do you want to generate another fake news headline? (yes/no): ".strip().lower())
    
    if user_input == "no":
        break
    
print("\n Thank you for using Fake News Generator!!!")
