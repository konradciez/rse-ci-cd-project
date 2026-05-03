import numpy as np
from numba import njit
from pint import UnitRegistry

ureg = UnitRegistry()

@njit
def fast_sum_squares(n):
    """Funkcja zoptymalizowana przez Numba (JIT)."""
    result = 0.0
    for i in range(n):
        result += i**2
    return result

def calculate_kinetic_energy(mass_val, velocity_val):
    """Funkcja używająca Pint do obliczeń fizycznych z jednostkami."""
    # Definiowanie wartości z jednostkami
    mass = mass_val * ureg.kilogram
    velocity = velocity_val * (ureg.meter / ureg.second)
    
    # Wzór: E = 1/2 * m * v^2
    energy = 0.5 * mass * velocity**2
    return energy.to(ureg.joule)