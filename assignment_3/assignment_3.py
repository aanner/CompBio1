import numpy as np
import matplotlib.pyplot as plt


def calc_next_population(n, R, alpha):
    return n * R * np.exp(-alpha * n)


n_timesteps = 301
alpha = 0.01
R = 2
n_t = np.zeros(n_timesteps)
n_t_0 = 900
n_t[0] = n_t_0

fig = plt.figure()
ax_bif = fig.add_subplot(211)
ax_time = fig.add_subplot(212)
for R in range(300):
    print(R)
    for i in range(n_timesteps - 1):

        n_t[i + 1] = calc_next_population(n_t[i], R * 0.1, alpha)
    ax_bif.plot([R] * 100, n_t[-100:], '.', markersize=0.2, color='blue')

for R in [50, 100, 135]:
    for i in range(n_timesteps - 1):
        n_t[i + 1] = calc_next_population(n_t[i], R * 0.1, alpha)
    ax_time.plot(n_t)

ax_time.set_xlim([0, 50])
plt.show()
