from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.circuit.library import zz_feature_map

sim = AerSimulator()

# 实验1：贝尔态
qc1 = QuantumCircuit(2)
qc1.h(0)
qc1.cx(0, 1)
qc1.measure_all()
result1 = sim.run(qc1, shots=1024).result()
print("贝尔态:", result1.get_counts())

# 实验2：GHZ态
qc2 = QuantumCircuit(3)
qc2.h(0)
qc2.cx(0, 1)
qc2.cx(1, 2)
qc2.measure_all()
result2 = sim.run(qc2, shots=1024).result()
print("GHZ态:", result2.get_counts())

# 实验3：ZZ特征映射
fm = zz_feature_map(feature_dimension=4, reps=1)
print("特征映射CNOT门数量:", fm.decompose().count_ops().get('cx', 0))