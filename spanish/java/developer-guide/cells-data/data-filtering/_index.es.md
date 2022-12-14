---
title: Filtrado de datos
type: docs
weight: 60
url: /es/java/data-filtering/
---
{{% alert color="primary" %}}

Microsoft Excel proporciona algunas buenas funciones para filtrar automáticamente los datos de la hoja de cálculo. Aspose.Cells es totalmente compatible con las funciones de autofiltro de Microsoft de Excel. Este artículo explica cómo usar las funciones en Microsoft Excel y cómo codificarlas usando Aspose.Cells.

{{% /alert %}}

## **Datos de autofiltro**

El filtrado automático es la forma más rápida de seleccionar solo los elementos de la hoja de trabajo que desea mostrar en una lista. La función de autofiltro permite a los usuarios filtrar elementos en una lista de acuerdo con un criterio establecido. Filtra por texto, números o fechas.

### **Autofiltro en Microsoft Excel**

Para activar la función de autofiltro en Microsoft Excel:

1. Haga clic en la fila de encabezado en una hoja de cálculo.
1. Desde el**Datos**menú, seleccione**Filtrar**y entonces**Autofiltro**.

Cuando aplica un filtro automático a una hoja de trabajo, los interruptores de filtro (flechas negras) aparecen a la derecha de los encabezados de las columnas.

1. Haga clic en una flecha de filtro para ver una lista de opciones de filtro.

Algunas de las opciones de autofiltro son:

|**Opciones**|**Descripción**|
|:- |:- |
|Todos|Muestra todos los elementos de la lista una vez.|
|Disfraz|Personalice los criterios de filtro como contiene/no contiene|
|Filtrar por color|Filtros basados en color relleno|
|Filtros de fecha|Filtra filas según diferentes criterios en la fecha|
|Filtros numéricos|Diferentes tipos de filtro en números como comparación, promedios y Top 10, etc.|
|Filtros de texto|Diferentes filtros como comienza con, termina con, contiene, etc.|
|Espacios en blanco/No espacios en blanco|Estos filtros se pueden implementar a través de Text Filter Blank|
Los usuarios filtran manualmente los datos de su hoja de trabajo en Microsoft Excel usando estas opciones.

### **Autofiltro con Aspose.Cells**

Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)que representa un archivo de Excel. los[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)la clase contiene un[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)que permite el acceso a cada hoja de trabajo en el archivo de Excel.

Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo. Para crear un autofiltro, utilice el[**Autofiltro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)propiedad de la[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)clase. los[**Autofiltro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)La propiedad es un objeto de la[**Autofiltro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)clase, que proporciona la[**Rango**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range)propiedad para especificar el rango de celdas que componen una fila de encabezado. Se aplica un filtro automático al rango de celdas que es la fila de encabezado.

En cada hoja de trabajo, solo puede especificar un rango de filtro. Esto está limitado por Microsoft Excel. Para el filtrado de datos personalizado, utilice el[**Autofiltro.Personalizado**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) método.

En el ejemplo que se muestra a continuación, hemos creado el mismo Autofiltro usando Aspose.Cells que creamos usando Microsoft Excel en la sección anterior.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **Diferentes tipos de filtro**

Aspose.Cells proporciona múltiples opciones para aplicar diferentes tipos de filtros como filtro de color, filtro de fecha, filtro de número, filtro de texto, filtros en blanco y filtros sin blanco.

##### **Color de relleno**

Aspose.Cells proporciona una función[**añadirFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter(int,%20int,%20com.aspose.cells.CellsColor,%20com.aspose.cells.CellsColor)para filtrar datos según la propiedad de color de relleno de las celdas. En el ejemplo que se muestra a continuación, se usa un archivo de plantilla que tiene diferentes colores de relleno en la primera columna de la hoja para probar la función de filtrado de color. Los siguientes archivos se pueden descargar para verificar la funcionalidad.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **Fecha**

Se pueden implementar diferentes tipos de filtros de fecha, como filtrar todas las filas que tienen fechas en enero de 2018. El siguiente código de ejemplo demuestra este filtro usando[**añadirFiltroFecha**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int)) función. Los siguientes archivos se pueden utilizar para probar esta funcionalidad.

1. [Fecha.xlsx](72417317.xlsx)
1. [Fecha filtrada.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **Fecha dinámica**

A veces, se requieren filtros dinámicos basados en una fecha, como todas las celdas que tienen fechas en enero, independientemente del año. En este caso,[**Filtro Dinámico**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter(int,%20int)) se usa como se indica en el siguiente código de ejemplo. Los siguientes archivos se pueden utilizar para las pruebas.

1. [Fecha.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **Número**

Los filtros personalizados se pueden aplicar usando Aspose.Cells como seleccionar celdas que tengan un número entre un rango dado. El siguiente ejemplo demuestra el uso de[**disfraz()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) función para filtrar números. Los archivos de muestra se pueden descargar desde los siguientes enlaces.

1. [Número.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **Texto**

Si una columna contiene texto y se van a seleccionar celdas que contengan un texto en particular,[**filtrar()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter(int,%20java.lang.String)) se puede utilizar la función. En el siguiente ejemplo, el archivo de plantilla contiene una lista de países y se debe seleccionar la fila que contiene el nombre de un país en particular. El siguiente código demuestra el filtrado de texto utilizando los siguientes archivos de ejemplo.

1. [Texto.xlsx](72417322.xlsx)
1. [Texto filtrado.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **espacios en blanco**

Si una columna contiene texto de modo que pocas celdas están en blanco y se requiere un filtro para seleccionar aquellas filas solo donde hay celdas en blanco,[**combinar espacios en blanco ()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks(int)) se puede utilizar como se muestra a continuación. Los archivos de muestra se pueden descargar desde los siguientes enlaces.

1. [En blanco.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **No espacios en blanco**

Cuando se deban filtrar celdas que tengan texto, utilice[**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks(int)) función de filtro como se demuestra a continuación. Los archivos de muestra se pueden descargar desde los siguientes enlaces.

1. [En blanco.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **Filtro personalizado con Contiene**

Excel proporciona filtros personalizados como filas de filtro que contienen una cadena específica. Esta función está disponible en Aspose.Cells y se muestra a continuación filtrando los nombres en el archivo de muestra. Los archivos de muestra se pueden descargar desde los siguientes enlaces.

1. [origenNombresDePaísesDeMuestra.xlsx](sourseSampleCountryNames.xlsx)
1. [OutSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **Filtro personalizado con NotContains**

Excel proporciona filtros personalizados como filas de filtro que no contienen una cadena específica. Esta función está disponible en Aspose.Cells y se muestra a continuación filtrando los nombres en el archivo de muestra que se proporciona a continuación.

1. [origenNombresDePaísesDeMuestra.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **Filtro personalizado con BeginsWith**

Excel proporciona filtros personalizados como filas de filtro que comienzan con una cadena específica. Esta función está disponible en Aspose.Cells y se muestra a continuación filtrando los nombres en el archivo de muestra que se proporciona a continuación.

1. [origenNombresDePaísesDeMuestra.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **Filtro personalizado con Termina con**

Excel proporciona filtros personalizados como filas de filtro que terminan con una cadena específica. Esta función está disponible en Aspose.Cells y se muestra a continuación filtrando los nombres en el archivo de muestra que se proporciona a continuación.

1. [origenNombresDePaísesDeMuestra.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **Temas avanzados**
- [Aplicar filtro avanzado de Microsoft Excel para mostrar registros que cumplen criterios complejos](/cells/es/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Obtenga todos los índices de filas ocultas después de actualizar el Autofiltro](/cells/es/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

