---
title: Ändern Sie die Cells-Ausrichtung und behalten Sie die vorhandene Formatierung bei
type: docs
weight: 340
url: /de/net/change-cells-alignment-and-keep-existing-formatting/
---
## **Mögliche Nutzungsszenarien**

Manchmal möchten Sie die Ausrichtung mehrerer Zellen ändern, aber auch die vorhandene Formatierung beibehalten. Aspose.Cells ermöglicht Ihnen dies mit der[**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments) Eigentum. Wenn Sie es einstellen**Stimmt** , Ausrichtungsänderungen finden sonst nicht statt. Bitte beachten Sie,[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) Objekt wird als Parameter an übergeben[**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle)Methode, die die Formatierung tatsächlich auf einen Bereich von Zellen anwendet.

## **Ändern Sie die Cells-Ausrichtung und behalten Sie die vorhandene Formatierung bei**

 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](67338585.xlsx) , erstellt den Bereich und zentriert ihn horizontal und vertikal und behält die vorhandene Formatierung bei. Der folgende Screenshot vergleicht die Beispiel-Excel-Datei und[Excel-Datei ausgeben](67338586.xlsx)und zeigt, dass die gesamte vorhandene Formatierung der Zellen gleich ist, außer dass die Zellen jetzt horizontal und vertikal zentriert ausgerichtet sind.

![todo: Bild_alt_Text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
