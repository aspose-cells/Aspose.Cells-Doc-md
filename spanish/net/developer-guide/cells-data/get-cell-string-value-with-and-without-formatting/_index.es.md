---
title: Obtenga el valor de cadena Cell con y sin formato
type: docs
weight: 240
url: /es/net/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells proporciona un método[**Cell.ObtenerValorDeCadena()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) que se puede usar para obtener el valor de cadena de la celda con o sin formato. Suponga que tiene una celda con valor 0.012345 y la ha formateado para mostrar solo dos lugares decimales. Luego se mostrará como 0.01 en Excel. Puede recuperar valores de cadena como 0.01 y como 0.012345 usando el[**Cell.ObtenerValorDeCadena()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) método. Se necesita[**CellValueFormatoEstrategia**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)enum como un parámetro que tiene los siguientes valores

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.Ninguno

{{% /alert %}}

 El siguiente código de ejemplo explica el uso de[**Cell.ObtenerValorDeCadena()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)método.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
