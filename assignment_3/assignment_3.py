import numpy as np
import matplotlib.pyplot as plt


def calc_next_population(n, R, alpha):
    return n * R * np.exp(-alpha * n)



# simulation
n_timesteps = 301
alpha = 0.01
R = 2
R_index = [50, 100, 135]
n_t = np.zeros(n_timesteps)
n_t_0 = 900
n_t[0] = n_t_0


fig1 = plt.figure()
ax_bif = fig1.add_subplot(111)
ax_bif.set_xlabel('Number of offspring per individual, R')
ax_bif.set_ylabel('Steady state population, N*')
ax_bif.set_xlim([0, (n_timesteps - 1) * 0.1])
ax_bif.grid()
fig2 = plt.figure()
ax_time = fig2.add_subplot(111)
ax_time.set_xlabel('Simulation steps')
ax_time.set_ylabel('Population size, N')
ax_time.grid()
ax_time.set_xlim([0, 30])

for R in range(n_timesteps):
    print(R)
    for i in range(n_timesteps - 1):

        n_t[i + 1] = calc_next_population(n_t[i], R * 0.1, alpha)
    ax_bif.plot([R * 0.1] * 100, n_t[-100:], '.', markersize=0.2, color='blue')

for R in R_index:
    for i in range(n_timesteps - 1):
        n_t[i + 1] = calc_next_population(n_t[i], R * 0.1, alpha)
        n_star1 = n_t[-1:]
        n_star2 = n_t[-2:]
        n_star4 = n_t[-4:]
    ax_time.plot(n_t)

plt.subplots_adjust(hspace=0.5)

plt.show()
