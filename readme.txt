- Name Nam Nguyen

- UTA ID 1001823561

- Programming language used for the task Python, the code is omega compatible. 

- How the code is structured:
* Node class:
+ The '__init__' method contains attributes like 'self', 'Parent', 'current', 'cost', 'depth', 'total', 'uninformed' that would be used in the main method.
+ The '__str__' method provides a string representation of the node.

* Function definitions:
+ The 'expand_node' function generates child nodes based on the current node, map, and heuristic values.
+ The 'get_key' function is a key function for sorting.
+ The 'reconstruct_path' function reconstructs the path from the goal node to the start node.
+ The 'read_input_files' function reads the input file to create a map.
+ The 'read_heuristic_files' function reads the heuristic values from the given file.
+ The 'main()' function performs the search.

* Main execution:
+ Checks to see if the command line arguments provided wants to perform an informed search or an uninformed search.
+ Reads the input file and handles cases where there is no input file found.
+ Initializes variables for output and initializes the fringe with the starting node.
+ Performs the search loop until either the goal state is reached or there is no path to the goal state.
+ Print the output based on the search results.

* Node expansion loop:
+ Expands nodes from the fringe, generating successors/child nodes.
+ Updatse the closed set and adds successors to the fringe.
+ Sorts the fringe based on the cost or total depending on the search type
+ Updates the maximum fringe size (situational).

*Output:
+ Prints the number of nodes popped, expanded, generated, and reconstructs the path if the goal state is reached.
+ Prints the number of nodes popped, expanded, generated, "Distance: infinity", and "Route: none" if there is no path to the goal state.

*Command line usage:
+ The code checks if the command line arguments are provided for the input file, start city, desstination city, and the heuristic file (optional).

- Instructions: 
+ For PC:
- Check to make sure the latest version of Python is installed (if not, install Python from the official websitee and add Python to path during the installation).
- Open the command prompt by pressing "Window icon + R", type "cmd", and press Enter .
- Use the "cd" command to navigate to the directory where the Python code is located (cd/path/to/source/code).
- Execute the Python script using the command: "python3 find_route.py input_filename.txt origin_city destination_city heuristic_filename.txt" (the output will be displayed after the script is executed).

+ For Linux/Mac:
- Check to make sure the latest version of Python is installed (if not, use "sudo apt-get update" and "sudo apt-get install python3")
- Open the terminal
- Use the "cd" command to navigate to the directory where the Python code is located (cd/path/to/source/code).
- Execute the Python script using the command: "python3 find_route.py input_filename.txt origin_city destination_city heuristic_filename.txt" (the output will be displayed after the script is executed).

+For Omega:
- Connect to Omega through the terminal (or connect to a VPN if not on campus ground).
- Use the SSH command in your local terminal to log in to the Omega account ("ssh username@omega_address").
- Upload your Python script and input files into your Omega account.
- - Use the "cd" command to navigate to the directory where the Python code is located (cd/path/to/source/code).
- - Execute the Python script using the command: "python find_route.py input_filename.txt origin_city destination_city heuristic_filename.txt" (the output will be displayed after the script is executed).
