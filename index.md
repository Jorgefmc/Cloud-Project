# Proyecto Cloud de medias anuales

## Problema y origen de los datos

Existen infinidad de lugares donde encontrar las temperaturas medias diaria como [por ejemplo esta](https://datosclima.es/Aemet2013/DescargaDatos.html) que utiliza datos de AEMET, pero no es tan fácil encontrar las medias anuales, por lo cual, hemos querido proporcionar un software que nos calcule estas medias utilizando los datos ya existentes. 

Todos los datos utilizados para el ejemplo esta aplicación han sido extraídos de https://datosclima.es/Aemet2013/DescargaDatos.html aunque originalmente pertenecen a la AEMET. Estos han sido convertidos de formato .xls a .csv 

## En relación a la aplicación

Para el desarrollo de la aplicación se ha utilizado mapReduce sobre Hadoop, desarrollando en Python. Esta orientado a que pueda utilizarse con un servicio Cloud Computing ya que se utiliza gran cantidad de datos.

Esta aplicación, no tiene ninguna iteración con el usuario como tal, es un programa, que simplemente con ejecutarlo, coge todos los ficheros .csv con un nombre especifico que existen en una carpeta, y genera los resultados con las medias anuales en otro fichero, el cual se almacena.


## Diseño del codigo (Mapp Reduce)
## Como funciona la app que se necesita y que no
## Eficiencia
## Que hemos aprendido 
## Posibles mejoras
## Que nos ha molado, que nos a costado, que hariamos diferente la proxima vez, lo mas frustrante, 

----------------------------------------------------------------------------------------------------------------------------------------


## Welcome to GitHub Pages


You can use the [editor on GitHub](https://github.com/Jorgefmc/Cloud-Project/edit/master/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Jorgefmc/Cloud-Project/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
