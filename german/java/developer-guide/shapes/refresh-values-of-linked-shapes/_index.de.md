---
title: Aktualisieren Sie die Werte verknüpfter Formen
type: docs
weight: 3000
url: /de/java/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

Manchmal haben Sie eine verknüpfte Form in Ihrer Excel-Datei, die mit einer Zelle verknüpft ist. In Microsoft Excel ändert das Ändern des Werts der verknüpften Zelle auch den Wert der verknüpften Form. Dies funktioniert auch gut mit Aspose.Cells, wenn Sie Ihre Arbeitsmappe im Format XLS oder XLSX speichern möchten. Wenn Sie Ihre Arbeitsmappe jedoch im Format PDF oder HTML speichern möchten, müssen Sie anrufen[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue())-Methode, um den Wert der verknüpften Form zu aktualisieren.

{{% /alert %}}

## Beispiel

 Der folgende Screenshot zeigt die Excel-Quelldatei, die im folgenden Beispielcode verwendet wird. Es hat einen Link**Bild 1** mit Zelle A1 verknüpft. Wir werden den Wert der Zelle A1 mit Aspose.Cells ändern und dann anrufen[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue() )-Methode zum Aktualisieren des Werts von**Bild 1** und speichern Sie es im Format PDF.

![todo: Bild_alt_Text](refresh-values-of-linked-shapes_1.png)

Sie können die herunterladen[Excel-Quelldatei](5472956.xlsx) und die[Ausgang PDF](5472955.pdf) aus den angegebenen Links.

### Java-Code zum Aktualisieren der Werte verknüpfter Formen

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
