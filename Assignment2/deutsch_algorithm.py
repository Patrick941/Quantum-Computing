import qiskit
from qiskit import *

def run_quantum_circuit(message_qubit, backend):
    qc = QuantumCircuit(3, 3)
    
    qc.measure_all()
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