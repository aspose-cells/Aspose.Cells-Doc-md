---
title: Ein Pivot Table erstellen
type: docs
weight: 10
url: /de/python-java/create-a-pivot-table/
---

## **Ein Pivot-Table erstellen**
Aspose.Cells für Python via Java bietet die Möglichkeit, Pivot-Tabellen zu erstellen. Um eine Pivot-Tabelle mit Aspose.Cells zu erstellen, befolgen Sie bitte die folgenden Schritte:

1. Fügen Sie einige Daten zu den Arbeitsblattzellen hinzu, indem Sie die [setValue](https://reference.aspose.com/cells/python/asposecells.api/cell#Value)-Eigenschaft des [Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell)-Objekts verwenden. Diese Daten dienen als Datenquelle für die Pivot-Tabelle.
1. Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)-Methode [add](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)) aufrufen, die im [Worksheet](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)-Objekt gekapselt ist.
1. Greifen Sie auf das [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)-Objekt aus der [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)zu, indem Sie den Index des [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)-Objekts übergeben.
1. Verwenden Sie eines der oben erklärten Pivot-Tabellen-Objekte, die im [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)Objekt gekapselt sind, um die Pivot-Tabelle zu verwalten.

Der folgende Code-Ausschnitt zeigt das Erstellen einer Pivot-Tabelle mit der Aspose.Cells-API.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
