import torch
import torch.nn as nn
import torch.optim as optim

# Define a dynamic model class
class DynamicModel(nn.Module):
    def __init__(self, graph):
        super(DynamicModel, self).__init__()
        self.layers = nn.ModuleList()

        for node in nx.topological_sort(graph):
            layer_data = graph.nodes[node]
            if layer_data["type"] == "Dense":
                self.layers.append(nn.Linear(in_features=128, out_features=layer_data["units"]))
            elif layer_data["type"] == "Dropout":
                self.layers.append(nn.Dropout(layer_data["rate"]))

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

# Instantiate the model
model = DynamicModel(DGM)

# Define Optimizer
optimizer = optim.Adam(model.parameters(), lr=hyperparameters["learning_rate"])
