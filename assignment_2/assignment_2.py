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
    colors = ['red', 'green', 'orange', 'blue']
    N_inits_len = len(N_inits)

    N_vec = np.zeros((timesteps, N_inits_len))
    N_vec_pert = np.zeros((timesteps, N_inits_len))
    x = np.linspace(0, timesteps, timesteps)

    fig_growth = plt.figure()
    ax_growth = fig_growth.add_subplot(111)

    fig_pert = plt.figure()
    ax_pert = fig_pert.add_subplot(111)
    for ind, N in enumerate(N_inits):
        N_vec[0] = N
        N_vec_pert[0] = N
        for k in range(1, timesteps):
            N_vec[k, ind] = N_new(N_vec[k - 1, ind])
            N_vec_pert[k, ind] = N * (1 + r)**k
        ax_growth.loglog(x, N_vec[:, ind], color=colors[ind])

        ax_pert.plot(x[:20], N_vec[:20, ind], color=colors[ind],
                     label='Percentage difference: ' + str(round(N_vec_pert[20, ind] / N_vec[20, ind] * 10) / 10))
        ax_pert.plot(x[:20], N_vec_pert[:20, ind], color=colors[ind])

    ax_growth.set_xlim([0, x[-1]])
    ax_growth.set_title('Population growth for different initial populations')
    ax_growth.set_xlabel('Simulation steps')
    ax_growth.set_ylabel('Population, N')
    ax_growth.minorticks_on()
    ax_growth.grid(True, which='both')

    ax_pert.set_xlim([0, 19])
    ax_pert.set_title('Simulated perturbation versus actual population growth')
    ax_pert.set_xlabel('Simulation steps')
    ax_pert.set_ylabel('Population, N')
    ax_pert.grid()
    ax_pert.legend()
    plt.show()


def N_new(N):
    global r
    global b
    global K
    return (r + 1) * N / (1 + (N / K)**(b))


main()
