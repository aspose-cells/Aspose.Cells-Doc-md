---
title: Clasificación de datos
type: docs
weight: 90
url: /es/java/sort-data-of-excel/
---
{{% alert color="primary" %}}

La clasificación de datos es una de las muchas características útiles de Microsoft Excel. Permite a los usuarios ordenar datos para que sea más fácil de escanear.

Aspose.Cells le permite ordenar los datos de la hoja de trabajo alfabética o numéricamente. Funciona de la misma manera que Microsoft Excel para ordenar datos.

{{% /alert %}}

## **Clasificación de datos en Microsoft Excel**

Para ordenar datos en Microsoft Excel:

1.  Seleccione**Datos** desde el**Clasificar** menú.
 Se muestra el cuadro de diálogo Ordenar.
1. Seleccione una opción de clasificación.

Generalmente, la clasificación se realiza en una lista, definida como un grupo contiguo de datos donde los datos se muestran en columnas.

**El cuadro de diálogo Ordenar en Microsoft Excel**

![todo:imagen_alternativa_texto](data-sorting_1.png)

## **Clasificación de datos con Aspose.Cells**

 Aspose.Cells proporciona el[**clasificador de datos**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) clase utilizada para ordenar datos en orden ascendente o descendente. La clase tiene algunos miembros importantes, por ejemplo, métodos como[**establecerClave1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) ... [**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2) y[**establecerPedido1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1) ... [**establecerPedido2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2)Estos miembros se utilizan para definir claves ordenadas y especificar el orden de clasificación de las claves.

 Debe definir claves y establecer el orden de clasificación antes de implementar la clasificación de datos. La clase proporciona la[**clasificar**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) método utilizado para realizar la clasificación de datos en función de los datos de celda en una hoja de cálculo.

 los[**clasificar**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) método acepta los siguientes parámetros:

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), las celdas de la hoja de cálculo.
- [**área de celda**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea), el rango de celdas. Defina el área de la celda antes de aplicar la clasificación de datos.

Este ejemplo muestra cómo ordenar datos usando Aspose.Cells API. El ejemplo usa un archivo de plantilla "Book1.xls" y ordena datos por rango de datos (A1:B14) en la primera hoja de trabajo:

Este ejemplo utiliza el archivo de plantilla "Book1.xls" creado en Microsoft Excel.

**Archivo de plantilla de Excel completo con datos**

![todo:imagen_alternativa_texto](data-sorting_2.png)

Después de ejecutar el código a continuación, los datos se ordenan de manera adecuada, como puede ver en el archivo de salida de Excel.

**Archivo de salida de Excel después de ordenar los datos**

![todo:imagen_alternativa_texto](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

 Para ordenar*De izquierda a derecha* , utilizar el[**Clasificador de datos. Ordenar de izquierda a derecha**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight) atributo.

{{% /alert %}}

## **Ordenar datos con color de fondo**

 Excel proporciona la función para ordenar los datos según el color de fondo. La misma característica se proporciona usando Aspose.Cells usando[**clasificador de datos**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) dónde[**OrdenarPorTipo.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR) se puede utilizar en[**añadirClave()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int) ) para ordenar los datos según el color de fondo. Todas las celdas que contienen el color especificado en el[**añadirClave()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)), la función se coloca en la parte superior o inferior de acuerdo con la configuración de SortOrder y el orden del resto de las celdas no cambia en absoluto.

Los siguientes son los archivos de muestra que se pueden descargar para probar esta función:

[muestraBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[ejemplo de salidaBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **Temas avanzados**
- [Ordenar datos en columna con lista de ordenación personalizada](/cells/es/java/sort-data-in-column-with-custom-sort-list/)
- [Especificación de advertencia de ordenación al ordenar datos](/cells/es/java/specifying-sort-warning-while-sorting-data/)

