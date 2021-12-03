# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 23:05:47 2021

@author: janga
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const
from scipy.optimize import curve_fit
#from uncertainties import ufloat
X=[0]
#Der Umkehrintegrator
#Daten einlesen
fI    = np.loadtxt('daten/umkehrintegrator.dat', usecols=[0], dtype=float)
UessI = np.loadtxt('daten/umkehrintegrator.dat', usecols=[1], dtype=float)
UassI = np.loadtxt('daten/umkehrintegrator.dat', usecols=[2], dtype=float)

fII    = np.loadtxt('daten/invertierenderdifferenzierer.dat', usecols=[0], dtype=float)
UessII = np.loadtxt('daten/invertierenderdifferenzierer.dat', usecols=[1], dtype=float)
UassII = np.loadtxt('daten/invertierenderdifferenzierer.dat', usecols=[2], dtype=float)
#Verstärkungsaktor berechen
xI=UassI/UessI 
xII=UassII/UessII

#Fit
startpunkt1=0
startpunkt2=0
anzahl1=4
anzahl2=11
fIred=X*anzahl1
xIred=X*anzahl1
fIIred=X*anzahl2
xIIred=X*anzahl2
a=0
while a < len(fIred):
    fIred[a]=fI[a+startpunkt1]
    xIred[a]=xI[a+startpunkt1]
    a=a+1

b=0
while b < len(fIIred):
    fIIred[b]=fII[b+startpunkt2]
    xIIred[b]=xII[b+startpunkt2]
    b=b+1
    
    
def exponentiell(x,g,h):
    return g*x**h
    
paramsIII, covariance_matrixIII = curve_fit(exponentiell, fIred , xIred)
uncertaintiesIII = np.sqrt(np.diag(covariance_matrixIII))
for name, value, uncertainty in zip('gh', paramsIII, uncertaintiesIII): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')
    
paramsIV, covariance_matrixIV = curve_fit(exponentiell, fIIred , xIIred)
uncertaintiesIV = np.sqrt(np.diag(covariance_matrixIV))
for name, value, uncertainty in zip('gh', paramsIV, uncertaintiesIV): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

plotIII = np.linspace(fIred[0], fIred[len(fIred)-1])
plotIV = np.linspace(fIIred[0], fIIred[len(fIIred)-1])


#Plot zum Umkehrintegrator
plt.plot(plotIII,exponentiell(plotIII,*paramsIII), 'b-',label=r'$af^b$')
plt.plot(fI,xI,'ro',label='Messwerte')
plt.xscale("log")
plt.yscale("log")
plt.xlabel(r'Frequenz $f$ / Hz')
plt.ylabel(r'Verstärkungsfaktor $x$')
plt.title('Der Umkehrintegrator')
plt.legend(loc='best')
plt.savefig('content/grafiken/umkehrintegrator.pdf')
plt.show()

#Plot zum invertierenden Differenzierer
plt.plot(plotIV,exponentiell(plotIV,*paramsIV), 'b-',label=r'$af^b$')
plt.plot(fII,xII,'ro',label='Messwerte')
plt.xscale("log")
plt.yscale("log")
plt.xlabel(r'Frequenz $f$ / Hz')
plt.ylabel(r'Verstärkungsfaktor $x$')
plt.title('Der invertierende Differenzierer')
plt.legend(loc='best')
plt.savefig('content/grafiken/invdifferenzierer.pdf')
plt.show()