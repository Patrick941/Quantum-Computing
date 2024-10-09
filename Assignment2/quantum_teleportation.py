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