# This is a grocery store list


# Define a function to add an item to the list
def add_food(grocery_list: list, food: str):
    grocery_list.append(food)
    return grocery_list

# Define a function to remove an item from the list
def remove_food(grocery_list: list, food: str):
    if food in grocery_list:
        grocery_list.remove(food)
    else:
        print("Please enter a food that is in your list.")

# If not, display a message saying the item is not in the list

# Define a function to display the grocery list

# If the list is not empty, print all items with numbers

# If the list is empty, display a message