---
title: Aktualisieren Sie Verweise in anderen Arbeitsblättern, während Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen
type: docs
weight: 5000
url: /de/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Dieser Artikel zeigt, wie man Verweise in anderen Tabellen beim Löschen leerer Spalten und Zeilen in einer Tabelle mit der Aspose.Cells für Python via .NET API aktualisiert.
keywords: Python Excel Bibliothek, Python Aktualisieren von Verweisen in anderen Tabellen beim Löschen leerer Spalten und Zeilen in einer Tabelle, Aktualisieren von Verweisen beim Entfernen leerer Spalten und Zeilen in einer Tabelle in Python.
---

{{% alert color="primary" %}}

Wenn Sie leere Spalten und Zeilen in einer Tabelle löschen, werden die Verweise in anderen Tabellen ungültig. Wenn Sie dieses Verhalten vermeiden möchten und möchten, dass diese Verweise auf die aktuelle Tabelle in anderen Tabellen ebenfalls aktualisiert werden, verwenden Sie bitte die [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/)-Eigenschaft und setzen Sie sie auf **true**.

{{% /alert %}}

## **Aktualisieren Sie Verweise in anderen Arbeitsblättern, während Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen**

Bitte beachten Sie den folgenden Beispielcode und seine Konsolenausgabe. Die Zelle E3 in der zweiten Tabelle hat eine Formel =Blatt1!C3, die sich auf die Zelle C3 in der ersten Tabelle bezieht. Wenn Sie [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) auf **true** setzen, wird diese Formel aktualisiert und wird zu =Blatt1!A1, wenn Sie leere Spalten und Zeilen in der ersten Tabelle löschen. Wenn Sie jedoch [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) auf **false** setzen, bleibt die Formel in Zelle E3 der zweiten Tabelle =Blatt1!C3 und wird ungültig.

### **Programmierbeispiel**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-UpdateReferenceInWorksheets.py" >}}

### **Konsolenausgabe**

Dies ist die Konsolenausgabe des obigen Beispielcodes, wenn [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) auf **true** gesetzt wurde.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

Dies ist die Konsolenausgabe des obigen Beispielcodes, wenn [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) auf **false** gesetzt wurde. Wie Sie sehen können, wurde die Formel in Zelle E3 der zweiten Tabelle nicht aktualisiert und ihr Zellenwert beträgt jetzt 0 statt 4, was ungültig ist.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
