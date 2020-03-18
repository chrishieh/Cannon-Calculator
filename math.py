pressure = 689476 #pascal
barrel_length = 3.2    #meters
atmospheric_pressure = 100000
cross_section_area = .02 #meters squared
gamma = 7/5    # 7/5 for adiabatic, 2 for isothermal
friction = 0
reservoir = .1 #v naught
mass = .028



one = (2 / mass)
two = (pressure * reservoir/(gamma - 1))
three = (1 - (reservoir / (cross_section_area * barrel_length + reservoir)) ** (gamma - 1))
four = cross_section_area*barrel_length*atmospheric_pressure

velocity = ((one*(two*(three))) - four)
velocity **= .5
print(velocity, "meters per second")

print("kinetic energy =", .5 * (velocity ** 2) * mass, "joules")

print("for reference, the energy of a .45 caliber bullet is 600j and a 50 cal is 18,000")