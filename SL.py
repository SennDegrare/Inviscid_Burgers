# Semi Lagrangian (First order)
# Interpolation helper with periodic boundary
def interpol(x, u):
    x_p = np.concatenate((x, x + 2.0)) #Size of interval is 2
    u_p = np.concatenate((u, u))
    return interp1d(x_p, u_p, kind='linear', fill_value='extrapolate') #Linear interpolation under PBC

def semi_lag(N, L,  T):
    x = np.linspace(-L, L, N, endpoint=False)
    dx = x[1]-x[0]
    u0 = u_in(x) #Initial condition
    dt = 0.3*dx/np.max(u0) # mu = 0.3 is the Courant factor
    tsteps = int(t/dt)
    
    u = u0.copy()

    for _ in range(tsteps):
        u_i = interpol(x, u)
        x_d = (x - dt * u) % 2.0 #The departure point
        u = u_i(x_d)

    return x, u