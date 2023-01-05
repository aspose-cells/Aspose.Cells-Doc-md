---
title: Copiar alturas de fila del rango de origen al rango de destino
type: docs
weight: 590
url: /es/net/copy-row-heights-of-source-range-to-destination-range/
---
{{% alert color="primary" %}}

 En algún momento, el usuario necesita copiar las alturas de las filas del rango de origen al rango de destino. Aspose.Cells proporciona[**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) enumeración para este propósito. cuando vas a establecer[**PasteOptions.PasteType**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions/properties/pastetype) propiedad con[**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) enum, las alturas de todas las filas dentro del rango de origen se copiarán en el rango de destino.

{{% /alert %}}

 El siguiente código de ejemplo explica cómo usar[**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype)enum para copiar las alturas de fila del rango de origen en el rango de destino. Una vez que abra el archivo de Excel de salida generado por este código en Microsoft Excel, verá que las alturas de las filas del rango de destino son exactamente las mismas que las alturas de las filas del rango de origen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetRowHeights-GetRowHeightsOfSourceRangeToDestinationRange.cs" >}}
