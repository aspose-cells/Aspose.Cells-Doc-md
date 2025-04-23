---
title: Ordenación de Datos
type: docs
weight: 130
url: /es/nodejs-cpp/sort-data-of-excel/
description: Aprende cómo ordenar datos usando la API Aspose.Cells for Node.js via C++.
keywords: Ordenar datos en orden ascendente o descendente, ordenar datos según el color de fondo
---

{{% alert color="primary" %}}

La ordenación de datos es una de las muchas funciones útiles de Microsoft Excel. Permite a los usuarios ordenar datos para facilitar su revisión. La API Aspose.Cells for Node.js via C++ permite a los desarrolladores ordenar datos en una hoja de cálculo alfabéticamente o numéricamente, de manera similar a como lo hace Microsoft Excel.

{{% /alert %}}

## **Ordenar Datos en Microsoft Excel**

Para ordenar datos en Microsoft Excel:

1. Seleccione **Datos** del menú **Ordenar**. Se mostrará el cuadro de diálogo Ordenar.
1. Seleccione una opción de ordenación.

Generalmente, la ordenación se realiza en una lista - definida como un grupo contiguo de datos donde los datos se muestran en columnas.

## **Ordenación de datos con Aspose.Cells**

La Aspose.Cells for Node.js via C++ proporciona la clase [**DataSorter**](https://reference.aspose.com/cells/nodejs-cpp/datasorter) utilizada para ordenar datos en orden ascendente o descendente. La clase tiene algunos miembros importantes, por ejemplo, propiedades como Key1 ... Key3 y Order1 ... Order3. Estos miembros se usan para definir las claves ordenadas y especificar el orden de ordenación de las claves.

Debes definir claves y establecer el orden de clasificación antes de implementar la clasificación de datos. La clase proporciona el método [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) utilizado para realizar la clasificación de datos basada en los datos de las celdas en una hoja de cálculo.

El método [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) acepta los siguientes parámetros:

- [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), las celdas para la hoja de cálculo subyacente.
- [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea), el rango de celdas. Define el área de celdas antes de aplicar la clasificación de datos.

Este ejemplo utiliza el archivo de plantilla "Book1.xls" creado en Microsoft Excel. Después de ejecutar el código a continuación, los datos se clasifican adecuadamente.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataSorting-1.js" >}}

{{% alert color="primary" %}}

Si deseas ordenar *de izquierda a derecha*, utiliza el atributo [**DataSorter.setSortLeftToRight**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortLeftToRight-boolean-).

{{% /alert %}}

### **Clasificación de datos con color de fondo**

Excel ofrece funciones para ordenar datos según el color de fondo. La misma función se proporciona con Aspose.Cells for Node.js via C++ usando DataSorter, donde [**SortOnType**](https://reference.aspose.com/cells/nodejs-cpp/sortontype/).CellColor puede usarse en [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) para ordenar datos basados en el color de fondo. Todas las celdas que contienen el color especificado en la función [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) se colocan en la parte superior o inferior según la configuración SortOrder, y el orden del resto de las celdas no se altera.

A continuación se muestran los archivos de muestra que se pueden descargar para probar esta característica:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithBackgroundColor-1.js" >}}

## **Temas avanzados**
- [Ordenar datos en una columna con lista de orden personalizado](/cells/es/nodejs-cpp/sort-data-in-column-with-custom-sort-list/)
- [Especificar advertencia de clasificación al ordenar datos](/cells/es/nodejs-cpp/specifying-sort-warning-while-sorting-data/)

