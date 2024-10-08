import qiskit
from qiskit import *
def run_quantum_circuit():
        qc = QuantumCircuit(1)
        qc.x(0)
        qc.h(0)
        print(qc.draw())