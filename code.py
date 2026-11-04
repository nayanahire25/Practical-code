import numpy as np

# Define circuit components
R1, R2, R3 = 10, 20, 30
V1, V2 = 10, 5

# KVL equations
A = np.array([[R1 + R2, -R2],
              [-R2, R2 + R3]])

B = np.array([V1, -V2])

# Solve currents
currents = np.linalg.solve(A, B)

print(f"Loop Current I1: {currents[0]:.2f} A")
print(f"Loop Current I2: {currents[1]:.2f} A")

# KCL equations
A = np.array([[1/R1 + 1/R2, -1/R2],
              [-1/R2, 1/R2 + 1/R3]])

B = np.array([V1/R1, 0])

# Solve node voltages
node_voltages = np.linalg.solve(A, B)

print(f"Node Voltage V1: {node_voltages[0]:.2f} V")
print(f"Node Voltage V2: {node_voltages[1]:.2f} V")