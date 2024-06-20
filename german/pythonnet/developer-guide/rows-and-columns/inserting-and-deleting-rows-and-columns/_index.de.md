---
title: Einfügen und Löschen von Zeilen und Spalten einer Excel Datei
linktitle: Einfügen und Löschen von Zeilen und Spalten
type: docs
weight: 70
url: /de/python-net/inserting-and-deleting-rows-and-columns/
description: Dieser Artikel zeigt, wie man Zeilen und Spalten mithilfe der Aspose.Cells für Python via .NET API einfügt und löscht.
keywords: Python Excel Library, Aspose.Cells Python verwalten Zeilen und Spalten, Python Zeilen und Spalten einfügen, Python Zeilen und Spalten löschen, Python Zeilen und Spalten entfernen.
---

## **Einführung**

Beim Erstellen eines neuen Arbeitsblatts von Grund auf oder bei der Arbeit an einem vorhandenen Arbeitsblatt müssen möglicherweise zusätzliche Zeilen oder Spalten hinzugefügt werden, um mehr Daten aufzunehmen. Umgekehrt können auch Zeilen oder Spalten von bestimmten Positionen im Arbeitsblatt gelöscht werden.
Um diese Anforderungen zu erfüllen, bietet Aspose.Cells für Python via .NET eine sehr einfache Reihe von Klassen und Methoden, die unten diskutiert werden.

### **Zeilen und Spalten verwalten**

Aspose.Cells für Python via .NET bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-Sammlung, die alle Zellen im Arbeitsblatt darstellt.

Die [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-Sammlung bietet mehrere Methoden zur Verwaltung von Zeilen und Spalten in einem Arbeitsblatt. Einige davon werden unten diskutiert.

{{% alert color="primary" %}}

Wenn Zeilen oder Spalten hinzugefügt werden, wird der Inhalt im Arbeitsblatt nach unten oder nach rechts verschoben, und wenn Zeilen oder Spalten entfernt werden, wird der Inhalt nach oben oder nach links verschoben.

{{% /alert %}}


## **Zeilen und Spalten einfügen**

### **Wie man eine Zeile einfügt**

Fügen Sie eine Zeile in das Arbeitsblatt an einer beliebigen Stelle ein, indem Sie die Methode [**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) der Sammlung [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) aufrufen. Die Methode [**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) übernimmt den Index der Zeile, an der die neue Zeile eingefügt wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARow-1.py" >}}

### **Wie man mehrere Zeilen einfügt**

Um mehrere Zeilen in ein Arbeitsblatt einzufügen, rufen Sie die Methode [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) der Sammlung [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) auf. Die Methode [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) übernimmt zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die neuen Zeilen eingefügt werden.
- Anzahl der Zeilen, die insgesamt eingefügt werden müssen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.py" >}}

### **Wie man eine Zeile mit Formatierung einfügt**

Um eine Zeile mit Formatierungsoptionen einzufügen, verwenden Sie die Überladung von [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int-aspose.cells.InsertOptions), die [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) als Parameter akzeptiert. Setzen Sie die [**copy_format_type**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions/copy_format_type/)-Eigenschaft der Klasse [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) mit der [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/)-Enumeration. Die [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/)-Enumeration hat drei unten aufgeführte Elemente.

- SAME_AS_ABOVE: Formatiert die Zeile genauso wie die darüberliegende Zeile.
- SAME_AS_BELOW: Formatiert die Zeile genauso wie die darunterliegende Zeile.
- CLEAR: Löscht die Formatierung.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.py" >}}

### **Wie man eine Spalte einfügt**

Entwickler können auch eine Spalte in das Arbeitsblatt an beliebiger Stelle einfügen, indem sie die Methode [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) der Sammlung [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) aufrufen. Die Methode [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) erfordert den Index der Spalte, in die die neue Spalte eingefügt werden soll.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingAColumn-1.py" >}}

## **Zeilen und Spalten löschen**

### **Wie man mehrere Zeilen löscht**

Um mehrere Zeilen aus einem Arbeitsblatt zu löschen, rufen Sie die Methode [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) der Sammlung [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) auf. Die Methode [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) erfordert zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die Zeilen gelöscht werden.
- Anzahl der Zeilen, die insgesamt gelöscht werden müssen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.py" >}}


### **Wie man eine Spalte löscht**

Um eine Spalte aus dem Arbeitsblatt an beliebiger Stelle zu löschen, rufen Sie die Methode [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) der Sammlung [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) auf. Die Methode [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) erfordert den Index der zu löschenden Spalte.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingAColumn-1.py" >}}
