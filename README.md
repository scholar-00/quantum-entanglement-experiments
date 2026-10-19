# Quantum Entanglement Verification

## Overview
This project verifies core concepts of quantum entanglement and feature mapping using Qiskit. It demonstrates two-body entanglement (Bell state), multi-body entanglement (GHZ state), and the entanglement structure within a ZZ feature map circuit.

## Environment
*   **Qiskit:** 2.5.2
*   **Python:** 3.10
*   **Platform:** Jupyter Notebook

## Core Principles
*   **Bell State:** `1/√2(|00⟩ + |11⟩)`, prepared via a Hadamard gate followed by a CNOT gate.
*   **GHZ State:** `1/√2(|000⟩ + |111⟩)`, prepared via a Hadamard gate and two sequential CNOT gates.
*   **ZZ Feature Map:** Encodes classical data into quantum states and introduces correlations between features using CNOT gates.

## Experimental Results

### 1. Bell State
*   **Measurement Results:** `{'00': 508, '11': 516}`
*   **Analysis:** Only `00` and `11` are observed (each ~50%). The states `01` and `10` are completely absent. 
*   **Conclusion:** This perfect correlation confirms the state vector is `[0.7071, 0, 0, 0.7071]`, representing `1/√2(|00⟩ + |11⟩)`.

### 2. GHZ State
*   **Measurement Results:** `{'000': 515, '111': 509}`
*   **Analysis:** Only `000` and `111` are observed (each ~50%). The other 6 possible states are entirely absent.
*   **Conclusion:** This demonstrates global entanglement across all three qubits.

### 3. ZZ Feature Map Circuit
*   **Setup:** 4 qubits, with 6 CNOT gates (all pairwise combinations) and phase rotation gates inserted between them.
*   **Conclusion:** The ZZ feature map introduces correlations via CNOTs, which is a critical step for encoding classical data in Quantum Machine Learning.

## Key Takeaway
**Entanglement = The inability to be factored into a tensor product.** The "missing terms" in the measurement outcomes (e.g., `01` and `10` in the Bell state) are direct evidence of entanglement.
