---
title: Slicer aktualisieren
type: docs
weight: 50
url: /de/net/updating-slicer/
description: Dieser Artikel zeigt, wie Sie verknüpfte Pivot Tabellen aktualisieren, indem Sie den Slicer über die Aspose.Cells for .NET API aktualisieren.
keywords: Aspose.Cells C# Slicer aktualisieren, C# wie man den Slicer ändert, wie man den Slicer in C# anpasst, wie man die Slicer Elemente auswählt oder abwählt.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie den Slicer in Microsoft Excel aktualisieren möchten, seine Elemente auswählen oder abwählen, wird dann die Slicer-Tabelle oder Pivot-Tabelle entsprechend aktualisiert. Verwenden Sie bitte [**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems), um Slicer-Elemente auszuwählen oder abzuwählen und rufen Sie dann die Methode [**Slicer.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh) auf, um die Slicer-Tabelle oder Pivot-Tabelle zu aktualisieren.

## **Wie man den Slicer aktualisiert**

Der folgende Beispielscode lädt die [Beispiel-Excel-Datei](67338475.xlsx), die einen vorhandenen Slicer enthält. Es entwählt die 2. und 3. Elemente des Slicers und aktualisiert den Slicer. Anschließend speichert es die Arbeitsmappe unter [Ausgabe-Excel-Datei](67338476.xlsx). Der folgende Screenshot zeigt die Auswirkung des Beispielscodes auf die Beispiel-Excel-Datei. Wie Sie auf dem Screenshot sehen können, wurde durch das Aktualisieren des Slicers mit ausgewählten Elementen auch die Pivot-Tabelle entsprechend aktualisiert.

![todo:image_alt_text](updating-slicer_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
