---
title: Diskret gruppering av pivottabellfält
description: Lär dig hur du grupperar pivottabellfältobjekt i anpassade namngivna grupper såsom frukt och grönsaker med hjälp av DiscreteGroupItem och PivotFieldGroupOptions.DiscreteGroupItems i Aspose.Cells for Node.js via C++.
linktitle: Diskret gruppering
keywords: Aspose.Cells, pivottabell, diskret gruppering, DiscreteGroupItem, PivotFieldGroupOptions, gruppera pivottabellsobjekt, anpassade grupper, PivotField.Group, Node.js, Excel-pivottabell
type: docs
weight: 90
url: /sv/nodejs-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
- Automatisk gruppering samlar objekt efter datatyp, till exempel datum till månader och kvartal eller tal till intervall. Diskret gruppering löser det motsatta problemet genom att samla specifika, orelaterade objekt i anpassade namngivna grupper, till exempel produkter i frukt och grönsaker, butiker i regioner eller konton i zoner. Aspose.Cells for Node.js via C++ tillhandahåller diskret gruppering via klassen `DiscreteGroupItem` och egenskapen `PivotFieldGroupOptions.discreteGroupItems`.
- `DiscreteGroupItem` är ett gruppnamn plus de objekt som tillhör det. Objekt kan identifieras på två sätt, antingen med deras namn (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) eller med deras nollbaserade positioner i källdata (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Båda formerna ger samma resultat.
- Diskret gruppering tillämpas på ett fält i rad‑ eller kolumnområdet i pivottabellen genom att skicka alternativen till `pivotField.group(pivotFieldGroupOptions)`.

## **Gruppera pivottabellfältobjekt efter namn**
Följande exempel bygger en liten försäljningslista (produkt, datum och belopp), skapar en pivottabell från den med `product` i radområdet, `date` i kolumnområdet och `amount` i datatområdet, och definierar sedan två anpassade grupper efter objektnamn, frukt (grape, cherry) och grönsaker (carrot, potato). Resultatet visar en tvånivå radlayout, gruppnamnet som det yttre lagret och de ursprungliga objekten indenterade under, så trender kan läsas per anpassad grupp och per objekt.

```javascript
const AsposeCells = require("aspose.cells.node");
// Create a new workbook and get the first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Populate data
cells.get(0, 0).setValue("product");
cells.get(1, 0).setValue("grape");
cells.get(2, 0).setValue("carrot");
cells.get(3, 0).setValue("potato");
cells.get(4, 0).setValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Add date header and values
cells.get(0, 1).setValue("date");
cells.get(1, 1).setValue(new Date(2021, 1, 5));   // February is month 1
cells.get(2, 1).setValue(new Date(2022, 2, 8));
cells.get(3, 1).setValue(new Date(2023, 3, 10));
cells.get(4, 1).setValue(new Date(2024, 4, 16));
// Apply date style to the date column
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Add amount header and values
cells.get(0, 2).setValue("amount");
cells.get(1, 2).setValue(50);
cells.get(2, 2).setValue(60);
cells.get(3, 2).setValue(70);
cells.get(4, 2).setValue(80);
// Add a pivot table at cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// Group specific items into custom groups by item names
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
// Calculate pivot data and save the workbook
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

Efter `calculateData()` visar radområdet i pivottabellen frukt (grape 50, cherry 80) och grönsak (carrot 60, potato 70) med totalsumman 260, och kolumnetiketterna behåller de fyra datumen (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Gruppera pivottabellfältobjekt efter index**
När objektnamnen är långa eller lokalanpassade identifierar den andra konstruktorn av `DiscreteGroupItem` objekten med index. Indexen är nollbaserade positioner för objekten i den ordning de förekommer i källdatan, inte alfabetisk ordning. I exempeldata ovan är grape objekt 0, carrot objekt 1, potato objekt 2 och cherry objekt 3, så frukt är `{ 0, 3 }` och grönsak är `{ 1, 2 }`. Resultatet är identiskt med exempel baserat på namn.

```javascript
const AsposeCells = require("aspose.cells.node");
// Create workbook and get first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Fill data
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Date column header
cells.get(0, 1).putValue("date");
// Date values
cells.get(1, 1).putValue(new Date(2021, 1, 5));   // Feb 5, 2021
cells.get(2, 1).putValue(new Date(2022, 2, 8));   // Mar 8, 2022
cells.get(3, 1).putValue(new Date(2023, 3, 10));  // Apr 10, 2023
cells.get(4, 1).putValue(new Date(2024, 4, 16));  // May 16, 2024
// Apply date style to date cells
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Amount column header and values
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
const fruit = new AsposeCells.DiscreteGroupItem("fruit", [0, 3]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", [1, 2]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
// Save the workbook
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Obs**

{{% alert color="primary" %}}
- Objekt som inte tilldelas någon anpassad grupp förloras inte. De förblir i pivottabellen på samma nivå som de anpassade grupperna, varje som ett eget enskilt objekt. I exemplet ovan lämnar endast frukt‑gruppen moroten och potatisen i radområdet som fristående poster bredvid frukt‑gruppen.
- `PivotFieldGroupOptions.newPivotField`‑egenskapen styr layouten för diskret gruppering. Standardvärdet är true, vilket lägger till det grupperade fältet som ett nytt yttre fält bredvid det ursprungliga, vilket ger den tvånivålayout som visas ovan (`rowFields` växer till 2). Sätt den till false för att ersätta det ursprungliga fältet istället, då visar radområdet en enda nivå som endast innehåller gruppnamnen med deras aggregerade värden, frukt 130 (50 + 80) och grönsak 130 (60 + 70).
- De namn‑baserade och index‑baserade konstruktörerna för `DiscreteGroupItem` kan blandas i samma `PivotFieldGroupOptions.discreteGroupItems`‑array.
{{% /alert %}}

## **Related Articles**
- [Gruppera pivottabellfält i pivottabellen](/cells/sv/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [Lägg till rad‑ och kolumnfält i pivottabell](/cells/sv/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Använd stil på pivottabell](/cells/sv/nodejs-cpp/apply-style-to-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}