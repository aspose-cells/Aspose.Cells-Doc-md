---
title: Especifique si la tabla dinámica es compatible con Excel2003 al actualizar la tabla dinámica
type: docs
weight: 80
url: /es/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells proporciona la propiedad [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) que puede utilizar para especificar si la tabla dinámica es compatible con Excel2003 al actualizar la tabla dinámica. Si es verdadero, una cadena debe ser menor o igual a 255 caracteres, por lo que si la cadena es mayor a 255 caracteres, se truncará. Si es falso, una cadena no tendrá la restricción mencionada anteriormente. El valor predeterminado es verdadero.

{{% /alert %}}

## **Especifique si la tabla dinámica es compatible con Excel2003 al actualizar la tabla dinámica**

El siguiente código de ejemplo explica el uso de la propiedad [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible). La cadena original tiene 383 caracteres de longitud. Pero cuando la propiedad [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) se establece en verdadero y se actualiza la tabla dinámica, los datos de la celda B5 de la tabla dinámica se truncan y tiene 255 caracteres de longitud. Sin embargo, cuando la propiedad [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) se establece en falso y se vuelve a actualizar la tabla dinámica, los datos de la celda B5 de la tabla dinámica no se truncan y permanecen con 383 caracteres de longitud. Por favor, lea los comentarios dentro del código para una mejor comprensión de esta propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
