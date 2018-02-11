import numpy as np
import matplotlib.pyplot as plt


def main():
    global timesteps
    global r
    global A
    global K
    global N_0
    global dt
    ''' Simulation parameters '''
    timesteps = 2000
    r = 0.1
    A = 20
    K = 100
    N_0 = 50
    dt = 0.2
    T_delay_vec = np.linspace(0.1, 5, 5 / 0.1)
    print(T_delay_vec)
    ''' Plotting vaeiables '''
    plot_indices = [5, 33, 45]
    fig = plt.figure()
    fig.tight_layout()

    ax_behaviour = fig.add_subplot(211)
    ax_behaviour.set_title('Delay embedding for population')
    ax_behaviour.set_xlabel('N(t)')
    ax_behaviour.set_ylabel('N(t + dt)')
    ax_behaviour.grid()
    # ax_behaviour.legend({'Exponential decay', 'Damped oscillations', })
    ax_time_evolution = fig.add_subplot(212)
    ax_time_evolution.set_title('Time evolution for population')
    ax_time_evolution.set_xlabel('Simulation steps')
    ax_time_evolution.set_ylabel('Population')
    ax_time_evolution.set_xlim([0, timesteps])
    ax_time_evolution.grid()

    # ax_behaviour.legend({'Exponential decay', 'Damped oscillatio
    ''' Finding equalibrium value, knowing that 0.1 yiels no oscillations '''

    T_delay = 0.1
    n_delay = int(np.ceil(T_delay / dt))
    N = np.zeros(timesteps + n_delay)
    simulate_population(N, n_delay)
    N_inf = N[-1]

    ''' Simulating different time delays '''
    is_oscillating = False
    counter = 0
    for T_delay in T_delay_vec:
        n_delay = int(np.ceil(T_delay / dt))
        T_delay = n_delay * dt
        N = np.zeros(timesteps + n_delay)
        simulate_population(N, n_delay)

        if N[-1] > N_inf + 0.5 and is_oscillating == False:

            T_H = T_delay
            ax_behaviour.plot(N[2 * n_delay:], N[n_delay:-n_delay],
                              label='T_H = ' + str(T_delay))
            ax_time_evolution.plot(N[n_delay:], label='T_H= ' + str(T_delay))
            is_oscillating = True
            print('Oscillations at T = ' + str(T_H))

        if counter in plot_indices:

            ax_behaviour.plot(N[2 * n_delay:], N[n_delay:-n_delay],
                              label='T = ' + str(np.round(10 * T_delay) / 10))
            ax_time_evolution.plot(N[n_delay:], label='T = ' + str(T_delay))
        counter += 1
    plt.subplots_adjust(hspace=0.5)
    ax_behaviour.legend()
    plt.show()


def simulate_population(N, n_delay):
    global timesteps
    global r
    global A
    global K
    global N_0
    global dt
    for i in range(n_delay):
        N[i] = N_0
    for i in range(n_delay, n_delay + timesteps):
        N[i] = N_t_plus_h(N, i - 1, n_delay)


def N_t_plus_h(N, n, n_delay):
    global r
    global A
    global K
    global dt
    N_t_plus_h = N[n] + dt * (r * N[n] * (1 - N[n - n_delay] / K) * (N[n] / A - 1))
    return N_t_plus_h


main()
