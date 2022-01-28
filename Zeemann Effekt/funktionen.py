# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:18:55 2022

@author: janga
"""
import numpy as np
from PIL import Image
from scipy.signal import find_peaks
import scipy.constants as const
import matplotlib.pyplot as plt
import os

def zuschneiden(dateipfad,speicherpfad):
    img = Image.open(dateipfad)
    width, height = img.size
    zugeschnitten=img.crop((0,height/2,width,height/2+1))
    imgGray = zugeschnitten.convert('L')
    imgGray.save(speicherpfad)
    pix=imgGray.load()
    Helligkeitswerte=[]
    a=0
    while a < width:
        Helligkeitswerte.append(pix[a,0])
        a=a+1
    return Helligkeitswerte


def peakfinder(Helligkeitswerte,mindestwert,speicherpfad):
   peaks, _ = find_peaks(Helligkeitswerte, height=mindestwert)
   txt='.txt'
   Peaks='peaks'
   Helligkeit='helligkeit'
   np.savetxt((speicherpfad+Peaks+txt), peaks,fmt='%d')
   np.savetxt((speicherpfad+Helligkeit+txt), Helligkeitswerte,fmt='%d')

def selektion(peaks,helligkeitswerte):
    a=0
    returnarray=[]
    while a<(len(peaks)-1):
        if peaks[a]<(peaks[a+1]-5):
            if helligkeitswerte[peaks[a]] > helligkeitswerte[peaks[a+1]]:
                returnarray.append(peaks[a])
                a=a+1
            elif helligkeitswerte[peaks[a]] < helligkeitswerte[peaks[a+1]]:
                returnarray.append(peaks[a+1])
                a=a+1
            elif helligkeitswerte[peaks[a]] == helligkeitswerte[peaks[a+1]]:
                returnarray.append(int(round((peaks[a]+peaks[a+1])/2,0)))
                a=a+1
        else:
            returnarray.append(peaks[a])
            a=a+1
    return returnarray

def marker(dateipfad,speicherpfad,position):
    img = Image.open(dateipfad)
    width, height = img.size
    array=np.array(img) 
    
    
   
    y=0
    while y < len(position)-1:
        z=0
        while z < height:
            array[z,position[y]]=(0,247,0)
            z=z+1
        y=y+1
    newimg=Image.fromarray(array)
    newimg.save(speicherpfad)
    
def plotten(dateipfad,speicherpfad,titel,farbe):
    txt='.txt'
    Helligkeit='helligkeit'
    Peaks='peaks'
    Plot='plot.pdf'
    helligkeit=np.loadtxt((dateipfad +Helligkeit+txt),dtype=int)
    #peaks=selektion(np.loadtxt((dateipfad +Peaks+txt),dtype=int), helligkeit)
    peaks=np.loadtxt((dateipfad +Peaks+txt),dtype=int)
  
    x=np.linspace(0,len(helligkeit),len(helligkeit))
    a=0
    y=[]
    while a < len(peaks):
        y.append(helligkeit[peaks[a]])
        a=a+1
    plt.plot(x,helligkeit, farbe)
    plt.plot(peaks,y,'gx')
    plt.grid(color='lightgray',linestyle='-',linewidth=0.5)
    plt.title(titel)
    plt.xlabel('Pixel Nr.')
    plt.ylabel('Helligkeit')
    plt.savefig(speicherpfad+Plot)
    plt.show()
    
def pixelzaehler1(dateipfad):
    a=0
    returnarray=[]
    txt='.txt'
    Peaks='peaks'
    peaks=np.loadtxt((dateipfad +Peaks+txt),dtype=int)
    while a<len(peaks)-1:
        returnarray.append(peaks[a+1]-peaks[a])
        a=a+1
    return returnarray
    
def pixelzaehler2(dateipfad):
    a=0
    returnarray=[]
    txt='.txt'
    Peaks='peaks'
    peaks=np.loadtxt((dateipfad +Peaks+txt),dtype=int)
    while a<len(peaks)-1:
        returnarray.append(peaks[a+1]-peaks[a])
        a=a+2
    
    return returnarray
    
def wellenlaengenverschiebung(DELTAs,deltas,deltalam):
    if len(DELTAs)==len(deltas):
        a=0
        returnarray1=[]
        while a < len(DELTAs):
            returnarray1.append(round(((deltas[a]*deltalam)/2*DELTAs[a]),4))
            a=a+1
        
        mittelwert=round(sum(returnarray1)/len(returnarray1),2)
        mittelwertfehler=round(np.std(returnarray1, ddof=1) / np.sqrt(np.size(returnarray1)),2)
    else:
        print('Die Arrays haben nicht die selbe Länge!!!')
    
    return returnarray1 , mittelwert , mittelwertfehler
def landefaktoren(deltalamda,B,Lambda):
    mu=const.value('Bohr magneton')
    g=(deltalamda*const.h*const.c)/(mu*B*Lambda**2)
    return g
    
def tabellenkopf(speicherpfad,caption,label,dokuentenname):
    tex='.tex'
    if os.path.isfile(speicherpfad+dokuentenname+tex)==True:
        os.remove(speicherpfad+dokuentenname+tex)
    datei2=open(speicherpfad+dokuentenname+tex,'a') # öffne die datei im append modus ...
    datei2.write("\\begin{table}") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\centering") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\caption{"+ caption +"}") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\label{tab:"+label+"}") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\sisetup{table-format=1.2}") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\\begin{tabular}{S[table-format=3.2] S S S [table-format=3.2]}") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\\toprule") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("{Mode Nr.} & {$\Delta S$/px}&{$\delta S$ /px}&{$\delta \lambda$}\\" + "\\") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\midrule") 
    datei2.write("\n")#springe in die nächste zeile
    return (speicherpfad+dokuentenname+tex)
    
def tabellenkoerper(datensatz1,datensatz2,datensatz3,speichern):
    if len(datensatz1)==len(datensatz2) & len(datensatz1)==len(datensatz3):
        anfang='{$$' 
        mitte='$$}&{$$'
        ende='$$}\\'
        ende2='\\'
        datei2=open(speichern,'a')
        a=0
        Nr=np.linspace(0,len(datensatz1),len(datensatz1))
        while a < len(datensatz1):
            datei2=open(speichern,'a')
            tuple1=anfang+str(int(round(Nr[a],0))) +mitte+str(datensatz1[a]) + mitte + str(datensatz2[a]) + mitte + str(datensatz3[a]) + ende +ende2
            datei2.write(str(tuple1)) 
            datei2.write("\n")#springe in die nächste zeile
            datei2.close() # schließe die datei
            a=a+1
        
    else:
        print('Die Datensätze sind nicht gleich lang!!!')

def tabellenfuss(Mittelwert,Mittelwertfehler,speicherpfad):
    anfang='{$$' 
    mitte='$$}&{$$'
    ende='$$}\\'
    ende2='\\'
    durchschnitt='\diameter'
    pm='\pm'
    tuple1=anfang+ durchschnitt +mitte+mitte + mitte + str(Mittelwert) + pm +str(Mittelwertfehler)+ ende +ende2
    datei2=open(speicherpfad,'a')
    datei2.write("\\midrule") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write(str(tuple1))
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\\bottomrule") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\\end{tabular}") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\\end{table}") 
    datei2.write("\n")#springe in die nächste zeile