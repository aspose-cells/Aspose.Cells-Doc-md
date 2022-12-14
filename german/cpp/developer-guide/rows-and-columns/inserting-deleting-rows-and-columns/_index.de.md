---
title: Einfügen, Löschen von Zeilen und Spalten
type: docs
weight: 40
url: /de/cpp/inserting-deleting-rows-and-columns/
---
## **Einführung**
Unabhängig davon, ob Sie ein neues Arbeitsblatt von Grund auf neu erstellen oder an einem vorhandenen Arbeitsblatt arbeiten, müssen wir möglicherweise zusätzliche Zeilen oder Spalten hinzufügen, um mehr Daten aufzunehmen. Umgekehrt müssen wir möglicherweise auch Zeilen oder Spalten von bestimmten Positionen im Arbeitsblatt löschen. Um diese Anforderungen zu erfüllen, stellt Aspose.Cells einen sehr einfachsten Satz von Klassen und Methoden bereit, die unten besprochen werden.
### **Zeilen und Spalten verwalten**
 Aspose.Cells bietet eine Klasse,[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) , die eine Microsoft Excel-Datei darstellt. Das[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Klasse enthält eine[IArbeitsblätter](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse. Das[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse bietet eine[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Auflistung, die alle Zellen im Arbeitsblatt darstellt.

 Das[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Die Sammlung bietet mehrere Methoden zum Verwalten von Zeilen und Spalten in einem Arbeitsblatt. Einige davon werden unten besprochen.

{{% alert color="primary" %}} 

Wenn Zeilen oder Spalten hinzugefügt werden, wird der Inhalt im Arbeitsblatt nach unten oder rechts verschoben, und wenn Zeilen oder Spalten entfernt werden, wird der Inhalt nach oben oder links verschoben.

{{% /alert %}} 
#### **Zeile einfügen**
 Fügen Sie an beliebiger Stelle eine Zeile in das Arbeitsblatt ein, indem Sie die aufrufen[Zeile einfügen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7) Methode der[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Sammlung. Das[Zeile einfügen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7)-Methode nimmt den Index der Zeile, in der die neue Zeile eingefügt wird.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow.cpp" >}}


#### **Mehrere Zeilen einfügen**
 Um mehrere Zeilen in ein Arbeitsblatt einzufügen, rufen Sie die auf[Zeilen einfügen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0) Methode der[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Sammlung. Das[Zeilen einfügen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0)Die Methode benötigt zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die neuen Zeilen eingefügt werden.
- Anzahl der Zeilen, die Gesamtzahl der Zeilen, die eingefügt werden müssen.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows.cpp" >}}


#### **Löschen mehrerer Zeilen**
Um mehrere Zeilen aus einem Arbeitsblatt zu löschen, rufen Sie die auf[Zeilen löschen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1) Methode der[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Sammlung. Das[Zeilen löschen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1)Die Methode benötigt zwei Parameter:

- Zeilenindex, der Index der Zeile, aus der die Zeilen gelöscht werden.
- Anzahl der Zeilen, die Gesamtzahl der Zeilen, die gelöscht werden müssen.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows.cpp" >}}


#### **Spalte einfügen**
 Entwickler können auch an beliebiger Stelle eine Spalte in das Arbeitsblatt einfügen, indem sie die aufrufen[Spalte einfügen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55) Methode der[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Sammlung.[Spalte einfügen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55)-Methode übernimmt den Index der Spalte, in die die neue Spalte eingefügt wird.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn.cpp" >}}


#### **Löschen Sie eine Spalte**
 Um eine Spalte an einer beliebigen Stelle aus dem Arbeitsblatt zu löschen, rufen Sie die auf[Spalte löschen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b) Methode der[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Sammlung. Das[Spalte löschen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b)-Methode nimmt den Index der zu löschenden Spalte.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn.cpp" >}}
