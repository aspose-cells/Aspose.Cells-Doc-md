---
title: Cómo filtrar celdas en blanco o no en blanco
type: docs
weight: 85
url: /es/nodejs-cpp/how-to-filter-blanks-and-non-blanks/
description: Aprende cómo filtrar vacíos y no vacíos usando la API Aspose.Cells for Node.js via C++.
keywords: Filtrar celdas en blanco, filtrar celdas no en blanco, filtrar celdas en blanco en la hoja de cálculo, filtrar celdas no en blanco en la hoja de cálculo, filtrar celdas en blanco en Excel, filtrar celdas no en blanco en Excel, filtrar celdas en blanco y no en blanco en Excel
---

## **Escenarios de uso posibles**
Filtrar datos en Excel es una herramienta valiosa que mejora el análisis, la exploración y la presentación de datos al permitir a los usuarios centrarse en subconjuntos específicos de datos según sus criterios, lo que hace que el proceso general de manipulación e interpretación de datos sea más eficiente y efectivo.

## **Cómo filtrar celdas en blanco o no en blanco en Excel**
En Excel, puedes filtrar fácilmente celdas en blanco o no en blanco utilizando las opciones de filtrado. Así es como puedes hacerlo:

### **Cómo filtrar celdas en blanco en Excel**
1. Selecciona el Rango: Haz clic en la letra del encabezado de columna para seleccionar toda la columna o selecciona el rango donde deseas filtrar celdas en blanco.
1. Abre el Menú de Filtro: Ve a la pestaña "Datos" en la cinta de opciones.
<br>
<image src="1.png" width="70%" />
1. Opciones de Filtro: Haz clic en el botón "Filtro". Esto agregará flechas de filtro al rango seleccionado.
1. Filtrar Celdas en Blanco: Haz clic en la flecha de filtro en la columna que deseas filtrar en blanco. Desmarca todas las opciones excepto "En blanco" y haz clic en Aceptar. Esto mostrará solo las celdas en blanco en esa columna.
<br>
<image src="2.png" width="70%" />
1. El resultado es el siguiente:
<br>
<image src="3.png" width="70%" />

### **Cómo filtrar celdas no en blanco en Excel**
1. Selecciona el Rango: Haz clic en la letra del encabezado de columna para seleccionar toda la columna o selecciona el rango donde deseas filtrar celdas no en blanco.
1. Abre el Menú de Filtro: Ve a la pestaña "Datos" en la cinta de opciones.
<br>
<image src="1.png" width="70%" />
1. Opciones de Filtro: Haz clic en el botón "Filtro". Esto agregará flechas de filtro al rango seleccionado.
1. Filtrar Celdas no en Blanco: Haz clic en la flecha de filtro en la columna que deseas filtrar no en blanco. Desmarca todas las opciones excepto "No en blanco" o "Personalizado" y establece las condiciones correspondientes. Haz clic en Aceptar. Esto mostrará solo las celdas que no están en blanco en esa columna.
<br>
<image src="4.png" width="70%" />
1. El resultado es el siguiente:
<br>
<image src="5.png" width="70%" />

## **Cómo filtrar vacíos usando Aspose.Cells for Node.js via C++**
Si una columna contiene texto y algunas celdas están vacías, y se requiere filtrar solo aquellas filas que contienen celdas vacías, se pueden usar las funciones [**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#matchBlanks-number-) y [**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#addFilter-number-string-) como se demuestra a continuación. 

Consulta el siguiente código de muestra que carga el [archivo de Excel de muestra](sample.xlsx) que contiene algunos datos ficticios. El código de muestra utiliza tres métodos para filtrar en blanco. Luego guarda el libro como [archivo de Excel de salida](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FilterBlanks.js" >}}


## **Cómo filtrar no vacíos usando Aspose.Cells for Node.js via C++**

Por favor, vea el siguiente código de ejemplo que carga el [archivo de Excel de muestra](sample.xlsx) que contiene algunos datos ficticios. Después de cargar el archivo, llame a la función [AutoFilter.matchNonBlanks(number)](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#matchNonBlanks-number-) para filtrar datos no vacíos, y finalmente guarde el libro de trabajo como [archivo de Excel de salida](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FilterNonBlanks.js" >}}

