import csv

# Function to read aliases from nodes CSV file
def read_aliases(filename):
    aliases = set()
    with open(filename, 'r', newline='', encoding='utf-8') as nodes_csv:
        reader = csv.DictReader(nodes_csv)
        for row in reader:
            aliases.add(row['Public Address'])
    return aliases

# Function to filter edges based on existing nodes
def filter_edges(nodes_csv, edges_csv):
    aliases = read_aliases(nodes_csv)
    filtered_edges = []

    with open(edges_csv, 'r', newline='', encoding='utf-8') as edges_file:
        reader = csv.DictReader(edges_file)
        for row in reader:
            node1 = row['Node 1 Public Key']
            node2 = row['Node 2 Public Key']
            # Check if both nodes exist in the set of aliases
            if node1 in aliases and node2 in aliases:
                filtered_edges.append(row)
                print(row['Node 1 Public Key'], row['Node 2 Public Key'], row['Capacity'])

    return filtered_edges

# Paths to nodes and edges CSV files
nodes_csv_file = 'nodes.csv'
edges_csv_file = 'edges.csv'

# Filter edges
filtered_edges = filter_edges(nodes_csv_file, edges_csv_file)

# Write filtered edges to a new CSV file
with open('filtered_edges.csv', 'w', newline='', encoding='utf-8') as filtered_edges_file:
    fieldnames = ['Node 1 Public Key', 'Node 2 Public Key', 'Capacity']
    writer = csv.DictWriter(filtered_edges_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(filtered_edges)

print("Filtered edges saved to filtered_edges.csv")
