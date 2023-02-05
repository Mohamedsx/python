import json
import random

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid][0] == target:
            return mid
        elif arr[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def insert_sort(arr):
    for i in range(1, len(arr)):
        key_name, key_value = arr[i]
        j = i-1
        while j >= 0 and arr[j][1][0] < key_value[0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = (key_name, key_value)
    return arr

# Load player data from JSON file
def load_data():
    try:
        with open("player_data.json", "r") as file:
            data = json.load(file)
            return data
    except:
        return {}

# Save player data to JSON file
def save_data(data):
    with open("player_data.json", "w") as file:
        json.dump(data, file)

# Store player data as a dictionary
player_data = load_data()

# Get player name from input
player_name = input("Enter your name: ")

# Check if player is an existing player
index = binary_search(list(player_data.items()), player_name)
if index != -1:
    player_score, player_tries = player_data[player_name]
else:
    player_score = 0
    player_tries = 0
    player_data[player_name] = [player_score, player_tries]

items = ["apple", "banana", "carrot", "dog", "egg", "flower", "guitar", "hat", "icecream", "jacket", "kangaroo",
         "lemon", "moon", "newspaper", "ocean", "pen", "quilt", "raccoon", "sunflower", "table", "umbrella", "violin",
         "watch", "xylophone"]
description = ["A round fruit with red or green skin and a white, juicy interior",
               "A long, curved fruit with a yellow or green skin and soft, sweet flesh",
               "A long, thin, orange root vegetable with a crisp texture",
               "A four-legged mammal with fur, a wagging tail, and a friendly disposition",
               "A oval shaped, white, or brown, oval shaped food item that comes from chickens",
               "A plant with brightly coloured petals and a sweet fragrance, often given as a gift",
               "A musical instrument with six strings and a hollow body, used for playing a variety of music",
               "A head covering worn for warmth, protection from the sun or rain, or as a fashion accessory",
               "A sweet, creamy frozen dessert made from milk, cream, and sugar",
               " A type of clothing worn on the upper body, typically made of a warm material",
               "A marsupial native to Australia, known for its powerful hind legs and tail used for hopping",
               "A small, round citrus fruit with a sour, acidic taste and a bright yellow skin",
               "A natural satellite of the Earth, visible at night as a bright, round object in the sky",
               " A printed publication containing news, articles, and information, often distributed daily",
               "A vast body of salt water that covers more than 70% of the Earth's surface",
               "A writing instrument with a small, replaceable ink cartridge, used for writing on paper",
               "A type of bedding made of two layers of fabric stitched together with padding in between",
               "A mammal with a distinctive black and white face, known for its intelligence and adaptability",
               "A tall, yellow-flowered plant with large, ray-like petals and a dark central disk",
               "A piece of furniture with a flat top and one or more legs, used for supporting objects or holding things",
               "A portable, collapsible canopy supported on a central pole, used for protection from rain or sun",
               "A stringed musical instrument with four strings, held between the chin and shoulder and played with a bow",
               "A small timepiece worn on the wrist or carried in a pocket, used for keeping track of time",
               " A musical instrument consisting of a set of wooden bars that are struck with a mallet to produce musical tones"]

# combine the two arrays together

combine = list(zip(description, items))
# create 6 random items with description
random_items = random.sample(combine, 6)
# creating counter for correct guess and current element
correct_guess = 0
current_element = 0
tries = 3
while correct_guess < 3 and current_element < len(random_items):
      incorrect_guess = 0

      print(f"Description: {random_items[current_element][0]}")

      while incorrect_guess < 3:
        print("what item am I?:")
        player_guess = str(input())
        if player_guess == random_items[current_element][1]:
          player_score += 1
          print("you guessed correctly! your score is now {}".format(player_score))
          correct_guess += 1
          current_element += 1
          break

        else:
          incorrect_guess += 1
          tries -= 1
          print("incorrect guess, you have {} tries left". format(tries))

      if incorrect_guess == 3:
        current_element += 1
        break

if correct_guess == 3:
  print("CONGRATULATIONS YOU HAVE WON!, your Final score is {}".format(player_score))

else:
  print("SORRY, YOU HAVE LOST")

# Update player score and number tries
player_tries += 1
player_data[player_name] = [player_score, player_tries]

# Save Updated player data
save_data(player_data)

# Sort player data by score and create a league table
league_table = insert_sort(list(player_data.items()))

# Store league table data in a separate json file
with open("league_table.json", "w") as file:
  json.dump(league_table, file)

# Display the league table
print("League Table:")
for player in league_table:
    print("{}: {}".format(player[0], player[1][0]))
