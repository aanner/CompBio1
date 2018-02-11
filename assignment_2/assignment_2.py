import numpy as np
import matplotlib.pyplot as plt


def main():
    global K
    global r
    global b

    ''' Simulation parameters '''
    K = 1000
    r = 0.1
    b = 1
    timesteps = 100
    N_inits = [1, 2, 3, 10]
    N_inits_len = len(N_inits)

    N_vec=np.zeros((timesteps, N_inits_len))
    x=np.linspace(1,timesteps,timesteps)
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    for ind, N in enumerate(N_inits):
        N_vec[0]=N
        for k in range(1,timesteps):
            N_vec[k,ind]=N_new(N_vec[k-1,ind])
        ax1.plot(x, N_vec[:,ind])
        ax2.plot(N_vec[:-1, ind], N_vec[1:, ind])

    plt.show()

def N_new(N):
    global r
    global b
    global K
    return (r+1)*N/(1+(N/K)**(b))

main()
