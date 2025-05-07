# Lax-Friedrichs
def u_Lax(N,L,t):
    x = np.linspace(-L, L, N, endpoint=False)
    dx = x[1]-x[0]
    u0 = u_in(x) #Initial condition
    dt = 0.3*dx/np.max(u0) # mu = 0.3 is the Courant factor
    tsteps = int(t/dt)
    def f(u):
        return 0.5*u**2
    
    u = u0.copy()
    for _ in range(tsteps):
        u_new = np.zeros_like(u)
        u_new[1:-1] = 0.5 * (u[2:] + u[:-2]) - dt / (2 * dx) * (f(u[2:]) - f(u[:-2]))
        # u_new[0] = 0.5 * (u[1] + u[-1]) - dt / (2 * dx) * (f(u[1]) - f(u[-1]))
        u_new[-1] = u_new[0]  # enforce periodicity
        u = u_new
    return x, u