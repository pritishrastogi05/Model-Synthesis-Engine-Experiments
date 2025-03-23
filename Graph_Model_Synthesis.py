import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Initialize Model
model = Sequential()

# Iterate through nodes to add layers
for node in nx.topological_sort(DGM):  # Ensuring correct layer order
    layer_data = DGM.nodes[node]
    if layer_data["type"] == "Dense":
        model.add(Dense(layer_data["units"], activation=layer_data["activation"]))
    elif layer_data["type"] == "Dropout":
        model.add(Dropout(layer_data["rate"]))

# Compile the model
model.compile(optimizer=hyperparameters["optimizer"], 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

print(model.summary())
