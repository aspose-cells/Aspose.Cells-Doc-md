---
title: Slicer aktualisieren
type: docs
weight: 50
url: /de/java/updating-slicer/
---
## **Mögliche Nutzungsszenarien**
Wenn Sie den Slicer in Microsoft Excel aktualisieren möchten, aktivieren oder deaktivieren Sie seine Elemente, dann wird die Slicer-Tabelle oder Pivot-Tabelle entsprechend aktualisiert. Bitte verwende[Slicer.SlicerCache.SlicerCacheItems](https://reference.aspose.com/cells/java/com.aspose.cells/slicercache#SlicerCacheItems)Slicer-Artikel mit Aspose.Cells an- oder abwählen und dann anrufen[Slicer.refresh()](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#refresh\(\))-Methode zum Aktualisieren der Slicer-Tabelle oder Pivot-Tabelle.
## **Slicer aktualisieren**
Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](67338506.xlsx)die einen vorhandenen Slicer enthält. Es deselektiert die 2. und 3. Elemente des Slicers und aktualisiert den Slicer. Anschließend wird die Arbeitsmappe als[Excel-Datei ausgeben](67338505.xlsx). Der folgende Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispiel-Excel-Datei. Wie Sie im Screenshot sehen können, hat das Aktualisieren des Slicers mit ausgewählten Elementen auch die Pivot-Tabelle entsprechend aktualisiert.

![todo: Bild_alt_Text](updating-slicer_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-UpdatingSlicer.java" >}}
