---
title: Filtrado de Datos
type: docs
weight: 85
url: /es/python-net/data-filtering/
description: Aprenda cómo agregar filtro de datos mediante el uso de la API Aspose.Cells for Python via .NET.
keywords: Biblioteca de Excel de Python, Agregar filtro por color en Python, Agregar filtros de fecha en Python, Agregar filtros numéricos en Python, Agregar filtro dinámico en Python, Agregar filtros de texto en Python, Agregar filtro personalizado con Contiene en Python, Agregar filtro personalizado con No Contiene en Python, Agregar filtro personalizado con Comienza con en Python, Agregar filtro personalizado con Termina con en Python
---

{{% alert color="primary" %}}

Microsoft Excel proporciona algunas características útiles para autofiltrar datos de hojas de cálculo. Aspose.Cells for Python via .NET totalmente soporta las características de autofiltrado de Microsoft Excel. Este artículo explica cómo usar las características en Microsoft Excel y cómo codificarlas usando Aspose.Cells for Python via .NET.

{{% /alert %}}

## **Datos de Autofiltro**

El autofiltrado es la forma más rápida de seleccionar solo aquellos elementos de la hoja de cálculo que desea mostrar en una lista. La función de autofiltro permite a los usuarios filtrar elementos en una lista según un criterio establecido. Filtrar según texto, números o fechas.

### **Autofiltro en Microsoft Excel**

Para activar la función de autofiltro en Microsoft Excel:

1. Haz clic en la fila de encabezado en una hoja de cálculo.
1. Desde el menú **Datos**, selecciona **Filtrar** y luego **Autofiltro**.

Cuando aplicas un autofiltro a una hoja de cálculo, aparecen interruptores de filtro (flechas negras) a la derecha de los encabezados de las columnas.

1. Haz clic en una flecha de filtro para ver una lista de opciones de filtro.

Algunas de las opciones de autofiltro son:

|**Opciones**|**Descripción**|
| :- | :- |
|All|Mostrar todos los elementos en la lista una vez.|
|Custom|Personalizar criterios de filtro como contiene/no contiene|
|Filter by Color|Filtros basados en el color rellenado|
|Date Filters|Filtrar filas basadas en diferentes criterios en la fecha|
|Number Filters|Diferentes tipos de filtro en números como comparación, promedios y Top 10, etc.|
|Text Filters|Diferentes filtros como comienza con, termina con, contiene, etc,|
|Blanks/Non Blanks|Estos filtros pueden implementarse a través de Filtro de Texto en Blanco|

Los usuarios filtran manualmente sus datos de hoja de cálculo en Microsoft Excel utilizando estas opciones.

### **Autofiltro con la biblioteca Aspose.Cells para Python Excel**

Aspose.Cells for Python via .NET proporciona una clase, Workbook que representa un archivo de Excel. La clase Workbook contiene una colección de Worksheets que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase Worksheet. La clase Worksheet proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para crear un autofiltro, utilice la propiedad AutoFilter de la clase Worksheet. La propiedad AutoFilter es un objeto de la clase AutoFilter, que proporciona la propiedad Range para especificar el rango de celdas que forman una fila de encabezado. Un autofiltro se aplica al rango de celdas que es la fila de encabezado.

En cada hoja de cálculo, solo se puede especificar un rango de filtro. Esto está limitado por Microsoft Excel. Para el filtrado personalizado de datos, utilice el método AutoFilter.Custom.

En el ejemplo dado a continuación, hemos creado el mismo Autofiltro usando Aspose.Cells para Python via .NET como lo creamos usando Microsoft Excel en la sección anterior.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterData-1.py" >}}

#### **Diferentes tipos de filtro**

Aspose.Cells for Python via .NET proporciona múltiples opciones para aplicar diferentes tipos de filtros como Filtro de color, Filtro de fecha, Filtro de número, Filtro de texto, Filtros en blanco y No en blanco.

##### **Color de relleno**

Aspose.Cells for Python via .NET proporciona una función AddFillColorFilter para filtrar datos basados en la propiedad de color de relleno de las celdas. En el ejemplo dado a continuación, se utiliza un archivo de plantilla con diferentes colores de relleno en la primera columna de la hoja para probar la función de filtrado de color. Los archivos de ejemplo se pueden descargar desde los siguientes enlaces.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterColor-1.py" >}}

##### **Fecha**

Se pueden implementar diferentes tipos de filtros de fecha como filtrar todas las filas que tienen fechas en enero de 2018. El siguiente ejemplo de código demuestra este filtro mediante la función AddDateFilter. Se proporcionan los archivos de ejemplo a continuación.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDate-1.py" >}}

##### **Fecha dinámica**

A veces se requieren filtros dinámicos basados en la fecha, como todas las celdas que tienen fechas en enero, independientemente del año. En este caso, se utiliza la función DynamicFilter según se muestra en el siguiente ejemplo de código. Se proporcionan los archivos de ejemplo a continuación.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDynamicFilter-1.py" >}}

##### **Número**

Se pueden aplicar filtros personalizados utilizando Aspose.Cells for Python via .NET como seleccionar celdas que tienen números entre un rango dado. El siguiente ejemplo demuestra el uso de la función Custom() para filtrar números. Se proporcionan los archivos de ejemplo a continuación.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNumber-1.py" >}}

##### **Texto**

Si una columna contiene texto y se deben seleccionar celdas que contienen un texto particular, se puede utilizar la función Filtro(). En el siguiente ejemplo, el archivo de plantilla contiene una lista de países y se debe seleccionar una fila que contenga el nombre de un país en particular. El siguiente código demuestra la filtración de texto. Los archivos de ejemplo se muestran a continuación.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterText-1.py" >}}

##### **Vacíos**

Si una columna contiene texto y algunas celdas están en blanco, y se requiere un filtro para seleccionar solo aquellas filas donde las celdas en blanco están presentes, se puede utilizar la función CoincidirBlancos() como se demuestra a continuación. Los archivos de ejemplo se muestran a continuación.

1. [EnBlanco.xlsx](72417324.xlsx)
1. [EnBlancoFiltrado.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterBlank-1.py" >}}

##### **No vacíos**

Cuando se deben filtrar celdas que contienen texto, utilizar la función de filtro CoincidirNoVacios como se demuestra a continuación. Los archivos de ejemplo se muestran a continuación.

1. [EnBlanco.xlsx](72417324.xlsx)
1. [NoVaciosFiltrado.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNonBlank-1.py" >}}

##### **Filtro personalizado con Contiene**

Excel proporciona filtros personalizados como filtrar filas que contienen cierta cadena específica. Esta función está disponible en Aspose.Cells para Python via .NET y se muestra a continuación filtrando los nombres en el archivo de ejemplo. Los archivos de ejemplo se muestran a continuación.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-Contains-1.py" >}}

##### **Filtro personalizado con NoContiene**

Excel proporciona filtros personalizados como filtrar filas que no contienen cierta cadena específica. Esta función está disponible en Aspose.Cells para Python via .NET y se muestra a continuación filtrando los nombres en el archivo de ejemplo dado a continuación.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-NotContains-1.py" >}}

##### **Filtro personalizado que comienza con**

Excel proporciona filtros personalizados como filtrar filas que comienzan con una cadena específica. Esta característica está disponible en Aspose.Cells para Python via .NET y se muestra a continuación filtrando los nombres en el archivo de muestra dado a continuación.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterBeginsWith-1.py" >}}

##### **Filtro personalizado que termina con**

Excel proporciona filtros personalizados como filtrar filas que terminan con una cadena específica. Esta característica está disponible en Aspose.Cells para Python via .NET y se muestra a continuación filtrando los nombres en el archivo de muestra dado a continuación.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterEndsWith-1.py" >}}

## **Temas avanzados**
- [Aplicar Filtro Avanzado de Microsoft Excel para Mostrar Registros que Cumplen Criterios Complejos](/cells/es/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Obtener Todos los Índices de Filas Ocultas Después de Actualizar el Autofiltro](/cells/es/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
{{< app/cells/assistant language="python-net" >}}
