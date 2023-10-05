import copy

# Define a function that takes in a state as a dictionary and returns True if the state meets the conditions and False if it does not
def isValid(state):
    

# Define a function that takes in a state as a dictionary and returns a list of all valid states that can be reached from 1 move of the input state
# This function will need to call the function isValid(state)
def get_next_states(state):


# Define a recursive function that takes in a current_state and win_state and returns the path to those states using the Depth First Search algorithm
# This function will need to call the function get_next_states(state), as well as itself
def dfs(current_state, win_state):
    
    
# Test your code! Does it solve the river crossing riddle?
initial_state = {
    "wolf": False,
    "goat": False,
    "cabbage": False,
    "person": False
}

win_state = {
    "wolf": True,
    "goat": True,
    "cabbage": True,
    "person": True
}

visited_states = [initial_state]
path = []

if dfs(initial_state, win_state):
    for index, step in enumerate(path):
        print("After move", index+1, "the state is ", step)
else:
    print("No solution found.")

