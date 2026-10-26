---
title: Infoga pivottabell
linktitle: Infoga pivottabell
description: Skapa och formatera pivottabeller med Aspose.Cells for Node.js via C++.
keywords: Skapa pivottabell, Infoga pivottabell, Formatera pivottabell.
type: docs
weight: 160
url: /sv/nodejs-cpp/create-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Vad är en pivottabell?**
En pivottabell är en interaktiv sammanfattningsrapport: den sammanfattar en stor mängd rådata, som anges rad för rad, i en kompakt matris utan en enda formel. Du väljer vilka kolumner som blir radetiketter, vilka som blir kolumnetiketter och vilka som aggregeras som värden – pivottabellen utför grupperingen och beräkningarna:
- **Sammanfatta** – total försäljning per produkt, region eller kvartal i stället för långa formelkedjor.
- **Jämför** – kategorier på raderna och perioder på kolumnerna omvandlar en platt lista till en korsrapport där trender syns med en blick.
- **Gräns ned** – dubbelklicka på valfritt sammanfattningsvärde för att granska källraderna bakom det.
- **Uppdatera** – när källdatan ändras räknas hela rapporten om med en enda uppdatering.
Typiska användningsområden är säljdashboardar, kostnadsfördelningar och lageranalyser, exempelvis vid frågor av formen "hur kan dessa siffror brytas ned per kategori och tid?". Aspose.Cells for Node.js via C++ skapar samma pivottabeller programmatiskt, så att de arbetsböcker som programmet genererar kan innehålla färdiga rapporter i stället för enbart rådata.

### **Pivottabellens objektmodell**
Aspose.Cells for Node.js via C++ tillhandahåller en uppsättning särskilda klasser som används för att skapa och styra pivottabeller. Klasserna används för att skapa och konfigurera [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)-objekt, som är byggstenarna i en pivottabell. Objekten är:
- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) representerar ett fält i en [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) representerar en samling av alla [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield)-objekt i en [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) representerar en PivotTable i ett kalkylblad.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) representerar en samling av alla [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)-objekt i ett kalkylblad.

### **Skapa en enkel pivottabell med Aspose.Cells**
Att skapa en pivottabell innebär tre steg: skriv källdatan till celler i ett kalkylblad, lägg till pivottabellen på en vald plats och placera pivotfälten i rad-, kolumn- och dataområdena.
1. Lägg till data i ett kalkylblad med hjälp av metoden [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) i objektet [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). Denna data används som pivottabellens datakälla.
2. Lägg till en pivottabell i kalkylbladet genom att anropa metoden [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) i samlingen [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection): `add(sourceData, row, column)`. `sourceData` är källintervallet (till exempel "A1:C8"); `row` och `column` är de nollbaserade koordinaterna för destinationscellen i pivottabellens övre vänstra hörn (cell E3 innebär rad 2, kolumn 4). Metoden returnerar det nya objektet [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) direkt.
3. Placera pivotfälten med hjälp av metoden `addFieldToArea` i objektet [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable): ett fältnamn placeras i radområdet (`PivotFieldType.Row`), kolumnområdet (`PivotFieldType.Column`) eller dataområdet (`PivotFieldType.Data`).
4. Spara arbetsboken – pivottabellen inkluderas i den sparade filen.
När exempelkoden har körts läggs en pivottabell till i kalkylbladet.

```javascript
const AsposeCells = require("aspose.cells.node");

// Skapa en ny arbetsbok och hämta det första kalkylbladet
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Skriv källdata: försäljning per sport och kvartal
sheet.getCells().get("A1").putValue("Sport");
sheet.getCells().get("B1").putValue("Quarter");
sheet.getCells().get("C1").putValue("Sales");
sheet.getCells().get("A2").putValue("Golf");
sheet.getCells().get("B2").putValue("Qtr3");
sheet.getCells().get("C2").putValue(1500);
sheet.getCells().get("A3").putValue("Golf");
sheet.getCells().get("B3").putValue("Qtr4");
sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Tennis");
sheet.getCells().get("B4").putValue("Qtr3");
sheet.getCells().get("C4").putValue(600);
sheet.getCells().get("A5").putValue("Tennis");
sheet.getCells().get("B5").putValue("Qtr4");
sheet.getCells().get("C5").putValue(1500);
sheet.getCells().get("A6").putValue("Tennis");
sheet.getCells().get("B6").putValue("Qtr3");
sheet.getCells().get("C6").putValue(4070);
sheet.getCells().get("A7").putValue("Tennis");
sheet.getCells().get("B7").putValue("Qtr4");
sheet.getCells().get("C7").putValue(5000);
sheet.getCells().get("A8").putValue("Golf");
sheet.getCells().get("B8").putValue("Qtr3");
sheet.getCells().get("C8").putValue(6430);

// Lägg till en pivottabell vid destinationscellen E3, med A1:C8 som källa
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Tilldela pivotfält: Sport till Rader, Quarter till Kolumner, Sales till Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");

// Spara arbetsboken
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
När ett cellintervall tilldelas som datakälla måste intervallet gå från det övre vänstra hörnet till det nedre högra hörnet. "A1:C3" är exempelvis ett giltigt intervall, men "C3:A1" är det inte.
{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}