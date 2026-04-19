"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
import numpy as np


def generate_data(seed):
    """Generate synthetic temperature sensor data and timestamps.

    Creates simulated temperature readings from two sensors with specified
    statistical properties and evenly spaced timestamps over a 10-second period.

    Parameters
    ----------
    seed : int
        Seed for the random number generator to ensure reproducible results.
        Should be the last 4 digits of your Drexel ID.

    Returns
    -------
    sensor_a : ndarray of shape (200,)
        Temperature readings from Sensor A in Celsius, normally distributed
        with mean 25°C and standard deviation 3°C.
    sensor_b : ndarray of shape (200,)
        Temperature readings from Sensor B in Celsius, normally distributed
        with mean 27°C and standard deviation 4.5°C.
    timestamps : ndarray of shape (200,)
        Evenly spaced timestamps from 0 to 10 seconds.
    """
    rng = np.random.default_rng(seed)
    sensor_a = rng.normal(25, 3, 200)
    sensor_b = rng.normal(27, 4.5, 200)
    timestamps = np.linspace(0, 10, 200)
    return sensor_a, sensor_b, timestamps


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Create a scatter plot of sensor temperature readings over time.

    Plots temperature readings from two sensors against timestamps on the
    provided Axes object, with Sensor A in blue and Sensor B in orange.

    Parameters
    ----------
    sensor_a : array-like
        Temperature readings from Sensor A in Celsius.
    sensor_b : array-like
        Temperature readings from Sensor B in Celsius.
    timestamps : array-like
        Time values in seconds, same length as sensor arrays.
    ax : matplotlib.axes.Axes
        The Axes object on which to draw the scatter plot.

    Returns
    -------
    None
        Modifies the input Axes object in place.
    """
    ax.scatter(timestamps, sensor_a, color='blue', label='Sensor A', alpha=0.7)
    ax.scatter(timestamps, sensor_b, color='orange', label='Sensor B', alpha=0.7)
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Sensor Temperature Readings Over Time')
    ax.legend()
    ax.grid(True, alpha=0.3)