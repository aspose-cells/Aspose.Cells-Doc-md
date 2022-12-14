---
title: Copiar alturas de fila del rango de origen al rango de destino
type: docs
weight: 250
url: /es/java/copy-row-heights-of-source-range-to-destination-range/
---
{{% alert color="primary" %}} 

 En algún momento, el usuario necesita copiar las alturas de las filas del rango de origen al rango de destino. Aspose.Cells proporciona[PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) enumeración para este propósito. cuando vas a establecer[PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) propiedad con[PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) enum, las alturas de todas las filas dentro del rango de origen se copiarán en el rango de destino.

{{% /alert %}} 
## **Copiar alturas de fila del rango de origen al rango de destino**
 El siguiente código de ejemplo explica cómo usar[PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS)enum para copiar las alturas de fila del rango de origen en el rango de destino. Una vez que abra el archivo de Excel de salida generado por este código en Microsoft Excel, verá que las alturas de las filas del rango de destino son exactamente las mismas que las alturas de las filas del rango de origen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
