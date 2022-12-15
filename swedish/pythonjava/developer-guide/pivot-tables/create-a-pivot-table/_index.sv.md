---
title: Skapa en pivottabell
type: docs
weight: 10
url: /sv/python-java/create-a-pivot-table/
---
## **Skapa en pivottabell**
Aspose.Cells for Python via Java tillhandahåller funktionen för att skapa pivottabeller. För att skapa en pivottabell med Aspose.Cells, följ stegen nedan:

1. Lägg till några data till kalkylbladsceller genom att använda[Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell)objekt[satt värde](https://reference.aspose.com/cells/python/asposecells.api/cell#Value)fast egendom. Dessa data kommer att användas som en datakälla för pivottabellen.
1. Lägg till en pivottabell till kalkylbladet genom att anropa[PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)[Lägg till](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)metod, inkapslad i[Arbetsblad](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)objekt.
1. Få tillgång till[Pivottabell](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)objekt från[PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)genom att passera[Pivottabell](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)index.
1. Använd något av pivottabellsobjekten (förklarat ovan) inkapslade i[PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)objekt för att hantera pivottabellen.

Följande kodavsnitt visar hur man skapar en pivottabell med Aspose.Cells API.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
