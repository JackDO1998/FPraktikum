# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:57:16 2022

@author: janga
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const
from scipy.optimize import curve_fit
#from uncertainties import ufloat
X=[0]

#Daten einlesen
I   = np.loadtxt('daten/Hallsonde.dat', usecols=[0], dtype=float)
Broh = np.loadtxt('daten/Hallsonde.dat', usecols=[1], dtype=float)
B=Broh/1000

params, covariance_matrix = np.polyfit(I, B, deg=3, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip('abcd', params, errors):
    print(f'{name} = {value:.5f} ± {error:.5f}')
x_plot = np.linspace(0, 5)

plt.plot(
    x_plot,
    params[0] * x_plot**3 + params[1] * x_plot**2 + params[2] * x_plot + params[3],
    label='Ausgleichskurve')
plt.plot(I,B,'kx',label='Messpunkte')
plt.title(r'Magnetfeld in Abhängigkeit des Spulenstroms')
plt.xlabel(r'Spulenstrom $I$ / A')
plt.ylabel(r'Flussdichte $B$ / T')
plt.legend(loc='best')
plt.savefig('content/grafiken/magnetfeld.pdf')
plt.show()
