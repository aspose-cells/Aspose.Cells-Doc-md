---
title: Copiar alturas de fila del rango de origen al rango de destino
type: docs
weight: 590
url: /es/net/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}}

A veces el usuario necesita copiar las alturas de fila del rango de origen al rango de destino. Aspose.Cells proporciona el enum [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) para este propósito. Cuando se establece la propiedad [**PasteOptions.PasteType**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions/properties/pastetype) con el enum [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype), las alturas de todas las filas dentro del rango de origen se copiarán al rango de destino.

{{% /alert %}}

El siguiente código de ejemplo explica cómo usar el enum [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) para copiar las alturas de fila del rango de origen en el rango de destino. Una vez que abra el archivo excel de salida generado por este código en Microsoft Excel, verá que las alturas de fila del rango de destino son exactamente las mismas que las alturas de fila del rango de origen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetRowHeights-GetRowHeightsOfSourceRangeToDestinationRange.cs" >}}
{{< app/cells/assistant language="csharp" >}}
