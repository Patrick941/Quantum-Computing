from qiskit import *
from qiskit.circuit.library import QFT

def run_quantum_circuit(input_state, backend):
    """
    Initializes a quantum circuit with the given input state and applies QFT twice.
    """
    num_qubits = len(input_state)

    # Define quantum and classical registers
    q = QuantumRegister(num_qubits, 'q')
    c = ClassicalRegister(num_qubits, 'c')
    qc = QuantumCircuit(q, c)

    # Initialize qubits based on input
    for i, value in enumerate(input_state):
        if value == '1':
            qc.x(q[i])  # Apply X gate to set |1> if the input is 1

    # Apply the QFT twice
    # Apply the QFT and its inverse
    qc.append(QFT(num_qubits=num_qubits, approximation_degree=0, do_swaps=True), q)
    qc.append(QFT(num_qubits=num_qubits, approximation_degree=0, do_swaps=True), q)
    # Measure the qubits
    qc.measure(q, c)

    # Draw and display the circuit
    # print(qc.draw(output='text'))

    # Compile and run the circuit
    qc_compiled = transpile(qc, backend=backend)
    job = backend.run(qc_compiled)

    result = job.result()
    counts = result.get_counts()
    return counts