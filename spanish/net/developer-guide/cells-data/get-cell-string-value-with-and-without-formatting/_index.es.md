---
title: Obtenga el valor de cadena Cell con y sin formato
type: docs
weight: 240
url: /es/net/get-cell-string-value-with-and-without-formatting/
description: Aprenda cómo obtener el valor de cadena Cell con y sin formato a través de Aspose.Cells for .NET API.
keywords: Get Cell String Value with and without Formatting, Retrieve Cell String Value with and without Formatting, Obtain Cell String Value with and without Formatting
---
{{% alert color="primary" %}}

 Aspose.Cells proporciona un método[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)que se puede utilizar para obtener el valor de cadena de la celda con o sin formato. Supongamos que tiene una celda con el valor 0,012345 y la ha formateado para mostrar solo dos decimales. Luego se mostrará como 0,01 en Excel. Puede recuperar valores de cadena como 0,01 y 0,012345 utilizando el[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) método. Se necesita[**Estrategia de formato de valor de celda**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)enumeración como un parámetro que tiene los siguientes valores

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.Ninguno

{{% /alert %}}

 El siguiente código de muestra explica el uso de[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)método.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
