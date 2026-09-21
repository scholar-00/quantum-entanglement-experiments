# 量子纠缠与多体系统的模拟验证

## 实验目的

验证量子计算中的两大核心概念：
1. 两体纠缠：通过贝尔态验证两个量子比特的完美关联。
2. 多体纠缠：通过GHZ态验证三个量子比特的全局关联。
3. 特征映射：分析ZZ特征映射电路中的纠缠结构。

## 实验环境

- Qiskit 2.5.2
- Python 3.10
- Jupyter Notebook

## 实验原理

- 贝尔态：1/√2(|00⟩ + |11⟩)，由H门+CNOT门制备。
- GHZ态：1/√2(|000⟩ + |111⟩)，由H门+两个CNOT门制备。
- ZZ特征映射：把经典数据编码到量子态，并通过CNOT门引入特征间的关联。

## 实验步骤与结果

### 实验1：贝尔态

电路：
```python
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

测量结果：{'00': 508, '11': 516}

分析：

只有00和11出现，各约50%

01和10完全消失

证明两个量子比特完美关联

状态向量：[0.7071, 0, 0, 0.7071]，对应 1/√2(|00⟩ + |11⟩)

实验2：GHZ态
电路：s

python
qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.measure_all()
测量结果：{'000': 515, '111': 509}

分析：

只有000和111出现，各约50%

其他6种组合完全消失

证明三个量子比特全局关联

实验3：ZZ特征映射电路分析
电路结构：

4个量子比特

6个CNOT门（所有两两配对）

每个CNOT之间插入相位旋转门，编码特征间的乘积

CNOT门数量：6个

结论
两体纠缠：贝尔态测量结果只有00和11，证明两个量子比特完美关联。

多体纠缠：GHZ态测量结果只有000和111，证明三个量子比特全局关联。

特征映射：ZZ特征映射通过CNOT门引入特征间关联，是量子机器学习中编码经典数据的关键步骤。

核心结论：纠缠 = 无法拆成张量积。测量结果的“缺失项”（如贝尔态中的01和10）就是纠缠的直接证据。

附录：完整代码
python
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
