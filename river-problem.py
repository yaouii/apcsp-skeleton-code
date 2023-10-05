import copy


def isValid(state):
    if state["wolf"] == state["goat"] and state["wolf"] != state["person"]:
        return False
    elif state["cabbage"] == state["goat"] and state["cabbage"] != state["person"]:
        return False
    else:
        return True



def get_next_states(state):

    next_states = []

    same_side = []
    for key in state:
        if state["person"] == state[key] and key != "person":
            same_side.append(key)
    print("This is the same side list ", same_side)

    for item in same_side:
       
        temp_state = copy.deepcopy(state)
        temp_state["person"] = not state["person"]
        temp_state[item] = not state[item]
        
        if (isValid(temp_state)):
            next_states.append(temp_state)
        else:
            temp_state[item] = state[item]
            next_states.append(temp_state)

    print(next_states)
    return next_states

def dfs(current_state, win_state):
    
    if current_state == win_state:
        return True  # Goal state reached

    visited_states.append(current_state)

    next_states = get_next_states(current_state)
     
    for next_state in next_states:
        if next_state not in visited_states:
            path.append(next_state)
            if dfs(next_state, win_state):
                return True  # Goal state found
            path.pop()

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

visited_states = []
path = []

if dfs(initial_state, win_state):
    for index, step in enumerate(path):
        print("After move", index+1, "the state is ", step)
else:
    print("No solution found.")

