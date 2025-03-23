import networkx as nx
import json

# Load JSON output from G.A.M.
with open("gam_output.json", "r") as f:
    data = json.load(f)

# Create Directed Graph for DGM
DGM = nx.DiGraph()

# Add Nodes (Layers)
for node in data["nodes"]:
    DGM.add_node(node["id"], **node)

# Add Edges (Connections)
for edge in data["edges"]:
    DGM.add_edge(edge["from"], edge["to"])

# Store Hyperparameters & Dynamic Rules
hyperparameters = data["hyperparameters"]
dynamic_rules = data["dynamic_rules"]

print("Graph Nodes:", DGM.nodes(data=True))
print("Graph Edges:", DGM.edges())
print("Hyperparameters:", hyperparameters)
print("Dynamic Rules:", dynamic_rules)
