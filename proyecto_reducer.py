#!/usr/bin/python

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
readed = False
for line in sys.stdin:
	temperaturas, precipitaciones = line.split( '\t' )
	if precipitaciones == "validar":
		if readed:
			print anio + ": "
			precipitacionMediaAnual = precipitacionMediaAnual / contadorPrepAnual
			temperaturaMediaAnual = temperaturaMediaAnual / contadorTempAnual
			print precipitacionMediaAnual
			print temperaturaMediaAnual
			temperaturaMediaAnual = 0
			precipitacionMediaAnual = 0
			contadorPrepAnual = 0
			contadorTempAnual = 0
			anio = int(temperaturas)

		else:
			reader = True
			anio = int(temperaturas)
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
precipitacionMedia = precipitacionMedia / contadorPrecipitaciones
temperaturaMedia = temperaturaMedia / contadorTemperaturas
print temperaturaMedia
print precipitacionMedia
