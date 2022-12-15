---
title: Slicer zu einer Pivot-Tabelle erstellen
type: docs
weight: 10
url: /de/python-java/create-slicer-to-a-pivot-table/
---
## **Mögliche Nutzungsszenarien**
Datenschnitte werden verwendet, um Daten schnell zu filtern. Sie können verwendet werden, um Daten sowohl in einer Tabelle als auch in einer Pivot-Tabelle zu filtern. Microsoft Mit Excel können Sie einen Slicer erstellen, indem Sie eine Tabelle oder Pivot-Tabelle auswählen und dann auf klicken*Einfügen > Slicer*. Aspose.Cells for Python via Java stellt die Methode Worksheet.getSlicers().add() zum Erstellen von Slicern bereit.
## **Slicer zu einer Pivot-Tabelle erstellen**
Das folgende Code-Snippet lädt die[Beispiel-Excel-Datei](106364966.xlsx)die die Pivot-Tabelle enthält. Anschließend erstellt es den Slicer basierend auf dem ersten Basis-Pivot-Feld. Schließlich speichert es die Arbeitsmappe in[Ausgang XLSX](106364967.xlsx)Format. Der folgende Screenshot zeigt den von Aspose.Cells erstellten Slicer in der Excel-Ausgabedatei.

![todo: Bild_alt_Text](create-slicer-to-a-pivot-table_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-CreateSlicerToPivotTable.py" >}}
