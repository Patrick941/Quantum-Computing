import qiskit
import superdenseCoding_classes
from qiskit_ibm_runtime import QiskitRuntimeService
import os
from qiskit_aer import AerSimulator, Aer

print(f"Qiskit version: {qiskit.__version__}")

current_dir = os.path.dirname(os.path.abspath(__file__))
api_key_path = os.path.join(current_dir, '..', 'apiKey.txt')

with open(api_key_path, 'r') as file:
    api_key = file.read().strip()


mode = 'aer'
if (mode == 'ibm'):
    service = QiskitRuntimeService(channel="ibm_quantum", token=api_key)
    backend = service.backend(name="ibm_brisbane")
    print(f"Number of qubits in backend: {backend.num_qubits}")
elif (mode == 'aer'):
    backend = AerSimulator()

superdenseCoding_classes.run_quantum_circuit([0,  0], backend)

