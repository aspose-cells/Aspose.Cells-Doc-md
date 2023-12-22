---
title: Clasificación de datos
type: docs
weight: 130
url: /es/net/sort-data-of-excel/
description: Aprenda a ordenar datos utilizando Aspose.Cells for .NET API.
keywords: Sort data in ascending or descending order, Sort data based on the background color
---
{{% alert color="primary" %}}

La clasificación de datos es una de las muchas funciones útiles de Microsoft Excel. Permite a los usuarios solicitar datos para facilitar el escaneo. Aspose.Cells permite a los desarrolladores ordenar los datos de la hoja de cálculo alfabética o numéricamente, lo que funciona de la misma manera que Microsoft Excel lo hace para ordenar los datos.

{{% /alert %}}

##  **Ordenar datos en Microsoft Excel**

Para ordenar datos en Microsoft Excel:

1.  Seleccionar**Datos** desde el**Clasificar** menú. Se mostrará el cuadro de diálogo Ordenar.
1. Seleccione una opción de clasificación.

Generalmente, la clasificación se realiza en una lista, definida como un grupo contiguo de datos donde los datos se muestran en columnas.

##  **Ordenar datos con Aspose.Cells**

 Aspose.Cells proporciona la[**Clasificador de datos**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)Clase utilizada para ordenar datos en orden ascendente o descendente. La clase tiene algunos miembros importantes, por ejemplo, propiedades como Clave1... Clave3 y Orden1... Orden3. Estos miembros se utilizan para definir claves ordenadas y especificar el orden de clasificación de las claves.

 Debe definir claves y establecer el orden de clasificación antes de implementar la clasificación de datos. La clase proporciona la[**Clasificar**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index)Método utilizado para realizar la clasificación de datos según los datos de las celdas de una hoja de trabajo.

 El[**Clasificar**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1)El método acepta los siguientes parámetros:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), las celdas de la hoja de trabajo subyacente.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea), el rango de celdas. Defina el área de la celda antes de aplicar la clasificación de datos.

Este ejemplo utiliza el archivo de plantilla "Book1.xls" creado en Microsoft Excel. Después de ejecutar el código siguiente, los datos se ordenan adecuadamente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

 Si desea ordenar *De izquierda a derecha*, utilice el[**Clasificador de datos.Ordenar de izquierda a derecha**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright) atributo.

{{% /alert %}}

###  **Ordenar datos con color de fondo**

Excel proporciona funciones para ordenar datos según el color de fondo. La misma característica se proporciona usando Aspose.Cells usando DataSorter donde[**Ordenar por tipo**](https://reference.aspose.com/cells/net/aspose.cells/sortontype) .CellColor se puede utilizar en[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) para ordenar datos según el color de fondo. Todas las celdas que contienen un color específico en el[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey), la función se coloca en la parte superior o inferior según la configuración SortOrder y el orden del resto de las celdas no cambia en absoluto.

A continuación se muestran los archivos de muestra que se pueden descargar para probar esta función:

[muestraBackGroundFile.xlsx](81920906.xlsx)

[muestra de salidaBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

##  **Temas avanzados**
- [Ordenar datos en columna con lista de clasificación personalizada](/cells/es/net/sort-data-in-column-with-custom-sort-list/)
- [Especificación de advertencia de clasificación al ordenar datos](/cells/es/net/specifying-sort-warning-while-sorting-data/)
