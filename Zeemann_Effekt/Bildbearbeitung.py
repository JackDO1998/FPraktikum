# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 17:59:50 2022

@author: janga
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
X=[0]

dateiname1='blau mit magnet 0 (2)'
dateiname2='blau mit magnet 90 (2)'
dateiname3='blau ohne magnet 0 (2)'
dateiname4='blau ohne magnet 90 (2)'
dateiname5='rot mit magnet 0 (2)'
dateiname6='rot mit magnet 90 (2)'
dateiname7='rot ohne magnet 0 (2)'
dateiname8='rot ohne magnet 90 (2)'

def listeneintrag(Nummer,Breite,Helligkeit,speichern):
    anfang='{$$' 
    mitte='$$}&{$$'
    ende='$$}\\'
    ende2='\\'
    tuple1=anfang+ str(Nummer) + mitte + str(Breite) + mitte + str(Helligkeit) + ende +ende2
    datei2=open(speichern,'a') # öffne die datei im append modus ...
    datei2.write(str(tuple1)) 
    datei2.write("\n")#springe in die nächste zeile
    datei2.close() # schließe die datei

def linienvermessung(dateiname,helligkeit):
    anfang='{$$' 
    mitte='$$}&{$$'
    ende='$$}\\'
    ende2='\\'
    durchschnitt='\diameter'
    pm='\pm'
    dateityp='.JPG'
    datei=dateiname+dateityp
    pfad1='daten/Bilder2/'
    pfad2='daten/bearbeitet/'
    suchpfad=pfad1+datei
    sl='/'
    pdf='.pdf'
    speicherpfad=pfad2 + dateiname
    speicherpfadII='content/grafiken'
    plot=sl+dateiname+pdf
    tex='/Daten.tex'
    if not os.path.exists(speicherpfad):
        os.makedirs(speicherpfad)
    if os.path.isfile(speicherpfad+tex)==True:
        os.remove(speicherpfad+tex)
    datei2=open(speicherpfad+tex,'a') # öffne die datei im append modus ...
    datei2.write("\\begin{table}[t]") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\centering") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\caption{Daten aus:"+dateiname+".}") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\label{tab:"+dateiname+"}") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\sisetup{table-format=1.2}") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\\begin{tabular}{S[table-format=3.2] S S S [table-format=3.2]}") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\\toprule") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("{Linie Nr.} & {Breite/[$\si[]{px}$]}&{Helligkeit}\\" + "\\") 
    datei2.write("\n")#springe in die nächste zeile
    datei2.write("\midrule") 
    datei2.write("\n")#springe in die nächste zeile
    
    datei2.close() # schließe die datei
    img = Image.open(suchpfad)
    width, height = img.size
    zugeschnitten=img.crop((0,height/2,width,height/2+1))
    imgGray = zugeschnitten.convert('L')
    imgGray.save((pfad2+dateiname+sl+dateiname+dateityp))
    pix=imgGray.load()

    datensatz=X*width 
    z=0
    while z<width:
        datensatz[z]=pix[z,0]
        z=z+1
        
    xwert=np.linspace(0,width,width)
    plt.plot(xwert,datensatz)
    plt.title('Helligkeitswerte der Pixel',)
    plt.xlabel('Pixelnummer')
    plt.ylabel('Helligkeit')
    plt.savefig((speicherpfadII+plot))
    plt.show()


    a=0
    b=0
    c=0
    Breite=[]
    Helligkeit=[]
    
    wert=0
    while a < width:
        if pix[a,0]>helligkeit:
            d=a
            while pix[d,0]>helligkeit:
                b=b+1
                d=d+1
                wert=wert+pix[d,0]
            if b >10:
                listeneintrag(c,b,round(wert/b,2),speicherpfad+tex)
                Breite.append(b)
                Helligkeit.append(wert/b)
                c=c+1
            b=0
            a=d
            wert=0
        a=a+1
    mittelwertb=round(sum(Breite)/c,2)
    mittelwertfehlerb=round(np.std(Breite, ddof=1) / np.sqrt(np.size(Breite)),2)
    mittelwerth=round(sum(Helligkeit)/c,2)
    mittelwertfehlerh=round(np.std(Helligkeit, ddof=1) / np.sqrt(np.size(Helligkeit)),2)
    tuple1=anfang+ durchschnitt + mitte + str(mittelwertb) + pm +str(mittelwertfehlerb)+ mitte +str(mittelwerth) + pm +str(mittelwertfehlerh)+ ende +ende2
    datei2=open(speicherpfad+tex,'a')
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




linienvermessung(dateiname1,180)
linienvermessung(dateiname2,175)
linienvermessung(dateiname3,150)
linienvermessung(dateiname4,150)
linienvermessung(dateiname5,10)
linienvermessung(dateiname6,10)
linienvermessung(dateiname7,8)
linienvermessung(dateiname8,8)