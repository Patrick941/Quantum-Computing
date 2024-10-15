---
title: "Assignment 2: Quantum Algorithms"
author: "Patrick Farmer 20331828"
date: "15-10-2024"
header-includes:
  - \usepackage{minted}
  - \usemintedstyle{friendly}
---

![](https://www.tcd.ie/media/tcd/site-assets/images/tcd-logo.png)

\clearpage

## Introduction
This labs aims to investigate the workings and usage of a couple of quantum algorithms. The 3 algorithms taken for this lab are:
* Superdense Coding
* Quantum Teleportation
* Deutsch's Algorithm

### Superdense Coding
The algorithm is used to send two classical bits of information using only one qubit. The algorithm works by using a Bell pair to entangle two qubits. The bell pair that I used was the following:
$$
\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)
$$
Say we have two people, Alice and Bob. Alice takes the first qubit of the bell pair, Bob takes the second qubit. Alice then performs the following operations on her qubit:
1. Apply the Hadamard gate
2. Apply the CNOT gate
3. Then if the first bit of the message is 1, apply the Z gate
4. Then if the second bit of the message is 1, apply the X gate
Alice then sends her qubit to Bob. Bob then applies the following operations to his qubit:
1. Apply the CNOT gate
2. Apply the Hadamard gate
Bob then measures the qubits and gets the two bits of information that Alice sent.

### Quantum Teleportation


## Appendix
```{=latex}
\inputminted{python}{deutsch_algorithm.py}