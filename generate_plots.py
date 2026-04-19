"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
import numpy as np
import matplotlib.pyplot as plt


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


def plot_histogram(data, ax, bins=30, color="steelblue", title="Histogram"):
    """Create a histogram of the provided data array.

    Plots a histogram of the values in the data array on the provided
    Axes object with customizable bins, color, and title.

    Parameters
    ----------
    data : array-like
        The data array to plot.
    ax : matplotlib.axes.Axes
        The Axes object on which to draw the histogram.
    bins : int, optional
        Number of bins for the histogram (default is 30).
    color : str, optional
        Color of the histogram bars (default is "steelblue").
    title : str, optional
        Title for the histogram plot (default is "Histogram").

    Returns
    -------
    None
        Modifies the input Axes object in place.
    """
    ax.hist(data, bins=bins, color=color, alpha=0.7)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title(title)
    ax.grid(True, alpha=0.3)


def main():
    """Generate sensor data and create publication-quality plots.

    Generates synthetic temperature data using a fixed seed, creates a 2x2
    subplot figure with scatter plot, histograms of Sensor A and B, and
    summary statistics in the bottom-right cell, adjusts the layout, and
    saves the figure as a PNG file.

    Returns
    -------
    None
    """
    seed = 1234  # Replace with last 4 digits of your Drexel ID
    sensor_a, sensor_b, timestamps = generate_data(seed)

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    plot_scatter(sensor_a, sensor_b, timestamps, axes[0, 0])
    plot_histogram(sensor_a, axes[0, 1], color='blue', title='Histogram of Sensor A')
    plot_histogram(sensor_b, axes[1, 0], color='orange', title='Histogram of Sensor B')

    # Summary statistics in bottom-right
    axes[1, 1].axis('off')
    stats = f"""
    Summary Statistics:

    Sensor A:
    Mean: {np.mean(sensor_a):.2f} °C
    Std: {np.std(sensor_a):.2f} °C

    Sensor B:
    Mean: {np.mean(sensor_b):.2f} °C
    Std: {np.std(sensor_b):.2f} °C

    Overall:
    Mean: {np.mean(np.concatenate([sensor_a, sensor_b])):.2f} °C
    """
    axes[1, 1].text(0.1, 0.5, stats, transform=axes[1, 1].transAxes, fontsize=10, verticalalignment='center')

    plt.tight_layout()
    plt.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')
    plt.close(fig)  # Close to free memory


if __name__ == '__main__':
    main()