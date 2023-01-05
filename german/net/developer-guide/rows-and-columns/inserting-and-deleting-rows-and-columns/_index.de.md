---
title: Einfügen und Löschen von Zeilen und Spalten einer Excel-Datei
linktitle: Einfügen und Löschen von Zeilen und Spalten
type: docs
weight: 70
url: /de/net/inserting-and-deleting-rows-and-columns/
---
## **Einführung**

Unabhängig davon, ob Sie ein neues Arbeitsblatt von Grund auf neu erstellen oder an einem vorhandenen Arbeitsblatt arbeiten, müssen wir möglicherweise zusätzliche Zeilen oder Spalten hinzufügen, um mehr Daten aufzunehmen. Umgekehrt müssen wir möglicherweise auch Zeilen oder Spalten von bestimmten Positionen im Arbeitsblatt löschen.
Um diese Anforderungen zu erfüllen, stellt Aspose.Cells einen sehr einfachsten Satz von Klassen und Methoden bereit, die unten besprochen werden.

### **Zeilen und Spalten verwalten**

Aspose.Cells bietet eine Klasse[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Auflistung, die alle Zellen im Arbeitsblatt darstellt.

 Das[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Die Sammlung bietet mehrere Methoden zum Verwalten von Zeilen und Spalten in einem Arbeitsblatt. Einige davon werden unten besprochen.

{{% alert color="primary" %}}

Wenn Zeilen oder Spalten hinzugefügt werden, wird der Inhalt im Arbeitsblatt nach unten oder rechts verschoben, und wenn Zeilen oder Spalten entfernt werden, wird der Inhalt nach oben oder links verschoben.

{{% /alert %}}


## **Zeilen und Spalten einfügen**

### **Zeile einfügen**

 Fügen Sie an beliebiger Stelle eine Zeile in das Arbeitsblatt ein, indem Sie die aufrufen[**Zeile einfügen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Das[**Zeile einfügen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)-Methode nimmt den Index der Zeile, in der die neue Zeile eingefügt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **Mehrere Zeilen einfügen**

 Um mehrere Zeilen in ein Arbeitsblatt einzufügen, rufen Sie die auf[**Zeilen einfügen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Das[**Zeilen einfügen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)Die Methode benötigt zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die neuen Zeilen eingefügt werden.
- Anzahl der Zeilen, die Gesamtzahl der Zeilen, die eingefügt werden müssen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **Zeile mit Formatierung einfügen**

Um eine Zeile mit Formatierungsoptionen einzufügen, verwenden Sie die[**Zeilen einfügen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)Überlastung, die dauert[**Einfügeoptionen**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) als Parameter. Stellen Sie die ein[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Eigentum von[**Einfügeoptionen**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) Klasse mit[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Aufzählung. Das[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)Die Aufzählung hat drei Mitglieder, wie unten aufgeführt.

- SameAsAbove: Formatiert die Zeile genauso wie die obige Zeile.
- SameAsBelow: Formatiert die Zeile genauso wie die untere Zeile.
- Löschen: Löscht die Formatierung.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **Spalte einfügen**

 Entwickler können auch an beliebiger Stelle eine Spalte in das Arbeitsblatt einfügen, indem sie die aufrufen[**Spalte einfügen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Sammlung. Das[**Spalte einfügen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)-Methode übernimmt den Index der Spalte, in die die neue Spalte eingefügt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **Zeilen und Spalten löschen**

### **Mehrere Zeilen löschen**

Um mehrere Zeilen aus einem Arbeitsblatt zu löschen, rufen Sie die auf[**Zeilen löschen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Das[**Zeilen löschen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)Die Methode benötigt zwei Parameter:

- Zeilenindex, der Index der Zeile, aus der die Zeilen gelöscht werden.
- Anzahl der Zeilen, die Gesamtzahl der Zeilen, die gelöscht werden müssen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **Löschen Sie eine Spalte**

 Um eine Spalte an einer beliebigen Stelle aus dem Arbeitsblatt zu löschen, rufen Sie die auf[**Spalte löschen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Das[**Spalte löschen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)-Methode nimmt den Index der zu löschenden Spalte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
