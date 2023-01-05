---
title: Zeilenhöhe und Spaltenbreite anpassen
type: docs
weight: 10
url: /de/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

Wenn Sie mit Tabellenkalkulationen arbeiten und Daten zu Zeilen oder Spalten hinzufügen, müssen Sie möglicherweise die Höhe von Zeilen oder die Breite von Spalten ändern. Manchmal bedeutet das Anwenden von Formatierungen auf Zeilen oder Spalten, dass die aktuelle Höhe oder Breite geändert werden muss, um die Daten anzuzeigen. Normalerweise passen Benutzer Zeilenhöhen und Spaltenbreiten in einer WYSIWYG-Umgebung mit Microsoft Excel an. Aber mit Aspose.Cells können Entwickler diese Operationen zur Laufzeit ausführen.

{{% /alert %}} 
## **Arbeiten mit Zeilen**
### **Anpassen der Zeilenhöhe**
 Aspose.Cells bietet eine Klasse,[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) das stellt eine Microsoft Excel-Datei dar. Das[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Klasse enthält a[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse. Das[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse bietet a[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Auflistung, die alle Zellen im Arbeitsblatt darstellt. Das[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)-Sammlung bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden weiter unten ausführlicher besprochen.
#### **Festlegen der Höhe einer Zeile**
 Es ist möglich, die Höhe einer einzelnen Zeile durch Aufrufen von festzulegen[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Sammlung[SetRowHeight](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f) Methode. Das[SetRowHeight](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f)Die Methode nimmt die folgenden Parameter wie folgt:

- **Zeilenindex**, der Index der Zeile, deren Höhe Sie ändern.
- **Zeilenhöhe**, die Zeilenhöhe, die auf die Zeile angewendet werden soll.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow.cpp" >}}


#### **Festlegen der Höhe aller Zeilen in einem Arbeitsblatt**
 Wenn Entwickler für alle Zeilen im Arbeitsblatt dieselbe Zeilenhöhe festlegen müssen, können sie dies mithilfe von tun[Standardhöhe festlegen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a0b79a3163e2b601aa1b6a6a1e3f1467f) Methode der[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Sammlung.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet.cpp" >}}
## **Arbeiten mit Spalten**
### **Einstellen der Breite einer Spalte**
 Legen Sie die Breite einer Spalte fest, indem Sie die aufrufen[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Sammlung[SetColumnWidth](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987) Methode. Das[SetColumnWidth](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987)Die Methode nimmt die folgenden Parameter an:

- **Spaltenindex**, der Index der Spalte, deren Breite Sie ändern.
- **Spaltenbreite**, die gewünschte Spaltenbreite.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn.cpp" >}}
### **Festlegen der Breite aller Spalten in einem Arbeitsblatt**
 Um dieselbe Spaltenbreite für alle Spalten im Arbeitsblatt festzulegen, verwenden Sie die[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Sammlung[SetStandardBreite](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a48f5dbccc3bf4bb9e6e882094b500bd7)Methode.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet.cpp" >}}
