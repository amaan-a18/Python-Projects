def getTextFromFile(fileName):
  with open(fileName, "r") as file:
    return file.readlines()

fileName = "US_States.txt"
lines = getTextFromFile(fileName) #Read the data from the file

"""2. Create the adjacency list."""

adjacencies = dict()  #Dictionary to store the adjacency list
for line in lines:  #Reading each line in the adjacency list
  line = line.replace("\n", "") #Getting rid of any new lines
  node = line.split("\t")[0]  #Finding the state
  neighbours = line.split("\t")[1].replace("\n", "").split(",") #Finding the neighbours
  adjacencies[node] = neighbours  #Storing the neighbours for the state

"""3. Write the map-colouring function"""

def colour_map(graph, state_names, num_colours):
  assigned_colours = {state: None for state in state_names} #Initialization of colours to None for all states.

  #Function to check if the colouring is safe
  def is_safe(state, colour, current_colours):
    for neighbour in graph[state]:  #Looping through all the neighbours
      if current_colours.get(neighbour) == colour:
        return False  #If the neighbour is having the same colour, then it is not safe
    return True #If no neighbour is having the same colour, then it is safe.

  #Function to implement backtracking
  def backtrack(state_index):
    if state_index == len(state_names): #Check if we have completed the colouring
      return True
    current_state = list(graph.keys())[state_index] #Select the first uncoloured state

    for colour in range(num_colours): #For the colours in the map colours...
      if is_safe(current_state, colour, assigned_colours):  #Check and see if the colouring is safe
        assigned_colours[current_state] = colour  #If the colouring is safe, then we assign to the node and continue
        if backtrack(state_index + 1):  #Check to see if the next state can be assigned...
          return True #Return that the next node can be checked.
        assigned_colours[current_state] = None  #The next node is not safe, so we must backtrack. This is done by unassigning the node.
    return False  #No solution is found after backtracking through all the nodes and all the values

  if backtrack(0):  #If we find a suitable colouring starting from the first state
    return assigned_colours #Return the selected set of colours
  else:
    return None #Else say that no solution is possible

mapColours = ["RED", "BLUE", "GREEN", "YELLOW"] #4 colours - we can try lesser colours as well!
num_colors = len(mapColours)
coloured_map = colour_map(adjacencies, list(adjacencies.keys()), num_colors)

if coloured_map:
    for state, colour in coloured_map.items():
        print(f"State: {state}, Color: {mapColours[colour]}")
else:
    print("No solution found for the given number of colors.")