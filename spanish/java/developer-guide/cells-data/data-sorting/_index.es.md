---
title: Ordenación de Datos
type: docs
weight: 90
url: /es/java/sort-data-of-excel/
---

{{% alert color="primary" %}}

La clasificación de datos es una de las muchas funciones útiles de Microsoft Excel. Permite a los usuarios ordenar datos para que sea más fácil de escanear.

Aspose.Cells te permite ordenar datos de la hoja de cálculo alfabética o numéricamente. Funciona de la misma manera que Microsoft Excel para ordenar datos.

{{% /alert %}}

## **Ordenar Datos en Microsoft Excel**

Para ordenar datos en Microsoft Excel:

1. Selecciona **Datos** en el menú **Ordenar**.
   Se muestra el cuadro de diálogo Ordenar.
1. Seleccione una opción de ordenación.

Generalmente, la ordenación se realiza en una lista - definida como un grupo contiguo de datos donde los datos se muestran en columnas.

**El cuadro de diálogo de ordenar en Microsoft Excel**

![todo:image_alt_text](data-sorting_1.png)

## **Ordenación de datos con Aspose.Cells**

Aspose.Cells proporciona la clase [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) utilizada para ordenar datos en orden ascendente o descendente. La clase tiene miembros importantes, por ejemplo, métodos como [**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1)... [**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2)... y [**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1)... [**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2). Estos miembros se utilizan para definir claves ordenadas y especificar el orden de clasificación de la clave.

Debes definir claves y establecer el orden de clasificación antes de implementar la clasificación de datos. La clase proporciona el método [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) utilizado para realizar la clasificación de datos basada en los datos de las celdas en una hoja de cálculo.

El método [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) acepta los siguientes parámetros:

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), las celdas de la hoja de cálculo.
- [**CellArea**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea), el rango de celdas. Define el área de celdas antes de aplicar la clasificación de datos.

Este ejemplo muestra cómo ordenar datos usando la API de Aspose.Cells. El ejemplo utiliza un archivo de plantilla "Book1.xls" y ordena datos para el rango de datos (A1:B14) en la primera hoja de cálculo:

Este ejemplo utiliza el archivo de plantilla "Book1.xls" creado en Microsoft Excel.

**Archivo de Excel de plantilla completo con datos**

![todo:image_alt_text](data-sorting_2.png)

Después de ejecutar el siguiente código, los datos se ordenan apropiadamente, como se puede ver en el archivo de Excel de salida.

**Archivo de Excel de salida después de ordenar datos**

![todo:image_alt_text](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

Para ordenar *de izquierda a derecha*, use el atributo [**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight).

{{% /alert %}}

## **Clasificación de datos con color de fondo**

Excel proporciona la función de ordenar datos basados en el color de fondo. La misma función se proporciona usando Aspose.Cells utilizando [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) donde [**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR) puede ser usado en [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)) para ordenar datos basados en el color de fondo. Todas las celdas que contienen un color especificado en la [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)), función se colocan en la parte superior o inferior según la configuración de SortOrder y el orden del resto de las celdas no cambia en absoluto.

A continuación se muestran los archivos de muestra que se pueden descargar para probar esta característica:

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **Temas avanzados**
- [Ordenar datos en una columna con lista de orden personalizado](/cells/es/java/sort-data-in-column-with-custom-sort-list/)
- [Especificar advertencia de clasificación al ordenar datos](/cells/es/java/specifying-sort-warning-while-sorting-data/)

