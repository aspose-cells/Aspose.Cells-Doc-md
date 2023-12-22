---
title: Zeilenhöhe und Spaltenbreite anpassen
type: docs
weight: 10
url: /de/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

Wenn Sie mit Tabellenkalkulationen arbeiten und Daten zu Zeilen oder Spalten hinzufügen, müssen Sie möglicherweise die Höhe von Zeilen oder die Breite von Spalten ändern. Manchmal bedeutet das Anwenden von Formatierungen auf Zeilen oder Spalten, dass die aktuelle Höhe oder Breite geändert werden muss, um die Daten anzuzeigen. Normalerweise passen Benutzer Zeilenhöhen und Spaltenbreiten in einer WYSIWYG-Umgebung mit Microsoft Excel an. Mit Aspose.Cells können Entwickler diese Vorgänge jedoch zur Laufzeit ausführen.

{{% /alert %}} 
##  **Arbeiten mit Zeilen**
###  **Zeilenhöhe anpassen**
 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) das stellt eine Microsoft Excel-Datei dar. Der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält a[WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Dies ermöglicht den Zugriff auf jedes Arbeitsblatt in der Excel-Datei. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse bietet a[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung, die alle Zellen im Arbeitsblatt darstellt. Der[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Die Sammlung bietet verschiedene Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden im Folgenden ausführlicher besprochen.
####  **Festlegen der Höhe einer Zeile**
 Es ist möglich, die Höhe einer einzelnen Zeile durch Aufrufen von festzulegen[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung[SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) Methode. Der[SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/)Die Methode übernimmt die folgenden Parameter wie folgt:

- *Zeilenindex**, der Index der Zeile, deren Höhe Sie ändern.
- *Zeilenhöhe**, die auf die Zeile anzuwendende Zeilenhöhe.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


####  **Festlegen der Höhe aller Zeilen in einem Arbeitsblatt**
 Wenn Entwickler für alle Zeilen im Arbeitsblatt die gleiche Zeilenhöhe festlegen müssen, können sie dies mithilfe von tun[SetStandardHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) Methode der[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Sammlung.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
##  **Arbeiten mit Spalten**
###  **Festlegen der Breite einer Spalte**
 Legen Sie die Breite einer Spalte fest, indem Sie die aufrufen[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung[SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) Methode. Der[SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/)Die Methode benötigt die folgenden Parameter:

- *Spaltenindex**, der Index der Spalte, deren Breite Sie ändern.
- *Spaltenbreite**, die gewünschte Spaltenbreite.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
###  **Festlegen der Breite aller Spalten in einem Arbeitsblatt**
 Um für alle Spalten im Arbeitsblatt die gleiche Spaltenbreite festzulegen, verwenden Sie die[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung[SetStandardWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/)Methode.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
