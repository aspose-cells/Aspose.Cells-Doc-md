---
title: Obtener el valor de cadena de la celda con o sin formato
type: docs
weight: 240
url: /es/net/get-cell-string-value-with-and-without-formatting/
description: Aprenda cómo obtener el valor de cadena de la celda con o sin formato a través de la API Aspose.Cells for .NET.
keywords: Obtener el valor de cadena de la celda con o sin formato, recuperar el valor de cadena de la celda con o sin formato, obtener el valor de cadena de la celda con o sin formato
---

{{% alert color="primary" %}}

Aspose.Cells proporciona un método [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) que se puede usar para obtener el valor de cadena de la celda con o sin ningún formato. Suponga que tiene una celda con el valor 0.012345 y lo ha formateado para mostrar solo dos decimales. Entonces se mostrará como 0.01 en Excel. Puede recuperar los valores de cadena tanto como 0.01 como 0.012345 utilizando el método [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue). Toma un parámetro de tipo [**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy/) enum que tiene los siguientes valores

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

El siguiente código de ejemplo explica el uso del método [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
