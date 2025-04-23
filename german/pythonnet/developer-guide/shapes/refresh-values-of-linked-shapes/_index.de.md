---
title: Aktualisieren von Werten verknüpfter Formen
type: docs
weight: 3200
url: /de/python-net/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Manchmal haben Sie eine verlinkte Form in Ihrer Excel-Datei, die mit einer Zelle verknüpft ist. In Microsoft Excel ändert sich der Wert der verknüpften Zelle, wenn der Wert geändert wird, in der verknüpften Form. Dies funktioniert auch mit Aspose.Cells für Python via .NET, wenn Sie Ihre Arbeitsmappe im XLS- oder XLSX-Format speichern möchten. Wenn Sie Ihre Arbeitsmappe jedoch im PDF- oder HTML-Format speichern möchten, müssen Sie die Methode [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value) aufrufen, um den Wert der verknüpften Form zu aktualisieren.

{{% /alert %}}

## Beispiel

Der folgende Screenshot zeigt die Quelldatei Excel, die im untenstehenden Beispielcode verwendet wird. Sie enthält ein verknüpftes Bild, das mit den Zellen A1 bis E4 verbunden ist. Wir werden den Wert der Zelle B4 mit Aspose.Cells für Python via .NET ändern und dann [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value) Methode aufrufen, um den Wert des Bildes zu aktualisieren und in PDF-Format zu speichern.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Sie können die [Quell-Excel-Datei](95584291.xlsx) und die [Ausgabedatei im PDF-Format](95584292.pdf) von den angegebenen Links herunterladen.

## C#-Code zum Aktualisieren der Werte verknüpfter Formen

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-RefreshValueOfLinkedShapes-1.py" >}}
