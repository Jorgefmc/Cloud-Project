#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import csv
import os
import datetime

i = datetime.datetime.now()
linea=0
ignore = ""
finish = False
anio = 2014
mes = 01
dia = 01
comprueba = True
filename = 'Aemet'
#f1=open('Aemet2014-01-01.csv', 'r')
while anio < i.year:
	if os.path.exists('Aemet%04d-%02d-%02d.csv' %(anio, mes, dia)):
		while mes < 12:
			while dia < 31:
				if os.path.exists('Aemet%04d-%02d-%02d.csv' % (anio, mes, dia)):	
					f1=open('Aemet%04d-%02d-%02d.csv' %(anio, mes, dia), 'r')
					finish = False
					for line in f1:
						if linea < 5:
							re.sub(r'^\W+|\W+$', "", ignore)
							linea = linea+1
							if(!finish):
								print anio + '\t' + "validar"
								finish = True

						else:
							#line = re.sub(r'^\W+|\W+$', "", line)
							columnas = re.split(r"\t", line)
							temperaturas = re.split(r"\n", columnas[4])
							precipitaciones = re.split(r"\n", columnas[7])

							for t in temperaturas:
								for p in precipitaciones:
									if len(p) == 0 and len(t) == 0:
										print ("" + "\t" + "")
									elif len(p) == 0:
										print (t + "\t" + "")
									elif len(t) == 0:
										print ("" + "\t" + p)
									else:
										print (t + "\t" + p)
					f1.close()
					linea = 0
				dia = dia + 1
			mes = mes + 1
			dia = 01
		anio = anio + 1
		mes = 01
	else:	
		if dia < 31:
			dia = dia + 1
		else:
			if mes < 12:
				mes = mes +1
			else:	
				if anio < i.year:
					anio = anio + 1
				mes = 01
			dia = 01
		#comprueba = False

