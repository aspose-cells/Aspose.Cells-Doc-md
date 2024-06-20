---
title: Especifique si la tabla dinámica es compatible con Excel2003 al actualizar la tabla dinámica
type: docs
weight: 880
url: /es/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}} 

Aspose.Cells proporciona la propiedad [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) que puede utilizar para especificar si la tabla dinámica es compatible con Excel2003 al actualizar la tabla dinámica. Si es **verdadero**, una cadena debe ser menor o igual a 255 caracteres, por lo que si la cadena es mayor a 255 caracteres, se truncará. Si es **falso**, una cadena no tendrá la restricción mencionada. El valor predeterminado es **verdadero**.

{{% /alert %}} 
## **Especifique si la tabla dinámica es compatible con Excel2003 al actualizar la tabla dinámica**
El siguiente código de muestra explica el uso de la propiedad [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible). La cadena original tiene una longitud de 383 caracteres. Pero cuando se establece [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) en **verdadero** y se actualiza la tabla dinámica, los datos de la celda B5 de la tabla dinámica se truncan y tienen una longitud de 255 caracteres. Sin embargo, cuando se establece [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) en **falso** y se actualiza nuevamente la tabla dinámica, los datos de la celda B5 de la tabla dinámica no se truncan y siguen teniendo una longitud de 383 caracteres. Descargue también el [archivo de Excel de muestra](5472558.xlsx) utilizado en este código, el [archivo de Excel de salida](5472557.xlsx) generado por él y su salida de consola para su referencia. También lea los comentarios dentro del código para comprender mejor esta propiedad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **Salida de la consola**
Esta es la salida de consola del código de muestra anterior cuando se ejecuta con el [archivo de Excel de muestra](5472558.xlsx) dado.



{{< highlight java >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
