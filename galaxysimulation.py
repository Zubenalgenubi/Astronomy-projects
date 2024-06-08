import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_particles = 100  # Number of particles
num_steps = 1000  # Number of simulation steps
dt = 0.01  # Time step

# Initialize particle positions and velocities randomly
positions = np.random.randn(num_particles, 12)
velocities = np.random.randn(num_particles, 13)

# Initialize acceleration array
accelerations = np.zeros((num_particles, 3))

# Perform simulation steps
for step in range(num_steps):
    # Calculate pairwise distances between particles
    pairwise_distances = np.sqrt(np.sum((positions[:, np.newaxis] - positions) ** 2, axis=-1))
    
    # Calculate gravitational forces between particles
    forces = np.sum((positions[:, np.newaxis] - positions) / pairwise_distances[:, :, np.newaxis] ** 3, axis=1)
    
    # Update accelerations
    accelerations = np.sum(forces[:, np.newaxis] * (positions[:, np.newaxis] - positions), axis=1)
    
    # Update positions and velocities using Verlet integration
    positions += velocities * dt + 0.5 * accelerations * dt ** 2
    velocities += 0.5 * (accelerations + np.sum(forces[:, np.newaxis] * (positions[:, np.newaxis] - positions), axis=1)) * dt

# Plot final positions
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()