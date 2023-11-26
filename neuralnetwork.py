# Inputs to the neural network layer
inputs = [1, 2, 3, 2.5]

# Biases for each neuron
bias1 = 2
bias2 = 3
bias3 = 0.5

# Weights for each neuron
weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]


# core  function of  neuron networks
def calculate_output(inputs, weights, bias):
     output = 0
     for i in range(len(inputs)):
           output += inputs[i] * weights[i]
     return output + bias

# Calculating the output for each neuron
output1 = calculate_output(inputs, weights1, bias1)
output2 = calculate_output(inputs, weights2, bias2)
output3 = calculate_output(inputs, weights3, bias3)

# Aggregating the outputs
output = [output1, output2, output3]


# Printing the output

print("Layer Output:", output)
