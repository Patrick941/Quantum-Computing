import qiskit
import superdenseCoding_classes
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit import QuantumCircuit, transpile, assemble, Aer, AerSimulator, execute

print(f"Qiskit version: {qiskit.__version__}")

with open('../apiKey.txt', 'r') as file:
    api_key = file.read().strip()

service = QiskitRuntimeService(channel="ibm_quantum", token=api_key)

backend = service.backend(name="ibm_brisbane")
print(f"Number of qubits in backend: {backend.num_qubits}")


run_quantum_circuit()

