import json
import csv

# Load JSON data
with open('C:\\Users\\bhuri\\OneDrive\\Desktop\\Courses\\Blockchain\\Project-Blockchain copy\\Project-Blockchain copy\\LN_2019.08.15.json', 'r',encoding='utf-8') as json_file:

    data = json.load(json_file)

# Extract nodes information
nodes_data = []
for node in data['nodes']:
    alias = node['alias']
    public_addresses = node['pub_key']
    nodes_data.append({
        'Alias': alias,
        'Public Address': ''.join(public_addresses),

    })

# Extract edges information
edges_data = []
for edge in data['edges']:
    node1_pub = edge['node1_pub']
    node2_pub = edge['node2_pub']
    capacity = edge['capacity']
    edges_data.append({
        'Node 1 Public Key': node1_pub,
        'Node 2 Public Key': node2_pub,
        'Capacity': capacity
    })

# Write nodes data to CSV
# Write nodes data to CSV
with open('nodes.csv', 'w', newline='', encoding='utf-8') as nodes_csv:
    fieldnames = ['Alias', 'Public Address']
    writer = csv.DictWriter(nodes_csv, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(nodes_data)

# Write edges data to CSV
with open('edges.csv', 'w', newline='', encoding='utf-8') as edges_csv:
    fieldnames = ['Node 1 Public Key', 'Node 2 Public Key', 'Capacity']
    writer = csv.DictWriter(edges_csv, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(edges_data)

print("CSV files generated successfully.")


print("CSV files generated successfully.")
