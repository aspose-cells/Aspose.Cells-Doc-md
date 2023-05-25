---
title: Leere Zeilen und Spalten in einem Arbeitsblatt löschen
type: docs
weight: 300
url: /de/net/delete-blank-rows-and-columns-in-a-worksheet/
---
{{% alert color="primary" %}}

Es ist möglich, alle leeren Zeilen und Spalten aus einem Arbeitsblatt zu löschen. Dies ist nützlich, wenn Sie beispielsweise eine PDF-Datei aus einer Microsoft-Excel-Datei generieren und nur Zeilen und Spalten konvertieren möchten, die Daten oder zugehörige Objekte enthalten.

Verwenden Sie die folgenden Aspose.Cells-Methoden, um leere Zeilen und Spalten zu löschen:

1.  Um leere Zeilen zu löschen, verwenden Sie die[**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows) Methode. Bitte beachten Sie, dass dies für leere Zeilen, die gelöscht werden, nicht nur erforderlich ist[**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) sollte wahr sein, aber es sollte auch kein sichtbarer Kommentar für irgendeine Zelle in diesen Zeilen definiert sein und keine Pivot-Tabelle, deren Bereich sich mit ihnen überschneidet.
1.  Um leere Spalten zu löschen, verwenden Sie die[**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns) Methode.

{{% /alert %}}

##  C#-Code zum Löschen leerer Zeilen

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

##  C#-Code zum Löschen leerer Spalten

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
