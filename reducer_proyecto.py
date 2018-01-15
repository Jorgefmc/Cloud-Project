#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

temperaturaMedia = 0.0
precipitacionMedia = 0.0
contadorTemperaturas = 0
contadorPrecipitaciones = 0
contadorTempAnual = 0
contadorPrepAnual = 0
precipitacionMediaAnual = 0
temperaturaMediaAnual = 0
anio = 0
actual = 0
readed = False
f1=open("log.txt",'w')
print "Media Temperaturas en ºC: " + "\t" + "Media precipitaciones en mm:"
f1.write("Media Temperaturas en ºC: \tMedia precipitaciones en mm:\n")
for line in sys.stdin:
	temperaturas, precipitaciones = line.split( '\t' )
	if precipitaciones == "validar\n":
		
		if readed:
			anio = int(temperaturas)
			if actual != anio:
				precipitacionMediaAnual = precipitacionMediaAnual / contadorPrepAnual
				temperaturaMediaAnual = temperaturaMediaAnual / contadorTempAnual
				print str(actual) + ":\t " + str(temperaturaMediaAnual)+ "\t\t\t" + str(precipitacionMediaAnual)
				f1.write(str(actual) + ":\t " + str(temperaturaMediaAnual)+ "\t\t\t" + str(precipitacionMediaAnual) + "\n")
				temperaturaMediaAnual = 0
				precipitacionMediaAnual = 0
				contadorPrepAnual = 0
				contadorTempAnual = 0
				actual = anio

		else:
			readed = True
			anio = int(temperaturas)
			actual = anio
	else:		
		if precipitaciones != "" and precipitaciones !='\n' and precipitaciones != '\t':
			precipitaciones = re.sub(",",".", precipitaciones)
			precipitacionMedia = precipitacionMedia + float(precipitaciones)
			precipitacionMediaAnual = precipitacionMediaAnual + float(precipitaciones)
			contadorPrepAnual = contadorPrepAnual + 1
			contadorPrecipitaciones = contadorPrecipitaciones + 1			
		if temperaturas != "" and temperaturas != '\n' and temperaturas != '\t':
			temperaturas = re.sub(",",".", temperaturas)
			temperaturaMedia = temperaturaMedia + float(temperaturas)
			temperaturaMediaAnual = temperaturaMediaAnual + float(temperaturas)
			contadorTemperaturas = contadorTemperaturas + 1
			contadorTempAnual = contadorTempAnual + 1
precipitacionMediaAnual = precipitacionMediaAnual / contadorPrepAnual
temperaturaMediaAnual = temperaturaMediaAnual / contadorTempAnual
print str(actual) + ":\t " + str(temperaturaMediaAnual) + "\t\t\t" + str(precipitacionMediaAnual)
f1.write(str(actual) + ":\t " + str(temperaturaMediaAnual)+ "\t\t\t" + str(precipitacionMediaAnual) + "\n")
precipitacionMedia = precipitacionMedia / contadorPrecipitaciones
temperaturaMedia = temperaturaMedia / contadorTemperaturas
print "Total:\t " + str(temperaturaMedia) + "\t\t\t" + str(precipitacionMedia)
f1.write("Total:\t " + str(temperaturaMedia)+ "\t\t\t" + str(precipitacionMedia) + "\n")


