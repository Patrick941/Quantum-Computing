---
title: "Assignment 2: Quantum Algorithms"
author: "Patrick Farmer 20331828"
date: "15-10-2024"
header-includes:
  - \usepackage{minted}
  - \usemintedstyle{friendly}
---

![](https://www.tcd.ie/media/tcd/site-assets/images/tcd-logo.png)

\clearpage

## Introduction
This labs aims to investigate the workings and usage of a couple of quantum algorithms. The 3 algorithms taken for this lab are:
* Superdense Coding
* Quantum Teleportation
* Deutsch's Algorithm

### Superdense Coding
The algorithm is used to send two classical bits of information using only one qubit. The algorithm works by using a Bell pair to entangle two qubits. The bell pair that I used was the following:
$$
\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)
$$
Say we have two people, Alice and Bob. Alice takes the first qubit of the bell pair, Bob takes the second qubit. Alice then performs the following operations on her qubit:
1. Apply the Hadamard gate
2. Apply the CNOT gate
3. Then if the first bit of the message is 1, apply the Z gate
4. Then if the second bit of the message is 1, apply the X gate
Alice then sends her qubit to Bob. Bob then applies the following operations to his qubit:
1. Apply the CNOT gate
2. Apply the Hadamard gate
Bob then measures the qubits and gets the two bits of information that Alice sent.\
This was implemented with the following code:
```python
import qiskit
from qiskit import *

def run_quantum_circuit(qubits, backend):
    qc = QuantumCircuit(4)
    # Initilaise qubits based on function input
    qc.initialize([1 - qubits[0], qubits[0]], 0)
    qc.initialize([1 - qubits[1], qubits[1]], 1)
    # Create state |00> + |11>
    qc.initialize([1, 0], 2) # Alice's qubit
    qc.initialize([1, 0], 3) # Bob's qubit
    qc.h(2)
    qc.cx(2, 3)
    # Apply pauli gates based on message qubits
    qc.cz(0,2)
    qc.cx(1,2)
    # Recreate the two message qubits from the one
    qc.cx(2, 3)
    qc.h(2)
    qc.measure_all()
    print(qc.draw())
    
    qc_compiled = transpile(qc, backend=backend)
    job = backend.run(qc_compiled) 
    
    result = job.result()
    counts = result.get_counts()
    for key, value in counts.items():
        print(f"Message Cubits: {key[1::-1]}\nReceived Cubits: {key[3:1:-1]}\n")
```

### Quantum Teleportation
The algorithm is used to teleport a qubit from one location to another. The algorithm works by using a Bell pair to entangle two qubits. The bell pair that I used was the following:
$$
\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)
$$
Say we have two people, Alice and Bob. Alice takes the first qubit of the bell pair, Bob takes the second qubit. Alice then performs the following operations on her qubit and the message qubit: (This gets the tensor product)
1. Apply the CNOT gate
2. Apply the Hadamard gate
The tensor product is then sent to Bob. Bob then applies the following operations to his qubit:
1. Apply the CNOT gate (based on the second qubit of the tensor product)
2. Apply the Z gate (based on the first qubit of the tensor product)
Bob then measures his qubit which is now the message qubit.



```python
import qiskit
from qiskit import *

def run_quantum_circuit(message_qubit, backend):
    qc = QuantumCircuit(3, 3)

    # Create the state to be teleported in qubit 0
    qc.initialize(message_qubit, 0)
    qc.initialize([1, 0], 1)
    qc.initialize([1, 0], 2)

    # Create Bell State |00> + |11>
    qc.h(1)
    qc.cx(1, 2)

    # Get tensor product of qubits 0 and 1
    qc.cx(0, 1)
    qc.h(0)
    
    # The tensor product is given from alice to bob
    # The message qubit is recovered from the tensor product
    qc.cx(1, 2)
    qc.cz(0, 2)

    # The message qubit is measured
    qc.measure(2, 2)

    # qc.measure_all()
    print(qc.draw())
    
    qc_compiled = transpile(qc, backend=backend)
    job = backend.run(qc_compiled) 
    result = job.result()
    counts = result.get_counts()
    alpha0 = round(message_qubit[0] ** 2, 3)
    alpha1 = round(message_qubit[1] ** 2, 3)
    print(f"Message Qubits: {alpha0}|0⟩ + {alpha1}|1⟩")
    print(f"Received Qubits: ", end="")
    for key, value in counts.items():
        sum_values = sum(counts.values())
        print(f"{round(value/sum_values, 3)}|{key[0]}⟩ ", end="")
    print("")
```
