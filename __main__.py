import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 2nd order differential eq
def func_motion(var, t):
    g =  9.80665

    dxdt = var[1]
    dvdt = -g

    return [dxdt, dvdt]

# 2D visualization
def plot2d(t_list, y_list, t_label, y_label, color, linewidth, label):
    plt.xlabel(t_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.plot(t_list, y_list, color=color, linewidth=linewidth, label=label)

    plt.legend()
    plt.show()

def main():
    t_list = np.linspace(0.0, 10.0, 1000)
    m_init = [100.0, 0.0]
    m_list = odeint(func_motion, m_init, t_list)

    plot2d(t_list, m_list[:, 0], "$t$", "$x(t)$", "m", 3, "$(d^2*x/dt^2) = -g$")
    plot2d(t_list, m_list[:, 1], "$t$", "$v(t)$", "r", 3, "$(d^2*x/dt^2) = -g$")

if __name__ == '__main__':
    main()