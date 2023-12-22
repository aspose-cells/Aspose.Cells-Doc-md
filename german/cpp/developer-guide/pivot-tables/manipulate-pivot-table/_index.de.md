---
title: Pivot-Tabelle manipulieren
type: docs
weight: 20
url: /de/cpp/manipulate-pivot-table/
---
##  **Mögliche Nutzungsszenarien**
Neben der Erstellung neuer Pivot-Tabellen können Sie auch die neuen und vorhandenen Pivot-Tabellen bearbeiten. Sie können die Daten im Quellbereich der Pivot-Tabelle ändern und sie dann aktualisieren und berechnen, um die neuen Werte der Pivot-Tabellenzellen zu erhalten. Benutzen Sie bitte[PivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) Und[PivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/)Methoden, nachdem Sie die Werte im Quellbereich der Pivot-Tabelle geändert haben, um die Pivot-Tabelle zu aktualisieren.
##  **Pivot-Tabelle manipulieren**
 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](23167013.xlsx) und greift auf die vorhandene Pivot-Tabelle in ihrem ersten Arbeitsblatt zu. Es ändert den Wert der Zelle B3, die sich im Quellbereich der Pivot-Tabelle befindet, und aktualisiert dann die Pivot-Tabelle. Bevor es die Pivot-Tabelle aktualisiert, greift es auf den Wert der Pivot-Tabellenzelle H8 zu, der 15 ist, und nach dem Aktualisieren der Pivot-Tabelle ändert sich sein Wert auf 6. Bitte sehen Sie sich die an[Excel-Datei ausgeben](23167014.xlsx)mit diesem Code generiert und der Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispiel-Excel-Datei. Bitte sehen Sie sich auch die Konsolenausgabe unten an, die den Wert der Pivot-Tabellenzelle H8 vor und nach der Aktualisierung der Pivot-Tabelle zeigt.

![todo:image_alt_text](manipulate-pivot-table_1.png)
##  **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable-new.cpp" >}}
##  **Konsolenausgabe**
 Unten sehen Sie die Konsolenausgabe des obigen Beispielcodes, wenn er mit dem bereitgestellten Code ausgeführt wird[Beispiel-Excel-Datei](23167013.xlsx).

{{< highlight "java" >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
