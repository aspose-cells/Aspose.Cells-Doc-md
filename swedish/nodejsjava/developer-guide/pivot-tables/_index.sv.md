---
title: Infoga pivottabell
linktitle: Infoga pivottabell
description: Skapa och formatera pivottabeller i Excel-kalkylarksfiler med Aspose.Cells for Node.js via Java.
keywords: Skapa pivottabell, Infoga pivottabell, Formatera pivottabell, Aspose.Cells for Node.js via Java.
type: docs
weight: 160
url: /sv/nodejs-java/create-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Vad är en pivottabell?**
En pivottabell är en interaktiv sammanfattningsrapport: den komprimerar en stor mängd rådata, ordnad rad för rad, till en kompakt matris utan en enda formel. Du avgör vilka kolumner som ska bli radetiketter, vilka som ska bli kolumnetiketter och vilka som ska aggregeras som värden – pivottabellen utför grupperingen och beräkningen:
- **Sammanfatta** – total försäljning per produkt, region eller kvartal i stället för långa formelkedjor.
- **Jämför** – kategorier på raderna och perioder i kolumnerna gör en enkel lista till en korsrapport där trender syns tydligt med ett ögonkast.
- **Granska detaljer** – dubbelklicka på valfritt sammanfattningsvärde för att undersöka källraderna bakom det.
- **Uppdatera** – när källdatan ändras räknas hela rapporten om med en enda uppdatering.
Typiska användningsområden är säljinstrumentpaneler, kostnadsfördelningar och lageranalys. De används för att besvara frågor av formen ”hur bryts de här siffrorna ned per kategori och tid?”. Aspose.Cells for Node.js via Java skapar motsvarande pivottabeller programmatiskt, så att arbetsböcker som ditt program genererar kan innehålla färdiga rapporter i stället för enbart rådata.

### **Objektmodell för pivottabell**
Aspose.Cells tillhandahåller ett antal klasser som används för att skapa och styra pivottabeller. De centrala byggstenarna är:
- `PivotField` representerar ett fält i en `PivotTable`.
- `PivotFieldCollection` representerar en samling av alla `PivotField`-objekt i `PivotTable`.
- `PivotTable` representerar en pivottabell i ett kalkylblad.
- `PivotTableCollection` representerar en samling av alla `PivotTable`-objekt i ett kalkylblad.

### **Skapa en enkel pivottabell med Aspose.Cells**
Att skapa en pivottabell innebär fyra steg: skriv källdatan till cellerna i kalkylbladet, lägg till pivottabellen på den valda destinationen och placera pivotfälten i rad-, kolumn- och dataområdena.
1. Lägg till data i ett kalkylblad med cellens `putValue`-metod. Datan används som pivottabellens datakälla.
2. Lägg till en pivottabell i kalkylbladet genom att anropa `PivotTables`-samlingens `add`-metod: `add(sourceData, row, column)`. `sourceData` är källintervallet (till exempel "A1:C8"); `row` och `column` är de nollbaserade rad- och kolumnkoordinaterna för destinationscellen i pivottabellens övre vänstra hörn (cellen E3 innebär rad 2, kolumn 4). Metoden returnerar direkt det nya `PivotTable`-objektet.
3. Placera pivotfälten med `PivotTable`-objektets `addFieldToArea`-metod: ett fältnamn placeras i radområdet (`PivotFieldType.ROW`), kolumnområdet (`PivotFieldType.COLUMN`) eller dataområdet (`PivotFieldType.DATA`).
4. Spara arbetsboken – pivottabellen skrivs till den sparade filen.
När exempelkoden har körts läggs pivottabellen till i kalkylbladet.

```javascript
const AsposeCells = require("aspose.cells");

// Skapa en ny arbetsbok och hämta det första kalkylarket
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Skriv källdatan: försäljning per sport och kvartal
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

// Lägg till en pivottabell vid destinationscellen E3, med källdata från A1:C8
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Tilldela pivotfält: Sport till Rader, Quarter till Kolumner, Sales till Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");

// Spara arbetsboken
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
När ett cellintervall tilldelas som datakälla måste det gå från övre vänstra hörnet till nedre högra hörnet. För exempel är "A1:C3" ett giltigt intervall, men "C3:A1" är det inte.
{{% /alert %}}

## Relaterade artiklar
- [Lägg till filterfält i en pivottabell med Aspose.Cells for Node.js via Java](/cells/sv/nodejs-java/add-page-field-in-pivot-table/)
- [Använd stilar på pivottabeller i Aspose.Cells for Node.js via Java](/cells/sv/nodejs-java/apply-style-to-pivot-table/)
- [Ändra layouten för sidfält i en pivottabell](/cells/sv/nodejs-java/change-page-field-layout/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Hantera värdefält i pivottabeller med Aspose.Cells for Node.js via Java](/cells/sv/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}