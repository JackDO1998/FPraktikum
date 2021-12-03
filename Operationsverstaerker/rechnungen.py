# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 22:36:07 2021
@author: janga
IN DIESEM DOKUMENT AUSWERTUNG ZU AUFGABE a UND b!!!
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const
from scipy.optimize import curve_fit
#from uncertainties import ufloat
X=[0]

#Daten einlesen
fI    = np.loadtxt('daten/ersteschaltung.dat', usecols=[0], dtype=float)
UessI = np.loadtxt('daten/ersteschaltung.dat', usecols=[1], dtype=float)
UassI = np.loadtxt('daten/ersteschaltung.dat', usecols=[2], dtype=float)

fII    = np.loadtxt('daten/ersteschaltungII.dat', usecols=[0], dtype=float)
UessII = np.loadtxt('daten/ersteschaltungII.dat', usecols=[1], dtype=float)
UassII = np.loadtxt('daten/ersteschaltungII.dat', usecols=[2], dtype=float)

#Verstärkungen berechnen
VerstaerkungI = UassI/UessI
VerstaerkungII = UassII/UessII

#Plateau
a=7
b=9
plateauI=X*a
fIplateau=X*a
plateauII=X*b
fIIplateau=X*b
i=0
while i < len(plateauI):
    plateauI[i]=VerstaerkungI[i]
    fIplateau[i]=fI[i]
    i=i+1

j=0
while j < len(plateauII):
    plateauII[j]=VerstaerkungII[j]
    fIIplateau[j]=fII[j]
    j=j+1
    
#Abfall
a=6
b=8
k=a+1
abfallI=X*(len(VerstaerkungI)-k)
fIabfall=X*(len(VerstaerkungI)-k)
while k <= (len(abfallI)+a):
    abfallI[k-(a+1)]=VerstaerkungI[k]
    fIabfall[k-(a+1)]=fI[k]
    k=k+1

l=b+1
abfallII=X*(len(VerstaerkungI)-l)
fIIabfall=X*(len(VerstaerkungI)-l)
while l <= (len(abfallII)+b):
    abfallII[l-(b+1)]=VerstaerkungII[l]
    fIIabfall[l-(b+1)]=fII[l]
    l=l+1
    
print(VerstaerkungI)
print(abfallI)

#Fits
paramsI, covariance_matrixI = np.polyfit(fIplateau, plateauI, deg=1, cov=True)
errorsI = np.sqrt(np.diag(covariance_matrixI))
for name, value, error in zip('cd', paramsI, errorsI):
    print(f'{name} = {value:.3f} ± {error:.3f}')
    
paramsII, covariance_matrixII = np.polyfit(fIIplateau, plateauII, deg=1, cov=True)
errorsII = np.sqrt(np.diag(covariance_matrixII))
for name, value, error in zip('ef', paramsII, errorsII):
    print(f'{name} = {value:.3f} ± {error:.3f}')

def exponentiell(x,g,h):
    return g*x**h
    
paramsIII, covariance_matrixIII = curve_fit(exponentiell, fIabfall , abfallI, p0=(32000,1))
uncertaintiesIII = np.sqrt(np.diag(covariance_matrixIII))
for name, value, uncertainty in zip('gh', paramsIII, uncertaintiesIII): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')
    
paramsIV, covariance_matrixIV = curve_fit(exponentiell, fIIabfall , abfallII, p0=(32000,1))
uncertaintiesIV = np.sqrt(np.diag(covariance_matrixIV))
for name, value, uncertainty in zip('gh', paramsIV, uncertaintiesIV): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')
    
plotI = np.linspace(fIplateau[0], fIplateau[len(fIplateau)-1])
plotII = np.linspace(fIIplateau[0], fIIplateau[len(fIIplateau)-1])
plotIII = np.linspace(fIabfall[0], fIabfall[len(fIabfall)-1])
plotIV = np.linspace(fIIabfall[0], fIIabfall[len(fIIabfall)-1])

#Plot erstellen
plt.plot(plotI, paramsI[0] * plotI + paramsI[1],'k-', label='Lineare Regression')
plt.plot(plotII, paramsII[0] * plotII + paramsII[1],'k-')
plt.plot(plotIII,exponentiell(plotIII,*paramsIII), 'b-',label=r'$af^b$')
plt.plot(plotIV,exponentiell(plotIV,*paramsIV),'b-')
plt.plot(fI,VerstaerkungI,'ro',label=r'$R_1/R_2=1/100$')
plt.plot(fII,VerstaerkungII,'go',label=r'$R_1/R_2=1/10$')
plt.xscale("log")
plt.yscale("log")
plt.title("Verstärkung in abhängigkeit der Frequenz")
plt.xlabel(r'Frequenz $f$ / Hz')
plt.ylabel(r'Verstärkungsfaktor $x$')
plt.legend(loc='best')
plt.savefig('content/grafiken/verstaerkung.pdf')
plt.show()

#Daten zur Phasenverschiebung einlesen
taI = np.loadtxt('daten/ersteschaltung.dat', usecols=[3], dtype=float)
teI = np.loadtxt('daten/ersteschaltung.dat', usecols=[4], dtype=float)
taII = np.loadtxt('daten/ersteschaltungII.dat', usecols=[3], dtype=float)
teII = np.loadtxt('daten/ersteschaltungII.dat', usecols=[4], dtype=float)


# delta t berechnen
dtI=teI-taI
dtII=teII-taII


# delta phi (in Einheiten von pi) berechen
o=0
dphiI=X*len(dtI)
while o <len(dtI):
    dphiI[o]=2*fI[o]*dtI[o]/1000
    o=o+1

p=0
dphiII=X*len(dtII)
while p < len(dtII):
    dphiII[p]=2*fII[p]*dtII[p]/1000
    p=p+1
    

plt.plot(fI,dphiI,'ro',label=r'$R_1/R_2=1/100$')
plt.plot(fII,dphiII,'go',label=r'$R_1/R_2=1/10$')
plt.plot(fI,dphiI,'r-')
plt.plot(fII,dphiII,'g-')
plt.title('Phasenverschiebung')
plt.xlabel(r'Frequenz $f$ / Hz')
plt.ylabel(r'Phasenverschiebungswinkel $\phi$ / $\pi$')
plt.legend(loc='best')
plt.savefig('content/grafiken/phasenverschiebung.pdf')
plt.show()








