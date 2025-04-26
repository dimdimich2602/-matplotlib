import numpy as np
import matplotlib.pyplot as plt

num_groups = 5
points_per_group = 10
central_points = np.array([[0, 0], [5, 5], [-5, 5], [5, -5], [-5, -5]])

np.random.seed(0)
deviations_x = np.random.uniform(-1, 1, (num_groups, points_per_group))
deviations_y = np.random.uniform(-1, 1, (num_groups, points_per_group))

groups = []
for i in range(num_groups):
    group = central_points[i] + np.vstack((deviations_x[i], deviations_y[i])).T
    groups.append(group)

mean_points = []
max_deviations = []

for group in groups:
    mean_point = np.mean(group, axis=0)
    max_deviation = np.max(np.abs(group - mean_point), axis=0)
    mean_points.append(mean_point)
    max_deviations.append(max_deviation)

mean_points = np.array(mean_points)
max_deviations = np.array(max_deviations)

plt.figure(figsize=(10, 6))

colors = ['r', 'g', 'b', 'c', 'm']
for i, group in enumerate(groups):
    plt.scatter(group[:, 0], group[:, 1], color=colors[i], label=f'Группа {i + 1}')
    plt.errorbar(mean_points[i, 0], mean_points[i, 1],
                 xerr=max_deviations[i, 0], yerr=max_deviations[i, 1],
                 fmt='o', color='black', capsize=5)

plt.title('График с учётом погрешностей')
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color='grey', lw=0.5, ls='--')
plt.axvline(0, color='grey', lw=0.5, ls='--')
plt.legend()
plt.grid()
plt.axis('equal')

plt.show()