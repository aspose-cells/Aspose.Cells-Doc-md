---
title: Einfügen, Löschen von Zeilen und Spalten
type: docs
weight: 40
url: /de/cpp/inserting-deleting-rows-and-columns/
---

## **Einführung**
Ob beim Erstellen eines neuen Arbeitsblatts von Grund auf oder beim Arbeiten an einem vorhandenen Arbeitsblatt, wir können zusätzliche Zeilen oder Spalten hinzufügen, um mehr Daten aufzunehmen. Im Gegensatz dazu müssen wir möglicherweise auch Zeilen oder Spalten von bestimmten Positionen im Arbeitsblatt löschen. Um diese Anforderungen zu erfüllen, bietet Aspose.Cells eine sehr einfache Reihe von Klassen und Methoden, die unten diskutiert werden.
### **Verwalten von Zeilen und Spalten**
Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei darstellt. Die Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält eine [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) -Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) dargestellt. Die Klasse [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bietet eine [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) -Sammlung, die alle Zellen im Arbeitsblatt repräsentiert.

Die [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) -Sammlung bietet verschiedene Methoden zum Verwalten von Zeilen und Spalten in einem Arbeitsblatt. Einige davon werden unten diskutiert.

{{% alert color="primary" %}} 

Wenn Zeilen oder Spalten hinzugefügt werden, wird der Inhalt im Arbeitsblatt nach unten oder nach rechts verschoben, und wenn Zeilen oder Spalten entfernt werden, wird der Inhalt nach oben oder nach links verschoben.

{{% /alert %}} 
#### **Eine Zeile einfügen**
Fügen Sie eine Zeile in das Arbeitsblatt an einer beliebigen Stelle ein, indem Sie die [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) -Methode der [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) -Sammlung aufrufen. Die [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) -Methode übernimmt den Index der Zeile, an der die neue Zeile eingefügt werden soll.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


#### **Einfügen mehrerer Zeilen**
Um mehrere Zeilen in ein Arbeitsblatt einzufügen, rufen Sie die [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) -Methode der [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) -Sammlung auf. Die [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) -Methode verwendet zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die neuen Zeilen eingefügt werden.
- Anzahl der Zeilen, die insgesamt eingefügt werden müssen.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


#### **Mehrere Zeilen löschen**
Um mehrere Zeilen aus einem Arbeitsblatt zu löschen, rufen Sie die [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) -Methode der [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) -Sammlung auf. Die [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) -Methode verwendet zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die Zeilen gelöscht werden.
- Anzahl der Zeilen, die insgesamt gelöscht werden müssen.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


#### **Eine Spalte einfügen**
Entwickler können auch eine Spalte in das Arbeitsblatt an einer beliebigen Stelle einfügen, indem sie die [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) -Methode der [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) -Sammlung aufrufen. Die [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) -Methode übernimmt den Index der Spalte, an dem die neue Spalte eingefügt werden soll.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


#### **Eine Spalte löschen**
Um eine Spalte aus dem Arbeitsblatt an einer beliebigen Stelle zu löschen, rufen Sie die [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) -Methode der [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) -Sammlung auf. Die [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) -Methode übernimmt den Index der zu löschenden Spalte.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
