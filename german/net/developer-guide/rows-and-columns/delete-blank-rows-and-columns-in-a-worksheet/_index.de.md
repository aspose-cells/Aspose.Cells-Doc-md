---
title: Löschen von leeren Zeilen und Spalten in einem Arbeitsblatt
type: docs
weight: 300
url: /de/net/delete-blank-rows-and-columns-in-a-worksheet/
---

{{% alert color="primary" %}}

Es ist möglich, alle leeren Zeilen und Spalten aus einem Arbeitsblatt zu löschen. Dies ist nützlich, wenn beispielsweise eine PDF-Datei aus einer Microsoft Excel-Datei generiert wird und nur Zeilen und Spalten konvertiert werden sollen, die Daten oder zugehörige Objekte enthalten.

Verwenden Sie die folgenden Aspose.Cells-Methoden, um leere Zeilen und Spalten zu löschen:

1. Um leere Zeilen zu löschen, verwenden Sie die [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows)-Methode. Bitte beachten Sie, dass für die zu löschenden leeren Zeilen nicht nur erforderlich ist, dass [**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) wahr sein sollte, sondern es dürfen auch keine sichtbaren Kommentare für Zellen in diesen Zeilen definiert sein und kein Pivot-Table, dessen Bereich mit ihnen kollidiert.
1. Um leere Spalten zu löschen, verwenden Sie die [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns)-Methode.

{{% /alert %}}

## C#-Code zum Löschen leerer Zeilen

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

## C#-Code zum Löschen leerer Spalten

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
