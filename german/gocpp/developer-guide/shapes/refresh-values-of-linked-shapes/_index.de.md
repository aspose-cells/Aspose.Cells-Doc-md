---
title: Werte verknüpfter Formen mit Golang über C++ aktualisieren
linktitle: Aktualisieren von Werten verknüpfter Formen
type: docs
weight: 3200
url: /de/go-cpp/refresh-values-of-linked-shapes/
description: Lernen Sie, wie Sie die Werte verbundener Formen in Excel Dateien mit Aspose.Cells for C++ aktualisieren.
---

{{% alert color="primary" %}}

Manchmal haben Sie eine verknüpfte Form in Ihrer Excel-Datei, die mit einigen Zellen verknüpft ist. In Microsoft Excel ändert sich beim Ändern des Werts der verknüpften Zelle auch der Wert der verknüpften Form. Dies funktioniert auch gut mit Aspose.Cells, wenn Sie Ihre Arbeitsmappe im XLS- oder XLSX-Format speichern möchten. Wenn Sie Ihre Arbeitsmappe jedoch im PDF- oder HTML-Format speichern möchten, müssen Sie die [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/go-cpp/shapecollection/updateselectedvalue/)-Methode aufrufen, um den Wert der verknüpften Form zu aktualisieren.

{{% /alert %}}

## Beispiel

Das folgende Screenshot zeigt die Quell-Excel-Datei, die im untenstehenden Beispielcode verwendet wird. Es enthält ein verbundenes Bild, das mit den Zellen A1 bis E4 verknüpft ist. Wir werden den Wert der Zelle B4 mit Aspose.Cells ändern und dann die [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/go-cpp/shapecollection/updateselectedvalue/)-Methode aufrufen, um den Wert des Bildes zu aktualisieren und als PDF zu speichern.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Sie können die [Quell-Excel-Datei](95584291.xlsx) und das [Ausgabepdf](95584292.pdf) über die bereitgestellten Links herunterladen.

### C++-Code zum Aktualisieren der Werte verbundener Formen

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshValuesOfLinkedShapes.go" >}}
