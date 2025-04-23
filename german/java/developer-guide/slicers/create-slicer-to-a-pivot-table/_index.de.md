---
title: Erstellen Sie Slicer für eine Pivot Tabelle
type: docs
weight: 10
url: /de/java/create-slicer-to-a-pivot-table/
---

## **Mögliche Verwendungsszenarien**
Der Slicer wird verwendet, um Daten schnell zu filtern. Er kann zum Filtern von Daten sowohl in einer Tabelle als auch in einer Pivot-Tabelle verwendet werden. Microsoft Excel erlaubt die Erstellung eines Slicers, indem man eine Tabelle oder Pivot-Tabelle auswählt und dann *Einfügen > Slicer* klickt. Aspose.Cells ermöglicht ebenfalls die Erstellung eines Slicers mit der Methode [Worksheet.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add-com.aspose.cells.PivotTable-int-int-com.aspose.cells.PivotField-).
## **Erstellen Sie ein Schneidwerkzeug zu einem Pivot-Table**
Bitte sehen Sie den folgenden Beispielcode. Es lädt die [Beispiel-Excel-Datei](67338498.xlsx), die die Pivot-Tabelle enthält. Es erstellt dann den Slicer auf Basis des ersten Basispivotfelds. Schließlich speichert es die Arbeitsmappe im [Ausgabe-XLSX](67338497.xlsx)- und [Ausgabe-XLSB](67338496.xlsb)-Format. Der folgende Screenshot zeigt den von Aspose.Cells in der Ausgabe-Excel-Datei erstellten Slicer.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
