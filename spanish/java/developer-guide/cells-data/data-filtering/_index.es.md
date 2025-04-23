---
title: Filtrado de Datos
type: docs
weight: 60
url: /es/java/data-filtering/
---

{{% alert color="primary" %}}

Microsoft Excel proporciona algunas funciones buenas para el autofiltrado de datos en hojas de trabajo. Aspose.Cells es compatible completamente con las funciones de autofiltrado de Microsoft Excel. Este artículo explica cómo usar las funciones en Microsoft Excel y cómo codificarlas usando Aspose.Cells.

{{% /alert %}}

## **Datos de Autofiltro**

El autofiltrado es la forma más rápida de seleccionar solo aquellos elementos de la hoja de cálculo que desea mostrar en una lista. La función de autofiltro permite a los usuarios filtrar elementos en una lista según un criterio establecido. Filtrar según texto, números o fechas.

### **Autofiltro en Microsoft Excel**

Para activar la función de autofiltro en Microsoft Excel:

1. Haz clic en la fila de encabezado en una hoja de cálculo.
1. Desde el menú **Datos**, seleccione **Filtrar** y luego **Autofiltro**.

Cuando aplicas un autofiltro a una hoja de cálculo, aparecen interruptores de filtro (flechas negras) a la derecha de los encabezados de las columnas.

1. Haz clic en una flecha de filtro para ver una lista de opciones de filtro.

Algunas de las opciones de autofiltro son:

|**Opciones**|**Descripción**|
| :- | :- |
|All|Mostrar todos los elementos en la lista una vez.|
|Custom|Personalizar criterios de filtro como contiene/no contiene|
|Filter by Color|Filtros basados en el color rellenado|
|Date Filters|Filtrar filas basadas en diferentes criterios en la fecha|
|Number Filters| Diferente tipo de filtro en números como comparación, promedios y Top 10, etc.|
|Text Filters|Diferentes filtros como comienza con, termina con, contiene, etc,|
|Blanks/Non Blanks|Estos filtros pueden implementarse a través de Filtro de Texto en Blanco|
Los usuarios filtran manualmente sus datos de hoja de cálculo en Microsoft Excel utilizando estas opciones.

### **Autofiltro con Aspose.Cells**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para crear un autofiltro, use la propiedad [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) de la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La propiedad [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) es un objeto de la clase [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter), que proporciona la propiedad [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range) para especificar el rango de celdas que conforman una fila de encabezado. Un autofiltro se aplica al rango de celdas que es la fila de encabezado.

En cada hoja de cálculo, solo puede especificar un rango de filtro. Esto está limitado por Microsoft Excel. Para filtrado de datos personalizado, use el método [**AutoFilter.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom-int-int-java.lang.Object-).

En el ejemplo dado a continuación, hemos creado el mismo Autofiltro utilizando Aspose.Cells como lo creamos utilizando Microsoft Excel en la sección anterior.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **Diferentes tipos de filtro**

Aspose.Cells ofrece múltiples opciones para aplicar diferentes tipos de filtros como Filtro de Color, Filtro de Fecha, Filtro de Número, Filtro de Texto, Filtros en Blanco y Filtros no en Blanco.

##### **Color de relleno**

Aspose.Cells proporciona una función [**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter-int-int-com.aspose.cells.CellsColor-com.aspose.cells.CellsColor-) para filtrar datos basados en la propiedad de color de relleno de las celdas. En el ejemplo dado a continuación, se utiliza un archivo de plantilla con diferentes colores de relleno en la primera columna de la hoja para probar la función de filtrado por color. Los siguientes archivos se pueden descargar para verificar la funcionalidad.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **Fecha**

Se pueden implementar diferentes tipos de filtros de fecha como filtrar todas las filas con fechas en enero de 2018. El siguiente código de muestra demuestra este filtro usando la función [**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter-int-int-int-int-int-int-int-int-). Los siguientes archivos se pueden utilizar para probar esta funcionalidad.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **Fecha dinámica**

A veces se requieren filtros dinámicos basados en una fecha como todas las celdas con fechas en enero independientemente del año. En este caso, se utiliza la función [**DynamicFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter-int-int-) como se indica en el siguiente código de ejemplo. Los siguientes archivos se pueden utilizar para probar.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **Número**

Los filtros personalizados se pueden aplicar usando Aspose.Cells como seleccionar celdas que tienen un número entre un rango dado. El siguiente ejemplo demuestra el uso de la función [**custom()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom-int-int-java.lang.Object-) para filtrar números. Los archivos de ejemplo se pueden descargar desde los siguientes enlaces.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **Texto**

Si una columna contiene texto y se deben seleccionar celdas que contienen un texto específico, se puede usar la función [**filter()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter-int-java.lang.String-). En el siguiente ejemplo, el archivo de plantilla contiene una lista de países y se debe seleccionar la fila que contiene un nombre de país específico. El siguiente código demuestra el filtrado de texto usando los archivos de ejemplo a continuación.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **Vacíos**

Si una columna contiene texto de manera que algunas celdas están en blanco, y se requiere un filtro para seleccionar solo aquellas filas donde hay celdas en blanco presentes, se puede usar la función [**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks-int-) como se demuestra a continuación. Los archivos de ejemplo se pueden descargar desde los siguientes enlaces.

1. [EnBlanco.xlsx](72417324.xlsx)
1. [EnBlancoFiltrado.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **No vacíos**

Cuando se desea filtrar celdas que contienen algún texto, se utiliza la función [**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks-int-) como se demuestra a continuación. Los archivos de ejemplo se pueden descargar desde los siguientes enlaces.

1. [EnBlanco.xlsx](72417324.xlsx)
1. [NoVaciosFiltrado.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **Filtro personalizado con Contiene**

Excel proporciona filtros personalizados como filtrar filas que contienen una cadena específica. Esta característica está disponible en Aspose.Cells y se demuestra a continuación filtrando los nombres en el archivo de ejemplo. Los archivos de ejemplo se pueden descargar desde los siguientes enlaces.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **Filtro personalizado con NoContiene**

Excel proporciona filtros personalizados como filtrar filas que no contienen alguna cadena específica. Esta función está disponible en Aspose.Cells y se demuestra a continuación filtrando los nombres en el archivo de muestra proporcionado a continuación.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **Filtro personalizado que comienza con**

Excel proporciona filtros personalizados como filtrar filas que comienzan con una cadena específica. Esta función está disponible en Aspose.Cells y se demuestra a continuación filtrando los nombres en el archivo de muestra proporcionado a continuación.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **Filtro personalizado que termina con**

Excel proporciona filtros personalizados como filtrar filas que terminan con una cadena específica. Esta función está disponible en Aspose.Cells y se muestra a continuación filtrando los nombres en el archivo de muestra proporcionado a continuación.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **Temas avanzados**
- [Aplicar Filtro Avanzado de Microsoft Excel para Mostrar Registros que Cumplen Criterios Complejos](/cells/es/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Obtener Todos los Índices de Filas Ocultas Después de Actualizar el Autofiltro](/cells/es/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

{{< app/cells/assistant language="java" >}}
