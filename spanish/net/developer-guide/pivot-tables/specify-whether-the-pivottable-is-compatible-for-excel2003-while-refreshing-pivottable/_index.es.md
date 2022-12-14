---
title: Especifique si la tabla dinámica es compatible con Excel 2003 mientras actualiza la tabla dinámica
type: docs
weight: 80
url: /es/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}}

 Aspose.Cells proporciona el[**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)propiedad que puede usar para especificar si la tabla dinámica es compatible con Excel2003 mientras actualiza la tabla dinámica. Si es verdadero, una cadena debe tener menos o igual a 255 caracteres, por lo que si la cadena tiene más de 255 caracteres, se truncará. Si**falso** , una cadena no tendrá la restricción antes mencionada. El valor predeterminado es**verdadero**.

{{% /alert %}}

## **Especifique si la tabla dinámica es compatible con Excel 2003 mientras actualiza la tabla dinámica**

 El siguiente código de ejemplo explica el uso de[**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) propiedad. La cadena original tiene 383 caracteres. Pero cuando[**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) se establece la propiedad**verdadero** y la tabla dinámica se actualiza, los datos de la celda B5 de la tabla dinámica se truncan y pasan a tener 255 caracteres. Sin embargo cuando[**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) se establece la propiedad**falso** y la tabla dinámica se actualiza nuevamente, los datos de la celda B5 de la tabla dinámica no se truncan y siguen teniendo 383 caracteres. Lea los comentarios dentro del código para comprender mejor esta propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
