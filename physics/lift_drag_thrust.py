def lift(rho, v, S, CL):
    return 0.5 * rho * v**2 * S * CL

def drag(rho, v, S, CD):
    return 0.5 * rho * v**2 * S * CD

def thrust(rho, v, S, CT):
    return 0.5 * rho * v**2 * S * CT


# Example usage:
rho = 1.225  # Air density
V = 12       # m/s
Cl = 1.5
Cd = 1.0
A = 0.4      # m^2
lift_force = lift(rho, V, Cl, A)
drag_force = drag(rho, V, Cd, A)
thrust_force = thrust(rho, V, Cl, A)

print("Lift:", lift_force)
print("Drag:", drag_force)
print("Thrust:", thrust_force)