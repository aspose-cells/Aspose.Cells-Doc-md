---
title: Aktualisieren Sie die Werte verknüpfter Formen
type: docs
weight: 3200
url: /de/net/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

Manchmal haben Sie eine verknüpfte Form in Ihrer Excel-Datei, die mit einer Zelle verknüpft ist. In Microsoft Excel ändert das Ändern des Werts der verknüpften Zelle auch den Wert der verknüpften Form. Das funktioniert auch gut mit Aspose.Cells, wenn Sie Ihre Arbeitsmappe im XLS- oder XLSX-Format speichern möchten. Wenn Sie Ihre Arbeitsmappe jedoch im PDF- oder HTML-Format speichern möchten, müssen Sie anrufen[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) -Methode, um den Wert der verknüpften Form zu aktualisieren.

{{% /alert %}}

## Beispiel

 Der folgende Screenshot zeigt die Excel-Quelldatei, die im folgenden Beispielcode verwendet wird. Es hat ein verknüpftes Bild, das mit den Zellen A1 bis E4 verknüpft ist. Wir werden den Wert der Zelle B4 mit Aspose.Cells ändern und dann anrufen[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue)-Methode, um den Wert des Bildes zu aktualisieren und im PDF-Format zu speichern.

![todo: Bild_alt_Text](refresh-values-of-linked-shapes_1.jpg)

Sie können die herunterladen[Excel-Quelldatei](95584291.xlsx) und die[PDF ausgeben](95584292.pdf) aus den angegebenen Links.

### C#-Code zum Aktualisieren der Werte verknüpfter Formen

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-RefreshValueOfLinkedShapes-1.cs" >}}
