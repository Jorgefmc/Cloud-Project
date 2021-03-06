# Proyecto Cloud de medias anuales

## Problema y origen de los datos

Existen infinidad de lugares donde encontrar las temperaturas medias diaria como por ejemplo, [esta](https://datosclima.es/Aemet2013/DescargaDatos.html) que utiliza datos de AEMET, pero no es tan fácil encontrar las medias anuales, por lo cual, hemos querido proporcionar un software que nos calcule estas medias utilizando los datos ya existentes. 

Todos los datos utilizados para el ejemplo esta aplicación han sido extraídos de https://datosclima.es/Aemet2013/DescargaDatos.html aunque originalmente pertenecen a la AEMET. Estos han sido convertidos de formato .xls a .csv, con tabuladores como delimitador de campo.

Partimos de diferentes columnas con la información de temperaturas mínimas, máximas, medias, rachas de viento y precipitaciones en diferentes rangos horarios recogidas por distintas estaciones meteorológicas. De estos datos nos quedamos con las precipitaciones diarias y la temperatura media recogidas por las estaciones, tratando estos datos para hallar las medias, primero diarias y, tras acumularse, anuales.

## En relación a la aplicación

Para el desarrollo de la aplicación se ha utilizado mapReduce sobre Hadoop, en Python. Esta orientado a que pueda utilizarse con un servicio Cloud Computing ya que se utiliza gran cantidad de datos.

Esta aplicación, no tiene ninguna interacción con el usuario como tal, es un programa, que simplemente con ejecutarlo, coge todos los ficheros .csv con un nombre especifico que existen en una carpeta, y genera los resultados con las medias anuales en otro fichero, el cual se almacena.

## Otros aspectos

A lo largo del desarrollo de esta aplicación hemos adquirido varios conocimientos.
  - Utilizacion de mapReduce
  - Programación con Python
  - Utilizacion de servicios Cloud
  - Usar servicio como GitHub y GitHub Pages

En visión a futuro se podrían añadir varias mejoras, a parte de las evidentes en eficiencia y similares, se podría incluir un script que transforme de forma automática del formato .xls (descargado) a .csv (utilizado por la aplicación) para facilitar el trabajo al usuario. También seria útil ampliar las funcionalidades, poder hallar medias sobre otros patrones, o permitir al usuario elegir de que año quiere las medias en concreto.

Las cosas positivas que sacamos de este proyecto, es que a día de hoy las tecnologías aplicadas a Cloud están en auge permanente y haber aprendido a manejarlas al igual que a utilizar repositorios Git es un salto en nuestra preparación para más adelante. 

Toda parte positiva tiene su parete negativa, y es verdad que hemos aprendido a programar un poco en Python, pero el no conocer nada del lenguaje nos ha hecho ir muy lentos desarrollando la aplicación, aunque la parte más frustrante y tediosa ha sido tener que utilizar datos .csv y que los disponibles fueran todos .xls .

### Salida de datos
En las siguientes imagenes mostramos la salida de datos tanto en consola como en el log:
<img src="datos.png" alt="consola" class="inline"/>
<img src="Pantallazo-1.png" alt="log" class="inline"/>

### Código

- [Mapper](https://github.com/Jorgefmc/Weather-Averages/blob/master/mapper_proyecto.py)
- [Reducer](https://github.com/Jorgefmc/Weather-Averages/blob/master/reducer_proyecto.py)

### Desarrolladores

- [Carolina Martínez Pérez](https://github.com/CarolMaper)
- [Adrián Montero Torralbo](https://github.com/Montero14)
- [Javier Sesé García](https://github.com/JaviSese)
- [Jorge Fdez-Montes Cabanillas](https://github.com/Jorgefmc)
