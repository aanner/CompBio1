

def calc_next_population_2(n, R, alpha):
    n = n * R * np.exp(-alpha * n)
    return n * R * np.exp(-alpha * n)


def calc_next_population_3(n, R, alpha):
    n = n * R * np.exp(-alpha * n)
    n = n * R * np.exp(-alpha * n)
    return n * R * np.exp(-alpha * n)


def calc_next_population_4(n, R, alpha):
    n = n * R * np.exp(-alpha * n)
    n = n * R * np.exp(-alpha * n)
    n = n * R * np.exp(-alpha * n)
    return n * R * np.exp(-alpha * n)


def calc_next_population_5(n, R, alpha):
    n = n * R * np.exp(-alpha * n)
    n = n * R * np.exp(-alpha * n)
    n = n * R * np.exp(-alpha * n)
    return n * R * np.exp(-alpha * n)


# Embedded delay map
n = np.linspace(1, n_t_0, 10000)
fig_embedd_1 = plt.figure()

ax_embedd_1 = fig_embedd_1.add_subplot(111)
ax_embedd_1.plot(n, calc_next_population(n, R_index[0], alpha), label='$\eta_{t + 1}$')
ax_embedd_1.plot(n, calc_next_population(n, R_index[1], alpha), label='$\eta_{t + 2}$')
ax_embedd_1.plot(n, calc_next_population(n, R_index[2], alpha), label='$\eta_{t + 3}$')
ax_embedd_1.plot(n, n)

ax_embedd_1.legend()

fig_embedd_2 = plt.figure()
ax_embedd_2 = fig_embedd_2.add_subplot(111)
ax_embedd_2.plot(n, calc_next_population_2(n, R_index[0], alpha))
ax_embedd_2.plot(n, calc_next_population_2(n, R_index[1], alpha))
ax_embedd_2.plot(n, calc_next_population_2(n, R_index[2], alpha))

ax_embedd_2.plot(n, n)

fig_embedd_3 = plt.figure()
ax_embedd_3 = fig_embedd_3.add_subplot(111)
ax_embedd_3.semilogx(n, calc_next_population_4(n, R_index[0], alpha))
ax_embedd_3.semilogx(n, calc_next_population_4(n, R_index[1], alpha))
ax_embedd_3.semilogx(n, calc_next_population_4(n, R_index[2], alpha))

ax_embedd_3.semilogx(n, n)
