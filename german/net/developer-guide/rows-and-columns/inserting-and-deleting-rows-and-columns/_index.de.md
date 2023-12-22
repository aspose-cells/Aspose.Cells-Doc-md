---
title: Einfügen und Löschen von Zeilen und Spalten einer Excel-Datei
linktitle: Einfügen und Löschen von Zeilen und Spalten
type: docs
weight: 70
url: /de/net/inserting-and-deleting-rows-and-columns/
description: In diesem Artikel wird gezeigt, wie Sie Zeilen und Spalten mit Aspose.Cells for .NET API einfügen und löschen.
keywords: Aspose.Cells C# manage rows and columns, insert rows and columns, delete rows and columns
---
##  **Einführung**

Unabhängig davon, ob wir ein neues Arbeitsblatt von Grund auf erstellen oder an einem vorhandenen Arbeitsblatt arbeiten, müssen wir möglicherweise zusätzliche Zeilen oder Spalten hinzufügen, um mehr Daten aufzunehmen. Umgekehrt müssen wir möglicherweise auch Zeilen oder Spalten an bestimmten Positionen im Arbeitsblatt löschen.
Um diese Anforderungen zu erfüllen, stellt Aspose.Cells einen sehr einfachen Satz von Klassen und Methoden bereit, die unten erläutert werden.

###  **Zeilen und Spalten verwalten**

Aspose.Cells bietet eine Klasse[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , das eine Microsoft Excel-Datei darstellt. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Sammlung, die alle Zellen im Arbeitsblatt darstellt.

 Der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Die Sammlung bietet mehrere Methoden zum Verwalten von Zeilen und Spalten in einem Arbeitsblatt. Einige davon werden im Folgenden besprochen.

{{% alert color="primary" %}}

Wenn Zeilen oder Spalten hinzugefügt werden, wird der Inhalt im Arbeitsblatt nach unten oder rechts verschoben, und wenn Zeilen oder Spalten entfernt werden, wird der Inhalt nach oben oder links verschoben.

{{% /alert %}}


##  **Fügen Sie Zeilen und Spalten ein**

###  **So fügen Sie eine Zeile ein**

 Fügen Sie an einer beliebigen Stelle eine Zeile in das Arbeitsblatt ein, indem Sie die aufrufen[**Zeile einfügen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Der[**Zeile einfügen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)Die Methode übernimmt den Index der Zeile, in die die neue Zeile eingefügt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

###  **So fügen Sie mehrere Zeilen ein**

 Um mehrere Zeilen in ein Arbeitsblatt einzufügen, rufen Sie auf[**Zeilen einfügen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Der[**Zeilen einfügen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)Die Methode benötigt zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die neuen Zeilen eingefügt werden.
- Anzahl der Zeilen, die Gesamtzahl der Zeilen, die eingefügt werden müssen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

###  **So fügen Sie eine Zeile mit Formatierung ein**

Um eine Zeile mit Formatierungsoptionen einzufügen, verwenden Sie die[**Zeilen einfügen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)Überlastung, die dauert[**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) als Parameter. Stellen Sie die ein[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Eigentum von[**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) Klasse mit[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Aufzählung. Der[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)Die Aufzählung hat drei Mitglieder, wie unten aufgeführt.

- SameAsAbove: Formatiert die Zeile genauso wie die obige Zeile.
- SameAsBelow: Formatiert die Zeile genauso wie die Zeile unten.
- Löschen: Löscht die Formatierung.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

###  **So fügen Sie eine Spalte ein**

 Entwickler können auch an einer beliebigen Stelle eine Spalte in das Arbeitsblatt einfügen, indem sie die aufrufen[**Spalte einfügen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Sammlung. Der[**Spalte einfügen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)Die Methode übernimmt den Index der Spalte, in die die neue Spalte eingefügt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

##  **Zeilen und Spalten löschen**

###  **So löschen Sie mehrere Zeilen**

 Um mehrere Zeilen aus einem Arbeitsblatt zu löschen, rufen Sie auf[**Zeilen löschen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Der[**Zeilen löschen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)Die Methode benötigt zwei Parameter:

- Zeilenindex, der Index der Zeile, aus der die Zeilen gelöscht werden.
- Anzahl der Zeilen, die Gesamtzahl der Zeilen, die gelöscht werden müssen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


###  **So löschen Sie eine Spalte**

 Um an einer beliebigen Stelle eine Spalte aus dem Arbeitsblatt zu löschen, rufen Sie auf[**Spalte löschen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Der[**Spalte löschen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)Die Methode verwendet den Index der zu löschenden Spalte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
