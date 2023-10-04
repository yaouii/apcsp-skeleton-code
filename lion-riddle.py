import copy

def isValid(state):
    if state["num_lions_left"] < 0 or state["num_lions_right"] < 0 or state["num_wildabeasts_left"] < 0 or state["num_wildabeasts_right"] < 0:
        return False
    else:
        if state["num_lions_left"] > state["num_wildabeasts_left"] or state["num_lions_right"] > state["num_wildabeasts_right"]:
            return False
        else:
            return True

def generate_next_states(current_state):
    next_states = []

    # Determine the side of the river the boat is on
    if current_state["boat"] == "left":
        for lions_to_move in range(1, 3):
            for wildabeasts_to_move in range(1, 3):
                # Ensure that at least one animal is moved on each side
                if lions_to_move + wildabeasts_to_move >= 1:
                    new_state = copy.deepcopy(current_state)

                    new_state["num_lions_left"] -= lions_to_move
                    new_state["num_wildabeasts_left"] -= wildabeasts_to_move
                    new_state["num_lions_right"] += lions_to_move
                    new_state["num_wildabeasts_right"] += wildabeasts_to_move
                    new_state["boat"] = "right"

                    if isValid(new_state):
                        next_states.append(new_state)
    else:
        for lions_to_move in range(1, 3):
            for wildabeasts_to_move in range(1, 3):
                # Ensure that at least one animal is moved on each side
                if lions_to_move + wildabeasts_to_move >= 1:
                    new_state = copy.deepcopy(current_state)

                    new_state["num_lions_right"] -= lions_to_move
                    new_state["num_wildabeasts_right"] -= wildabeasts_to_move
                    new_state["num_lions_left"] += lions_to_move
                    new_state["num_wildabeasts_left"] += wildabeasts_to_move
                    new_state["boat"] = "left"

                    if isValid(new_state):
                        next_states.append(new_state)
    
    return next_states

def dfs(current_state, win_state):
    if current_state == win_state:
        return True  # Goal state reached

    visited_states.append(current_state)

    next_states = generate_next_states(current_state)
     
    for next_state in next_states:
        if next_state not in visited_states:
            path.append(next_state)
            if dfs(next_state, win_state):
                return True  # Goal state found
            path.pop()

# Example usage:
initial_state = {
    "boat": "left",
    "num_lions_left": 3,
    "num_wildabeasts_left": 3,
    "num_lions_right": 0,
    "num_wildabeasts_right": 0,
}

win_state = {
    "boat" : "right",
    "num_lions_left" : 0,
    "num_wildabeasts_left" : 0,
    "num_lions_right" : 3, 
    "num_wildabeasts_right" : 3
}

visited_states = []
path = []

print("Initially, there are", initial_state["num_lions_left"], "lions &", initial_state["num_wildabeasts_left"], "wildebeasts on the left.")
print("There are", initial_state["num_lions_right"], "lions &", initial_state["num_wildabeasts_right"], "wildebeasts on the right.")
print("The boat is on the", initial_state["boat"])

if dfs(initial_state, win_state):
    for index, step in enumerate(path):
        print("After move", index+1, "there are", step["num_lions_left"], "lions &", step["num_wildabeasts_left"], "wildebeasts on the left.")
        print("&", step["num_lions_right"], "lions &", step["num_wildabeasts_right"], "wildebeats on the right.")
        print("The boat is on the", step["boat"])
else:
    print("No solution found.")
