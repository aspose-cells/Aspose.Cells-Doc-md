---
title: Anpassen der Zeilenhöhe und Spaltenbreite
type: docs
weight: 10
url: /de/cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

Wenn Sie mit Tabellenkalkulationen arbeiten und Daten zu Zeilen oder Spalten hinzufügen, müssen Sie möglicherweise die Höhe von Zeilen oder die Breite von Spalten ändern. Manchmal muss die aktuelle Höhe oder Breite geändert werden, um Daten anzuzeigen, wenn Formatierungen auf Zeilen oder Spalten angewendet werden. Normalerweise passen Benutzer die Zeilenhöhen und Spaltenbreiten in einer WYSIWYG-Umgebung mit Microsoft Excel an. Aber mit Aspose.Cells können Entwickler diese Operationen zur Laufzeit durchführen.

{{% /alert %}} 
## **Arbeiten mit Zeilen**
### **Anpassen der Zeilenhöhe**
Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält eine [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) repräsentiert. Die Klasse [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bietet eine [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung, die alle Zellen im Arbeitsblatt repräsentiert. Die [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung bietet verschiedene Methoden zur Verwaltung von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden unten genauer erläutert.
#### **Die Höhe einer Zeile festlegen**
Es ist möglich, die Höhe einer einzelnen Zeile durch Aufrufen der Methode [SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) der [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung festzulegen. Die Methode [SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) nimmt die folgenden Parameter wie folgt entgegen:

- **Zeilenindex**, der Index der Zeile, deren Höhe geändert wird.
- **Zeilenhöhe**, die auf die Zeile anzuwendende Zeilenhöhe.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


#### **Die Höhe aller Zeilen in einem Arbeitsblatt festlegen**
Wenn Entwickler die gleiche Zeilenhöhe für alle Zeilen in einem Arbeitsblatt festlegen müssen, können sie dies mit der Methode [SetStandardHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) der [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung tun.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
## **Arbeiten mit Spalten**
### **Einstellen der Breite einer Spalte**
Legen Sie die Breite einer Spalte fest, indem Sie die Methode [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) der Sammlung [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) aufrufen. Die Methode [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) verwendet die folgenden Parameter:

- **Spaltenindex**, der Index der Spalte, deren Breite geändert wird.
- **Spaltenbreite**, die gewünschte Spaltenbreite.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
### **Einstellen der Breite aller Spalten in einem Arbeitsblatt**
Um dieselbe Spaltenbreite für alle Spalten im Arbeitsblatt festzulegen, verwenden Sie die Methode [SetStandardWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/) der Sammlung [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
