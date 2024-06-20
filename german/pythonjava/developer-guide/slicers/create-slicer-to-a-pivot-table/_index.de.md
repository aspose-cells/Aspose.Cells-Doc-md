---
title: Erstellen Sie Slicer für eine Pivot Tabelle
type: docs
weight: 10
url: /de/python-java/create-slicer-to-a-pivot-table/
---

## **Mögliche Verwendungsszenarien**
Slicer werden verwendet, um Daten schnell zu filtern. Sie können sowohl in einer Tabelle als auch in einer Pivot-Tabelle verwendet werden. Microsoft Excel ermöglicht es Ihnen, einen Slicer zu erstellen, indem Sie eine Tabelle oder eine Pivot-Tabelle auswählen und dann auf *Einfügen > Slicer* klicken. Aspose.Cells for Python via Java bietet die Methode Worksheet.getSlicers().add(), um einen Slicer zu erstellen.
## **Erstellen Sie ein Schneidwerkzeug zu einem Pivot-Table**
Der folgende Code-Schnipsel lädt die [Beispiel-Excel-Datei](106364966.xlsx) mit der Pivot-Tabelle. Anschließend erstellt er den Slicer basierend auf dem ersten Basisspaltenfeld. Schließlich speichert er die Arbeitsmappe im Format [Ausgabe-XLSX](106364967.xlsx). Das folgende Bild zeigt den Slicer, der von Aspose.Cells in der Ausgabe-Excel-Datei erstellt wurde.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-CreateSlicerToPivotTable.py" >}}
