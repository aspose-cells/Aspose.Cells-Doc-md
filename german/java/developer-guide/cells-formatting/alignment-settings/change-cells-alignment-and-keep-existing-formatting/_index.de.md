---
title: Ändern Sie die Cells-Ausrichtung und behalten Sie die vorhandene Formatierung bei
type: docs
weight: 260
url: /de/java/change-cells-alignment-and-keep-existing-formatting/
---
## **Mögliche Nutzungsszenarien**

Manchmal möchten Sie die Ausrichtung mehrerer Zellen ändern, aber auch die vorhandene Formatierung beibehalten. Aspose.Cells ermöglicht Ihnen dies mit der[**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments) Eigentum. Wenn Sie es einstellen**Stimmt** , Ausrichtungsänderungen finden sonst nicht statt. Bitte beachten Sie,[**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) Objekt wird als Parameter an übergeben[**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag))-Methode, die die Formatierung tatsächlich auf den Zellbereich anwendet.

## **Ändern Sie die Cells-Ausrichtung und behalten Sie die vorhandene Formatierung bei**

Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](67338592.xlsx), erstellt den Bereich und zentriert ihn horizontal und vertikal und behält die vorhandene Formatierung bei. Der folgende Screenshot vergleicht die Beispiel-Excel-Datei und[Excel-Datei ausgeben](67338591.xlsx)und zeigt, dass die gesamte vorhandene Formatierung der Zellen gleich ist, außer dass die Zellen jetzt horizontal und vertikal zentriert ausgerichtet sind.

![todo: Bild_alt_Text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
