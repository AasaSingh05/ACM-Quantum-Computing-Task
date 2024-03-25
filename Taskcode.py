from qiskit import QuantumCircuit, execute, Aer

def add_three_numbers(num1, num2, num3):
    # Create a 4-qubit quantum circuit
    qc = QuantumCircuit(5, 3)

    # Encode the three numbers in binary format
    for idx, num in enumerate([num1, num2, num3]):
        binary_num = format(num, '03b')  # Assuming 3-bit numbers
        for bit_idx, bit in enumerate(binary_num):
            if bit == '1':
                qc.x(idx * 1 + bit_idx)

    # Binary addition logic
    qc.cx(0, 3)
    qc.cx(1, 3)
    qc.cx(2, 3)
    qc.ccx(0, 1, 4)
    qc.ccx(0, 2, 4)
    qc.ccx(1, 2, 4)


    # Measure the result
    qc.measure([2, 1, 0], [2, 1, 0])  # Reverse order for display convenience

    # Simulate the circuit
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1).result()
    counts = result.get_counts(qc)

    return counts

# Example usage:
num1 = 2
num2 = 3
num3 = 4
counts = add_three_numbers(num1, num2, num3)
print(f"Result: {counts}")
