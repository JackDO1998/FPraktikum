# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 12:04:43 2022

@author: janga
"""
import funktionen



JPG='.JPG'
tex='.tex'
rohdateipfad='Daten/Bilder2/Gimb2/'
speicherpfad='Daten/Bilder2/grayscale2/'
datei1='blau mit magnet 0 gimb'
datei2='blau mit magnet 90 gimb'
datei3='blau ohne magnet 0 gimb'
datei4='blau ohne magnet 90 gimb'
datei5='rot mit magnet 0 gimb'
datei6='rot mit magnet 90 gimb'
datei7='rot ohne magnet 0 gimb'
datei8='rot ohne magnet 90 gimb'



#Helligkeitswerte=funktionen.zuschneiden((rohdateipfad + datei1 + JPG),(speicherpfad + datei1 + JPG))
#funktionen.peakfinder(Helligkeitswerte,185,(speicherpfad + datei1))

#Helligkeitswerte=funktionen.zuschneiden((rohdateipfad + datei2 + JPG),(speicherpfad + datei2 + JPG))
#funktionen.peakfinder(Helligkeitswerte,175,(speicherpfad + datei2))

#Helligkeitswerte=funktionen.zuschneiden((rohdateipfad + datei3 + JPG),(speicherpfad + datei3 + JPG))
#funktionen.peakfinder(Helligkeitswerte,180,(speicherpfad + datei3))

#Helligkeitswerte=funktionen.zuschneiden((rohdateipfad + datei4 + JPG),(speicherpfad + datei4 + JPG))
#funktionen.peakfinder(Helligkeitswerte,120,(speicherpfad + datei4))

#Helligkeitswerte=funktionen.zuschneiden((rohdateipfad + datei5 + JPG),(speicherpfad + datei5 + JPG))
#funktionen.peakfinder(Helligkeitswerte,7,(speicherpfad + datei5))

#Helligkeitswerte=funktionen.zuschneiden((rohdateipfad + datei6 + JPG),(speicherpfad + datei6 + JPG))
#funktionen.peakfinder(Helligkeitswerte,15,(speicherpfad + datei6))

Helligkeitswerte=funktionen.zuschneiden((rohdateipfad + datei7 + JPG),(speicherpfad + datei7 + JPG))
funktionen.peakfinder(Helligkeitswerte,10,(speicherpfad + datei7))

#Helligkeitswerte=funktionen.zuschneiden((rohdateipfad + datei8 + JPG),(speicherpfad + datei8 + JPG))
#funktionen.peakfinder(Helligkeitswerte,10,(speicherpfad + datei8))
