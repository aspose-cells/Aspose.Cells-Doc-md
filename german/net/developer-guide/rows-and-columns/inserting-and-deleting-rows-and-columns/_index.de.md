---
title: Einfügen und Löschen von Zeilen und Spalten einer Excel Datei
linktitle: Einfügen und Löschen von Zeilen und Spalten
type: docs
weight: 70
url: /de/net/inserting-and-deleting-rows-and-columns/
description: Dieser Artikel zeigt, wie man Zeilen und Spalten über die Aspose.Cells for .NET API einfügt und löscht.
keywords: Aspose.Cells C# Zeilen und Spalten verwalten, Zeilen und Spalten einfügen, Zeilen und Spalten löschen
---

## **Einführung**

Beim Erstellen eines neuen Arbeitsblatts von Grund auf oder bei der Arbeit an einem vorhandenen Arbeitsblatt müssen möglicherweise zusätzliche Zeilen oder Spalten hinzugefügt werden, um mehr Daten aufzunehmen. Umgekehrt können auch Zeilen oder Spalten von bestimmten Positionen im Arbeitsblatt gelöscht werden.
Um diese Anforderungen zu erfüllen, bietet Aspose.Cells eine sehr einfache Reihe von Klassen und Methoden, die unten diskutiert werden.

### **Zeilen und Spalten verwalten**

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung, die alle Zellen im Arbeitsblatt repräsentiert.

Die [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung bietet mehrere Methoden zur Verwaltung von Zeilen und Spalten in einem Arbeitsblatt. Einige davon werden unten diskutiert.

{{% alert color="primary" %}}

Wenn Zeilen oder Spalten hinzugefügt werden, wird der Inhalt im Arbeitsblatt nach unten oder nach rechts verschoben, und wenn Zeilen oder Spalten entfernt werden, wird der Inhalt nach oben oder nach links verschoben.

{{% /alert %}}


## **Zeilen und Spalten einfügen**

### **Wie man eine Zeile einfügt**

Fügen Sie eine Zeile in das Arbeitsblatt an einer beliebigen Stelle ein, indem Sie die Methode [**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) der Sammlung [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) aufrufen. Die Methode [**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) übernimmt den Index der Zeile, an der die neue Zeile eingefügt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **Wie man mehrere Zeilen einfügt**

Um mehrere Zeilen in ein Arbeitsblatt einzufügen, rufen Sie die Methode [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) der Sammlung [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) auf. Die Methode [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) übernimmt zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die neuen Zeilen eingefügt werden.
- Anzahl der Zeilen, die insgesamt eingefügt werden müssen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **Wie man eine Zeile mit Formatierung einfügt**

Um eine Zeile mit Formatierungsoptionen einzufügen, verwenden Sie die Überladung von [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows), die [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) als Parameter akzeptiert. Setzen Sie die [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)-Eigenschaft der Klasse [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) mit der [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)-Enumeration. Die [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)-Enumeration hat drei unten aufgeführte Elemente.

- SameAsAbove: Formatiert die Zeile wie die darüber liegende Zeile.
- SameAsBelow: Formatiert die Zeile wie die unterhalb liegende Zeile.
- Löschen: Löscht das Format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **Wie man eine Spalte einfügt**

Entwickler können auch eine Spalte in das Arbeitsblatt an beliebiger Stelle einfügen, indem sie die Methode [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) der Sammlung [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) aufrufen. Die Methode [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) erfordert den Index der Spalte, in die die neue Spalte eingefügt werden soll.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **Zeilen und Spalten löschen**

### **Wie man mehrere Zeilen löscht**

Um mehrere Zeilen aus einem Arbeitsblatt zu löschen, rufen Sie die Methode [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) der Sammlung [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) auf. Die Methode [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) erfordert zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die Zeilen gelöscht werden.
- Anzahl der Zeilen, die insgesamt gelöscht werden müssen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **Wie man eine Spalte löscht**

Um eine Spalte aus dem Arbeitsblatt an beliebiger Stelle zu löschen, rufen Sie die Methode [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) der Sammlung [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) auf. Die Methode [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) erfordert den Index der zu löschenden Spalte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
