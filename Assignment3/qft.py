from qiskit import *

def qft_circuit(num_qubits):
    """
    Creates a Quantum Fourier Transform (QFT) circuit for a given number of qubits.
    """
    qc = QuantumCircuit(num_qubits)
    
    # Apply the QFT
    for qubit in range(num_qubits):
        qc.h(qubit)
        for other_qubit in range(qubit + 1, num_qubits):
            qc.cp(2 * 3.14159 / (2 ** (other_qubit - qubit + 1)), qubit, other_qubit)
    
    # Swap qubits for reversing bit order
    for qubit in range(num_qubits // 2):
        qc.swap(qubit, num_qubits - qubit - 1)
    
    qc.measure_all()
    return qc

def run_quantum_circuit(qubits, backend):
    """
    Initializes a quantum circuit with the given qubits and applies QFT.
    """
    num_qubits = len(qubits)
    qc = QuantumCircuit(num_qubits)

    # Initialize the state from input probabilities
    for i, value in enumerate(qubits):
        qc.initialize([1 - value, value], i)

    # Apply the QFT
    qft_qc = qft_circuit(num_qubits)
    qc.compose(qft_qc, inplace=True)

    # Compile and run the circuit
    print(qc.draw())
    qc_compiled = transpile(qc, backend=backend)
    job = backend.run(qc_compiled)

    result = job.result()
    counts = result.get_counts()
    print("Measurement Results:")
    print(counts)