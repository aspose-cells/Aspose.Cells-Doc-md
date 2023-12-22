---
title: Einfügen, Löschen von Zeilen und Spalten
type: docs
weight: 40
url: /de/cpp/inserting-deleting-rows-and-columns/
---
##  **Einführung**
Unabhängig davon, ob wir ein neues Arbeitsblatt von Grund auf erstellen oder an einem vorhandenen Arbeitsblatt arbeiten, müssen wir möglicherweise zusätzliche Zeilen oder Spalten hinzufügen, um mehr Daten aufzunehmen. Umgekehrt müssen wir möglicherweise auch Zeilen oder Spalten an bestimmten Positionen im Arbeitsblatt löschen. Um diese Anforderungen zu erfüllen, stellt Aspose.Cells einen sehr einfachen Satz von Klassen und Methoden bereit, die unten erläutert werden.
###  **Zeilen und Spalten verwalten**
 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) , das eine Microsoft Excel-Datei darstellt. Der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält eine[Arbeitsblätter](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse bietet eine[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Sammlung, die alle Zellen im Arbeitsblatt darstellt.

 Der[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Die Sammlung bietet mehrere Methoden zum Verwalten von Zeilen und Spalten in einem Arbeitsblatt. Einige davon werden im Folgenden besprochen.

{{% alert color="primary" %}} 

Wenn Zeilen oder Spalten hinzugefügt werden, wird der Inhalt im Arbeitsblatt nach unten oder rechts verschoben, und wenn Zeilen oder Spalten entfernt werden, wird der Inhalt nach oben oder links verschoben.

{{% /alert %}} 
####  **Fügen Sie eine Zeile ein**
 Fügen Sie an einer beliebigen Stelle eine Zeile in das Arbeitsblatt ein, indem Sie die aufrufen[Zeile einfügen](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) Methode der[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung. Der[Zeile einfügen](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)Die Methode übernimmt den Index der Zeile, in die die neue Zeile eingefügt wird.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


####  **Mehrere Zeilen einfügen**
 Um mehrere Zeilen in ein Arbeitsblatt einzufügen, rufen Sie auf[Zeilen einfügen](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) Methode der[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung. Der[Zeilen einfügen](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)Die Methode benötigt zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die neuen Zeilen eingefügt werden.
- Anzahl der Zeilen, die Gesamtzahl der Zeilen, die eingefügt werden müssen.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


####  **Mehrere Zeilen löschen**
 Um mehrere Zeilen aus einem Arbeitsblatt zu löschen, rufen Sie auf[Zeilen löschen](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) Methode der[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung. Der[Zeilen löschen](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)Die Methode benötigt zwei Parameter:

- Zeilenindex, der Index der Zeile, aus der die Zeilen gelöscht werden.
- Anzahl der Zeilen, die Gesamtzahl der Zeilen, die gelöscht werden müssen.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


####  **Fügen Sie eine Spalte ein**
 Entwickler können auch an einer beliebigen Stelle eine Spalte in das Arbeitsblatt einfügen, indem sie die aufrufen[Spalte einfügen](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) Methode der[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung.[Spalte einfügen](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)Die Methode übernimmt den Index der Spalte, in die die neue Spalte eingefügt wird.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


####  **Löschen Sie eine Spalte**
 Um an einer beliebigen Stelle eine Spalte aus dem Arbeitsblatt zu löschen, rufen Sie auf[Spalte löschen](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) Methode der[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung. Der[Spalte löschen](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)Die Methode verwendet den Index der zu löschenden Spalte.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
