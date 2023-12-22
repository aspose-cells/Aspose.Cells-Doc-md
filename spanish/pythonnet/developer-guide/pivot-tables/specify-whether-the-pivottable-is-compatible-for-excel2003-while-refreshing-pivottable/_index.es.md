---
title: Especifique si la tabla dinámica es compatible con Excel2003 mientras actualiza la tabla dinámica
type: docs
weight: 80
url: /es/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Este artículo muestra cómo especificar si la tabla dinámica es compatible con Excel2003 mientras se actualiza la tabla dinámica con Aspose.Cells for Python via .NET.
keywords: Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET proporciona la[**Tabla dinámica.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) propiedad que puede utilizar para especificar si la tabla dinámica es compatible con Excel2003 mientras actualiza la tabla dinámica. Si es verdadero, una cadena debe tener menos o igual de 255 caracteres, por lo que si la cadena tiene más de 255 caracteres, se truncará. Si es *falso**, una cadena no tendrá la restricción antes mencionada. El valor por defecto es verdadero**.

{{% /alert %}}

##  **Especifique si la tabla dinámica es compatible con Excel2003 mientras actualiza la tabla dinámica**

 El siguiente código de muestra explica el uso de[**Tabla dinámica.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) propiedad. La cadena original tiene 383 caracteres. Pero cuando[**Tabla dinámica.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) la propiedad está establecida**verdadero** y se actualiza la tabla dinámica, los datos de la celda B5 de la tabla dinámica se truncan y tienen 255 caracteres. Sin embargo cuando[**Tabla dinámica.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) la propiedad está establecida**FALSO** la tabla dinámica se actualiza nuevamente, los datos de la celda B5 de la tabla dinámica no se truncan y permanecen con 383 caracteres. Lea los comentarios dentro del código para comprender mejor esta propiedad.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
