## Health Potion

import random
health = 50
difficulty = input("Set the game difficulty: ")
potion_health = random.randint(25, 50) / int(difficulty)
print("Your health potion value is: " + str(potion_health))
health = health + potion_health
print('The current health is: ' + str(health))


