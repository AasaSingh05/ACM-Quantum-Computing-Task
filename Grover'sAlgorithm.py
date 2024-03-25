import numpy as np     
from qiskit import QuantumCircuit, transpile, Aer, IBMQ, execute, assemble
from qiskit.visualization import *

# Creating function for Equal Superposition states of two qubits:
def initialize(qc):
  qc.h(0)                          # Applying H gates to both qubits
  qc.h(1)
  qc.barrier()
grover_circuit = QuantumCircuit(2) # Initializing grover circuit
initialize(grover_circuit)
grover_circuit.draw('mpl')

def oracle_11(qc): 
	qc.cz(0,1)          # Apply a controlled Z gate
	qc.barrier()
oracle_11(grover_circuit)
grover_circuit.draw('mpl')

# Creating Grover's Diffusion operator:
def u_g(qc):
  qc.h(0)
  qc.h(1)
  qc.x(0)
  qc.x(1)
  qc.h(1)
  qc.cx(0,1)
  qc.x(0)
  qc.h(1)
  qc.h(0)
  qc.x(1)
  qc.h(1)
  qc.barrier()
u_g(grover_circuit)        # temporary circuit just to see what U_s looks like
grover_circuit.draw('mpl')

# Finally we measure the circuit:
grover_circuit.measure_all()
grover_circuit.draw('mpl')