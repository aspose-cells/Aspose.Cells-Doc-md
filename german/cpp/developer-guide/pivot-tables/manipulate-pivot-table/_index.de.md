---
title: Pivot Tabelle bearbeiten
type: docs
weight: 20
url: /de/cpp/manipulate-pivot-table/
---

## **Mögliche Verwendungsszenarien**
Neben dem Erstellen neuer Pivot-Tabellen können Sie die neuen und vorhandenen Pivot-Tabellen bearbeiten. Sie können die Daten im Quellenbereich der Pivot-Tabelle ändern und dann aktualisieren und berechnen und die neuen Werte der Zellen der Pivot-Tabelle erhalten. Verwenden Sie bitte die Methoden [PivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) und [PivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) nachdem Sie die Werte im Quellenbereich der Pivot-Tabelle geändert haben, um die Pivot-Tabelle zu aktualisieren.
## **Pivot-Tabelle bearbeiten**
Der folgende Beispielcode lädt die [Beispieldatei für Excel](23167013.xlsx) und greift auf die vorhandene Pivot-Tabelle in deren erster Arbeitsblatt zu. Er ändert den Wert der Zelle B3, die sich im Quellenbereich der Pivot-Tabelle befindet, und aktualisiert dann die Pivot-Tabelle. Bevor die Pivot-Tabelle aktualisiert wird, greift er auf den Wert der Pivot-Tabellenzelle H8 zu, der 15 beträgt, und nachdem die Pivot-Tabelle aktualisiert wurde, ändert sich der Wert auf 6. Bitte sehen Sie sich die mit diesem Code generierte [Ausgabedatei für Excel](23167014.xlsx) und den Screenshot an, der die Auswirkungen des Beispielcodes auf die Beispieldatei für Excel zeigt. Bitte sehen Sie auch die unten stehende Konsolenausgabe, in der der Wert der Pivot-Tabellenzelle H8 vor und nach der Aktualisierung der Pivot-Tabelle angezeigt wird.

![todo:image_alt_text](manipulate-pivot-table_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable-new.cpp" >}}
## **Konsolenausgabe**
Nachstehend finden Sie die Konsolenausgabe des obigen Beispielcodes, wenn er mit der bereitgestellten [Beispieldatei für Excel](23167013.xlsx) ausgeführt wird.

{{< highlight java >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
