# Sensor Data Plot Generator

A Python script that generates synthetic temperature sensor data and creates publication-quality visualizations including scatter plots, histograms, and comparative analyses.

## Installation

1. Activate the `ece105` conda environment:
   ```
   conda activate ece105
   ```

2. Install the required dependencies using conda or mamba:
   ```
   conda install numpy matplotlib
   ```
   or
   ```
   mamba install numpy matplotlib
   ```

## Usage

Run the script from the command line:
```
python generate_plots.py
```

The script will generate synthetic sensor data and automatically create and save the plots as a PNG file.

## Example Output

The script produces a single PNG file named `sensor_analysis.png` containing three side-by-side plots:

- **Scatter Plot**: Temperature readings from Sensor A (blue) and Sensor B (orange) plotted against time (0-10 seconds), showing the temporal distribution of measurements.
- **Histogram of Sensor A**: Distribution of temperature values for Sensor A, centered around 25°C with a standard deviation of 3°C.
- **Histogram of Sensor B**: Distribution of temperature values for Sensor B, centered around 27°C with a standard deviation of 4.5°C.

The plots are saved at 150 DPI with tight bounding boxes for high-quality publication use.

## AI Tools Used and Disclosure

This project was developed with assistance from GitHub Copilot, an AI-powered coding assistant integrated into Visual Studio Code. The Copilot chat interface was used iteratively to generate and implement Python code based on natural language prompts and intent comments. This included creating synthetic data generation functions, plotting utilities that modify matplotlib Axes objects in place, the main script logic for producing publication-quality visualizations, and documentation. The AI helped convert a Jupyter notebook implementation into a standalone script, ensuring proper function signatures, docstrings, and error-free execution.