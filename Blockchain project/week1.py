import networkx as nx
import matplotlib.pyplot as plt
import heapq

file_path="balances.txt"
def read_initial_balances(file_path):
    initial_balance = {}
    with open(file_path, "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            initial_balance[key.strip().strip('"')] = float(value.strip().strip(","))
    return initial_balance

def write_initial_balances(file_path, initial_balance):
    with open(file_path, "w") as file:
        for name, balance in initial_balance.items():
            file.write(f'"{name}"={balance},\n')

def read_user_balances(file_path):
    user_balances = {}
    with open(file_path, "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            user_balances[key.strip().strip('"')] = float(value.strip().strip(","))
    return user_balances

def write_user_balances(file_path, user_balances):
    with open(file_path, "w") as file:
        for name, balance in user_balances.items():
            file.write(f'"{name}"={balance},\n')
    
def update_balance(user_number, amount_to_add):
    user_balances = read_user_balances("balances.txt")
    users = list(user_balances.keys())
    if user_number >= 0 and user_number < len(users):
        user = users[user_number]
        user_balances[user] += amount_to_add
        write_user_balances(file_path, user_balances)
    else:
        print("Invalid user number")

def transfer(sender, receiver, amount, fee, initial_balance):
    if sender in initial_balance:
        initial_balance[sender] -= amount
        initial_balance[sender] -= fee
    else:
        print(f"{sender} is not a valid sender.")
        return
    
    if receiver in initial_balance:
        initial_balance[receiver] += amount
    else:
        print(f"{receiver} is not a valid receiver.")
        # Roll back sender's balance change
        initial_balance[sender] += amount
    write_initial_balances(file_path, initial_balance)

initial_balance = read_initial_balances("balances.txt")
print("Initial Balances:")
print(initial_balance)

# Algorithm 1
def payment_request(recipient, payment_amount,ledger):
    # Step 1: Validate recipient address
    if recipient not in ledger:
        return 2

    # Step 2: Simulate checking sender balance (assuming insufficient funds)
    if payment_amount > 20:
        return 3

    # In a real scenario, this would involve sending the payment through the path
    print(f"Payment request sent from {sender_address} to {recipient_address} for {payment_amount} BTC.")
    return 0


# Algorithm 2
iPair = tuple
class Graph:
    global_path = tuple
    def __init__(self, V: int): # Constructor
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self, u: int, v: int, w: int):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    # Prints shortest paths from src to all other vertices
    def shortestPath(self, src: int,dest: int):

        pq = []
        heapq.heappush(pq, (0, src,[src]))

        dist = [float('inf')] * self.V
        dist[src] = 0

        while pq:
            d, u, path = heapq.heappop(pq)
            if u == dest:
                print("Path Taken: ",path)
                break               

            # 'i' is used to get all adjacent vertices of a
            # vertex
            for v, weight in self.adj[u]:
                # If there is shorted path to v through u.
                if dist[v] > dist[u] + weight:
                    # Updating distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v, path+[v]))

        # Print shortest distances stored in dist[]
        return d, path     
		
# Function to update the transaction log file
def update_transaction_log_file(sender, recipient, amount, newpath):
    with open("new_log.txt", "a") as log_file:
        log_file.write(f"Sender: {sender}, Recipient: {recipient}, Amount: {amount}, Status: Success, Path: {newpath} \n")


# Algorithm 3
def payment_execution(sender_address, recipient_address, payment_amount, fee, newpath):
    update_transaction_log_file(sender_address, recipient_address, payment_amount, newpath)
    transfer(sender, recipient, payment_amount, fee, initial_balance)
    print(f"Payment of {payment_amount} BTC from {sender_address} to {recipient} successful.")
    print("Fee Charged: ", fee, " BTC")
    return 0

# Algorithm 4
def update_channel_state(channel_state, closed_channels, built_channels, balance_changes):
    for channel_id in closed_channels:
        if channel_id in channel_state:
            del channel_state[channel_id]
            print(f"Channel {channel_id} closed.")

    for channel_id in built_channels:
        if channel_id not in channel_state:
            channel_state[channel_id] = {"open": True}
            print(f"Channel {channel_id} built.")

    for channel_id, balance_change in balance_changes.items():
        if channel_id in channel_state:
            channel_state[channel_id]["balance"] += balance_change
            print(f"Channel {channel_id} balance updated: {balance_change}")
        else:
            print(f"Warning: Ignoring balance update for unknown channel {channel_id}")

    return channel_state

# Hardcoded hashes for 9 people
ledger = {
    "Alice": "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4",
    "Bob": "0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db",
    "Charlie": "0xCECDDf21b5E9f5f0FfE3f4b4d2e8f5f0f9f9f9f9",
    "David": "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984",
    "Eve": "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D",
    "Freddy": "0x5B38Da6a701c568545dCfcB03FcB875f56beddC2",
    "George": "0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02de",
    "Harry": "0xCECDDf21b5E9f5f0FfE3f4b4d2e8f5f0f9f9f9f1",
    "Ivy": "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F987",
}

# Graph representing the network
V = 9
g = Graph(V)
g.addEdge(0, 1, 0.04)
g.addEdge(0, 7, 0.08)
g.addEdge(1, 2, 0.08)
g.addEdge(1, 7, 0.11)
g.addEdge(2, 3, 0.07)
g.addEdge(2, 8, 0.02)
g.addEdge(2, 5, 0.04)
g.addEdge(3, 4, 0.09)
g.addEdge(3, 5, 0.14)
g.addEdge(4, 5, 0.10)
g.addEdge(5, 6, 0.02)
g.addEdge(6, 7, 0.01)
g.addEdge(6, 8, 0.06)
g.addEdge(7, 8, 0.07)

def find_edge_weight(map, tup):
    if(len(tup)>2):
        for i in range(len(tup) - 1):
            edge = (tup[i], tup[i + 1])
            flipped_edge = (tup[i + 1], tup[i])
            if edge in map:
                if(i==0):
                    update_balance(tup[i+1],map[edge])
                elif(i+1==len(tup)-1):
                    update_balance(tup[i], map[edge])
                else:
                    update_balance(tup[i],map[edge]/2)
                    update_balance(tup[i+1],map[edge]/2)
            elif flipped_edge in map:
                if(i==0):
                    update_balance(tup[i+1],map[flipped_edge])
                elif(i+1==len(tup)-1):
                    update_balance(tup[i], map[flipped_edge])
                else:
                    temp = map[flipped_edge]
                    update_balance(tup[i],temp/2)
                    update_balance(tup[i+1],temp/2)

map = {
    (0, 1): 0.04,
    (0, 7): 0.08,
    (1, 2): 0.08,
    (1, 7): 0.11,
    (2, 3): 0.07,
    (2, 8): 0.02,
    (2, 5): 0.04,
    (3, 4): 0.09,
    (3, 5): 0.14,
    (4, 5): 0.10,
    (5, 6): 0.02,
    (6, 7): 0.01,
    (6, 8): 0.06,
    (7, 8): 0.07
}


# For Plot
m = nx.Graph()

# Add edges
m.add_edge("Alice", "Bob", weight=0.04)
m.add_edge("Alice", "Harry", weight=0.08)
m.add_edge("Bob", "Charlie", weight=0.08)
m.add_edge("Bob", "Harry", weight=0.11)
m.add_edge("Charlie", "David", weight=0.07)
m.add_edge("Charlie", "Ivy", weight=0.02)
m.add_edge("Charlie", "Freddy", weight=0.04)
m.add_edge("David", "Eve", weight=0.09)
m.add_edge("David", "Freddy", weight=0.14)
m.add_edge("Eve", "Freddy", weight=0.10)
m.add_edge("Freddy", "George", weight=0.02)
m.add_edge("George", "Harry", weight=0.01)
m.add_edge("George", "Ivy", weight=0.06)
m.add_edge("Harry", "Ivy", weight=0.07)

# Choose sender, recipient, and amount from user input
sender = input("Enter sender's name (Alice, Bob, Charlie, David, Eve, Freddy, George, Harry, Ivy): ")
recipient = input("Enter recipient's name (Alice, Bob, Charlie, David, Eve, Freddy, George, Harry, Ivy): ")
amount = float(input("Enter amount to send (BTC): "))

# Convert sender and recipient to lowercase for case-insensitive matching
sender = sender.lower().capitalize()
recipient = recipient.lower().capitalize()

# Validate sender and recipient
if recipient not in ledger:
    print("Invalid recipient address or recipient does not accept payments")
else:
    recipient_address = ledger[recipient]
    sender_address = ledger[sender]

    # Call payment_request function
    request_state = payment_request(recipient, amount,ledger)
    # If request is successful, proceed with payment execution
    if request_state == 0:
        # Find shortest path
        cost, new_path = g.shortestPath(ord(sender[0].upper())-ord('A'), ord(recipient[0].upper())-ord('A'))
        
        # If path found, execute payment
        if cost:
            # execution_state = 0
            if(len(new_path)<=2):
                cost=0
            execution_state = payment_execution(sender, recipient_address, amount, cost, new_path)
            find_edge_weight(map, new_path)
            if execution_state == 0:
                print("Payment execution complete.")
                pos = nx.spring_layout(m)  # positions for all nodes
                nx.draw(m, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=10)

                # Draw edge weights
                labels = nx.get_edge_attributes(m, 'weight')
                nx.draw_networkx_edge_labels(m, pos, edge_labels=labels)

                # Show the graph
                plt.show()
            else:
                print("Payment execution failed.")
        else:
            print("No path found.")
            pos = nx.spring_layout(m)  # positions for all nodes
            nx.draw(m, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=10)

            # Draw edge weights
            labels = nx.get_edge_attributes(m, 'weight')
            nx.draw_networkx_edge_labels(m, pos, edge_labels=labels)

            # Show the graph
            plt.show()
            
    elif request_state == 2:
        print("Invalid recipient address or recipient does not accept payments")
    elif request_state == 3:
        print("Insufficient funds")
    else:
        print("Payment request pending")
