import numpy as np

# Example data
data = [
    [10, 10, 3, 0.25, 2.75, 2.5, 0.25, 2.25, 0.5, 12.620, 17.070, 0.294, 1.365, 12.438, 12.732, 16.314, 17.679],
    [10, 10, 3, 0.25, 2.75, 2.5, 0.5, 2, 0.5, 12.579, -1.000, 0.317, -1.000, 12.390, 12.707, 17.542, -1.000],
    [10, 10, 3, 0.25, 2.75, 2.5, 0.75, 1.75, 0.5, 12.580, -1.000, 0.320, -1.000, 12.391, 12.711, -1.000, -1.000],
    [10, 10, 3, 0.25, 2.75, 2.5, 1, 1.5, 0.5, 12.580, -1.000, 0.332, -1.000, 12.382, 12.714, -1.000, -1.000],
    [10, 10, 3, 0.25, 2.75, 2.5, 1.25, 1.25, 0.5, 12.569, -1.000, 0.337, -1.000, 12.371, 12.708, -1.000, -1.000],
    [10, 10, 3, 0.25, 2.75, 2.5, 1.5, 1, 0.5, 12.480, -1.000, 0.351, -1.000, 12.268, 12.619, -1.000, -1.000]
]

def objective_function(x, y):
    # Define your objective function here
    return (x**2 + y**2)

def particle_swarm_optimization(data, num_particles=10, num_iterations=100, inertia=0.5, cognitive_factor=1, social_factor=2):
    num_variables = 2  # Number of variables in the objective function
    num_data_points = len(data)
    
    # Initialize particle positions and velocities
    particles_position = np.random.uniform(low=-10, high=10, size=(num_particles, num_variables))
    particles_velocity = np.random.uniform(low=-1, high=1, size=(num_particles, num_variables))
    
    # Initialize personal best positions
    personal_best_positions = particles_position.copy()
    personal_best_values = np.zeros(num_particles)
    
    # Initialize global best position
    global_best_position = np.zeros(num_variables)
    global_best_value = float('inf')
    
    # Initialize the swarm
    for i in range(num_particles):
        x, y = particles_position[i]
        personal_best_values[i] = objective_function(x, y)
        if personal_best_values[i] < global_best_value:
            global_best_value = personal_best_values[i]
            global_best_position = particles_position[i]
    
    # Main loop
    for iteration in range(num_iterations):
        for i in range(num_particles):
            # Update velocity
            r1, r2 = np.random.rand(), np.random.rand()
            cognitive_velocity = cognitive_factor * r1 * (personal_best_positions[i] - particles_position[i])
            social_velocity = social_factor * r2 * (global_best_position - particles_position[i])
            particles_velocity[i] = inertia * particles_velocity[i] + cognitive_velocity + social_velocity
            
            # Update position
            particles_position[i] += particles_velocity[i]
            
            # Update personal best
            x, y = particles_position[i]
            value = objective_function(x, y)
            if value < personal_best_values[i]:
                personal_best_values[i] = value
                personal_best_positions[i] = particles_position[i]
                
                # Update global best
                if value < global_best_value:
                    global_best_value = value
                    global_best_position = particles_position[i]
        
    return global_best_position, global_best_value

# Example usage
best_position, best_value = particle_swarm_optimization(data)
print("Global best position:", best_position)
print("Global best value:", best_value)
