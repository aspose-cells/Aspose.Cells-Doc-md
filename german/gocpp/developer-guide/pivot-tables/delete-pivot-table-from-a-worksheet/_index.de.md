---
title: Pivot Tabelle aus einem Arbeitsblatt mit Golang via C++ löschen
linktitle: Pivot Tabelle löschen
type: docs
weight: 60
url: /de/go-cpp/delete-pivot-table-from-a-worksheet/
description: C++ Code zum Entfernen von PivotTabellen in Excel Arbeitsblättern mit Aspose.Cells.
keywords: c++ pivot tabelle aus arbeitsblatt entfernen, c++ pivot tabelle löschen, wie man pivot tabelle mit c++ löscht, pivot tabelle mit c++ entfernen, c++ pivot tabelle löschen, c++ pivot tabelle entfernen, pivot tabelle entfernen, pivot tabelle löschen, wie man pivot tabelle löscht
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Möglichkeit, eine Pivot-Tabelle aus einem Arbeitsblatt zu löschen oder zu entfernen. Sie können die Pivot-Tabelle unter Verwendung des Pivot-Tabelle-Objekts oder der Position der Pivot-Tabelle löschen. Bitte verwenden Sie die [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/)-Methode, um die Pivot-Tabelle unter Verwendung des Pivot-Tabelle-Objekts zu löschen, und die [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/)-Methode, um das Pivot-Tabellen-Objekt unter Verwendung seiner Position innerhalb der Pivot-Tabellensammlung zu löschen.

{{% /alert %}}

Der folgende Beispielcode löscht zwei Pivot-Tabellen aus dem Arbeitsblatt. Zuerst wird die Pivot-Tabelle mit [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/) Methode entfernt, dann mit [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeletePivotTableFromAWorksheet.go" >}}
