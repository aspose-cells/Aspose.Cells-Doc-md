---
title: Filtrado de datos
type: docs
weight: 85
url: /es/net/data-filtering/
---
{{% alert color="primary" %}}

Microsoft Excel proporciona algunas buenas funciones para filtrar automáticamente los datos de la hoja de cálculo. Aspose.Cells es totalmente compatible con las funciones de autofiltro de Microsoft de Excel. Este artículo explica cómo usar las funciones en Microsoft Excel y cómo codificarlas usando Aspose.Cells.

{{% /alert %}}

## **Datos de autofiltro**

El filtrado automático es la forma más rápida de seleccionar solo los elementos de la hoja de trabajo que desea mostrar en una lista. La función de autofiltro permite a los usuarios filtrar elementos en una lista de acuerdo con un criterio establecido. Filtra por texto, números o fechas.

### **Autofiltro en Microsoft Excel**

Para activar la función de autofiltro en Microsoft Excel:

1. Haga clic en la fila de encabezado en una hoja de cálculo.
1.  Desde el**Datos** menú, seleccione**Filtrar** y entonces**Autofiltro**.

Cuando aplica un filtro automático a una hoja de trabajo, los interruptores de filtro (flechas negras) aparecen a la derecha de los encabezados de las columnas.

1. Haga clic en una flecha de filtro para ver una lista de opciones de filtro.

Algunas de las opciones de autofiltro son:

|**Opciones**|**Descripción**|
|:- |:- |
|Todos|Muestra todos los elementos de la lista una vez.|
|Disfraz|Personalice los criterios de filtro como contiene/no contiene|
|Filtrar por Color|Filtros basados en color relleno|
|Filtros de fecha|Filtra filas según diferentes criterios en la fecha|
|Filtros numéricos|Diferentes tipos de filtro en números como comparación, promedios y Top 10, etc.|
|Filtros de texto|Diferentes filtros como comienza con, termina con, contiene, etc.|
|Espacios en blanco/No espacios en blanco|Estos filtros se pueden implementar a través de Text Filter Blank|

Los usuarios filtran manualmente los datos de su hoja de trabajo en Microsoft Excel usando estas opciones.

### **Autofiltro con Aspose.Cells**

Aspose.Cells proporciona una clase, Workbook, que representa un archivo de Excel. La clase Libro de trabajo contiene una colección de Hojas de trabajo que permite el acceso a cada hoja de trabajo en el archivo de Excel.

Una hoja de trabajo está representada por la clase Worksheet. La clase Worksheet proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo. Para crear un autofiltro, use la propiedad AutoFilter de la clase Worksheet. La propiedad AutoFilter es un objeto de la clase AutoFilter, que proporciona la propiedad Range para especificar el rango de celdas que componen una fila de encabezado. Se aplica un filtro automático al rango de celdas que es la fila de encabezado.

En cada hoja de trabajo, solo puede especificar un rango de filtro. Esto está limitado por Microsoft Excel. Para el filtrado de datos personalizado, utilice el método AutoFilter.Custom.

En el ejemplo que se muestra a continuación, hemos creado el mismo Autofiltro usando Aspose.Cells que creamos usando Microsoft Excel en la sección anterior.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

#### **Diferentes tipos de filtro**

Aspose.Cells proporciona múltiples opciones para aplicar diferentes tipos de filtros como filtro de color, filtro de fecha, filtro de número, filtro de texto, filtros en blanco y filtros sin blanco.

##### **Color de relleno**

Aspose.Cells proporciona una función AddFillColorFilter para filtrar datos según la propiedad de color de relleno de las celdas. En el ejemplo que se muestra a continuación, se usa un archivo de plantilla que tiene diferentes colores de relleno en la primera columna de la hoja para probar la función de filtrado de color. Los archivos de muestra se pueden descargar desde los siguientes enlaces.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

##### **Fecha**

Se pueden implementar diferentes tipos de filtros de fecha, como filtrar todas las filas que tienen fechas en enero de 2018. El siguiente código de ejemplo demuestra este filtro usando la función AddDateFilter. A continuación se proporcionan archivos de muestra.

1. [Fecha.xlsx](72417317.xlsx)
1. [Fecha filtrada.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

##### **Fecha dinámica**

A veces, se requieren filtros dinámicos basados en la fecha, como todas las celdas que tienen fechas en enero, independientemente del año. En este caso, la función DynamicFilter se usa como se indica en el siguiente código de ejemplo. A continuación se proporcionan archivos de muestra.

1. [Fecha.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

##### **Número**

Los filtros personalizados se pueden aplicar usando Aspose.Cells como seleccionar celdas que tengan un número entre un rango dado. El siguiente ejemplo demuestra el uso de la función Custom() para filtrar números. A continuación se proporcionan archivos de muestra.

1. [Número.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

##### **Texto**

Si una columna contiene texto y se van a seleccionar celdas que contengan un texto en particular, se puede usar la función Filter(). En el siguiente ejemplo, el archivo de plantilla contiene una lista de países y se debe seleccionar la fila que contiene el nombre de un país en particular. El siguiente código demuestra el filtrado de texto. A continuación se proporcionan archivos de muestra.

1. [Texto.xlsx](72417322.xlsx)
1. [Texto filtrado.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

##### **espacios en blanco**

Si una columna contiene texto de modo que pocas celdas están en blanco y se requiere un filtro para seleccionar esas filas solo donde hay celdas en blanco, la función MatchBlanks() se puede usar como se muestra a continuación. A continuación se proporcionan archivos de muestra.

1. [En blanco.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

##### **No espacios en blanco**

Cuando se deban filtrar celdas que tengan texto, use la función de filtro MatchNonBlanks como se muestra a continuación. A continuación se proporcionan archivos de muestra.

1. [En blanco.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

##### **Filtro personalizado con Contiene**

Excel proporciona filtros personalizados como filas de filtro que contienen una cadena específica. Esta función está disponible en Aspose.Cells y se muestra a continuación filtrando los nombres en el archivo de muestra. A continuación se proporcionan archivos de muestra.

1. [origenNombresDePaísesDeMuestra.xlsx](sourseSampleCountryNames.xlsx)
1. [OutSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

##### **Filtro personalizado con NotContains**

Excel proporciona filtros personalizados como filas de filtro que no contienen una cadena específica. Esta función está disponible en Aspose.Cells y se muestra a continuación filtrando los nombres en el archivo de muestra que se proporciona a continuación.

1. [origenNombresDePaísesDeMuestra.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

##### **Filtro personalizado con BeginsWith**

Excel proporciona filtros personalizados como filas de filtro que comienzan con una cadena específica. Esta función está disponible en Aspose.Cells y se muestra a continuación filtrando los nombres en el archivo de muestra que se proporciona a continuación.

1. [origenNombresDePaísesDeMuestra.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

##### **Filtro personalizado con Termina con**

Excel proporciona filtros personalizados como filas de filtro que terminan con una cadena específica. Esta función está disponible en Aspose.Cells y se muestra a continuación filtrando los nombres en el archivo de muestra que se proporciona a continuación.

1. [origenNombresDePaísesDeMuestra.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

## **Temas avanzados**
- [Aplicar filtro avanzado de Microsoft Excel para mostrar registros que cumplen criterios complejos](/cells/es/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Obtenga todos los índices de filas ocultas después de actualizar el Autofiltro](/cells/es/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
