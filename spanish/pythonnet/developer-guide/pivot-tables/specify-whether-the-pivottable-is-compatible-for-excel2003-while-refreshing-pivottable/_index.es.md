---
title: Especifique si la tabla dinámica es compatible con Excel2003 al actualizar la tabla dinámica
type: docs
weight: 80
url: /es/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Este artículo muestra cómo especificar si la tabla dinámica es compatible con Excel2003 al actualizar la tabla dinámica con Aspose.Cells para Python via .NET.
keywords: Aspose.Cells para Python Excel, biblioteca de Excel Python, Especificar si la tabla dinámica es compatible con Excel2003 al actualizar la tabla dinámica
---

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET proporciona la propiedad [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) que puede usar para especificar si la tabla dinámica es compatible con Excel2003 al actualizar la tabla dinámica. Si es verdadero, una cadena debe ser menor o igual a 255 caracteres, por lo que, si la cadena es mayor que 255 caracteres, se truncará. Si es **falso**, una cadena no tendrá la restricción mencionada anteriormente. El valor predeterminado es **verdadero**.

{{% /alert %}}

## **Cómo especificar si la tabla dinámica es compatible con Excel2003 al actualizar la tabla dinámica**

El siguiente código de ejemplo explica el uso de la propiedad [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/). La cadena original tiene 383 caracteres de longitud. Pero cuando la propiedad [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) se establece en verdadero y se actualiza la tabla dinámica, los datos de la celda B5 de la tabla dinámica se truncan y tiene 255 caracteres de longitud. Sin embargo, cuando la propiedad [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) se establece en falso y se vuelve a actualizar la tabla dinámica, los datos de la celda B5 de la tabla dinámica no se truncan y permanecen con 383 caracteres de longitud. Por favor, lea los comentarios dentro del código para una mejor comprensión de esta propiedad.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
