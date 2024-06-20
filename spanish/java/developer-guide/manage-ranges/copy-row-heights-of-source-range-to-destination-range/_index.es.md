---
title: Copiar alturas de fila del rango de origen al rango de destino
type: docs
weight: 250
url: /es/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

A veces el usuario necesita copiar las alturas de las filas del rango de origen al rango de destino. Aspose.Cells proporciona el enum [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) para este propósito. Cuando establezca la propiedad [PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) con el enum [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS), las alturas de todas las filas dentro del rango de origen se copiarán al rango de destino.

{{% /alert %}} 
## **Copiar alturas de fila del rango de origen al rango de destino**
El siguiente código de muestra explica cómo usar el enum [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) para copiar las alturas de fila del rango de origen en el rango de destino. Una vez que abras el archivo de Excel de salida generado por este código en Microsoft Excel, verás que las alturas de fila del rango de destino son exactamente iguales a las alturas de fila del rango de origen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
