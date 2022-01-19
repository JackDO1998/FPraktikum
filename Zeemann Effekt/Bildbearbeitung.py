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




def linienvermessung(dateiname,helligkeit):
    dateityp='.JPG'
    datei=dateiname+dateityp
    pfad1='daten/Bilder2/'
    pfad2='daten/bearbeitet/'
    suchpfad=pfad1+datei
    sl='/'
    speicherpfad=pfad2 + dateiname
    plot='/Helligkeitsplpot.pdf'
    if not os.path.exists(speicherpfad):
        os.makedirs(speicherpfad)
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
    plt.savefig((speicherpfad+plot))
    plt.show()


    a=0
    b=0
    c=0
    
    wert=0
    while a < width:
        if pix[a,0]>helligkeit:
            d=a
            while pix[d,0]>helligkeit:
                b=b+1
                d=d+1
                wert=wert+pix[d,0]
            if b >10:
                print('Linie Nr.:',c,' Breite:',b,'px   Position:',a,'bis:',d,'   Helligkeit: ',wert/b)
                c=c+1
            b=0
            a=d
            wert=0
        a=a+1





linienvermessung(dateiname1,100)
linienvermessung(dateiname2,175)
linienvermessung(dateiname3,150)
linienvermessung(dateiname4,150)
linienvermessung(dateiname5,10)
linienvermessung(dateiname6,10)
linienvermessung(dateiname7,8)
linienvermessung(dateiname8,8)