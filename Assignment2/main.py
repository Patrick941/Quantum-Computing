import qiskit
import superdense_coding
import quantum_teleportation
import deutsch_algorithm
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

# Capture and save the output of superdense_coding
superdense_output = capture_output(superdense_coding.run_quantum_circuit, [0, 0], backend)
with open(os.path.join(current_dir, 'superdense_output.txt'), 'w') as file:
    file.write(superdense_output)

# Capture and save the output of quantum_teleportation
teleportation_output = capture_output(quantum_teleportation.run_quantum_circuit, [math.sqrt(1/2), math.sqrt(1/2)], backend)
with open(os.path.join(current_dir, 'teleportation_output.txt'), 'w') as file:
    file.write(teleportation_output)

# Capture and save the output of deutsch_algorithm
deutsch_output = capture_output(deutsch_algorithm.run_quantum_circuit, backend)
with open(os.path.join(current_dir, 'deutsch_output.txt'), 'w') as file:
    file.write(deutsch_output)