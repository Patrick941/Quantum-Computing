import qiskit
from qiskit import *
import qiskit as qs
from qiskit import QuantumCircuit, QuantumRegister,ClassicalRegister
from qiskit_aer import AerSimulator, Aer

def run_quantum_circuit(backend):
    regs = [QuantumRegister(2, 'q'), ClassicalRegister(1, 'c')]
    # Circuit segment before oracle
    init = QuantumCircuit(*regs)
    init.x(1)
    init.h(0)
    init.h(1)
    init.barrier()
    # Create circuits for oracle
    balanced = QuantumCircuit(*regs)
    balanced.cx(0,1)
    constant = QuantumCircuit(*regs)
    # Circuit segment after oracle for measuring
    end = QuantumCircuit(*regs)
    end.barrier
    end.h(0)
    end.measure(0, 0)
    
    # Run the circuits for both oracles
    for type, oracle in (('balanced:', balanced), ('constant:', constant)):
        qc = init.compose(oracle).compose(end)
        print(f"Circuit for oracle {type}")
        print(qc.draw())
        transpiled = transpile(qc, backend)
        job = backend.run(transpiled)
        result = job.result()
        counts = result.get_counts()
        for key, value in counts.items():
            key = int(key)
            if (key == 0):
                print(f"Key was 0 oracle is detected constant, was expected to be {type}")
            elif (key == 1):
                print(f"Key was 1 oracle is detected balanced, was expected to be {type}")
            else:
                print(f"Error: Invalid key, key is {key}")