# 2D Heat Transfer Simulation

A Python implementation of two-dimensional heat transfer simulation using the Finite Difference Method (FDM). This project provides a numerical solution to the heat equation and visualizes the temperature distribution over time.

## Features

- 2D heat transfer simulation using explicit finite difference method
- Interactive visualization with Plotly
- Configurable simulation parameters
- Real-time temperature monitoring
- Animation controls (play, pause, step-by-step)
- Stability criterion checking (CFL condition)

## Mathematical Background

The simulation solves the 2D heat equation:

∂T/∂t = α(∂²T/∂x² + ∂²T/∂y²)

where:
- T is temperature
- t is time
- α is thermal diffusivity
- x, y are spatial coordinates

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd heat-transfer-simulation
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Simulation

```bash
python src/run_simulation.py
```

### Configuration

Edit the simulation parameters in `src/utils/config.py`:
- `nx`, `ny`: Grid dimensions
- `dx`, `dy`: Spatial step sizes
- `dt`: Time step
- `alpha`: Thermal diffusivity
- `steps`: Number of simulation steps
- `hot_region`: Initial hot region coordinates and temperature

## Project Structure

```
pro/
├── src/
│   ├── simulation/
│   │   ├── heat_transfer.py    # Core simulation logic
│   │   └── visualizer.py       # Plotting and animation
│   ├── utils/
│   │   └── config.py           # Configuration settings
│   └── run_simulation.py       # Main execution script
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

## Dependencies

- NumPy: Numerical computations
- Plotly: Interactive visualization

## Technical Details

- Uses explicit finite difference method for spatial discretization
- Forward Euler method for time integration
- Dirichlet boundary conditions (fixed temperature at boundaries)
- Interactive animation with play/pause controls and time slider
- CFL condition monitoring for numerical stability

## Limitations

- Explicit method requires small time steps for stability
- Fixed boundary conditions
- Uniform grid spacing

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
