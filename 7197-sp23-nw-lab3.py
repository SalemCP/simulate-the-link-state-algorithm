import networkx as nx
import matplotlib.pyplot as plt

# function to create graph from input file


def create_graph():
    # Read input from file
    with open('input_file.txt', 'r') as f:
        lines = f.readlines()

    n, m = map(int, lines[0].strip().split(','))

    # Create a new empty graph
    G = nx.Graph()

    # Add edges with weights to the graph
    for i in range(1, m+1):
        src, dst, weight = lines[i].strip().split(',')
        G.add_edge(src, dst, weight=int(weight))

    return G

# function uses dijkstra algorithm to find the shortest path


def dijkstra(G, source, dest):
    # Initialize distance dictionary with infinite distances for all nodes
    dist = {node: float('inf') for node in G.nodes()}
    dist[source] = 0

    # Initialize empty set to store visited nodes
    visited = set()

    # Loop through all nodes to find the shortest path
    while len(visited) < len(G.nodes()):
        # Find the node with the minimum distance
        min_dist = float('inf')
        min_node = None
        for node in G.nodes():
            if node not in visited and dist[node] < min_dist:
                min_dist = dist[node]
                min_node = node

        # If no node found, break out of the loop
        if min_node is None:
            break

        # Mark the node as visited
        visited.add(min_node)

        # Update the distances of its neighbors
        for neighbor in G.neighbors(min_node):
            if neighbor not in visited:
                new_dist = dist[min_node] + G[min_node][neighbor]['weight']
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist

    # Return the shortest distance from source to dest
    return dist[dest]

# function to generate forwarding table


def forward_Table(G, source):
    print("Forwarding table for " + source + ": ")
    least_cost_path = nx.shortest_path(G, source, weight='weight')
    print('+-------------+--------+')
    print('| Destination |  Link  |')
    print('+-------------+--------+')
    for i, elem in enumerate(least_cost_path):
        if elem != source:
            print('|     ' + elem + '     |   (' +
                  least_cost_path[elem][0] + ',' + least_cost_path[elem][1] + ')  |')
    print('+-------------+--------+')
    print()

# function to generate forwarding table using dijkstra algorithm


def forward_Table_dijkstra(G, source):
    print("Forwarding table for " + source +
          ":(Using Dijkstra) ")
    print('+-------------+--------+')
    print('| Destination |  Link  |')
    print('+-------------+--------+')
    for dest in sorted(G.nodes()):
        if dest != source:
            next_hop = None
            min_dist = float('inf')

            for neighbor in G.neighbors(source):
                new_dist = G[source][neighbor]['weight'] + \
                    dijkstra(G, neighbor, dest)
                if new_dist < min_dist:
                    min_dist = new_dist
                    next_hop = neighbor
            print('|     ' + dest + '     |   (' +
                  source + ',' + next_hop + ')  |')
    print('+-------------+--------+')
    print()


if __name__ == "__main__":

    # Create a graph from the input file
    G = create_graph()

# get user input
while True:
    print("\nPlease choose an option:")
    print("d - Compute forwarding tables using Dijkstra's algorithm")
    print("s - Compute forwarding tables using shortest path algorithm")
    print("p - Visualize the topology")
    print("e - Exit the program")
    method = input("> ")

    # handle user input
    if method == 'e':
        break
    elif method == 'd':
        print("Computing forwarding tables using Dijkstra's algorithm...")
        for src in sorted(G.nodes()):  # type: ignore
            forward_Table_dijkstra(G, src)  # type: ignore
    elif method == 's':
        print("Computing forwarding tables using shortest path algorithm...")
        for src in sorted(G.nodes()):  # type: ignore
            forward_Table(G, src)  # type: ignore
    elif method == 'p':
        print("Visualizing the topology...")
        pos = nx.spring_layout(G)  # type: ignore
        nx.draw(G, pos, with_labels=True)  # type: ignore
        labels = nx.get_edge_attributes(G, 'weight')  # type: ignore
        nx.draw_networkx_edge_labels(  # type: ignore
            G, pos, edge_labels=labels)  # type: ignore
        plt.show()
    else:
        print("Invalid option. Please try again.")
