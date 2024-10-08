import qiskit
from qiskit import *
def run_quantum_circuit(qubits, backend):
    qc = QuantumCircuit(4)
    # Initilaise qubits based on function input
    qc.initialize([1 - qubits[0], qubits[0]], 0)
    qc.initialize([1 - qubits[1], qubits[1]], 1)
    # Create state |00> + |11>
    qc.initialize([1, 0], 2)
    qc.initialize([1, 0], 3)
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
    if (len(counts) > 1):
        print("Error: Uncertain result")
    else:
        for key, value in counts.items():
            print(f"Message Cubits: {key[1::-1]}\nReceived Cubits: {key[3:1:-1]}\n")