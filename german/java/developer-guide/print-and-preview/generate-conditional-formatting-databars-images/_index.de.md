---
title: Generieren Sie DataBars-Bilder mit bedingter Formatierung
type: docs
weight: 170
url: /de/java/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 Manchmal müssen Sie Bilder von DataBars zur bedingten Formatierung generieren. Sie können Aspose.Cells verwenden[**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions))-Methode zum Generieren dieser Bilder. Dieser Artikel zeigt, wie Sie ein DataBar-Bild mit Aspose.Cells generieren.

{{% /alert %}}

## **Beispiel**

 Der folgende Beispielcode generiert das DataBar-Bild der Zelle C1. Zuerst greift es auf das Formatbedingungsobjekt der Zelle zu, und dann greift es von diesem Objekt aus auf das DataBar-Objekt zu und verwendet dessen[**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions))-Methode, um das Bild der Zelle zu erzeugen. Schließlich speichert es das Bild auf der Festplatte.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
