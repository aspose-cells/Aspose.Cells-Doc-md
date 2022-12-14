---
title: Clasificación de datos
type: docs
weight: 130
url: /es/net/sort-data-of-excel/
---
{{% alert color="primary" %}}

La clasificación de datos es una de las muchas características útiles de Microsoft Excel. Permite a los usuarios ordenar datos para que sea más fácil de escanear. Aspose.Cells permite a los desarrolladores ordenar los datos de la hoja de trabajo alfabética o numéricamente, lo que funciona de la misma manera que Microsoft Excel para ordenar los datos.

{{% /alert %}}

## **Clasificación de datos en Microsoft Excel**

Para ordenar datos en Microsoft Excel:

1.  Seleccione**Datos** desde el**Clasificar** menú. Se mostrará el cuadro de diálogo Ordenar.
1. Seleccione una opción de clasificación.

Generalmente, la clasificación se realiza en una lista, definida como un grupo contiguo de datos donde los datos se muestran en columnas.

## **Clasificación de datos con Aspose.Cells**

 Aspose.Cells proporciona el[**clasificador de datos**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)clase utilizada para ordenar datos en orden ascendente o descendente. La clase tiene algunos miembros importantes, por ejemplo, propiedades como Key1 ... Key3 y Order1 ... Order3. Estos miembros se utilizan para definir claves ordenadas y especificar el orden de clasificación de las claves.

 Debe definir claves y establecer el orden de clasificación antes de implementar la clasificación de datos. La clase proporciona la[**Clasificar**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index)método utilizado para realizar la clasificación de datos en función de los datos de celda en una hoja de trabajo.

 los[**Clasificar**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1)método acepta los siguientes parámetros:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), las celdas de la hoja de cálculo subyacente.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea), el rango de celdas. Defina el área de la celda antes de aplicar la clasificación de datos.

Este ejemplo utiliza el archivo de plantilla "Book1.xls" creado en Microsoft Excel. Después de ejecutar el siguiente código, los datos se ordenan adecuadamente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

 Si quieres ordenar*De izquierda a derecha* , utilizar el[**Clasificador de datos. Ordenar de izquierda a derecha**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright) atributo.

{{% /alert %}}

### **Ordenar datos con color de fondo**

 Excel proporciona funciones para ordenar los datos según el color de fondo. La misma característica se proporciona usando Aspose.Cells usando DataSorter donde[**ordenar por tipo**](https://reference.aspose.com/cells/net/aspose.cells/sortontype) .CellColor se puede utilizar en[**Agregar clave ()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) para ordenar los datos según el color de fondo. Todas las celdas que contienen el color especificado en el[**Agregar clave ()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey), la función se coloca en la parte superior o inferior de acuerdo con la configuración de SortOrder y el orden del resto de las celdas no cambia en absoluto.

Los siguientes son los archivos de muestra que se pueden descargar para probar esta función:

[muestraBackGroundFile.xlsx](81920906.xlsx)

[ejemplo de salidaBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

## **Temas avanzados**
- [Ordenar datos en columna con lista de ordenación personalizada](/cells/es/net/sort-data-in-column-with-custom-sort-list/)
- [Especificación de advertencia de ordenación al ordenar datos](/cells/es/net/specifying-sort-warning-while-sorting-data/)
