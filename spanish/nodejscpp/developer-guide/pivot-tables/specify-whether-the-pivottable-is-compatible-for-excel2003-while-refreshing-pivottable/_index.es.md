---
title: Especifique si la tabla dinámica es compatible con Excel2003 al actualizar la tabla dinámica
type: docs
weight: 80
url: /es/nodejs-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ proporciona la propiedad [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) que puede usarse para especificar si la tabla dinámica es compatible con Excel2003 al actualizar la tabla dinámica. Si es verdadero, la cadena debe tener menos o igual a 255 caracteres, por lo que si la cadena es mayor a 255 caracteres, será truncada. Si **falso**, la cadena no tendrá esta restricción. El valor predeterminado es **true**.

{{% /alert %}}

## **Especifique si la tabla dinámica es compatible con Excel2003 al actualizar la tabla dinámica**

El siguiente código de ejemplo explica el uso de la propiedad [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-). La cadena original tiene 383 caracteres de longitud. Pero cuando la propiedad [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) se establece en verdadero y se actualiza la tabla dinámica, los datos de la celda B5 de la tabla dinámica se truncan y tiene 255 caracteres de longitud. Sin embargo, cuando la propiedad [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) se establece en falso y se vuelve a actualizar la tabla dinámica, los datos de la celda B5 de la tabla dinámica no se truncan y permanecen con 383 caracteres de longitud. Por favor, lea los comentarios dentro del código para una mejor comprensión de esta propiedad.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyCompatibility-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
