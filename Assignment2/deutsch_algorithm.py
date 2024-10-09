import qiskit
from qiskit import *

def run_quantum_circuit(backend):
    qc = QuantumCircuit(3, 3)
    
    qc.measure_all()
    print(qc.draw())
    
    qc_compiled = transpile(qc, backend=backend)
    job = backend.run(qc_compiled) 
    result = job.result()
    counts = result.get_counts()
    print(counts)