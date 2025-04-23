---
title: Quellenbereichszeilenhöhen in Zielbereich kopieren
type: docs
weight: 250
url: /de/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

Manchmal muss der Benutzer die Zeilenhöhen aus dem Quellbereich in den Zielbereich kopieren. Aspose.Cells bietet die [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) Enumeration für diesen Zweck. Wenn Sie die [PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) Eigenschaft mit der [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) Enumeration setzen, werden die Höhen aller Zeilen im Quellbereich in den Zielbereich kopiert.

{{% /alert %}} 
## **Zeilenhöhen des Quellbereichs in den Zielbereich kopieren**
Der folgende Beispielcode zeigt, wie die [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) Enumeration verwendet wird, um die Zeilenhöhen des Quellbereichs in den Zielbereich zu kopieren. Wenn Sie die erzeugte Excel-Datei in Microsoft Excel öffnen, sehen Sie, dass die Zeilenhöhen des Zielbereichs genau den des Quellbereichs entsprechen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
{{< app/cells/assistant language="java" >}}
