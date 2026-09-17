---
title: Infoga pivot tabell
description: Skapa och formatera pivot tabell med Aspose.Cells för Python via .NET.
linktitle: Pivot tabeller
url: /sv/python-net/pivot-tables/
type: docs
weight: 160
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
keywords: Skapa pivot tabell, Infoga pivot tabell, Formatera pivot tabell.
---

## **Skapa Pivottabell**
Det är möjligt att använda Aspose.Cells för Python via .NET för att lägga till pivot-tabeller i kalkylblad programmatiskt.

### **Pivot-tabell objektmodell**
Aspose.Cells för Python via .NET tillhandahåller en särskild uppsättning klasser i [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) namespace som används för att skapa och kontrollera pivot-tabeller. Dessa klasser används för att skapa och ställa in [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) objekt, byggstenarna i en pivot-tabell. Objekten är:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) representerar en fält i en [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) representerar en samling av alla [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) objekt i [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) representerar en PivotTable på ett kalkylblad.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) representerar en samling av alla [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) objekt på ett kalkylblad.

### **Skapa en enkel pivot-tabell med hjälp av Aspose.Cells**
1. Lägg till data på ett kalkylblad genom att använda [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) objektets [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) metod.
   Denna data kommer att användas som pivot-tabellens datakälla.
1. Lägg till en pivot-tabell i kalkylbladet genom att anropa [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) samlingen [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) metod, som är innesluten i Worksheet-objektet.
1. Kom åt det nya [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)-objektet från [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)-samlingen genom att passera PivotTable-indexet.
1. Använd något av [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)-objekten (förklaras ovan) för att hantera pivot-tabellen.
Efter att ha kört exempelkoden läggs en pivot-tabell till kalkylbladet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}
När du tilldelar ett cellområde som datakälla måste området gå från övre vänstra till nedre högra. Till exempel är "A1:C3" giltigt men "C3:A1" är inte det.
{{% /alert %}}

## **Fortsatta ämnen**

{{< app/cells/assistant language="python-net" >}}