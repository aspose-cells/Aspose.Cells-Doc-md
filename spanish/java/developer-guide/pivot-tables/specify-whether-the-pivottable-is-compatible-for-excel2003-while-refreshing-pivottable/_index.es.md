---
title: Especifique si la tabla dinámica es compatible con Excel 2003 mientras actualiza la tabla dinámica
type: docs
weight: 880
url: /es/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}} 

 Aspose.Cells proporciona el[PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)propiedad que puede usar para especificar si la tabla dinámica es compatible con Excel2003 mientras actualiza la tabla dinámica. Si**verdadero** , una cadena debe tener menos o igual a 255 caracteres, por lo que si la cadena tiene más de 255 caracteres, se truncará. Si**falso** , una cadena no tendrá la restricción antes mencionada. El valor predeterminado es**verdadero**.

{{% /alert %}} 
## **Especifique si la tabla dinámica es compatible con Excel 2003 mientras actualiza la tabla dinámica**
 El siguiente código de ejemplo explica el uso de[PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) propiedad. La cadena original tiene 383 caracteres. Pero cuando[PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) la propiedad se establece en**verdadero** y la tabla dinámica se actualiza, los datos de la celda B5 de la tabla dinámica se truncan y pasan a tener 255 caracteres. Sin embargo cuando[PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) se establece la propiedad**falso** y la tabla dinámica se actualiza nuevamente, los datos de la celda B5 de la tabla dinámica no se truncan y siguen teniendo 383 caracteres. Por favor descarga el[ejemplo de archivo de Excel](5472558.xlsx) utilizado en este código,[archivo de salida de Excel](5472557.xlsx) generado por él y su salida de consola para su referencia. Lea también los comentarios dentro del código para una mejor comprensión de esta propiedad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **Salida de consola**
Aquí está la salida de la consola del código de muestra anterior cuando se ejecuta con el dado[ejemplo de archivo de Excel](5472558.xlsx).



{{< highlight "java" >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
