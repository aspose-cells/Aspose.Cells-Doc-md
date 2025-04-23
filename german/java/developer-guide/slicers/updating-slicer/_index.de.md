---
title: Slicer aktualisieren
type: docs
weight: 50
url: /de/java/updating-slicer/
---

## **Mögliche Verwendungsszenarien**
Wenn Sie einen Slicer in Microsoft Excel aktualisieren möchten, wählen oder abwählen Sie seine Elemente, das aktualisiert dann die Slicer-Tabelle oder Pivot-Tabelle entsprechend. Verwenden Sie [Slicer.SlicerCache.SlicerCacheItems](https://reference.aspose.com/cells/java/com.aspose.cells/slicercache#SlicerCacheItems), um Slicer-Elemente mit Aspose.Cells auszuwählen oder abzuwählen, und rufen Sie dann die Methode [Slicer.refresh()](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#refresh--) auf, um die Slicer-Tabelle oder Pivot-Tabelle zu aktualisieren. 
## **Slicer aktualisieren**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](67338506.xlsx), die einen vorhandenen Slicer enthält. Es hebt die 2. und 3. Elemente des Slicers ab und aktualisiert den Slicer. Danach speichert es die Arbeitsmappe als die [Ausgabe-Excel-Datei](67338505.xlsx). Der folgende Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispiel-Excel-Datei. Wie Sie im Screenshot sehen können, hat das Aktualisieren des Slicers mit ausgewählten Elementen auch die Pivot-Tabelle entsprechend aktualisiert.

![todo:image_alt_text](updating-slicer_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-UpdatingSlicer.java" >}}
{{< app/cells/assistant language="java" >}}
