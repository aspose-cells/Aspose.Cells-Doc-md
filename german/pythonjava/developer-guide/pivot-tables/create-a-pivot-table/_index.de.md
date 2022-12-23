---
title: Erstellen Sie eine Pivot-Tabelle
type: docs
weight: 10
url: /de/python-java/create-a-pivot-table/
---
## **Erstellen Sie eine Pivot-Tabelle**
Aspose.Cells for Python via Java bietet die Funktion zum Erstellen von Pivot-Tabellen. Um eine Pivot-Tabelle mit Aspose.Cells zu erstellen, gehen Sie bitte wie folgt vor:

1. Fügen Sie einige Daten zu Arbeitsblattzellen hinzu, indem Sie die verwenden[Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell)Objekt[setValue](https://reference.aspose.com/cells/python/asposecells.api/cell#Value)Eigentum. Diese Daten werden als Datenquelle für die Pivot-Tabelle verwendet.
1. Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die aufrufen[PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)[addieren](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\))-Methode, gekapselt in der[Arbeitsblatt](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)Objekt.
1. Greife auf ... zu[PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)Objekt aus der[PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)durch das Passieren der[PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)Index.
1. Verwenden Sie eines der (oben erläuterten) Pivot-Tabellenobjekte, die in gekapselt sind[PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)Objekt zum Verwalten der Pivot-Tabelle.

Das folgende Code-Snippet veranschaulicht das Erstellen einer Pivot-Tabelle mit Aspose.Cells API.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
