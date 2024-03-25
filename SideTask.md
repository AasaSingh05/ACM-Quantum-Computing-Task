# Grover's Algorithm and its implimentation

### What is Grover's algorithm?
- Grover's algorithm is a searching algorithm using the properites of a qubit and how it can be in a superposition state
- The Algorthm consists of three main steps:
  1) The probing of the values in the function
  2) Using the oracle function on the set, flipping the found values's amplitude to a negative value
  3) Amplifying the difference thus it increases the amplitude of the found value and decreases the rest
  4) Repeating the previous two step until the probability of finding that value is approximately 1
- In classical computing the searching of an element takes about O(n) time, whereas the time taken by this algorithm is O(sqrt(n))

### The individial steps taken
**1) The superposition of each qubit**
- Every bit is put in a state of superimposition by a Hadarmard Gate (H gate), where each bit is in a linear combination of the two states and are at equal probabilities of being either 0 or a 1

**2) The Oracle function and probing:**
- The oracle function takes the input for each elt and returns a value correspoding to if it is equal to the search key or not
- In this algorithm the oracle function returns the amplitude as itself when the element is not equal to the key
- The Oracle function will return the amplitude multiplied by -1 if the element is equal to the search key, effectively flipping the amplitude of the qubits

**3) Amplification of values**
- The mean of value of all the amplitudes is found, and we take the difference of all the amplitude with the mean
- We flip the amplitudes of all the bits with respect to the mean thus amplifying the value of the searched element and decreasing the amplitude of others

  **4) Final Step**
  - The Steps 2 And 3 are done repeatedly until the probability of the searched element is as close to 1 as possible.
  - Overusing of the steps 2 and 3 will cause all the values of the system to be back to the original of all amplitudes being of same probability.
  - The Step 2 and 3 together is what The Grover's Diffusion Operator does.
 
    
