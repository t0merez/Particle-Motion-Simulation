# Charged Particle Around a Dipole Simulation

## Overview

This project simulates the motion of a charged particle in the electric field of a static dipole.
The system is modeled using **Coulomb’s Law** and **Newton’s Second Law**, and the resulting equations of motion are solved numerically.

The main goal of the project is to:

* Simulate particle trajectories in a dipole field
* Compare numerical integration methods
* Investigate **energy conservation** of different numerical methods in a physical system
* Demonstrate **deterministic chaos** through sensitivity to initial conditions

---

## Features

* 3D simulation of charged particle motion
* Implementation of:

  * **Euler Method**
  * **Velocity Verlet Integration**
* Energy conservation comparison between methods
* Visualization of particle trajectories
* Log-distance plots demonstrating chaotic behavior
* Interactive 3D trajectory visualization (Plotly)

---

## Technologies Used

* **Python**
* **NumPy** — vector calculations
* **Matplotlib** — static plots
* **Plotly** — interactive 3D visualization
* **Pandas** — data handling
* **Jupyter Notebook**

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/t0merez/Particle-Motion-Simulation.git
cd Particle-Motion-Simulation
```

2. Install dependencies:

```bash
pip install numpy matplotlib plotly pandas
```

3. Run the simulation:

Open the Jupyter Notebook:

```bash
jupyter notebook
```

Then run the main simulation notebook.

---

## Project Structure

```
Particle-Motion-Simulation/
│
├── sim.py          # Particle class, physics functions and numerical methods
├── code_simulations.ipynb       # Main simulation notebook
├── code_chaos.ipynb              # Chaos Check Simulations
├── article.pdf           # Full project report
└── README.md
```

---

## Scientific Background

The simulation models the force acting on a charged particle using:

* **Coulomb’s Law**
* **Newton’s Second Law**
* Numerical integration techniques

The Velocity Verlet method is used for stable long-term simulations due to its superior energy conservation properties.

---

## Results

The project demonstrates:

* Stable and unstable particle trajectories
* Energy drift in Euler’s method
* Improved stability using Velocity Verlet
* Chaotic behavior resulting from small changes in initial conditions

---

## Author

**Tom Erez**
Computational Science Project — 2026

Under the guidance of:
**Shlomo Rozenfield**
