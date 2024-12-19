from simulation.heat_transfer import HeatTransferSimulation
from simulation.visualizer import HeatMapVisualizer
from utils.config import SimulationConfig

def main():
    # Get configuration
    config = SimulationConfig.get_default_config()

    # Initialize simulation
    simulation = HeatTransferSimulation(
        nx=config['nx'],
        ny=config['ny'],
        dx=config['dx'],
        dy=config['dy'],
        dt=config['dt'],
        alpha=config['alpha']
    )

    # Set initial conditions and run
    simulation.set_initial_conditions(config['hot_region'])
    simulation.run_simulation(config['steps'])

    # Create and display animation
    fig = HeatMapVisualizer.create_animation(simulation.frames)
    fig.show()

if __name__ == "__main__":
    main()
