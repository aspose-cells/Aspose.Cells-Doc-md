---
title: Copiar alturas de fila del rango de origen al rango de destino
type: docs
weight: 250
url: /es/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

A veces, el usuario necesita copiar la altura de las filas del rango de origen al rango de destino. Aspose.Cells proporciona el enum [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) para este propósito. Cuando configures la propiedad [PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) con el enum [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS), las alturas de todas las filas dentro del rango de origen se copiarán al rango de destino.

{{% /alert %}} 
## **Copiar alturas de fila del rango de origen al rango de destino**
El siguiente código de ejemplo explica cómo usar el enum [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) para copiar la altura de las filas del rango de origen al rango de destino. Cuando abras el archivo excel de salida generado por este código en Microsoft Excel, verás que las alturas de fila del rango de destino son exactamente iguales a las del rango de origen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
{{< app/cells/assistant language="java" >}}
