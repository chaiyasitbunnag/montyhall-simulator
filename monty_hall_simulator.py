import random

## To shuffle x doors
def shuffle_doors():
    door = ['car', 'goat', 'goat']
    random.shuffle(door)
    return door

## To switch door when goat showed   
def switch(doors):
    random_point = random.choice([0,1,2]) # Randomly select the door
    # Opened 'goat' from the other two doors
    opened = [idx for idx, element in enumerate(doors) if element == 'goat' and idx != random_point]
    opened = random.choice(opened)
    # Switch to the door which haven't been selected and opened
    switched = [element for idx, element in enumerate(doors) if idx not in [random_point, opened]][0]
    
    if switched == 'car':
        return True
    else:
        return False

set_doors = []
n_times = 1000000
for i in range(n_times):
    doors = shuffle_doors()
    set_doors.append(doors)

results = []
for doors in set_doors:
    results.append(switch(doors))
    
sum(results) / n_times