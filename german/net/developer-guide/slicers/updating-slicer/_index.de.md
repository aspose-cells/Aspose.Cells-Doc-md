---
title: Slicer aktualisieren
type: docs
weight: 50
url: /de/net/updating-slicer/
---
## **Mögliche Nutzungsszenarien**

Wenn Sie den Slicer in Microsoft Excel aktualisieren möchten, aktivieren oder deaktivieren Sie seine Elemente, dann wird die Slicer-Tabelle oder Pivot-Tabelle entsprechend aktualisiert. Bitte verwende[**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems)Slicer-Artikel mit Aspose.Cells an- oder abwählen und dann anrufen[**Slicer.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh)Methode zum Aktualisieren der Slicer-Tabelle oder Pivot-Tabelle.

## **Slicer aktualisieren**

 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](67338475.xlsx) die einen vorhandenen Slicer enthält. Es deselektiert die 2. und 3. Elemente des Slicers und aktualisiert den Slicer. Es speichert dann die Arbeitsmappe als[Excel-Datei ausgeben](67338476.xlsx). Der folgende Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispiel-Excel-Datei. Wie Sie im Screenshot sehen können, hat das Aktualisieren des Slicers mit ausgewählten Elementen auch die Pivot-Tabelle entsprechend aktualisiert.

![todo: Bild_alt_Text](updating-slicer_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
