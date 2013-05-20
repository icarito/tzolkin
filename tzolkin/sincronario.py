#!/usr/bin/python
# -*- coding: utf-8 -*-

tablaA = dict()
tablaA[1910] = 62
tablaA[1911] = 167
tablaA[1912] = 12
tablaA[1913] = 117
tablaA[1914] = 222
tablaA[1915] = 67
tablaA[1916] = 172
tablaA[1917] = 17
tablaA[1918] = 122
tablaA[1919] = 227
tablaA[1920] = 72
tablaA[1921] = 177
tablaA[1922] = 22
tablaA[1923] = 127
tablaA[1924] = 232
tablaA[1925] = 77
tablaA[1926] = 182
tablaA[1927] = 27
tablaA[1928] = 132
tablaA[1929] = 237
tablaA[1930] = 82
tablaA[1931] = 187
tablaA[1932] = 32
tablaA[1933] = 137
tablaA[1934] = 242
tablaA[1935] = 87
tablaA[1936] = 192
tablaA[1937] = 37
tablaA[1938] = 142
tablaA[1939] = 247
tablaA[1940] = 92
tablaA[1941] = 197
tablaA[1942] = 42
tablaA[1943] = 147
tablaA[1944] = 252
tablaA[1945] = 97
tablaA[1946] = 202
tablaA[1947] = 47
tablaA[1948] = 152
tablaA[1949] = 257
tablaA[1950] = 102
tablaA[1951] = 207
tablaA[1952] = 52
tablaA[1953] = 157
tablaA[1954] = 2
tablaA[1955] = 107
tablaA[1956] = 212
tablaA[1957] = 57
tablaA[1958] = 162
tablaA[1959] = 7
tablaA[1960] = 112
tablaA[1961] = 217
tablaA[1962] = 62
tablaA[1963] = 167
tablaA[1964] = 12
tablaA[1965] = 117
tablaA[1966] = 222
tablaA[1967] = 67
tablaA[1968] = 172
tablaA[1969] = 17
tablaA[1970] = 122
tablaA[1971] = 227
tablaA[1972] = 72
tablaA[1973] = 177
tablaA[1974] = 22
tablaA[1975] = 127
tablaA[1976] = 232
tablaA[1977] = 77
tablaA[1978] = 182
tablaA[1979] = 27
tablaA[1980] = 132
tablaA[1981] = 237
tablaA[1982] = 82
tablaA[1983] = 187
tablaA[1984] = 32
tablaA[1985] = 137
tablaA[1986] = 242
tablaA[1987] = 87
tablaA[1988] = 192
tablaA[1989] = 37
tablaA[1990] = 142
tablaA[1991] = 247
tablaA[1992] = 92
tablaA[1993] = 197
tablaA[1994] = 42
tablaA[1995] = 147
tablaA[1996] = 252
tablaA[1997] = 97
tablaA[1998] = 202
tablaA[1999] = 47
tablaA[2000] = 152
tablaA[2001] = 257
tablaA[2002] = 102
tablaA[2003] = 207
tablaA[2004] = 52
tablaA[2005] = 157
tablaA[2006] = 2
tablaA[2007] = 107
tablaA[2008] = 212
tablaA[2009] = 57
tablaA[2010] = 162
tablaA[2011] = 7
tablaA[2012] = 112
tablaA[2013] = 217
tablaA[2014] = 62
tablaA[2015] = 167
tablaA[2016] = 12
tablaA[2017] = 117
tablaA[2018] = 222
tablaA[2019] = 67
tablaA[2020] = 172
tablaA[2021] = 17
tablaA[2022] = 122
tablaA[2023] = 227
tablaA[2024] = 72
tablaA[2025] = 177
tablaA[2026] = 22
tablaA[2027] = 127
tablaA[2028] = 232
tablaA[2029] = 77
tablaA[2030] = 182

tablaB = dict()
tablaB[1] = 0
tablaB[2] = 31
tablaB[3] = 59
tablaB[4] = 90
tablaB[5] = 120
tablaB[6] = 151
tablaB[7] = 181
tablaB[8] = 212
tablaB[9] = 243
tablaB[10] = 13
tablaB[11] = 44
tablaB[12] = 74

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

sellos = dict()
sellos[1] = "Sol"
sellos[2] = "Dragón"
sellos[3] = "Viento"
sellos[4] = "Noche"
sellos[5] = "Semilla"
sellos[6] = "Serpiente"
sellos[7] = "Enlazador de Mundos"
sellos[8] = "Mano"
sellos[9] = "Estrella"
sellos[10] = "Luna"
sellos[11] = "Perro"
sellos[12] = "Mono"
sellos[13] = "Humano"
sellos[14] = "Caminante del Cielo"
sellos[15] = "Mago"
sellos[16] = "Águila"
sellos[17] = "Guerrero"
sellos[18] = "Tierra"
sellos[19] = "Espejo"
sellos[20] = "Tormenta"

ma = dict()
ma[1] = "Unifico"
ma[2] = "Polarizo"
ma[3] = "Activo"
ma[4] = "Defino"
ma[5] = "Confiero Poder"
ma[6] = "Organizo"
ma[7] = "Canalizo"
ma[8] = "Armonizo"
ma[9] = "Pulso"
ma[10] = "Perfecciono"
ma[11] = "Disuelvo"
ma[12] = "Me dedico"
ma[13] = "Perduro"

mg = dict()
mg[1] = "Magnético"
mg[2] = "Lunar"
mg[3] = "Eléctrico"
mg[4] = "Autoexistente"
mg[5] = "Entonado"
mg[6] = "Rítmico"
mg[7] = "Resonante"
mg[8] = "Galáctico"
mg[9] = "Solar"
mg[10] = "Planetario"
mg[11] = "Espectral"
mg[12] = "Cristal"
mg[13] = "Cósmico"

mh = dict()
mh[1] = "el Propósito"
mh[2] = "el Desafío"
mh[3] = "el Servicio"
mh[4] = "la Forma"
mh[5] = "el Esplendor"
mh[6] = "la Igualdad"
mh[7] = "la Sintonización"
mh[8] = "la Integridad"
mh[9] = "la Intención"
mh[10] = "la Manifestación"
mh[11] = "la Liberación"
mh[12] = "la Cooperación"
mh[13] = "la Presencia"

mc = dict()
mc[1] = "Atrayendo"
mc[2] = "Estabilizando"
mc[3] = "Vinculando"
mc[4] = "Midiendo"
mc[5] = "Comandando"
mc[6] = "Equilibrando"
mc[7] = "Inspirando"
mc[8] = "Modelando"
mc[9] = "Realizando"
mc[10] = "Produciendo"
mc[11] = "Divulgando"
mc[12] = "Universalizando"
mc[13] = "Transcendiendo"

mb = dict()
mb[1] = "Nutrir"
mb[2] = "Comunicar"
mb[3] = "Soñar"
mb[4] = "Atinar"
mb[5] = "Sobrevivir"
mb[6] = "Igualar"
mb[7] = "Conocer"
mb[8] = "Embellecer"
mb[9] = "Purificar"
mb[10] = "Amar"
mb[11] = "Jugar"
mb[12] = "Influenciar"
mb[13] = "Explorar"
mb[14] = "Encantar"
mb[15] = "Crear"
mb[16] = "Cuestionar"
mb[17] = "Evolucionar"
mb[18] = "Reflejar"
mb[19] = "Catalizar"
mb[20] = "Iluminar"

mf = dict()
mf[1] = "el Nacimiento"
mf[2] = "el Espíritu"
mf[3] = "la Abundancia"
mf[4] = "el Florecimiento"
mf[5] = "la Fuerza Vital"
mf[6] = "la Muerte"
mf[7] = "la Realización"
mf[8] = "la Elegancia"
mf[9] = "el Agua Universal"
mf[10] = "el Corazón"
mf[11] = "la Magia"
mf[12] = "la Libre Voluntad"
mf[13] = "el Espacio"
mf[14] = "la Atemporalidad"
mf[15] = "la Visión"
mf[16] = "la Inteligencia"
mf[17] = "la Navegación"
mf[18] = "el Sinfín"
mf[19] = "la Autogeneración"
mf[20] = "el Fuego Universal"

md = dict()
md[1] = "el Ser"
md[2] = "el Aliento"
md[3] = "la Intuición"
md[4] = "la Atención"
md[5] = "el Instinto"
md[6] = "la Oportunidad"
md[7] = "la Curación"
md[8] = "el Arte"
md[9] = "el Flujo"
md[10] = "la Lealtad"
md[11] = "la Ilusión"
md[12] = "la Sabiduría"
md[13] = "la Vigilancia"
md[14] = "la Receptividad"
md[15] = "la Mente"
md[16] = "la Intrepidez"
md[17] = "la Sincronía"
md[18] = "el Orden"
md[19] = "la Energía"
md[20] = "la Vida"

mee = dict()
mee[1] = "la entrada"
mee[2] = "la entrada"
mee[3] = "la entrada"
mee[4] = "la entrada"
mee[5] = "el almacén"
mee[6] = "el almacén"
mee[7] = "el almacén"
mee[8] = "el almacén"
mee[9] = "el proceso"
mee[10] = "el proceso"
mee[11] = "el proceso"
mee[12] = "el proceso"
mee[13] = "la salida"
mee[14] = "la salida"
mee[15] = "la salida"
mee[16] = "la salida"
mee[17] = "la matriz"
mee[18] = "la matriz"
mee[19] = "la matriz"
mee[20] = "la matriz"


def kin(x):
    valor_ano = tablaA[x.year]
    valor_mes = tablaB[x.month]
    valor = valor_ano + valor_mes + x.day
    if valor > 260:
        valor = valor - 260
    return valor


def sellonum(x):
    sellonum = kin(x) % 20
    if sellonum == 0:
        sellonum = 20
    return sellonum


def sello(x):
    return sellos[sellonum(x) + 1]


def raza(x):
    return "%s " % razas[kin(x) % 4 - 1]


def tononum(x):
    tononum = kin(x) % 13
    if tononum == 0:
        tononum = 13
    return tononum


def tono(x):
    return "%s" % tonosf[tononum(x)]


def firma(x):
    firma = "%s %s %s" % (sello(x),
                          tono(x),
                          raza(x))
    return(firma)


def afirmacion(x):
    sello = sellonum(x)
    tono = tononum(x)
    afirmacion = "\n" + ma[tono] + ' con el fin de ' + mb[sello] + "\n"\
                + mc[tono] + ' ' + md[sello] + "\n"\
                + 'Sello ' + mee[sello] + " de " + mf[sello] + "\n"\
                + 'Con el tono ' + mg[tono] + " de " + mh[tono] + "\n\n"

    if guia(x) == sello:
        afirmacion += "Me guía mi propio poder duplicado\n"
    else:
        afirmacion += "Me guía el poder de " + mf[guia(x)] + "\n"

    if kin(x) in [1, 20, 22, 39, 43, 51, 50, 58, 64, 69, 72, 77, 85, 88, 93,
                96, 165, 168, 173, 176, 184, 189, 192, 197, 203, 210, 211, 218,
                222, 239, 241, 260] or \
                (kin(x) > 105 and kin(x) < 116) or \
                (kin(x) > 145 and kin(x) < 156):
        afirmacion += "\nSoy un Portal de Activación Galáctica\n"

    return afirmacion


def onda(x):
    sello = sellonum(x)
    tono = tononum(x)
    onda = sello - tono + 1
    if onda < 1:
        if onda == 0:
            onda = 20
        else:
            onda = onda + 20
    return onda


def guia(x):
    guia = onda(x) + 13 * (tononum(x) - 1)
    guia = guia % 20
    if guia == 0:
        guia = 20
    return guia


def analogo(x):
    analogo = 19 - sellonum(x)
    if analogo == 0:
        analogo = 20
    if analogo == -1:
        analogo = 19
    return analogo


def oculto(x):
    oculto = 21 - sellonum(x)
    return oculto


def antipoda(x):
    antipoda = sellonum(x) + 10
    if antipoda > 20:
        antipoda = antipoda - 20
    return antipoda

#fecha = date(2012,10,19)
#print "Hoy"
#print "Kin %s" % str(kin(fecha))
#print sello(fecha)
#print tono(fecha)
#print raza(fecha)
