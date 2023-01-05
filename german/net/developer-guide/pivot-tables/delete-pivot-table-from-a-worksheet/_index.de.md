---
title: Pivot-Tabelle aus einem Arbeitsblatt löschen
type: docs
weight: 60
url: /de/net/delete-pivot-table-from-a-worksheet/
description: C#-Code zum Entfernen von PivotTable für Excel-Arbeitsblätter
keywords: c# remove pivot table from worksheet, c# remove pivot table from excel, how to delete pivot table with c#, delete pivot table with c#, delete pivot table from excel with c#, c# delete pivot table, c# remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---
{{% alert color="primary" %}}

 Aspose.Cells bietet eine Funktion zum Löschen oder Entfernen von Pivot-Tabellen aus einem Arbeitsblatt. Sie können die Pivot-Tabelle mit Pivot-Tabellenobjekt oder Pivot-Tabellenposition löschen. Bitte verwenden Sie die[**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) Methode zum Löschen der Pivot-Tabelle mit Pivot-Tabellenobjekt und[**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) Methode zum Löschen eines Pivot-Tabellenobjekts anhand seiner Position innerhalb der Pivot-Tabellensammlung.

{{% /alert %}}

 Der folgende Beispielcode löscht zwei Pivot-Tabellen aus dem Arbeitsblatt. Zuerst entfernt es die Pivot-Tabelle mit[**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) Methode und entfernt dann die Pivot-Tabelle mit[**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) Methode

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}
