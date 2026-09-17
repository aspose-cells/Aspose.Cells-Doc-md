---
title: Infoga pivot tabell
description: Skapa och formatera pivottabeller i Excel kalkylbladsfiler.
linktitle: Pivot tabeller
url: /sv/net/pivot-tables/
type: docs
weight: 160
keywords: Skapa pivot tabell, Infoga pivot tabell, Formatera pivot tabell.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Skapa Pivottabell**
Det är möjligt att använda Aspose.Cells för att lägga till pivottabeller i kalkylblad på ett programmatiskt sätt.

### **Pivot-tabell objektmodell**
Aspose.Cells tillhandahåller en speciell uppsättning klasser i namnrymden [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) som används för att skapa och kontrollera pivottabeller. Dessa klasser används för att skapa och ställa in [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)-objekt, byggstenarna i en pivottabell. Objekten är:
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) representerar en fält i en [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) representerar en samling av alla [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) objekt i [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) representerar en PivotTable på ett kalkylblad.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) representerar en samling av alla [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) objekt på ett kalkylblad.

### **Skapa en enkel pivot-tabell med hjälp av Aspose.Cells**
1. Lägg till data på ett kalkylblad genom att använda [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) objektets [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) metod.
   Denna data kommer att användas som pivot-tabellens datakälla.
1. Lägg till en pivot-tabell i kalkylbladet genom att anropa [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) samlingen [**add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) metod, som är innesluten i Worksheet-objektet.
1. Kom åt det nya [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)-objektet från [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)-samlingen genom att passera PivotTable-indexet.
1. Använd något av [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)-objekten (förklaras ovan) för att hantera pivot-tabellen.
Efter att ha kört exempelkoden läggs en pivot-tabell till kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}
När du tilldelar ett cellområde som datakälla måste området gå från övre vänstra till nedre högra. Till exempel är "A1:C3" giltigt men "C3:A1" är inte det.
{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}