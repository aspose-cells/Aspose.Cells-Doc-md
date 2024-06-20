---
title: Zellenausrichtung ändern und bestehendes Format beibehalten
type: docs
weight: 260
url: /de/java/change-cells-alignment-and-keep-existing-formatting/
---

## **Mögliche Verwendungsszenarien**

Manchmal möchten Sie die Ausrichtung mehrerer Zellen ändern, aber gleichzeitig die bestehende Formatierung beibehalten. Mit Aspose.Cells können Sie dies mit der [**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments)-Eigenschaft tun. Wenn Sie sie auf **true** setzen, werden Änderungen am Ausrichtung stattfinden, ansonsten nicht. Bitte beachten Sie, dass als Parameter an die Methode [**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) ein [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)-Objekt übergeben wird, das tatsächlich die Formatierung auf den Zellenbereich anwendet.

## **Zellenausrichtung ändern und vorhandenes Format beibehalten**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](67338592.xlsx), erstellt den Bereich, zentriert ihn horizontal und vertikal und behält die bestehende Formatierung bei. Der folgende Screenshot vergleicht die Beispiel-Excel-Datei und die [Ausgabedatei Excel](67338591.xlsx) und zeigt, dass die bestehende Formatierung der Zellen gleich ist, außer dass die Zellen nun horizontal und vertikal zentriert sind.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
