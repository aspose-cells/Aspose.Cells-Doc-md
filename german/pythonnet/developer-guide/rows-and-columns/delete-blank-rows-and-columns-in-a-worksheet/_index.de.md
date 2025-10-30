---
title: Löschen von leeren Zeilen und Spalten in einem Arbeitsblatt
type: docs
weight: 300
url: /de/python-net/delete-blank-rows-and-columns-in-a-worksheet/
description: In diesem Artikel wird beschrieben, wie man leere Zeilen und Spalten in einem Arbeitsblatt mit der Aspose.Cells für Python via .NET Bibliothek löscht.
keywords: Python Excel Bibliothek, Python lösche leere Zeilen, Python entferne leere Zeilen, Python lösche leere Spalten, Python entferne leere Spalten, Python lösche oder entferne leere Zeilen und Spalten.
---

{{% alert color="primary" %}}

Es ist möglich, alle leeren Zeilen und Spalten aus einem Arbeitsblatt zu löschen. Dies ist nützlich, wenn beispielsweise eine PDF-Datei aus einer Microsoft Excel-Datei generiert wird und nur Zeilen und Spalten konvertiert werden sollen, die Daten oder zugehörige Objekte enthalten.

Verwenden Sie die folgenden Aspose.Cells-Methoden, um leere Zeilen und Spalten zu löschen:

1. Um leere Zeilen zu löschen, verwenden Sie die [**Cells.delete_blank_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_rows)-Methode. Bitte beachten Sie, dass für die zu löschenden leeren Zeilen nicht nur erforderlich ist, dass [**Row.is_blank**](https://reference.aspose.com/cells/python-net/aspose.cells/row/is_blank/) wahr sein sollte, sondern es dürfen auch keine sichtbaren Kommentare für Zellen in diesen Zeilen definiert sein und kein Pivot-Table, dessen Bereich mit ihnen kollidiert.
1. Um leere Spalten zu löschen, verwenden Sie die [**Cells.delete_blank_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_columns)-Methode.

{{% /alert %}}

## C#-Code zum Löschen leerer Zeilen

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankRows-1.py" >}}

## C#-Code zum Löschen leerer Spalten

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankColumns-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
