# Create an High Score Tracker

# Create function to update the score
def update_score(scores: list, fresh_score: int):

# Append the new score to the list
    scores.append(fresh_score) # append is used to add things to the end of the list

# Sort the list in descending order
    scores.sort(reverse=True) # Study this part

# Keep the top 5 scores only
    return scores[:5]

# Make a list for the score
new_scores = []

# Use a loop to let the user enter scores until they type -1
while True:
    fresh_scores = int(input("Please enter a score, otherwise type the number -1 to stop! "))
    if fresh_scores == -1:
        break
# Call the function with each new score and display the updated top 5 scores
    new_scores = update_score(new_scores, fresh_scores)
    print(f"Here are the updated scores: {new_scores}")
        