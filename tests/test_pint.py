from core import calculate_kinetic_energy

def test_kinetic_energy_value():
    # 0.5 * 2kg * (3m/s)^2 = 9J
    energy = calculate_kinetic_energy(2, 3)
    assert energy.magnitude == 9.0
    assert str(energy.units) == "joule"