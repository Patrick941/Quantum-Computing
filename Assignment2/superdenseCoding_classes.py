import qiskit
from qiskit import QuantumCircuit, transpile, assemble, Aer, AerSimulator, execute

def run_quantum_circuit():
        qc = QuantumCircuit(1)
        qc.x(0)
        print(qc.draw())
        simulator = Aer.get_backend('qasm_simulator')
        compiled_circuit = transpile(qc, simulator)
        qobj = assemble(compiled_circuit)
        result = execute(qc, simulator).result()
        counts = result.get_counts(qc)
        print("\nTotal count for 0 and 1 are:", counts)