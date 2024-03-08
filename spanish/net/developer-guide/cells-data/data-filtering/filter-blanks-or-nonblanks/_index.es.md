---
title: Cómo filtrar espacios en blanco o no espacios en blanco
type: docs
weight: 85
url: /es/net/how-to-filter-blanks-and-non-blanks/
description: Aprenda a filtrar espacios en blanco y no espacios en blanco utilizando Aspose.Cells for .NET API.
keywords: Filter Blanks, Filter Non-Blanks, Filter Blanks in worksheet, Filter Non-Blanks in worksheet, Filter Blanks in excel, Filter Non-Blanks in excel, Filter Blanks and Non-Blanks in excel
---
##  **Posibles escenarios de uso**
El filtrado de datos en Excel es una herramienta valiosa que mejora el análisis, la exploración y la presentación de datos al permitir a los usuarios centrarse en subconjuntos específicos de datos según sus criterios, lo que hace que el proceso general de manipulación e interpretación de datos sea más eficiente y eficaz.

##  **Cómo filtrar espacios en blanco o no en blanco en Excel**
En Excel, puede filtrar fácilmente espacios en blanco o no en blanco utilizando las opciones de filtrado. Así es como puedes hacerlo:

###  **Cómo filtrar espacios en blanco en Excel**
1. Seleccione el rango: haga clic en la letra del encabezado de la columna para seleccionar la columna completa o seleccione el rango donde desea filtrar los espacios en blanco.
1. Abra el menú Filtro: vaya a la pestaña "Datos" en la cinta.
<br>
<image src="1.png" width="70%" />
1. Opciones de filtro: haga clic en el botón "Filtro". Esto agregará flechas de filtro al rango seleccionado.
1. Filtrar espacios en blanco: haga clic en la flecha de filtro en la columna en la que desea filtrar espacios en blanco. Anule la selección de todas las opciones excepto "Blancos" y haga clic en Aceptar. Esto mostrará solo las celdas en blanco en esa columna.
<br>
<image src="2.png" width="70%" />
1. El resultado de la siguiente manera:
<br>
<image src="3.png" width="70%" />

###  **Cómo filtrar espacios que no son espacios en blanco en Excel**
1. Seleccione el rango: haga clic en la letra del encabezado de la columna para seleccionar la columna completa o seleccione el rango donde desea filtrar los que no son espacios en blanco.
1. Abra el menú Filtro: vaya a la pestaña "Datos" en la cinta.
<br>
<image src="1.png" width="70%" />
1. Opciones de filtro: haga clic en el botón "Filtro". Esto agregará flechas de filtro al rango seleccionado.
1. Filtrar no espacios en blanco: haga clic en la flecha de filtro en la columna que desea filtrar no espacios en blanco. Anule la selección de todas las opciones excepto "No en blanco" o "Personalizado" y establezca las condiciones en consecuencia. Haga clic en Aceptar. Esto mostrará solo las celdas que no estén en blanco en esa columna.
<br>
<image src="4.png" width="70%" />
1. El resultado de la siguiente manera:
<br>
<image src="5.png" width="70%" />

##  **Cómo filtrar espacios en blanco usando Aspose.Cells**
 Si una columna contiene texto tal que pocas celdas están en blanco y se requiere un filtro para seleccionar aquellas filas solo donde hay celdas en blanco,[AutoFilter.MatchBlanks (índice de campo int)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchblanks/) y[AutoFilter.AddFilter (int fieldIndex, criterios de cadena)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/addfilter/) Las funciones se pueden utilizar como se muestra a continuación.

 Consulte el siguiente código de muestra que carga el[archivo de Excel de muestra](sample.xlsx) que contiene algunos datos ficticios. El código de muestra utiliza tres métodos para filtrar espacios en blanco. Luego guarda el libro de trabajo como[archivo de salida de Excel](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-blanks.cs" >}}

##  **Cómo filtrar espacios que no están en blanco usando Aspose.Cells**

 Consulte el siguiente código de muestra que carga el[archivo de Excel de muestra](sample.xlsx) que contiene algunos datos ficticios. Después de cargar el archivo, llame al[AutoFilter.MatchNonBlanks (índice de campo int)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchnonblanks/) función para filtrar datos que no estén en blanco y, finalmente, guardar el libro como[archivo de salida de Excel](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-non-blanks.cs" >}}

