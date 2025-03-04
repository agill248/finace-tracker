# This is a grocery store list


# Define a function to add an item to the list
def add_food(grocery_list: list, food: str):
    grocery_list.append(food)
    print("That food has been added!")
    return grocery_list

# Define a function to remove an item from the list
def remove_food(grocery_list: list, food: str):
    if food in grocery_list:
        grocery_list.remove(food)
        print("That food has been removed!")
    else:
        print("Please enter a food that is in your list.") # If not, display a message saying the item is not in the list
    return grocery_list

# Define a function to display the grocery list
def display_list(grocery_list: list):
    if grocery_list:
        print("\nHere is your current grocery list.")
        for index, food in enumerate(grocery_list, start=1): # Study this didn't understand had to check key
            print(f"{index}, {food}")
    else:
        print("Your grocery list is empty. Please fill it in with some yummy foods.") # If the list is empty, display a message

# Create a empty grocery list
grocery_list = []

# Use a loop to let the user choose an action: (1) Add, (2) Remove, (3) View and (4) Exit
print("Welcome to the Grocery Store List Simulator!")
while True:
    print("\nEnter a option: (1) Add a food, (2) Remove a food, (3) View your list, (4) Say a joke, (5) Recommend my favorite food place, (6) Exit")
    choice = input("Please enter your option.").strip()

    if choice == "1":
        food = input("Please enter a food to add.").strip()
        grocery_list = add_food(grocery_list, food)
    elif choice == "2":
        food = input("Please enter a food to remove!").strip()
        grocery_list = remove_food(grocery_list, food)
    elif choice == "3":
        display_list(grocery_list)
    elif choice == "4":
        print("Why is a graveyard a famous place? Because people are dying to get in there!")
    elif choice == "5":
        print("Next time you go out, go nandos their peri peri chicken is to die for!")
    elif choice == "6":
        print("Peace out!")
        break
    else:
        print("The choice you have made is invalid, please select a valid choice.")   
