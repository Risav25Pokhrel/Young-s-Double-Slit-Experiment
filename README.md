# Young's Double Slit Experiment — Quantum Simulation

> A quantum computing simulation of Young's Double Slit Experiment using Qiskit, demonstrating wave-particle duality, quantum superposition, and interference patterns — run on both the Qiskit AER simulator and real IBM quantum hardware.

---

## 🏅 Recognition

> **Honorable Mention — Future Leaders in Quantum Hackathon 2025**
> This project was awarded an **Honorable Mention** in the *"Implementing Quantum Experiments"* challenge under the **Education Track** of the **Future Leaders in Quantum Hackathon 2025**, organized by the Quantum Coalition and co-organised by ITU, powered by IonQ. The hackathon was held on **20 May 2025, Geneva, Switzerland**.

---

## Table of Contents

- [Overview](#overview)
- [Background](#background)
- [Project Structure](#project-structure)
- [Quantum Circuit Design](#quantum-circuit-design)
- [What Was Done](#what-was-done)
- [Prerequisites](#prerequisites)
- [Installation & Usage](#installation--usage)
- [References](#references)

---

## Overview

This project bridges one of the most celebrated experiments in classical physics with quantum computing. **Young's Double Slit Experiment** — which famously demonstrated the wave nature of light in 1801 — has a deep quantum analog: a single quantum particle in superposition simultaneously takes both paths, and its final measurement outcome is governed by quantum interference, not classical probability.

This notebook models that phenomenon using **Hadamard gates** and **phase gates** in Qiskit to construct a quantum circuit that replicates the interference pattern arising from two-path superposition. The circuit is validated on the **Qiskit AER simulator** and executed on **real IBM quantum hardware**.

---

## Background

### Classical Double Slit

In Young's original experiment, coherent light (or particles) are fired at a barrier with two slits. Rather than producing two bright bands as expected classically, the screen behind shows an **interference pattern** — alternating bright and dark fringes — proving that each particle travels through both slits simultaneously as a wave and interferes with itself.

### Quantum Analog

In the quantum version, this experiment captures the essence of **wave-particle duality**:

- A qubit prepared in superposition (`|+⟩ = H|0⟩`) encodes the two-path scenario — the particle simultaneously passes through both slits
- A **phase gate** introduces the path-length difference between the two slits, equivalent to the physical slit separation `d` and screen distance `L`
- A second **Hadamard gate** acts as the recombination — analogous to the wavefronts meeting at the screen
- **Measurement** collapses the state, with outcome probabilities forming the interference pattern

The key quantum principle at work: if you do **not** measure which slit the particle passes through, interference occurs. If you **do** measure (which-path information), the interference pattern vanishes — a phenomenon known as **quantum erasure**.

---

## Project Structure

```
Young-s-double-slit-experiment/
│
├── helpers/                        # Helper modules and utility functions
│   └── ...
│
├── double_slit_experiment.ipynb    # Main notebook: full simulation walkthrough
├── README.md
└── .gitignore
```

---

## Quantum Circuit Design

The quantum circuit models the double slit setup as follows:

```
|0⟩ ── H ── P(φ) ── H ── Measure
```

| Gate | Physical Analogy |
|------|-----------------|
| `H` (first) | Particle enters the double slit — enters superposition of both paths |
| `P(φ)` | Phase shift due to path-length difference (controlled by slit geometry) |
| `H` (second) | Wavefronts recombine at the screen |
| Measure | Detection event — collapse to 0 or 1 with interference-modulated probability |

By sweeping the phase `φ` from 0 to 2π, the measurement probability `P(|0⟩) = cos²(φ/2)` traces out the **interference fringe pattern**, exactly mirroring the classical intensity distribution on the screen.

---

## What Was Done

1. **Classical Simulation** — Reviewed wave interference principles and implemented a simple classical simulation of the double slit intensity pattern as a baseline

2. **Quantum Circuit Modeling** — Designed a quantum circuit using Hadamard and phase gates to mimic the two-slit setup and encode the path superposition

3. **Equivalent Circuit Formulation** — Mapped quantum operations to physical slit parameters, showing how superposition and interference arise naturally from the gate sequence

4. **Simulation on Qiskit AER** — Ran the circuit on the local statevector and QASM simulators to validate the theoretical interference fringe pattern

5. **Execution on Real IBM Quantum Hardware** — Submitted the circuit to a real IBM quantum backend, compared noisy hardware results against ideal simulation, and analyzed decoherence effects

6. **Which-Path Detection** — Explored the quantum erasure scenario by adding a measurement on an ancilla qubit to extract which-slit information, demonstrating the collapse of the interference pattern

---

## Prerequisites

| Package | Purpose |
|---------|---------|
| Python ≥ 3.8 | Core runtime |
| Qiskit | Quantum circuit construction and simulation |
| Qiskit IBM Runtime | Access to real IBM quantum hardware |
| NumPy | Phase sweep and numerical calculations |
| Matplotlib | Plotting interference patterns |
| Jupyter | Running the notebook |

---

## Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/Risav25Pokhrel/Young-s-double-slit-experiment.git
cd Young-s-double-slit-experiment
```

### 2. Install Dependencies

```bash
pip install qiskit qiskit-ibm-runtime numpy matplotlib jupyter
```

### 3. Run the Notebook

```bash
jupyter notebook double_slit_experiment.ipynb
```

Run cells in order to:
1. Simulate the classical interference pattern
2. Build and visualize the quantum circuit
3. Sweep the phase φ and plot the quantum interference fringe
4. Run on the AER simulator
5. *(Optional)* Submit to IBM quantum hardware — requires an [IBM Quantum account](https://quantum.ibm.com/)

For IBM hardware execution, set your API token:

```python
from qiskit_ibm_runtime import QiskitRuntimeService
QiskitRuntimeService.save_account(channel="ibm_quantum", token="YOUR_API_TOKEN")
```

---

## References

- Young, T. — *On the Theory of Light and Colours*, Phil. Trans. R. Soc. London **92**, 12–48 (1802). *(Original double slit paper)*
- Feynman, R. P., Leighton, R. B. & Sands, M. — *The Feynman Lectures on Physics, Vol. III*, Ch. 1 (1965). *(Quantum interpretation of the double slit)*
- Nielsen, M. A. & Chuang, I. L. — *Quantum Computation and Quantum Information*, Cambridge University Press (2000)
- [Qiskit Documentation](https://docs.quantum.ibm.com/)
- **Future Leaders in Quantum Hackathon 2025** — Quantum Coalition & ITU, Geneva, Switzerland (May 2025)

---

*Awarded **Honorable Mention** at the Future Leaders in Quantum Hackathon 2025 · Developed by [Risav Pokhrel](https://github.com/Risav25Pokhrel) · Institute of Engineering, Pulchowk Campus, Nepal*
