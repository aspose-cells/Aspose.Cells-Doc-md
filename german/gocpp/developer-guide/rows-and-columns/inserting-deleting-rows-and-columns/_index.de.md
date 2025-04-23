---
title: Einfügen, Löschen von Zeilen und Spalten
type: docs
weight: 40
url: /de/go-cpp/inserting-deleting-rows-and-columns/
---

## **Einführung**

Ob beim Erstellen eines neuen Arbeitsblatts von Grund auf oder beim Arbeiten an einem vorhandenen Arbeitsblatt, wir können zusätzliche Zeilen oder Spalten hinzufügen, um mehr Daten aufzunehmen. Im Gegensatz dazu müssen wir möglicherweise auch Zeilen oder Spalten von bestimmten Positionen im Arbeitsblatt löschen. Um diese Anforderungen zu erfüllen, bietet Aspose.Cells eine sehr einfache Reihe von Klassen und Methoden, die unten diskutiert werden.

### **Verwalten von Zeilen und Spalten**

Aspose.Cells stellt die Klasse [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) bereit, die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) repräsentiert. Die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse bietet eine [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung, die alle Zellen im Arbeitsblatt darstellt.

Die [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung stellt mehrere Methoden zur Verwaltung von Zeilen und Spalten in einem Arbeitsblatt bereit. Einige davon werden im Folgenden erläutert.

{{% alert color="primary" %}}

Wenn Zeilen oder Spalten hinzugefügt werden, wird der Inhalt im Arbeitsblatt nach unten oder nach rechts verschoben, und wenn Zeilen oder Spalten entfernt werden, wird der Inhalt nach oben oder nach links verschoben.

{{% /alert %}}

Fügen Sie eine Zeile in das Arbeitsblatt an beliebiger Stelle ein, indem Sie die [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) Methode der [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung aufrufen. Die [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) Methode nimmt den Index der Zeile, an der die neue Zeile eingefügt werden soll, als Parameter.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertRow.go" >}}

#### **Einfügen mehrerer Zeilen**

Um mehrere Zeilen in ein Arbeitsblatt einzufügen, rufen Sie die [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrows_int_int/) Methode der [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung auf. Die [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrowinsertrows_int_ints/) Methode nimmt zwei Parameter:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingMultipleRows.go" >}}

#### **Mehrere Zeilen löschen**

Um mehrere Zeilen aus einem Arbeitsblatt zu löschen, rufen Sie die [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) Methode der [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung auf. Die [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) Methode nimmt zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die Zeilen gelöscht werden.
- Anzahl der Zeilen, die insgesamt gelöscht werden müssen.

#### **Eine Spalte einfügen**

Entwickler können auch eine Spalte in das Arbeitsblatt an beliebiger Stelle einfügen, indem sie die [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) Methode der [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung aufrufen. Die [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) Methode nimmt den Index der Spalte, in die die neue Spalte eingefügt werden soll.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertColumn.go" >}}

Um eine Spalte aus einem Arbeitsblatt an beliebiger Stelle zu löschen, rufen Sie die [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) Methode der [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung auf. Die [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) Methode nimmt den Index der zu löschenden Spalte als Parameter.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteColumn.go" >}}
