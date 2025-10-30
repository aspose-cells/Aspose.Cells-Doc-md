---
title: Aktualisieren von Werten verknüpfter Formen
type: docs
weight: 3200
url: /de/python-java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Manchmal haben Sie eine verknüpfte Form in Ihrer Excel-Datei, die mit einigen Zellen verknüpft ist. In Microsoft Excel ändert sich beim Ändern des Werts der verknüpften Zelle auch der Wert der verknüpften Form. Dies funktioniert auch gut mit Aspose.Cells, wenn Sie Ihre Arbeitsmappe im XLS- oder XLSX-Format speichern möchten. Wenn Sie Ihre Arbeitsmappe jedoch im PDF- oder HTML-Format speichern möchten, müssen Sie die [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/python-java/asposecells.api/shapecollection#updateSelectedValue())-Methode aufrufen, um den Wert der verknüpften Form zu aktualisieren.

{{% /alert %}}

## Beispiel

Das folgende Bild zeigt die Quell-Excel-Datei, die im unten stehenden Beispielcode verwendet wird. Es hat ein verknüpftes Bild, das mit den Zellen A1 bis E4 verknüpft ist. Wir werden den Wert der Zelle B4 mit Aspose.Cells ändern und dann die [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/python-java/asposecells.api/shapecollection#updateSelectedValue())-Methode aufrufen, um den Wert des Bildes zu aktualisieren und es im PDF-Format zu speichern.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Sie können die [Quell-Excel-Datei](sampleRefreshValueOfLinkedShapes.xlsx) und die [Ausgabedatei PDF](95584292.pdf) von den bereitgestellten Links herunterladen.

## C#-Code zum Aktualisieren der Werte verknüpfter Formen

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-RefreshValueOfLinkedShapes-1.py" >}}
{{< app/cells/assistant language="csharp" >}}
