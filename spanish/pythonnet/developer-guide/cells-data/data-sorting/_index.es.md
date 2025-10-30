---
title: Ordenación de Datos
type: docs
weight: 130
url: /es/python-net/sort-data-of-excel/
description: Aprenda cómo ordenar datos utilizando la API de Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Ordenar datos en Python en orden ascendente o descendente, Ordenar datos en Python basados en el color de fondo.
---

{{% alert color="primary" %}}

La ordenación de datos es una de las muchas funciones útiles de Microsoft Excel. Permite a los usuarios ordenar datos para que sea más fácil de escanear. Aspose.Cells para Python via .NET permite a los desarrolladores ordenar datos de hojas de cálculo alfabética o numéricamente, funcionando de la misma manera que Microsoft Excel para ordenar datos.

{{% /alert %}}

## **Ordenar Datos en Microsoft Excel**

Para ordenar datos en Microsoft Excel:

1. Seleccione **Datos** del menú **Ordenar**. Se mostrará el cuadro de diálogo Ordenar.
1. Seleccione una opción de ordenación.

Generalmente, la ordenación se realiza en una lista - definida como un grupo contiguo de datos donde los datos se muestran en columnas.

## **Ordenar Datos con la Biblioteca Excel de Python Aspose.Cells**

Aspose.Cells for Python via .NET proporciona la clase [**DataSorter**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter) utilizada para ordenar datos en orden ascendente o descendente. La clase tiene algunos miembros importantes, por ejemplo, propiedades como Key1 ... Key3 y Order1 ... Order3. Estos miembros se utilizan para definir claves ordenadas y especificar el orden de clasificación de las claves.

Debes definir claves y establecer el orden de clasificación antes de implementar la clasificación de datos. La clase proporciona el método [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) utilizado para realizar la clasificación de datos basada en los datos de las celdas en una hoja de cálculo.

El método [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) acepta los siguientes parámetros:

- [**aspose.cells.Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), las celdas para la hoja de cálculo subyacente.
- [**aspose.cells.CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea), el rango de celdas. Define el área de celdas antes de aplicar la clasificación de datos.

Este ejemplo utiliza el archivo de plantilla "Book1.xls" creado en Microsoft Excel. Después de ejecutar el código a continuación, los datos se clasifican adecuadamente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DataSorting-1.py" >}}

{{% alert color="primary" %}}

Si deseas ordenar *de izquierda a derecha*, utiliza el atributo [**DataSorter.sort_left_to_right**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_left_to_right/).

{{% /alert %}}

### **Clasificación de datos con color de fondo utilizando la biblioteca de Excel Aspose.Cells para Python**

Excel proporciona funciones para clasificar datos basados en el color de fondo. La misma funcionalidad se proporciona utilizando Aspose.Cells para Python via .NET mediante DataSorter donde [**SortOnType**](https://reference.aspose.com/cells/python-net/aspose.cells/sortontype/). CellColor puede ser utilizado en [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any) para ordenar datos basados en el color de fondo. Todas las celdas que contienen el color especificado en la [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any), función se colocan en la parte superior o inferior según el orden de clasificación y el orden del resto de las celdas no cambia en absoluto.

A continuación se muestran los archivos de muestra que se pueden descargar para probar esta característica:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithBackgroundColor-1.py" >}}

## **Temas avanzados**
- [Ordenar datos en una columna con lista de orden personalizado](/cells/es/python-net/sort-data-in-column-with-custom-sort-list/)
- [Especificar advertencia de clasificación al ordenar datos](/cells/es/python-net/specifying-sort-warning-while-sorting-data/)
{{< app/cells/assistant language="python-net" >}}
