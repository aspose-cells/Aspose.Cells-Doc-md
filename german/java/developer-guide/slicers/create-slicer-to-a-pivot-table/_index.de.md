---
title: Erstellen Sie Slicer für eine Pivot Tabelle
type: docs
weight: 10
url: /de/java/create-slicer-to-a-pivot-table/
---

## **Mögliche Verwendungsszenarien**
Der Slicer wird verwendet, um Daten schnell zu filtern. Er kann sowohl in einer Tabelle als auch in einer Pivot-Tabelle verwendet werden. Microsoft Excel ermöglicht es Ihnen, einen Slicer zu erstellen, indem Sie eine Tabelle oder Pivot-Tabelle auswählen und dann auf *Einfügen > Slicer* klicken. Auch Aspose.Cells ermöglicht es Ihnen, einen Slicer mithilfe der Methode [Worksheet.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add\(com.aspose.cells.PivotTable,%20int,%20int,%20com.aspose.cells.PivotField\)) zu erstellen.
## **Erstellen Sie ein Schneidwerkzeug zu einem Pivot-Table**
Bitte sehen Sie den folgenden Beispielcode. Es lädt die [Beispiel-Excel-Datei](67338498.xlsx), die die Pivot-Tabelle enthält. Es erstellt dann den Slicer auf Basis des ersten Basispivotfelds. Schließlich speichert es die Arbeitsmappe im [Ausgabe-XLSX](67338497.xlsx)- und [Ausgabe-XLSB](67338496.xlsb)-Format. Der folgende Screenshot zeigt den von Aspose.Cells in der Ausgabe-Excel-Datei erstellten Slicer.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
