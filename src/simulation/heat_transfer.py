import numpy as np


class HeatTransferSimulation:
    def __init__(self, nx, ny, dx, dy, dt, alpha):
        self.nx = nx
        self.ny = ny
        self.dx = dx
        self.dy = dy
        self.dt = dt
        self.alpha = alpha
        self.temperature = np.zeros((ny, nx))
        self.new_temperature = np.zeros((ny, nx))
        self.frames = []
        self.stability_criterion()

    def stability_criterion(self):
        cfl = self.alpha * self.dt * (1 / self.dx * 2 + 1 / self.dy * 2)
        if cfl > 0.5:
            print("Warning: CFL condition violated. Simulation may be unstable.")

    def set_initial_conditions(self, hot_region=None):
        if hot_region:
            (x_start, x_end), (y_start, y_end), value = hot_region
            self.temperature[y_start:y_end, x_start:x_end] = value
        else:
            cx, cy = self.nx // 2, self.ny // 2
            self.temperature[cy, cx] = 100.0

    def apply_boundary_conditions(self):
        self.temperature[:, 0] = 0  # Left
        self.temperature[:, -1] = 0  # Right
        self.temperature[0, :] = 0  # Top
        self.temperature[-1, :] = 0  # Bottom

    def update_temperature(self):
        for i in range(1, self.ny - 1):
            for j in range(1, self.nx - 1):
                self.new_temperature[i, j] = self.temperature[
                    i, j
                ] + self.alpha * self.dt * (
                    (
                        self.temperature[i + 1, j]
                        - 2 * self.temperature[i, j]
                        + self.temperature[i - 1, j]
                    )
                    / self.dy**2
                    + (
                        self.temperature[i, j + 1]
                        - 2 * self.temperature[i, j]
                        + self.temperature[i, j - 1]
                    )
                    / self.dx**2
                )
        self.temperature[:] = self.new_temperature[:]
        self.frames.append(self.temperature.copy())

    def run_simulation(self, steps):
        for step in range(steps):
            self.apply_boundary_conditions()
            self.update_temperature()
            print(
                f"Step {step + 1}: Max Temp = {np.max(self.temperature):.2f}, Min Temp = {np.min(self.temperature):.2f}"
            )
