class SimulationConfig:
    DEFAULT_CONFIG = {
        'nx': 50,
        'ny': 50,
        'dx': 1.0,
        'dy': 1.0,
        'dt': 0.1,
        'alpha': 1.0,
        'steps': 100,
        'hot_region': ((20, 30), (20, 30), 100.0)
    }

    @classmethod
    def get_default_config(cls):
        return cls.DEFAULT_CONFIG.copy()
