---
title: Pivot Tabelle aus einem Arbeitsblatt löschen
type: docs
weight: 60
url: /de/net/delete-pivot-table-from-a-worksheet/
description: C# Code zum Entfernen von PivotTable für Excel Arbeitsblätter
keywords: c# Pivot Tabelle aus Arbeitsblatt entfernen, c# Pivot Tabelle aus Excel entfernen, wie man Pivot Tabelle mit c# löscht, Pivot Tabelle mit c# löschen, Pivot Tabelle aus Excel mit c# löschen, c# Pivot Tabelle löschen, c# Pivot Tabelle entfernen, Pivot Tabelle entfernen, Pivot Tabelle löschen, wie man Pivot Tabelle löscht
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Möglichkeit, eine Pivot-Tabelle aus einem Arbeitsblatt zu löschen oder zu entfernen. Sie können die Pivot-Tabelle unter Verwendung des Pivot-Tabelle-Objekts oder der Position der Pivot-Tabelle löschen. Bitte verwenden Sie die [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove)-Methode, um die Pivot-Tabelle unter Verwendung des Pivot-Tabelle-Objekts zu löschen, und die [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat)-Methode, um das Pivot-Tabellen-Objekt unter Verwendung seiner Position innerhalb der Pivot-Tabellensammlung zu löschen.

{{% /alert %}}

Der folgende Beispielcode löscht zwei Pivot-Tabellen aus dem Arbeitsblatt. Zuerst entfernt er die Pivot-Tabelle unter Verwendung der [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove)-Methode und dann entfernt er die Pivot-Tabelle unter Verwendung der [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat)-Methode

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}
