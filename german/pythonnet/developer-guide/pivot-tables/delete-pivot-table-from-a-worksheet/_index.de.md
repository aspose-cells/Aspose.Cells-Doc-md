---
title: Pivot Tabelle aus einem Arbeitsblatt löschen
type: docs
weight: 60
url: /de/python-net/delete-pivot-table-from-a-worksheet/
description: Python via .NET Code zum Entfernen von Pivot Tabellen für Excel Arbeitsblätter
keywords: Aspose.Cells für Python Excel, Excel Python Bibliothek, Python via .NET Entfernen von Pivot Tabellen aus Arbeitsblatt, Python via .NET Entfernen von Pivot Tabellen aus Excel, Wie man Pivot Tabelle mit Python via .NET löscht, Pivot Tabelle mit Python via .NET löscht, Pivot Tabelle von Excel mit Python via .NET löscht, Python via .NET löscht Pivot Tabelle, Python via .NET entfernt Pivot Tabelle, entfernt Pivot Tabelle, löscht Pivot Tabelle, wie man Pivot Tabelle löscht
---

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET bietet eine Funktion zum Löschen oder Entfernen von Pivot-Tabellen aus einem Arbeitsblatt. Sie können die Pivot-Tabelle mithilfe des Pivot-Tabellenobjekts oder der Pivot-Tabellenposition löschen. Bitte verwenden Sie die Methode [**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/), um die Pivot-Tabelle mithilfe des Pivot-Tabellenobjekts zu löschen, und die Methode [**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool), um das Pivot-Tabellenobjekt unter Verwendung seiner Position in der Pivot-Tabellensammlung zu löschen.

{{% /alert %}}

## **Wie man Pivot-Tabelle aus Arbeitsblatt mithilfe von Aspose.Cells für Python Excel-Bibliothek löscht**

Der folgende Beispielcode löscht zwei Pivot-Tabellen aus dem Arbeitsblatt. Zuerst entfernt er die Pivot-Tabelle unter Verwendung der [**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/)-Methode und dann entfernt er die Pivot-Tabelle unter Verwendung der [**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)-Methode

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}
