#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import date
import math

tablaA = dict()
tablaA[1910]=62
tablaA[1911]=167
tablaA[1912]=12
tablaA[1913]=117
tablaA[1914]=222
tablaA[1915]=67
tablaA[1916]=172
tablaA[1917]=17
tablaA[1918]=122
tablaA[1919]=227
tablaA[1920]=72
tablaA[1921]=177
tablaA[1922]=22
tablaA[1923]=127
tablaA[1924]=232
tablaA[1925]=77
tablaA[1926]=182
tablaA[1927]=27
tablaA[1928]=132
tablaA[1929]=237
tablaA[1930]=82
tablaA[1931]=187
tablaA[1932]=32
tablaA[1933]=137
tablaA[1934]=242
tablaA[1935]=87
tablaA[1936]=192
tablaA[1937]=37
tablaA[1938]=142
tablaA[1939]=247
tablaA[1940]=92
tablaA[1941]=197
tablaA[1942]=42
tablaA[1943]=147
tablaA[1944]=252
tablaA[1945]=97
tablaA[1946]=202
tablaA[1947]=47
tablaA[1948]=152
tablaA[1949]=257
tablaA[1950]=102
tablaA[1951]=207
tablaA[1952]=52
tablaA[1953]=157
tablaA[1954]=2
tablaA[1955]=107
tablaA[1956]=212
tablaA[1957]=57
tablaA[1958]=162
tablaA[1959]=7
tablaA[1960]=112
tablaA[1961]=217
tablaA[1962]=62
tablaA[1963]=167
tablaA[1964]=12
tablaA[1965]=117
tablaA[1966]=222
tablaA[1967]=67
tablaA[1968]=172
tablaA[1969]=17
tablaA[1970]=122
tablaA[1971]=227
tablaA[1972]=72
tablaA[1973]=177
tablaA[1974]=22
tablaA[1975]=127
tablaA[1976]=232
tablaA[1977]=77
tablaA[1978]=182
tablaA[1979]=27
tablaA[1980]=132
tablaA[1981]=237
tablaA[1982]=82
tablaA[1983]=187
tablaA[1984]=32
tablaA[1985]=137
tablaA[1986]=242
tablaA[1987]=87
tablaA[1988]=192
tablaA[1989]=37
tablaA[1990]=142
tablaA[1991]=247
tablaA[1992]=92
tablaA[1993]=197
tablaA[1994]=42
tablaA[1995]=147
tablaA[1996]=252
tablaA[1997]=97
tablaA[1998]=202
tablaA[1999]=47
tablaA[2000]=152
tablaA[2001]=257
tablaA[2002]=102
tablaA[2003]=207
tablaA[2004]=52
tablaA[2005]=157
tablaA[2006]=2
tablaA[2007]=107
tablaA[2008]=212
tablaA[2009]=57
tablaA[2010]=162
tablaA[2011]=7
tablaA[2012]=112
tablaA[2013]=217
tablaA[2014]=62
tablaA[2015]=167
tablaA[2016]=12
tablaA[2017]=117
tablaA[2018]=222
tablaA[2019]=67
tablaA[2020]=172
tablaA[2021]=17
tablaA[2022]=122
tablaA[2023]=227
tablaA[2024]=72
tablaA[2025]=177
tablaA[2026]=22
tablaA[2027]=127
tablaA[2028]=232
tablaA[2029]=77
tablaA[2030]=182

tablaB = dict()
tablaB[1]=0
tablaB[2]=31
tablaB[3]=59
tablaB[4]=90
tablaB[5]=120
tablaB[6]=151
tablaB[7]=181
tablaB[8]=212
tablaB[9]=243
tablaB[10]=13
tablaB[11]=44
tablaB[12]=74

razas = ['Roja', 'Blanca', 'Azul', 'Amarilla']

tonosf = dict()
tonosf[1] = "Magnetica"
tonosf[2] = "Lunar"
tonosf[3] = "Eléctrica"
tonosf[4] = "Auto-Existente"
tonosf[5] = "Entonada"
tonosf[6] = "Rítmica"
tonosf[7] = "Resonante"
tonosf[8] = "Galáctica"
tonosf[9] = "Solar"
tonosf[10] = "Planetaria"
tonosf[11] = "Espectral"
tonosf[12] = "Cristal"
tonosf[13] = "Cósmica"

sellos = [ "Sol",
        "Dragón",
        "Viento",
        "Noche",
        "Semilla",
        "Serpiente",
        "Enlazador de Mundos",
        "Mano",
        "Estrella",
        "Luna",
         "Perro",
         "Mono",
         "Humano",
         "Caminante del Cielo",
         "Mago",
         "Águila",
         "Guerrero",
         "Tierra",
         "Espejo",
         "Tormenta"]

def kin(x):
    valor_ano = tablaA[x.year]
    valor_mes = tablaB[x.month]
    valor = valor_ano + valor_mes + x.day
    if valor>260:
        valor = valor - 260
    return valor

def sello(x):
    return sellos[kin(x)%20]

def raza(x):
    return "%s " % razas[kin(x)%4-1]

def tono(x):
    return "%s " % tonosf[kin(x)%13]

#fecha = date(2012,10,19)
#print "Hoy"
#print "Kin %s" % str(kin(fecha))
#print sello(fecha)
#print tono(fecha)
#print raza(fecha)
