---
title: Infoga pivot tabell
linktitle: Pivot tabeller
type: docs
weight: 160
url: /sv/nodejs-cpp/create-pivot-table/
description: Skapa och formatera pivottabeller i Excel kalkylbladsfiler.
---

## **Skapa Pivottabell**

Det är möjligt att använda Aspose.Cells for Node.js via C++ för att programmässigt lägga till pivottabeller i kalkylblad.

### **Pivot-tabell objektmodell**

Aspose.Cells for Node.js via C++ tillhandahåller en speciell uppsättning klasser som används för att skapa och kontrollera pivottabeller. Dessa klasser används för att skapa och sätta [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) objekt, byggstenarna för en pivottabell. Objekt:

- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) representerar en fält i en [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) representerar en samling av alla [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) objekt i [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) representerar en PivotTable på ett kalkylblad.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) representerar en samling av alla [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) objekt på ett kalkylblad.

### **Skapa en enkel pivot-tabell med hjälp av Aspose.Cells**

1. Lägg till data på ett kalkylblad genom att använda [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) objektets [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) metod.
   Denna data kommer att användas som pivot-tabellens datakälla.
1. Lägg till en pivot-tabell i kalkylbladet genom att anropa [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) samlingen [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) metod, som är innesluten i Worksheet-objektet.
1. Kom åt det nya [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)-objektet från [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection)-samlingen genom att passera PivotTable-indexet.
1. Använd något av [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)-objekten (förklaras ovan) för att hantera pivot-tabellen.

Efter att ha kört exempelkoden läggs en pivot-tabell till kalkylbladet.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-create-pivot-table.js" >}}

{{% alert color="primary" %}}

När du tilldelar ett cellområde som datakälla måste området gå från övre vänstra till nedre högra. Till exempel är "A1:C3" giltigt men "C3:A1" är inte det.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
