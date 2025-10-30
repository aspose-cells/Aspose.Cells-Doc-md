---
title: Ordenación de datos con Golang mediante C++
linktitle: Ordenación de Datos
type: docs
weight: 130
url: /es/go-cpp/sort-data-of-excel/
description: Aprende cómo ordenar datos usando la API Aspose.Cells for C++.
keywords: Ordenar datos en orden ascendente o descendente, ordenar datos según el color de fondo
---

{{% alert color="primary" %}}

La ordenación de datos es una de las muchas funciones útiles de Microsoft Excel. Permite a los usuarios ordenar los datos para que sea más fácil escanearlos. Aspose.Cells permite a los desarrolladores ordenar datos de hojas de cálculo alfabética o numéricamente, que funciona de la misma manera que Microsoft Excel para ordenar datos.

{{% /alert %}}

## **Ordenar Datos en Microsoft Excel**

Para ordenar datos en Microsoft Excel:

1. Seleccione **Datos** del menú **Ordenar**. Se mostrará el cuadro de diálogo Ordenar.
1. Seleccione una opción de ordenación.

Generalmente, la ordenación se realiza en una lista - definida como un grupo contiguo de datos donde los datos se muestran en columnas.

## **Ordenación de datos con Aspose.Cells**

Aspose.Cells proporciona la clase [**DataSorter**](https://reference.aspose.com/cells/go-cpp/datasorter/) utilizada para ordenar datos en orden ascendente o descendente. La clase tiene algunos miembros importantes, por ejemplo, propiedades como Key1 ... Key3 y Order1 ... Order3. Estos miembros se utilizan para definir claves ordenadas y especificar el orden de clasificación de la clave.

Debes definir claves y establecer el orden de clasificación antes de implementar la clasificación de datos. La clase proporciona el método [**Sort**](https://reference.aspose.com/cells/go-cpp/datasorter/sort_cells_int_int_int_int/) utilizado para realizar la clasificación de datos basada en los datos de las celdas en una hoja de cálculo.

El método [**Sort**](https://reference.aspose.com/cells/go-cpp/datasorter/sort_cells_int_int_int_int/) acepta los siguientes parámetros:

- [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/), las celdas para la hoja de cálculo subyacente.
- [**CellArea**](https://reference.aspose.com/cells/go-cpp/cellarea/), el rango de celdas. Define el área de celdas antes de aplicar la clasificación de datos.

Este ejemplo utiliza el archivo de plantilla "Book1.xls" creado en Microsoft Excel. Después de ejecutar el código a continuación, los datos se clasifican adecuadamente.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSorting.go" >}}
{{% alert color="primary" %}}

Si deseas ordenar *de izquierda a derecha*, utiliza el atributo [**DataSorter.GetSortLeftToRight()**](https://reference.aspose.com/cells/go-cpp/datasorter/getsortlefttoright/).

{{% /alert %}}

### **Clasificación de datos con color de fondo**

Excel proporciona características para clasificar datos basados en el color de fondo. La misma característica se proporciona utilizando Aspose.Cells usando DataSorter donde [**SortOnType**](https://reference.aspose.com/cells/go-cpp/sortontype/).CellColor se puede utilizar en [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) para ordenar datos basados en el color de fondo. Todas las celdas que contienen el color especificado en la [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/), la función se colocan en la parte superior o inferior según la configuración de SortOrder y el orden del resto de las celdas no cambia en absoluto.

A continuación se muestran los archivos de muestra que se pueden descargar para probar esta característica:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSorting-1.go" >}}
## **Temas avanzados**
- [Ordenar datos en una columna con lista de orden personalizado](/cells/es/cpp/sort-data-in-column-with-custom-sort-list/)
- [Especificar advertencia de clasificación al ordenar datos](/cells/es/cpp/specifying-sort-warning-while-sorting-data/)
