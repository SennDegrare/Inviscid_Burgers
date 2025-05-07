# Leap-frog Centered in Space (Four Point)
def u_LFCS4(N, L, t):
    x = np.linspace(-L, L, N, endpoint=False)
    dx = x[1]-x[0]
    u = u_in(x) #Initial condition
    dt = 0.3*dx/np.max(u) # mu = 0.3 is the Courant factor
    tsteps = int(t/dt)
    
    u_0 = np.copy(u)
    u_1 = np.copy(u)
    for j in range(len(x)):
        u_1[j] = u[j]-u[j]*(4/3)*(u[(j+1)%N] - u[j-1])*dt/(2*dx)+u[j]*(1/3)*(u[(j+2)%N] - u[j-2])*dt/(4*dx)
    u_0[:] = u[:]
    u[:] = u_1[:]
    
    # Now that we have the first two iterations, we can begin the leapfrog
    tsteps = int(t//dt)
    for i in range(1,tsteps):
            for j in range(len(x)):
                u_1[j] = u_0[j] -u[j]*(4/3)*(u[(j+1)%N] - u[j-1])*dt/(2*dx)+u[j]*(1/3)*(u[(j+2)%N] - u[j-2])*dt/(4*dx)
            u_0[:] = u[:]
            u[:] = u_1[:]
    return x, u