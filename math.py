import tkinter as tk
pressure = 689476 #pascal
barrel_length = 3.2    #meters
atmospheric_pressure = 100000
cross_section_area = .02 #meters squared
gamma = 7/5    # 7/5 for adiabatic, 2 for isothermal
friction = 0
reservoir = .1 #v naught
mass = .028
final_velocity = 0

fields = ("Pressure (psi)", "Barrel Length (meters)", "Atmospheric Pressure (psi)", "Barrel Cross Section (m^2)", "Reservoir Volume (m^3)", "Projectile Mass (Kg)")


class math():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cannon Calculator")
        # self.root.geometry("600x300")
        ents = self.makeform(self.root, fields)
        b1 = tk.Button(self.root, text='Calculate',
                       command=(lambda e=ents: self.speed(e, self.root)))
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        b3 = tk.Button(self.root, text='Quit', command=self.root.quit)
        b3.pack(side=tk.LEFT, padx=5, pady=5)

        self.vel = tk.StringVar()
        self.vel.set("Velocity = 0 m/s")
        self.energy = tk.StringVar()
        self.energy.set("Kinetic Energy = 0 Joules")
        tk.Label(self.root, textvariable=self.vel).pack()
        tk.Label(self.root, textvariable=self.energy).pack()

        self.root.mainloop()

    def makeform(self, root, fields):
        entries = {}
        for field in fields:
            print(field)
            row = tk.Frame(root)
            lab = tk.Label(row, width=22, text=field+": ", anchor='w')
            ent = tk.Entry(row)
            if field == "Pressure (psi)":
                ent.insert(0, 100)
            elif field == "Barrel Length (meters)":
                ent.insert(0, 3.2)
            elif field == "Atmospheric Pressure (psi)":
                ent.insert(0, 14.7)
            elif field == "Barrel Cross Section (m^2)":
                ent.insert(0, 0.02)
            elif field == "Reservoir Volume (m^3)":
                ent.insert(0, 0.1)
            elif field == "Projectile Mass (Kg)":
                ent.insert(0, 0.028)
            row.pack(side=tk.TOP,
                     fill=tk.X,
                     padx=5,
                     pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT,
                     expand=tk.YES,
                     fill=tk.X)
            entries[field] = ent
        return entries

    def speed(self, entries, root):
        pressure =6894.76 * float(entries["Pressure (psi)"].get())  # pascal
        barrel_length = float(entries["Barrel Length (meters)"].get())  # meters
        atmospheric_pressure = 6894.76 * float(entries["Atmospheric Pressure (psi)"].get())
        cross_section_area = float(entries["Barrel Cross Section (m^2)"].get())  # meters squared
        gamma = 7 / 5  # 7/5 for adiabatic, 2 for isothermal
        friction = 0
        reservoir = float(entries["Reservoir Volume (m^3)"].get())  # v naught
        mass = float(entries["Projectile Mass (Kg)"].get())

        print(pressure, barrel_length, atmospheric_pressure, cross_section_area, reservoir, mass)

        one = (2 / mass)
        two = (pressure * reservoir / (gamma - 1))
        three = (1 - (reservoir / (cross_section_area * barrel_length + reservoir)) ** (gamma - 1))
        four = cross_section_area * barrel_length * atmospheric_pressure

        velocity = ((one * (two * (three))) - four)
        velocity **= .5


        velocity = ((one * (two * (three))) - four)
        velocity **= .5
        energy = .5 * mass * velocity ** 2
        final_velocity = velocity
        stringg = "Projectile Velocity =" + str(velocity) + " m/s"
        energystring = "Kinetic Energy = " + str(energy) + " Joules"
        self.vel.set(stringg)
        self.energy.set(energystring)
        print(velocity)
        return velocity


if __name__ == '__main__':
    meth = math()



# print(velocity, "meters per second")
#
# print("kinetic energy =", .5 * (velocity ** 2) * mass, "joules")
#
# print("for reference, the energy of a .45 caliber bullet is 600j and a 50 cal is 18,000")