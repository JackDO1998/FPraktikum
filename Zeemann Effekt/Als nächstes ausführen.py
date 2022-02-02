# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 16:25:03 2022

@author: janga
"""

import funktionen

txt='.txt'
rohdateipfad='daten/Bilder2/Gimb2/'
speicherpfad='daten/Bilder2/grayscale2/'
tabellenpfad='content/tabellen/'
datei1='blau mit magnet 0 gimb'
datei2='blau mit magnet 90 gimb'
datei3='blau ohne magnet 0 gimb'
datei4='blau ohne magnet 90 gimb'
datei5='rot mit magnet 0 gimb'
datei6='rot mit magnet 90 gimb'
datei7='rot ohne magnet 0 gimb'
datei8='rot ohne magnet 90 gimb'
name1='Blau | B-Feld: an | phi=0°'
name2='Blau | B-Feld: an | phi=90°'
name3='Blau | B-Feld: aus | phi=0°'
name4='Blau | B-Feld: aus | phi=90°'
name5='Rot | B-Feld: an | phi=0°'
name6='Rot | B-Feld: an | phi=90°'
name7='Rot | B-Feld: aus | phi=0°'
name8='Rot | B-Feld: aus | phi=90°'
b='b-'
r='r-'

funktionen.plotten((speicherpfad+datei1),(speicherpfad+datei1),name1,b)
funktionen.plotten((speicherpfad+datei2),(speicherpfad+datei2),name2,b)
funktionen.plotten((speicherpfad+datei3),(speicherpfad+datei3),name3,b)
funktionen.plotten((speicherpfad+datei4),(speicherpfad+datei4),name4,b)
#funktionen.plotten((speicherpfad+datei5),(speicherpfad+datei5),name5,r)
#funktionen.plotten((speicherpfad+datei6),(speicherpfad+datei6),name6,r)
#funktionen.plotten((speicherpfad+datei7),(speicherpfad+datei7),name7,r)
#funktionen.plotten((speicherpfad+datei8),(speicherpfad+datei8),name8,r)

DeltaSblau=funktionen.pixelzaehler1((speicherpfad+datei3))
DeltaSblau2=funktionen.pixelzaehler1((speicherpfad+datei4))
#DeltaSrot=funktionen.pixelzaehler1((speicherpfad+datei7))

deltaSblau=funktionen.pixelzaehler2((speicherpfad+datei1))
deltaSblau2=funktionen.pixelzaehler2((speicherpfad+datei2))
#deltaSrot=funktionen.pixelzaehler2((speicherpfad+datei5))

deltaLambdaDblau,mittelwertBlau=funktionen.wellenlaengenverschiebung(DeltaSblau, deltaSblau, 0.02695)
deltaLambdaDblau2,mittelwertBlau2=funktionen.wellenlaengenverschiebung(DeltaSblau2, deltaSblau2, 0.02695)
#deltaLambdaDrot,mittelwertRot=funktionen.wellenlaengenverschiebung(DeltaSrot, deltaSrot, 0.04891)

caption1='Wellenlaengenverschiebung der blauen Sigma-Linie.'
caption3='Wellenlaengenverschiebung der blauen Pi-Linie.'
caption2='Wellenlaengenverschiebung der roten Sigma-Linie.'
a=funktionen.tabellenkopf(tabellenpfad,caption1,'tabelleBlau','Tab Blau')
c=funktionen.tabellenkopf(tabellenpfad,caption3,'tabelleBlau2','Tab Blau2')
b=funktionen.tabellenkopf(tabellenpfad,caption2,'tabelleRot','Tab Rot')
funktionen.tabellenkoerper(DeltaSblau,deltaSblau,deltaLambdaDblau,a)
funktionen.tabellenkoerper(DeltaSblau2,deltaSblau2,deltaLambdaDblau2,c)
#funktionen.tabellenkoerper(DeltaSrot,deltaSrot,deltaLambdaDrot,b)
funktionen.tabellenfuss(mittelwertBlau,a)
funktionen.tabellenfuss(mittelwertBlau2,c)
#funktionen.tabellenfuss(mittelwertRot,b)

#grot=funktionen.landefaktoren(mittelwertRot, 0.4521, 0.6488)
gblau1=funktionen.landefaktoren(mittelwertBlau, 0.347, 0.48)
gblau2=funktionen.landefaktoren(mittelwertBlau2, 0.4521, 0.48)
#print('Lande Faktor Rot:',grot)
print('Lande Faktor Blau 1:',gblau1)
print('Lande Faktor Blau 2:',gblau2)
#AbwRot=funktionen.prozentualeAbweichung(1, grot)
AbwBlau1=funktionen.prozentualeAbweichung(1.5, gblau1)
AbwBlau2=funktionen.prozentualeAbweichung(0.5, gblau2)











