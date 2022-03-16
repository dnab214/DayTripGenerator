

# Welcome to your Day Trip Generator
import random


user_story_header = ("Welcome to your Day Trip Generator!")
print(user_story_header)

user_story_subheader = ("Let's get your day going!")
print(user_story_subheader)

my_destinations = []
my_destinations.append("Kaiserslautern")
my_destinations.append("Liverpool")
my_destinations.append("Burgundy")
my_destinations.append("Sardinia")
my_destinations.append("Malaga")

my_restaurants = []
my_restaurants.append("Extrablatt")
my_restaurants.append("Delamina")
my_restaurants.append("Caves Madeleine")
my_restaurants.append("Ambiente")
my_restaurants.append("Los Marangos")

my_transportation = []
my_transportation.append("tram")
my_transportation.append("taxi")
my_transportation.append("train")
my_transportation.append("Uber")

my_entertainment = []
my_entertainment.append("museum")
my_entertainment.append("site seeing")
my_entertainment.append("ziplining")
my_entertainment.append("wine tasting")
my_entertainment.append("ethnic parade")
my_entertainment.append("hiking")
my_entertainment.append("hookah lounge")

def random_from_list(my_choices):
    random_item = random.choice(my_choices)
    return random_item

rand_dest = random_from_list(my_destinations.append)

rand_rest = random_from_list(my_restaurants.append)

rand_trans = random_from_list(my_transportation.append)

rand_ent = random_from_list(my_entertainment.append)


def display_greeting():
    print("Good morning, Deondre!")

def first_question():
    print("Where would you like to go for today?")
    if(first_question) == (my_destinations[0]):
        print("Great! Now let's get some grub!")
    elif(first_question) == (my_destinations[1]):
        print("No worries! Let's try again.")
    elif(first_question) == (my_destinations[2]):
        print("No worries! Let's try again.")
    elif(first_question) == (my_destinations[3]):
        print("No worries! Let's try again.")
    elif(first_question) == (my_destinations[4]):
        print("We're out of options!")

for first_question in my_destinations[1]:
    print("Great! Now let's get some grub!")

for first_question in my_destinations[2]:
    print("Great! Now let's get some grub!")

for first_question in my_destinations[3]:
    print("Great! Now let's get some grub!")

for first_question in my_destinations[4]:
    print("Great! Now let's get some grub")



def second_question():
    print("Would you like to try out Extrablatt?")
    if(second_question) == (my_restaurants[0]):
        print("Awesome! That's the best spot in the city!")
    elif(second_question) == (my_restaurants[1]):
        print("Oops! That's not in this location.")
    elif(second_question) == (my_restaurants[2]):
        print("Oops! That's not in this location.")
    elif(second_question) == (my_restaurants[3]):
        print("Oops! That's not in this location.")
    elif(second_question) == (my_restaurants[4]):
        print("We're out of options!")


def third_question():
    print("How would you like to get there?")
    if(third_question) == (my_transportation[0]):
        print("Great! The next tram's coming at 1420.")
    elif(third_question) == (my_transportation[1]):
        print("Oh no! Let's try again.")
    elif(third_question) == (my_transportation[2]):
        print("Oh no! Let's try again.")
    elif(third_question) == (my_transportation[3]):
        print("We're out of options!")

for third_question in my_transportation[1]:
    print("Cool! There's a taxi that will arrive in 3 minutes.")

for third_question in my_transportation[2]:
    print("Alright! The next's train is set to arrive at 1500.")

for third_question in my_transportation[3]:
    print("According to Uber, the closest ride is 5 minutes away.")



def last_question():
    print("There's plenty of activities to choose from. Which would you like to do?")
    if(last_question) == (my_entertainment[0]):
        print("There's a museum nearby called Raastadt and it's a great place to visit. Let's go!")
    elif(last_question) == (my_entertainment[1]):
        print("Okay, no problem. Let's try again!")
    elif(last_question) == (my_entertainment[2]):
        print("Not feeling that right now I see. Give it another go!")
    elif(last_question) == (my_entertainment[3]):
        print("Bummer. Let's find something else!")
    elif(last_question) == (my_entertainment[4]):
        print("We only have a couple more options left!")
    elif(last_question) == (my_entertainment[5]):
        print("Only one choice left!")
    elif(last_question) == (my_entertainment[6]):
        print("We're all out of options, unfortunately!")


