---
title: Generieren von Miniaturbildern für bedingte Formatierung DataBars
type: docs
weight: 170
url: /de/java/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Manchmal muss man Bilder von bedingten Formatierungen DataBars generieren. Sie können die Methode von Aspose.Cells [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage-com.aspose.cells.Cell-com.aspose.cells.ImageOrPrintOptions-) verwenden, um diese Bilder zu generieren. In diesem Artikel wird gezeigt, wie man ein DataBar-Bild mit Aspose.Cells generiert.

{{% /alert %}}

## **Beispiel**

Der folgende Beispielcode generiert das DataBar-Bild der Zelle C1. Zuerst greift er auf das Formatbedingungsobjekt der Zelle zu und dann greift er aus diesem Objekt auf das DataBar-Objekt zu und verwendet seine [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage-com.aspose.cells.Cell-com.aspose.cells.ImageOrPrintOptions-)-Methode, um das Bild der Zelle zu generieren. Schließlich speichert er das Bild auf der Festplatte.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
{{< app/cells/assistant language="java" >}}
