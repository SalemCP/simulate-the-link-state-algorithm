# Shortest Path Algorithm using Dijkstra
This is a Python implementation of a network routing algorithm based on Dijkstra's algorithm. It computes the shortest path between nodes in a network using either Dijkstra's algorithm or the shortest path algorithm.

## Requirements
- Python 3.x
- networkx module
- matplotlib module
## Usage
1 - Clone or download the repository

2 - Install the required modules using pip
> pip install networkx

> pip install matplotlib

3 - Create a text file named input_file.txt in the same directory with the following format:	
 n,m
 src1,dst1,weight1
 src2,dst2,weight2
 ...
 srcm,dstm,weightm
 
- n: number of nodes
- m: number of edges
- srci: source node of edge i
- dsti: destination node of edge i
- weighti: weight of edge i

4 - Run the script
> python shortest_path_algorithm.py

5 - Choose an option:

- d: Compute forwarding tables using Dijkstra's algorithm
- s: Compute forwarding tables using the shortest path algorithm
- p: Visualize the topology
- e: Exit the program

## Analysis Methods
- The script provides two methods for computing forwarding tables:

Dijkstra's Algorithm: This method uses Dijkstra's algorithm to find the shortest path between each pair of nodes in the network. It then generates a forwarding table for each node that lists the next hop for each destination node. To use this method, choose the d option when prompted.

Shortest Path Algorithm: This method uses the built-in shortest_path function of the networkx library to find the shortest path between each pair of nodes in the network. It then generates a forwarding table for each node that lists the next hop for each destination node. To use this method, choose the s option when prompted.

## Output
- Forwarding table for each node in the network
- Visualization of the network topology (if the user chooses the 'p' option)

## License
This script is released under the MIT License. See the LICENSE file for more information.
