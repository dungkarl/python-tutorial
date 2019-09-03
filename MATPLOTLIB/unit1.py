"""
    Creating and Customizing First Plots
"""

import matplotlib.pyplot as plt
plt.style.use('ggplot')


ages = [25,26, 27, 28, 29, 30, 31, 32, 33]
salaries = [3800, 4001, 4114, 4309, 4442,4580,4651,4700, 4740]
py_salaries = [3910, 4301, 4414, 4479, 4562,4680,4751,4800, 4831]
javascript_salaries = [3765, 3951, 4114, 4309, 4442,4580,4651,4700, 4740]


# plot line
plt.plot(ages, salaries, color='k',linestyle='--', label='All Devs')
plt.plot(ages, py_salaries, 'b', label='Python')

#plt.scatter(ages, salaries)
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary by Age')
#plt.legend(['All Devs', 'Python'])
plt.legend()
plt.show()