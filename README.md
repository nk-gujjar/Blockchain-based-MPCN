# Blockchain Project (CS540)

## Group Details
**Group Number - 14**  
**Group Members :**  
Akanksh Caimi (2021CSB1064)  
Divyankar Shah (2021CSB1086)  
Harshit Kumar Ravi (2021CSB1093)  
Mohit Kumar (2021CSB1109)  
Nitesh Kumar (2021CSB1117)

## Research Paper Description
**MPCN-RP: A Routing Protocol for Blockchain-Based Multi-Charge Payment Channel Networks**  
The paper discusses how transactions can be efficiently routed through the network from sender to receiver, optimizing for cost, latency, or other factors important in blockchain environments through a more efficient algorithm.

## Project Overview
This blockchain project includes a set of Python scripts that manage a simulated blockchain environment focusing on transactions, balances, and network paths to simulate transactions between sender and receiver using MPCN algorithm. The primary script (`week2.py`) handles reading and updating user balances, transferring funds between users with fees, and generating a network graph to visualize transaction paths.

## File Structure
- `balances.txt`: Stores initial and updated balances of blockchain users.
- `new_log.txt`: (reserved for potential logging).
- `new_log2.txt`: Logs transactions including sender, recipient, amount, and transaction path.
- `README.md`: Readme file.
- `week1.py`: Contains earlier parts of the project (previous task).
- `week2.py`: Contains the main python script of the project.

## Features
- **Balance Management**: Read and write initial and updated user balances.
- **Transaction Processing**: Update balances based on user transactions, ensuring balance availability and validity of users.
- **Graph-based Transaction Pathfinding**: Utilize network graphs to determine and visualize paths for transactions (networkx is used for visualizing the graphical representation of the network of nodes).
- **Logging**: Record detailed logs of transactions including paths taken and transaction status in `new_log2.txt`.
- **Failure Handling**: Identify and handle transaction failures within the network graph, with pathfinding that skips failed nodes in next transactions.

## How to Run the Code
- Unzip the project folder and open the terminal in the project directory
- Run the main python script `week2.py`
    ```bash 
    python week2.py
    ``` 
- Put the sender, receiver and transaction amount (in BTC) in the prompt   

The transaction will start giving relevant information about the transaction (like path taken, fee charged, etc) along with a visual representation of the nodes.

### Prerequisites
Ensure you have Python installed along with the `networkx` and `matplotlib` libraries, which can be installed via pip:
```bash
pip install networkx matplotlib
```
