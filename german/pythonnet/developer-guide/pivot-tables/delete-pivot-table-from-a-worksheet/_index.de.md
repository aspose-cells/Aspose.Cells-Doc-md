---
title: Pivot-Tabelle aus einem Arbeitsblatt löschen
type: docs
weight: 60
url: /de/python-net/delete-pivot-table-from-a-worksheet/
description: Python via .NET Code zum Entfernen von PivotTable für Excel-Arbeitsblätter
keywords: Python via .NET remove pivot table from worksheet, Python via .NET remove pivot table from excel, how to delete pivot table with Python via .NET, delete pivot table with Python via .NET, delete pivot table from excel with Python via .NET, Python via .NET delete pivot table, Python via .NET remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET bietet eine Funktion zum Löschen oder Entfernen einer Pivot-Tabelle aus einem Arbeitsblatt. Sie können die Pivot-Tabelle mithilfe des Pivot-Tabellenobjekts oder der Pivot-Tabellenposition löschen. Bitte nutzen Sie die[**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) Methode zum Löschen der Pivot-Tabelle mithilfe des Pivot-Tabellenobjekts und[**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)Methode zum Löschen eines Pivot-Tabellenobjekts anhand seiner Position innerhalb der Pivot-Tabellensammlung.

{{% /alert %}}

 Der folgende Beispielcode löscht zwei Pivot-Tabellen aus dem Arbeitsblatt. Zuerst wird die Pivot-Tabelle entfernt[**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) Methode und dann entfernt es die Pivot-Tabelle mit[**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) Methode

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}
