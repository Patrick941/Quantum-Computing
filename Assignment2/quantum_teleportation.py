import qiskit
from qiskit import *

def run_quantum_circuit(bell_state, message_qubit, backend):
    if (bell_state > 3 or bell_state < 0):
        print("Error: Invalid Bell State")
        print("Selected a valid Bell State (0-3)\nState 0: |00> + |11>\nState 1: |10> + |01>\nState 2: |00> - |11>\nState 3: |10> - |01>")
        return
    bell_state_binary = format(bell_state, '02b')
    
    qc = QuantumCircuit(5)
    qc.initialize([1, 0], 0)
    qc.initialize([1, 0], 1)
    qc.initialize([1, 0], 2)
    qc.initialize([1, 0], 3)
    qc.initialize([message_qubit[0], message_qubit[1]], 4)
    
    # Create Bell State |00> + |11>
    qc.h(2)
    qc.cx(2, 3)
    qc.measure_all()
    # Convert to selected Bell State
    qc.cz(0,2)
    qc.cx(1,2)
    
    # Measure the Bell State

    qc.measure_all()
    print(qc.draw())
    
    qc_compiled = transpile(qc, backend=backend)
    job = backend.run(qc_compiled) 
    result = job.result()
    counts = result.get_counts()
    print(counts)