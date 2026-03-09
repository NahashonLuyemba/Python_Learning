import numpy as np
from scipy.signal import find_peaks

k1 = 1.28
k2 = 2.4e6
k3 = 33.6
k4 = 3.0e3
k5 = 1.0

A = 0.06
B = 0.02

X = 1e-6
Y = 1e-7
Z = 1e-6

dt = 0.001
t_final = 500
steps = int(t_final/dt)

t = np.zeros(steps)
X_vals = np.zeros(steps)

def derivatives(X,Y,Z):
    dX = k1*A*Y - k2*X*Y + k3*A*X - 2*k4*(X**2)
    dY = -k1*A*Y - k2*X*Y + k5*B*Z
    dZ = k3*A*X - k5*B*Z
    return dX,dY,dZ

for i in range(steps):

    t[i] = i*dt
    X_vals[i] = X

    k1x,k1y,k1z = derivatives(X,Y,Z)

    k2x,k2y,k2z = derivatives(
        X + 0.5*dt*k1x,
        Y + 0.5*dt*k1y,
        Z + 0.5*dt*k1z
    )

    k3x,k3y,k3z = derivatives(
        X + 0.5*dt*k2x,
        Y + 0.5*dt*k2y,
        Z + 0.5*dt*k2z
    )

    k4x,k4y,k4z = derivatives(
        X + dt*k3x,
        Y + dt*k3y,
        Z + dt*k3z
    )

    X += dt*(k1x + 2*k2x + 2*k3x + k4x)/6
    Y += dt*(k1y + 2*k2y + 2*k3y + k4y)/6
    Z += dt*(k1z + 2*k2z + 2*k3z + k4z)/6


peaks,_ = find_peaks(X_vals)
peak_times = t[peaks]
periods = np.diff(peak_times[:10])
avg_period = np.mean(periods)

print("Average oscillation period:", avg_period)