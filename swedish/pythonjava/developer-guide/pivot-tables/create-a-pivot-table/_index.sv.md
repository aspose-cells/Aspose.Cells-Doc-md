---
title: Skapa en pivottabell
type: docs
weight: 10
url: /sv/python-java/create-a-pivot-table/
---

## **Skapa en pivottabell**
Aspose.Cells för Python via Java ger funktionen att skapa pivottabeller. För att skapa en pivottabell med hjälp av Aspose.Cells, följ följande steg:

1. Lägg till lite data i kalkylbladsceller genom att använda objektets [Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell) egenskap [setValue](https://reference.aspose.com/cells/python/asposecells.api/cell#Value). Denna data kommer att användas som datakälla för pivottabellen.
1. Lägg till en pivottabell till kalkylbladet genom att anropa metoden [add](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)) i [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection), inkapslad i [Kalkylblad](https://reference.aspose.com/cells/python/asposecells.api/Worksheet) objekt.
1. Få åtkomst till [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)-objektet från [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection) genom att passera [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)-indexet.
1. Använd valfritt av pivottabell objekten (beskrivna ovan) inkapslat i [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection) objekt för att hantera pivottabellen.

Nedanstående kodavsnitt visar hur man skapar en pivottabell med Aspose.Cells API.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
