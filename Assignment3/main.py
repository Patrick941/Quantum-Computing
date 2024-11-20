import qiskit
import qft
from qiskit_ibm_runtime import QiskitRuntimeService
import os
from qiskit_aer import AerSimulator, Aer
import math
import io
import sys

print(f"Qiskit version: {qiskit.__version__}")

current_dir = os.path.dirname(os.path.abspath(__file__))
api_key_path = os.path.join(current_dir, '..', 'apiKey.txt')

if os.path.exists(api_key_path):
    with open(api_key_path, 'r') as file:
        api_key = file.read().strip()
else:
    api_key = os.getenv('API_KEY')
    if api_key is None:
        raise ValueError("API key not found in file or environment variable.")


mode = os.getenv('MODE', 'aer')
if (mode == 'ibm'):
    service = QiskitRuntimeService(channel="ibm_quantum", token=api_key)
    backend = service.backend(name="ibm_brisbane")
    print(f"Number of qubits in backend: {backend.num_qubits}")
elif (mode == 'aer'):
    backend = AerSimulator()



# Function to capture the output of a function
def capture_output(func, *args, **kwargs):
    captured_output = io.StringIO()          # Create StringIO object
    sys.stdout = captured_output             # Redirect stdout.
    func(*args, **kwargs)                    # Call the function.
    sys.stdout = sys.__stdout__              # Reset redirect.
    return captured_output.getvalue()        # Get the captured output.

input_qubits = [0.5, 0.5, 0.5]
qft.run_quantum_circuit(input_qubits, backend)
