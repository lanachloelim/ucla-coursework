# UCLA EC ENGR 115C: Final Project

Final project for EC ENGR 115C: Digital Electronic Circuits (Prof. Dejan Markovic, UCLA Winter 2025) completed by Lana Lim, Jared Velasquez, and Maria Campo Martins. Original GitHub repository [here](https://github.com/Jared-Velasquez/ece115c-project).

## 4-Bit Absolute-Value Detector

Built a circuit that flags whether the magnitude of a signed 4-bit input exceeds a programmable 3-bit threshold. Design goals were to minimise total energy while allowing at most a 40 % (1.4×) increase over the minimum practical worst-case delay.

### Three-phase flow:
1. Gate-level synthesis & logical-effort sizing (VDD = 1 V).
2. LTspice functional and timing verification to establish the minimum-delay baseline.
3. Joint gate-sizing + supply-voltage optimisation to hit the 1.4×-delay target with minimum energy.

## Repository Structure:
```plaintext
/docs    → project report, slides
/src     → schematic netlists
/spice   → LTspice test-benches and schematics
/scripts → sizing & optimisation notebooks, testing scripts
```

## Project Stats:
