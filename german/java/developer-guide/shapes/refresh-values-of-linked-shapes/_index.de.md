---
title: Aktualisieren von Werten verknüpfter Formen
type: docs
weight: 3000
url: /de/java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Manchmal haben Sie eine verknüpfte Form in Ihrer Excel-Datei, die mit einer Zelle verknüpft ist. In Microsoft Excel ändert das Ändern des Werts der verknüpften Zelle auch den Wert der verknüpften Form. Dies funktioniert auch problemlos mit Aspose.Cells, wenn Sie Ihre Arbeitsmappe im XLS- oder XLSX-Format speichern möchten. Wenn Sie Ihre Arbeitsmappe jedoch im PDF- oder HTML-Format speichern möchten, müssen Sie die Methode [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) aufrufen, um den Wert der verknüpften Form zu aktualisieren.

{{% /alert %}}

## Beispiel

Der folgende Screenshot zeigt die Quell-Excel-Datei, die im untenstehenden Beispielcode verwendet wird. Es hat ein verknüpftes Bild 1, das mit Zelle A1 verknüpft ist. Wir werden den Wert von Zelle A1 mit Aspose.Cells ändern und dann die Methode [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) aufrufen, um den Wert von Bild 1 zu aktualisieren und es im PDF-Format zu speichern.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.png)

Sie können die [Quell-Excel-Datei](5472956.xlsx) und das [Ausgabepdf](5472955.pdf) von den angegebenen Links herunterladen.

### Java-Code zum Aktualisieren der Werte von verknüpften Formen

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
{{< app/cells/assistant language="java" >}}
