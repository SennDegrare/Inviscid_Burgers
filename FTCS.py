# Forward in Time, Centered in Space (FTCS)
def u_FTCS(N, L, t):
    x = np.linspace(-L, L, N, endpoint=False)
    dx = x[1]-x[0]
    u0 = u_in(x) #u_in is the initial condition
    dt = 0.3*dx/np.max(u0) # mu = 0.3 is the Courant factor
    tsteps = int(t/dt)

    for _ in range(tsteps):
        u_temp = np.copy(u0)
        for j in range(len(x)):
            u_temp[j] = u0[j] - (dt/(2*dx)) * u0[j] * (u0[(j+1)%N] - u0[j-1])
        u0[:] = u_temp[:]
    return x, u0