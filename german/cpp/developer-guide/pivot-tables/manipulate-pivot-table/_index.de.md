---
title: Pivot-Tabelle manipulieren
type: docs
weight: 20
url: /de/cpp/manipulate-pivot-table/
---
## **Mögliche Nutzungsszenarien**
Neben dem Erstellen neuer Pivot-Tabellen können Sie die neuen und vorhandenen Pivot-Tabellen bearbeiten. Sie können die Daten im Quellbereich der Pivot-Tabelle ändern und dann aktualisieren und berechnen und die neuen Werte der Pivot-Tabellenzellen erhalten. Bitte verwende[IPivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/class/aspose.cells.pivot.i_pivot_table#ab6d71ded346508a1d4a93c59680ddaf6) und[IPivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/class/aspose.cells.pivot.i_pivot_table#a3d6ffec8ce2a7a4ccb58e0452a1733dd)Methoden, nachdem Sie die Werte im Quellbereich der Pivot-Tabelle geändert haben, um die Pivot-Tabelle zu aktualisieren.
## **Pivot-Tabelle manipulieren**
 Der folgende Beispielcode lädt die[Excel-Beispieldatei](23167013.xlsx) und greift auf die vorhandene Pivot-Tabelle in ihrem ersten Arbeitsblatt zu. Es ändert den Wert der Zelle B3, die sich innerhalb des Quellbereichs der Pivot-Tabelle befindet, und aktualisiert dann die Pivot-Tabelle. Bevor es die Pivot-Tabelle aktualisiert, greift es auf den Wert der Pivot-Tabellenzelle H8 zu, der 15 ist, und nach dem Aktualisieren der Pivot-Tabelle ändert sich sein Wert auf 6. Bitte beachten Sie die[Excel-Datei ausgeben](23167014.xlsx)generiert mit diesem Code und dem Screenshot, der die Auswirkung des Beispielcodes auf die Beispiel-Excel-Datei zeigt. Bitte sehen Sie sich auch die Konsolenausgabe unten an, die den Wert der Pivot-Tabellenzelle H8 vor und nach dem Aktualisieren der Pivot-Tabelle zeigt.

![todo: Bild_alt_Text](manipulate-pivot-table_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable.cpp" >}}
## **Konsolenausgabe**
 Unten sehen Sie die Konsolenausgabe des obigen Beispielcodes, wenn er mit dem bereitgestellten ausgeführt wird[Excel-Beispieldatei](23167013.xlsx).

{{< highlight "java" >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
