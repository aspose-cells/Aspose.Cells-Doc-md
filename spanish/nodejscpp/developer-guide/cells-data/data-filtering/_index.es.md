---
title: Filtrado de Datos
type: docs
weight: 85
url: /es/nodejs-cpp/data-filtering/
description: Aprende cómo agregar filtros de datos usando la API Aspose.Cells for Node.js via C++.
keywords: AgregarFiltroPorColor Node.js vía C++, AgregarFiltrosPorFecha Node.js vía C++, AgregarFiltrosPorNúmero Node.js vía C++, AgregarFiltroDinámico Node.js vía C++, AgregarFiltrosDeTexto Node.js vía C++, AgregarFiltroPersonalizado ConContains Node.js vía C++, AgregarFiltroPersonalizado ConNotContains Node.js vía C++, AgregarFiltroPersonalizado ConBeginsWith Node.js vía C++, AgregarFiltroPersonalizado ConEndsWith Node.js vía C++
---

{{% alert color="primary" %}}
Microsoft Excel ofrece buenas funciones para autofiltrar datos de hojas de cálculo. Aspose.Cells soporta completamente las funciones de autofiltrado de Microsoft Excel. Este artículo explica cómo usar las funciones en Microsoft Excel y cómo programarlas usando Aspose.Cells for Node.js via C++.
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

### **Autofiltrado con Aspose.Cells for Node.js via C++**

Aspose.Cells proporciona una clase, Workbook que representa un archivo de Excel. La clase Workbook contiene una colección de Worksheets que permite el acceso a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase Worksheet. La clase Worksheet proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para crear un autofiltro, utilice la propiedad AutoFilter de la clase Worksheet. La propiedad AutoFilter es un objeto de la clase AutoFilter, que proporciona la propiedad Range para especificar el rango de celdas que forman una fila de encabezado. Un autofiltro se aplica al rango de celdas que es la fila de encabezado.

En cada hoja de cálculo, solo se puede especificar un rango de filtro. Esto está limitado por Microsoft Excel. Para el filtrado personalizado de datos, utilice el método AutoFilter.Custom.

En el ejemplo a continuación, hemos creado el mismo Autofiltrado usando Aspose.Cells for Node.js via C++ como cuando lo hicimos usando Microsoft Excel en la sección anterior.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter.js" >}}

#### **Diferentes tipos de filtro**

Aspose.Cells ofrece múltiples opciones para aplicar diferentes tipos de filtros como Filtro de Color, Filtro de Fecha, Filtro de Número, Filtro de Texto, Filtros en Blanco y Filtros no en Blanco.

##### **Color de relleno**

Aspose.Cells provee una función AddFillColorFilter para filtrar datos basados en la propiedad de color de relleno de las celdas. En el ejemplo dado a continuación, se utiliza un archivo de plantilla con diferentes colores de relleno en la primera columna de la hoja para probar la función de filtrado por color. Los archivos de muestra se pueden descargar desde los siguientes enlaces.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FillColor.js" >}}


##### **Fecha**

Se pueden implementar diferentes tipos de filtros de fecha, como filtrar todas las filas con fechas en enero de 2018. El siguiente ejemplo muestra cómo implementar este filtro usando la función AddDateFilter. Se proporcionan archivos de ejemplo.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Date.js" >}}


##### **Fecha dinámica**

A veces se requieren filtros dinámicos basados en la fecha, como todas las celdas que tienen fechas en enero, independientemente del año. En este caso, se utiliza la función DynamicFilter según se muestra en el siguiente ejemplo de código. Se proporcionan los archivos de ejemplo a continuación.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-DynamicFilter.js" >}}


##### **Número**

Se pueden aplicar filtros personalizados utilizando Aspose.Cells como seleccionar celdas que tengan números dentro de un rango dado. El siguiente ejemplo demuestra el uso de la función Custom() para filtrar números. Los archivos de muestra se dan a continuación.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Number.js" >}}


##### **Texto**

Si una columna contiene texto y se desea seleccionar celdas que contienen un texto en particular, se puede usar la función Filter(). En el siguiente ejemplo, el archivo de plantilla contiene una lista de países y se desea seleccionar la fila que contiene un nombre de país en particular. El siguiente código demuestra cómo filtrar texto. Se proporcionan archivos de ejemplo.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Text.js" >}}


##### **Vacíos**

Si una columna contiene texto y algunas celdas están en blanco, y se requiere un filtro para seleccionar solo aquellas filas donde las celdas en blanco están presentes, se puede utilizar la función CoincidirBlancos() como se demuestra a continuación. Los archivos de ejemplo se muestran a continuación.

1. [EnBlanco.xlsx](72417324.xlsx)
1. [EnBlancoFiltrado.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Blanks.js" >}}


##### **No vacíos**

Cuando se deben filtrar celdas que contienen texto, utilizar la función de filtro CoincidirNoVacios como se demuestra a continuación. Los archivos de ejemplo se muestran a continuación.

1. [EnBlanco.xlsx](72417324.xlsx)
1. [NoVaciosFiltrado.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-NonBlanks.js" >}}


##### **Filtro personalizado con Contiene**

Excel proporciona filtros personalizados como filtrar filas que contienen alguna cadena específica. Esta función está disponible en Aspose.Cells y se demuestra a continuación filtrando los nombres en el archivo de muestra. Se proporcionan archivos de ejemplo a continuación.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-Contains.js" >}}


##### **Filtro personalizado con NoContiene**

Excel proporciona filtros personalizados como filtrar filas que no contienen una cadena específica. Esta función está disponible en Aspose.Cells y se demuestra a continuación filtrando los nombres en el archivo de muestra.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-NotContains.js" >}}


##### **Filtro personalizado que comienza con**

Excel proporciona filtros personalizados como filtrar filas que comienzan con una cadena específica. Esta función está disponible en Aspose.Cells y se demuestra a continuación filtrando los nombres en el archivo de muestra.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-BeginsWith.js" >}}


##### **Filtro personalizado que termina con**

Excel proporciona filtros personalizados como filtrar filas que terminan con una cadena específica. Esta función está disponible en Aspose.Cells y se muestra a continuación filtrando los nombres en el archivo de muestra proporcionado a continuación.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-EndsWith.js" >}}


## **Temas avanzados**
- [Aplicar Filtro Avanzado de Microsoft Excel para Mostrar Registros que Cumplen Criterios Complejos](/cells/es/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Obtener Todos los Índices de Filas Ocultas Después de Actualizar el Autofiltro](/cells/es/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
