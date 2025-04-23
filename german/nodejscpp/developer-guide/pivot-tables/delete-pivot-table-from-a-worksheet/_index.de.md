---
title: Pivot Tabelle aus einem Arbeitsblatt löschen
type: docs
weight: 60
url: /de/nodejs-cpp/delete-pivot-table-from-a-worksheet/
description: Aspose.Cells for Node.js via C++ Code zum Entfernen von PivotTable für Excel Arbeitsblätter
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js Bibliothek, Pivot Tabelle aus Arbeitsblatt entfernen, Pivot Tabelle aus Excel entfernen, wie man Pivot Tabelle mit Aspose.Cells for Node.js via C++ löscht, Pivot Tabelle löschen, Pivot Tabelle aus Excel löschen, Pivot Tabelle löschen, Aspose.Cells for Node.js via C++ Entfernen der Pivot Tabelle, Pivot Tabelle entfernen, Pivot Tabelle löschen, wie man Pivot Tabelle löscht
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ bietet eine Funktion zum Löschen oder Entfernen einer Pivot-Tabelle aus einem Arbeitsblatt. Sie können die Pivot-Tabelle entweder mit dem Pivot-Table-Objekt oder anhand ihrer Position löschen. Bitte verwenden Sie die [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-)-Methode, um die Pivot-Tabelle mit dem Pivot-Table-Objekt zu löschen, und die [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-)-Methode, um das Pivot-Table-Objekt anhand seiner Position innerhalb der Pivot-Tabellen-Sammlung zu löschen.

{{% /alert %}}

## **Wie man eine Pivot-Tabelle mit Aspose.Cells for Node.js via C++ aus einem Arbeitsblatt löscht**

Der folgende Beispielcode löscht zwei Pivot-Tabellen aus dem Arbeitsblatt. Zuerst entfernt er die Pivot-Tabelle unter Verwendung der [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-)-Methode und dann entfernt er die Pivot-Tabelle unter Verwendung der [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-)-Methode

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.js" >}}
