import sys
import operator


#Initialize the node structure class
class Node:
    def __init__(self, Parent, current, cost, depth, total, uninformed):
        self.Parent = Parent
        self.current = current
        self.cost = cost
        self.depth = depth
        self.total = total
        self.uninformed = uninformed

    # A string presentation of the node
    def __str__(self):
        if self.uninformed:
            return self.current+": g(n)= "+str(self.cost) + ",d= "+str(self.depth)+",Parent ->{"+str(self.Parent)+"}"
        else:
            return self.current+": g(n)="+str(self.cost)+",d= "+str(self.depth)+", f(n) = "+str(self.total)+", Parent ->{"+str(self.Parent)+"}"

 #Initialize the function that uses map and heuristic to create child nodes
def expand_node(node, map, heuristic, SearchType):
    actions = map[node.current]
    child = []
    for i in actions:
        costtotal = node.cost + i[1]
        if node.uninformed:
            child.append(Node(node, i[0], costtotal, node.depth + 1, 0, node.uninformed))
        else:
            child.append(Node(node, i[0], costtotal, node.depth + 1, costtotal + heuristic[i[0]], node.uninformed))
    return child

#Initialize the key function for sorting
def get_key(item, n):
    return item[n]

#Initialize the function that reconstruct the path from the node
def reconstruct_path(node, map, SearchType):
    path = []
    distance = node.cost
    while node is not None:
        parent = node.Parent
        if parent is not None:
            action = (a for a in map[parent.current] if a[0] == node.current)
            a = next(action)
            path.append(parent.current + " to " + node.current + ", " + str(a[1]) + " kms")
        node = parent
    path.reverse()
    print("distance : " + str(distance))
    print("route :")
    for i in path:
        print(i)

#Initialize the function that reads the input file
def read_input_files(file_name):
    file_data = open(file_name, 'r')
    city_map = {}
    for line in file_data:
        line = line.lstrip()
        line = line.rstrip()
        line = line.rstrip('\n')
        line = line.rstrip('\r')
        if line != 'END OF INPUT':
            city_distance = line.split(' ')
            city_distance[2] = float(city_distance[2])

            if city_distance[0] in city_map:  # handle city 1 --> city 2
                city_map[city_distance[0]].append([city_distance[1], city_distance[2]])
            else:
                city_map[city_distance[0]] = [[city_distance[1], city_distance[2]]]
            if city_distance[1] in city_map:  # handle city 2 --> city 1
                city_map[city_distance[1]].append([city_distance[0], city_distance[2]])
            else:
                city_map[city_distance[1]] = [[city_distance[0], city_distance[2]]]
        else:
            return city_map

#Initialize the function that reads the heuristic file
def read_heuristic_files(file_name):
    file_data = open(file_name, 'r')
    heuristic = {}
    for line in file_data:
        line = line.lstrip()
        line = line.rstrip()
        if line != 'END OF INPUT':
            data = line.split(' ')
            data[1] = float(data[1])
            heuristic[data[0]] = data[1]
        else:
             return heuristic
        

def main():
    #Check to see if the command line arguments provided wants to perform an informed search or an uninformed search
    if len(sys.argv) == 5:
        print("Informed Search")
        uninformed = False
    else:
        print("uninformed search")
        uninformed = True

    #Read the input file and handle cases where there is no input file indicated in the command line
    if len(sys.argv) != 1 :
       map = read_input_files(sys.argv[1])
    else:
        print("ERROR: No input file found")
        sys.exit()

    #Initialize the variables for the final output
    node_expanded = 0
    max_fringe = 0
    node_generated = 1
    node_popped = 0
    heu = {}

    #Check to see whether or not it's an informed search, if not read the heuristic file
    if not uninformed:
        heu = read_heuristic_files(sys.argv[4])

    #Initialize the fringe with the starting node
    fringe = []
    if uninformed:
        fringe.append(Node(None, sys.argv[2], 0, 0, 0, uninformed))
    else:
        fringe.append(Node(None, sys.argv[2], 0, 0, heu[sys.argv[2]], uninformed))

    closed = []

    #Initialize the max fringe before the loop
    if len(fringe) > max_fringe:
        max_fringe = len(fringe)

    #Initialize the search loop
    while len(fringe) > 0:
        node_popped += 1

        #Pop the node from the fringe
        node = fringe.pop(0)

        #Check to see if the goal state is reached
        if node.current != sys.argv[3]:

            #Check to see if the current state has been visited before
            if node.current not in closed:
                closed.append(node.current)

                #Generate successor nodes
                successor = expand_node(node, map, heu, node_expanded)

                #Initialize the loop to add successors to the fringe
                for i in successor:
                    fringe.append(i)
                    
                node_generated = node_generated + len(successor)
                node_expanded += 1

                #Sort the fringe based on 'cost' and 'total' depending on the search type
                if uninformed:
                    fringe = sorted(fringe, key=operator.attrgetter('cost'))
                else:
                    fringe = sorted(fringe, key=operator.attrgetter('total'))

                #Situational update for the max_fringe variable
                if len(fringe) > max_fringe:
                    max_fringe = len(fringe)

        #Print the output if the goal state is reached and exit
        else:
            print("Nodes Popped: " + str(node_popped))
            print("Nodes Expanded: " + str(node_expanded))
            print("Nodes Generated: " + str(node_generated))
            reconstruct_path(node, map,node_expanded)
            sys.exit()

    #Print the output if the no solution or path to the goal state is found
    else:
        print("Nodes Popped: " + str(node_popped))
        print("Nodes Expanded: " + str(node_expanded))
        print("Nodes Generated: " + str(node_generated))
        print("Distance: infinity")
        print("Route: none")

if __name__ == "__main__":
    main()