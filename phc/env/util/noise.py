import numpy as np
import torch

def scale_array_torch(array):
    max_abs_value = torch.max(torch.abs(array))
    scaled_array = array / max_abs_value
    return scaled_array, max_abs_value
    

def scale_array(array):
    max_abs_value = np.max(np.abs(array))
    scaled_array = array / max_abs_value
    rescaling_factor = max_abs_value
    return scaled_array,rescaling_factor

def rescale_array(array,rescaling_factor):
    return array * rescaling_factor

def simulate_ou_noise(size, delta_t, theta, sigma, mu=0.0):
    num_time_steps = size
    # Initialize the array for noise
    noise = np.zeros((num_time_steps, 3))
    # Initial values can optionally be set to different values
    noise[0, :] = np.random.normal(mu, sigma, 3)

    # Generate noise for each time step
    for t in range(1, num_time_steps):
        dt = delta_t
        dw = np.random.normal(0, np.sqrt(dt), 3)  # Brownian increments
        noise[t, :] = noise[t - 1, :] + theta * (mu - noise[t - 1, :]) * dt + sigma * dw

    return noise

def simulate_ou_noise_torch(size, delta_t, theta, sigma, mu=0.0):
    noise = torch.zeros((size, 3))
    noise[0, :] = torch.normal(mu, sigma, size=(3,))
    for t in range(1, size):
        dt = delta_t.to("cpu")
        dw = torch.normal(0, torch.sqrt(dt).item(), size=(3,))  # Brownian increments
        noise[t, :] = noise[t - 1, :] + theta * (mu - noise[t - 1, :]) * dt + sigma * dw
    
    return noise
    

def simulate_gaussian_noise(size, sigma, mu=0.0):
    size = (size, 3)
    noise = np.random.normal(mu, sigma, size)
    # Generate noise for each point in time       
    return noise

def simulate_gaussian_noise_torch(size, sigma, mu=0.0):
    return torch.normal(mu, sigma, size=(size, 3))