import heapq
import re
import time
import logging
import csv
import matplotlib.pyplot as plt

logging.basicConfig(filename='performance.log', level=logging.INFO)

#function to find index of sender
def findidx(sender):
    count=0
    for i in ledger:
       
        if i[0]==sender:
            return count
        count+=1
    return -1  
def findidx2(sender):
    count=0
    for i in ledger:
       
        if i[1]==sender:
            return count
        count+=1
    return -1


def log_performance(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logging.info(f"{func.__name__} executed in {end - start} seconds")
        return result
    return wrapper



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
    # Djikistra
    @log_performance
    def minimumFee(self, src: int,dest: int, failure: int):
        print("Source: ",src)
        print("Destination: ",dest)
        print("Failure: ",failure)
        
        pq = []
        heapq.heappush(pq, (0, src,[src]))

        dist = [float('inf')] * self.V
        dist[src] = 0
        print(len(self.adj[src]))
        for i in range(0,len(self.adj[src])):
            
            if self.adj[src][i][0] == dest:
                return 0, [src,dest]
        count =0
        while pq:
            count+=1
            d, u, path = heapq.heappop(pq)
            if u == failure:
                continue
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
        if len(path) == 1:
            return 0, []
        return d, path 

    # Optimised
    @log_performance
    def minimumCost(self, src: int,dest: int, failure: int):

        pq = []
        heapq.heappush(pq, (0, src,[src],0))
        beta = 0.002
        alpha = 0.7
        dist = [float('inf')] * self.V
        dist[src] = 0
        
        for i in range(0,len(self.adj[src])):
            if self.adj[src][i][0] == dest:
                return 0, [src,dest] 

        while pq:
            d, u, path, cost = heapq.heappop(pq)
            
            if u == failure:
                continue
            if u == dest:
                print("Path Taken: ",path)
                break             

            # 'i' is used to get all adjacent vertices of a
            # vertex
            for v, weight in self.adj[u]:
                # If there is shorted path to v through u.
                if dist[v] > dist[u] + weight*alpha + beta*len(path):
                    # Updating distance of v
                    dist[v] = dist[u] + weight*alpha + beta*len(path)
                    heapq.heappush(pq, (dist[v], v, path+[v], cost+weight))

        # Print shortest distances stored in dist[]
        if len(path) == 1:
            return 0, []
        return cost, path     

    # Minimum Hops
    @log_performance
    def minimumPath(self, src: int,dest: int, failure: int):

        pq = []
        heapq.heappush(pq, (0,0, src,[src]))
        dist = [float('inf')] * self.V
        dist[src] = 0

        for i in range(0,len(self.adj[src])):
            if self.adj[src][i][0] == dest:
                return 0, [src,dest]

        while pq:
            d,cost, u, path = heapq.heappop(pq)
            
            if u == failure:
                continue
            if u == dest:
                print("Path Taken: ",path)
                break             

            # 'i' is used to get all adjacent vertices of a
            # vertex
            for v, weight in self.adj[u]:
                # If there is shorted path to v through u.
                if dist[v] > dist[u] + 1:
                    # Updating distance of v
                    dist[v] = dist[u] + 1
                    heapq.heappush(pq, (dist[v], cost+weight, v, path+[v]))

        # Print shortest distances stored in dist[]
        if len(path) == 1:
            return 0, []
        return cost, path     
	

def calculate_total_execution_time(log_file_path):

    # Regex pattern to find the execution times in the log entries
    time_pattern = re.compile(r'executed in ([\d\.e\-]+) seconds')
    time_pattern2 = re.compile(r'extract_tuples_from_file executed in ([\d\.e\-]+) seconds')
    

    total_time = 0.0
    extra_time=0.0

    # Open the log file and process each line
    with open(log_file_path, 'r') as file:
        for line in file:
            # Search for the time pattern and extract the duration
            match = time_pattern.search(line)
            match2 = time_pattern2.search(line)
            if match:
                # Convert the captured time to a float and add it to the total
                execution_time = float(match.group(1))
                total_time += execution_time
            if match2:
                # Convert the captured time to a float and add it to the total
                execution_time = float(match.group(1))
                extra_time += execution_time

    return total_time, extra_time

initial_balance={}
# print("Initial Balances:")
# print(initial_balance)

#Adding Edges
def adding_edges(g):
    with open('edges.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # print(row[0],row[1])
            node1=findidx2(row[0])
            node2=findidx2(row[1])
            capacity = 1
            
            if(node1!=-1 and node2!=-1):
                 g.addEdge(node1,node2, capacity)
                
            # if(node2!=-1):
            #     print(row[1])
            # print("ndowdsjgh",node1,node2)
            # if(node1!=-1 and node2!=-1):
            #     print(node1,node2,capacity)
            #     g.addEdge(node1,node2, capacity)
            

# Algorithm 1
@log_performance
def payment_request(recipient, payment_amount,ledger):
   

    # Step 2: Simulate checking sender balance (assuming insufficient funds)
    if payment_amount > 20:
        return 3

    # In a real scenario, this would involve sending the payment through the path
    print(f"Payment request sent from {sender_address} to {recipient_address} for {payment_amount} BTC.")
    return 0
	
# Function to update the transaction log file
def update_transaction_log_file(sender, recipient, amount, newpath):
    with open("new_log2.txt", "a") as log_file:
        log_file.write(f"Sender: {sender}, Recipient: {recipient}, Amount: {amount}, Status: Success, Path: {newpath} \n")

# Algorithm 3
@log_performance
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

# Algorithm 5
file_path2 = 'new_log2.txt'
@log_performance
def extract_tuples_from_file(file_path2):
    tuples_list = []
    with open(file_path2, 'r') as file:
        for line in file:
            if line.strip():  # Check if the line is not empty
                match = re.match(r"Sender: (.*), Recipient: (.*), Amount: (.*), Status: (.*), Path: \[(.*)\]", line)
                if match:
                    sender, recipient, amount, status, path = match.groups()
                    amount = float(amount)
                    path = [int(node) for node in path.split(',')]
                    tuples_list.append((sender.strip(), recipient.strip(), amount, status.strip(), path))
                else:
                    print("Invalid format in line:", line)
    return tuples_list

tuples = extract_tuples_from_file(file_path2)
node_counts = {}

mx=0
fail_node=-1
for t in tuples:
    if t[3] == "Fail":
        for node in range(1,len(t[4])-1):
            node_counts[t[4][node]] = node_counts.get(t[4][node], 0) + 1
            if mx<=node_counts[t[4][node]]:
                mx=node_counts[t[4][node]]
                fail_node=t[4][node]

print("Node counts:", node_counts)
print("Node with maximum failures:", fail_node)

# Hardcoded hashes for 9 people
import csv

ledger = []

def add_nodes_to_ledger():
    with open('nodes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Skip the header row
        next(reader, None)
        for row in reader:
            alias = row[0]
            initial_balance[alias]=10
            public_address = row[1]
            # Append alias and public address as a tuple to the ledger list
            ledger.append((alias, public_address))
           

# Call the function to add nodes to the ledger
g=Graph(5000)
add_nodes_to_ledger()
adding_edges(g)
# print(findidx2("02c0ac82c33971de096d87ce5ed9b022c2de678f08002dc37fdb1b6886d12234b5"))



# print the adjaceny list offor nodes up to 1 to 10
    

        



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





# Choose sender, recipient, and amount from user input

for i in range(len(ledger)):
    print(i, ledger[i][0],ledger[i][1])
sender = input("Enter sender's name : ")
recipient = input("Enter recipient's name : ")
amount = float(input("Enter amount to send (BTC): "))

# Convert sender and recipient to lowercase for case-insensitive matching
global sender_address, recipient_address

recipientidx = findidx(recipient)
senderidx = findidx(sender)
# Validate sender and recipient
if recipientidx == -1 or senderidx == -1:
    print("Invalid recipient address or recipient does not accept payments, please try again.")
else:
    print("Sender: ", senderidx)
    print("Recipient: ", recipientidx)
    sender_address = ledger[senderidx][1]
    recipient_address = ledger[recipientidx][1]
    # Call payment_request function
    request_state = payment_request(recipient, amount,ledger)
    
    # If request is successful, proceed with payment execution
    if request_state == 0:
        # Find shortest path
        what_path = input("How would you like to send (1: Minimum Fee, 2: Optimised Cost, 3: Minimum Hops)?: ")
        if what_path == "1":
            cost, new_path = g.minimumFee(senderidx, recipientidx, fail_node)
        elif what_path == "2":
            cost, new_path = g.minimumCost(senderidx, recipientidx, fail_node)
        elif what_path == "3":
            cost, new_path = g.minimumPath(senderidx, recipientidx, fail_node)
        
        # If path found, execute payment
        if len(new_path) > 0:
            # execution_state = 0
            if(len(new_path)<=2):
                cost=0
            execution_state = payment_execution(sender, ledger[recipientidx][1], amount, cost, new_path)
            # find_edge_weight(map, new_path)
            if execution_state == 0:
                print("Payment execution complete.")
                t_time, e_time=calculate_total_execution_time("performance.log")
                print("Total Execution Time: ",t_time)
                print("Extra Time due to modification: ",e_time)
                print("Percentage increase in Time: ",(e_time/t_time)*100)
                # Example data: percentage increase over several measurements
                measurements = ['Time by MPCN-RP', 'Time by modified MPCN-RP']
                percentage_increases = [t_time-e_time, t_time]  # These would be calculated from your data

                fig, ax = plt.subplots(figsize=(10, 5))
                bars = ax.bar(measurements, percentage_increases, color='skyblue')

                plt.xlabel('Algorithm')
                plt.ylabel('Time')
                plt.title('Comparison')
                plt.show()

            else:
                print("Payment execution failed.")
        else:
            print("No path found.")
            
    elif request_state == 2:
        print("Invalid recipient address or recipient does not accept payments")
    elif request_state == 3:
        print("Insufficient funds")
    else:
        print("Payment request pending")
