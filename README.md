# Making a quantum circuit that adds three qubits together
## (i assumed this is like a full adder circuit for three qubits)
### *By Aasa Singh Bhui ( 23BBS0025 )*


**Documentation of my process:**
- Started by reading up about qubits and their represenation in a matricular form
- Went to IBM's website to read up about qiskit
- Found a lesson on the basics of quantum computing and basic gates with circuits
- Read up the blogs on each and decided to try making a sample circuit
- Opened up the circuit lab and played around with the interface finding new gates to read up about
- Tried making a smaller (half adder) using the CNOT gates
- Scaled up to the full adder with the CNOT and toffoli gates

**FORMULA FOR THE CIRCUIT:** 

- **_SUM = X (xor) Y (xor) Z_**
- **_CARRY = XY (xor) YZ (xor) XZ_**

**LOGIC:**
- We encode each of the inputted values into a 3 digit binary number
- We use controlled-NOT gates to implement the binary addition logic. The target qubit is the qubit where the result will be stored (qubit 3 in our case), and the control qubits are the qubits representing the bits of the numbers to be added.
- we apply the same logic but with toffoli gates to take account the carry of the circuit
- we measure the output to take the value of the SUM and CARRY of the two inputs

**_Circuit diagram:_**

![Screenshot 2024-03-25 123800](https://github.com/AasaSingh05/ACM-Quantum-Computing-Task/assets/158080819/e88a81b5-004b-4255-9771-d8616a0e922c)


**Logic table of the circuit:**

| x | y | z | Carry | Sum |
|--|--|--|---|---|
|0|0|0|0|0|
|0|0|1|0|1|
|0|1|0|0|1|
|0|1|1|1|0|
|1|0|0|0|1|
|1|0|1|1|0|
|1|1|0|1|0|
|1|1|1|1|1|

**OUTPUT: ( Test Case )**

![image](https://github.com/AasaSingh05/ACM-Quantum-Computing-Task/assets/158080819/95367d19-e239-464a-a061-7030ec225350)


sources:
- https://sci-hub.ru/10.1103/PhysRevA.60.2746
- https://www.youtube.com/watch?v=30U2DTfIrOU
- https://www.youtube.com/watch?v=c30KrWjHaw4
- https://chat.openai.com/
- https://gemini.google.com
