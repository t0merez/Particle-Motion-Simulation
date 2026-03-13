import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px
import pandas as pd
import copy

# Constants
K = 8.9875517873681764e9  # Coulomb's constant in N m²/C²
num_of_steps = 25000  # Number of simulation steps

# Particle class definition
class Particle:
    def __init__(self, position, velocity, mass, charge):
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.mass = mass
        self.charge = charge
        self.acceleration = np.zeros(3)

# Pole definition - they are stuck in place meaning they do not move or accelerate. No functions will change any of their data.
positive_side = Particle(position=[0, 0, 1], velocity=[0, 0, 0], mass= 1, charge=1)
negative_side = Particle(position=[0, 0, -1], velocity=[0, 0, 0], mass= 1, charge=-1)

#Function to compute the force on a particle due to the positive and negative poles.#
def compute_force(particle):
    r_pos = particle.position - positive_side.position
    r_neg = particle.position - negative_side.position
    
    # Calculate the magnitude of the forces
    F_pos = K * particle.charge * positive_side.charge / np.linalg.norm(r_pos)**2
    F_neg = K * particle.charge * negative_side.charge / np.linalg.norm(r_neg)**2
    
    # Calculate the direction of the forces
    F_pos_vector = F_pos * r_pos / np.linalg.norm(r_pos)
    F_neg_vector = F_neg * r_neg / np.linalg.norm(r_neg)
    
    # Total force is the sum of the forces from both poles
    total_force = F_pos_vector + F_neg_vector
    
    return total_force


# Calculate the acceleration of the particle based on the total force
def calculate_acceleration(particle):
    total_force = compute_force(particle)
    particle.acceleration = total_force / particle.mass


# Verlet integration method to update the position and velocity of the particle over time
def simulate_Verlet(p, dt=1e-7, steps = num_of_steps):
    pos = np.zeros((steps + 1, 3))
    vel = np.zeros((steps + 1, 3))
    
    # Store initial state
    pos[0] = p.position
    vel[0] = p.velocity

    for i in range(steps):
        calculate_acceleration(p)
        a_current = p.acceleration
        
        # Update velocity by half-step
        v_half = p.velocity + 0.5 * dt * a_current
        
        # Update position by full-step
        p.position = p.position + dt * v_half
        
        # Get new acceleration at the new position
        calculate_acceleration(p)
        a_new = p.acceleration
        
        # Finish velocity update
        p.velocity = v_half + 0.5 * dt * a_new

        pos[i+1] = p.position
        vel[i+1] = p.velocity
        
    return pos, vel

# Euler's method to update the position and velocity of the particle over time.
def simulate_Euler(p, dt=1e-7, steps=num_of_steps):
    pos = np.zeros((steps + 1, 3))
    vel = np.zeros((steps + 1, 3))
    
    # Store initial state
    pos[0] = p.position
    vel[0] = p.velocity

    for i in range(steps):
        calculate_acceleration(p)
        
        # Update velocity and position using Euler's method
        p.velocity = p.velocity + p.acceleration * dt
        p.position = p.position + p.velocity * dt

        pos[i+1] = p.position
        vel[i+1] = p.velocity
        
    return pos, vel


# Function to calculate the total energy of the particle at any given time, including kinetic and potential energy contributions.#
def calculateTotalEnergy(particle):
    # Calculate kinetic energy
    kinetic_energy = 0.5 * particle.mass * np.linalg.norm(particle.velocity)**2
    
    # Calculate potential energy due to the poles
    r_pos = np.linalg.norm(particle.position - positive_side.position)
    r_neg = np.linalg.norm(particle.position - negative_side.position)
    
    potential_energy_pos = K * particle.charge * positive_side.charge / r_pos
    potential_energy_neg = K * particle.charge * negative_side.charge / r_neg
    
    total_energy = kinetic_energy + potential_energy_pos + potential_energy_neg
    return total_energy


# Calculate the change in energy of the particle over the course of the simulation
def calculate_energy_change_verlet(particle, steps=num_of_steps):
    initial_energy = calculateTotalEnergy(particle)
    simulate_Verlet(particle, steps=steps, dt = 1e-9)

    final_energy = calculateTotalEnergy(particle)
    energy_change = final_energy - initial_energy
    
    return energy_change

def calculate_energy_change_euler(particle, steps=num_of_steps):
    initial_energy = calculateTotalEnergy(particle)
    simulate_Euler(particle, steps=steps, dt = 1e-9)

    final_energy = calculateTotalEnergy(particle)
    energy_change = final_energy - initial_energy
    
    return energy_change


# Function to plot the trajectory of the particle in 3D space, showing the positions of the positive and negative poles for reference.#
def plot_trajectory(particle, steps = num_of_steps):
    pos, _ = simulate_Verlet(particle, steps=steps)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(pos[:, 0], pos[:, 1], pos[:, 2], label='Trajectory')

    # Mark the start and end positions of the particle
    ax.scatter(*pos[0], color='green', marker='o', s=60, label='Start')
    ax.scatter(*pos[-1], color='magenta', marker='X', s=80, label='End')

    # Mark the fixed poles
    ax.plot(positive_side.position[0], positive_side.position[1], positive_side.position[2], 'ro', label='Positive Pole')
    ax.plot(negative_side.position[0], negative_side.position[1], negative_side.position[2], 'bo', label='Negative Pole')

    ax.legend()
    ax.set_title('Trajectory of the Particle')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    plt.show()

def compare_energy_change(particle, steps=num_of_steps):
    energy_change_verlet = calculate_energy_change_verlet(copy.deepcopy(particle), steps=steps)
    energy_change_euler = calculate_energy_change_euler(copy.deepcopy(particle), steps=steps)
    
    print(f"Energy change using Verlet method: {energy_change_verlet:.6e} J")
    print(f"Energy change using Euler method: {energy_change_euler:.6e} J")