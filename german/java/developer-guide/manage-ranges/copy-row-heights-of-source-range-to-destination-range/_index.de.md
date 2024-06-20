---
title: Quellenbereichszeilenhöhen in Zielbereich kopieren
type: docs
weight: 250
url: /de/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

Manchmal müssen Benutzer die Zeilenhöhen des Quellenbereichs in den Zielbereich kopieren. Aspose.Cells bietet das [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS)-Enum für diesen Zweck. Wenn Sie die Eigenschaft [PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) mit dem Enum [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) setzen, werden die Höhen aller Zeilen innerhalb des Quellenbereichs in den Zielbereich kopiert.

{{% /alert %}} 
## **Zeilenhöhen des Quellbereichs in den Zielbereich kopieren**
Der folgende Beispielscode erläutert, wie das [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS)-Enum verwendet wird, um die Zeilenhöhen des Quellenbereichs in den Zielbereich zu kopieren. Sobald Sie die Ausgabedatei öffnen, die durch diesen Code in Microsoft Excel generiert wurde, werden Sie feststellen, dass die Zeilenhöhen des Zielbereichs genau den Zeilenhöhen des Quellenbereichs entsprechen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
