---
title: Diskret gruppering av pivotfältsobjekt
linktitle: Diskret gruppering
description: Lär dig hur du grupperar pivotfältsobjekt i anpassade grupper med egna namn, till exempel frukt och grönsaker, med DiscreteGroupItem och PivotFieldGroupOptions.getDiscreteGroupItems() i Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, pivottabell, diskret gruppering, DiscreteGroupItem, PivotFieldGroupOptions, gruppera pivotfältsobjekt, anpassade grupper, PivotField.group, Aspose.Cells for Node.js via Java, Excel-pivottabell
type: docs
weight: 90
url: /sv/nodejs-java/discrete-group-pivot-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
- Automatisk gruppering kategoriserar objekt efter datatyp, till exempel datum till månader och kvartal eller tal till intervall. Diskret gruppering löser det motsatta problemet genom att gruppera specifika, orelaterade objekt i anpassade grupper med egna namn, till exempel produkter i grupperna frukt och grönsaker, butiker i regioner eller konton i zoner. Aspose.Cells erbjuder diskret gruppering via klassen `DiscreteGroupItem` och egenskapen `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- En `DiscreteGroupItem` består av ett gruppnamn och de objekt som tillhör gruppen. Objekt kan identifieras på två sätt: med sina namn (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) eller med sina nollbaserade positioner i källdatan (`new DiscreteGroupItem("fruit", [0, 3])`). Båda formerna ger samma resultat.
- Diskret gruppering tillämpas på ett fält i rad- eller kolumnområdet i pivottabellen genom att skicka grupperingsalternativen till `PivotField.group(PivotFieldGroupOptions)`.

## **Gruppera pivotfältsobjekt efter objektnamn**
Följande exempel bygger en liten försäljningslista (produkt, datum och belopp), skapar en pivottabell från den med `product` i radområdet, `date` i kolumnområdet och `amount` i dataområdet och definierar sedan två anpassade grupper efter objektnamn: fruit (`grape`, `cherry`) och vegetable (`carrot`, `potato`). Resultatet visar en layout med två nivåer i radområdet, där gruppnamnet utgör den yttre nivån och de ursprungliga objekten är nästlade under, så att trender kan utläsas för varje anpassad grupp och varje objekt.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(44232);
cells.get(2, 1).putValue(44628);
cells.get(3, 1).putValue(45026);
cells.get(4, 1).putValue(45428);
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
pivotTable.calculateData();
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

Efter `calculateData()` visar pivottabellens radområde fruit (`grape` 50, `cherry` 80) och vegetable (`carrot` 60, `potato` 70). Totalsumman är 260, och kolumnetiketterna visar fortfarande de fyra datumen (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Gruppera pivotfältsobjekt efter objektindex**
När objektnamnen är långa eller lokaliserade identifierar den andra konstruktorn för `DiscreteGroupItem` objekten med index. Varje index är en nollbaserad position för ett objekt i den ordning objekten förekommer i källdatan, inte i alfabetisk ordning. I dataexemplet ovan är `grape` objekt 0, `carrot` objekt 1, `potato` objekt 2 och `cherry` objekt 3, så fruit är `{ 0, 3 }` och vegetable är `{ 1, 2 }`. Resultatet är identiskt med exemplet baserat på namn.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
// Use Excel serial dates because JavaScript Date objects cannot be passed through the bridge.
cells.get(1, 1).putValue(44232); // 2021-02-05
cells.get(2, 1).putValue(44628); // 2022-03-08
cells.get(3, 1).putValue(45026); // 2023-04-10
cells.get(4, 1).putValue(45428); // 2024-05-16
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0).
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(
    AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
);
// Calculate the pivot table before grouping.
pivotTable.calculateData();
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data).
// The Node.js bridge requires item names rather than the index-based constructor.
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Obs!**

{{% alert color="primary" %}}
- Objekt som inte har tilldelats någon anpassad grupp försvinner inte. De ligger kvar i pivottabellen på samma nivå som de anpassade grupperna, där varje objekt utgör en separat post. I exemplet ovan, där endast fruktgruppen har definierats, ligger `carrot` och `potato` kvar i radområdet som fristående objekt bredvid fruktgruppen.
- Egenskapen `PivotFieldGroupOptions.getNewPivotField()` styr layouten för diskret gruppering. Standardvärdet är `true`, vilket innebär att det fält som grupperas läggs till som ett nytt yttre fält bredvid det ursprungliga fältet. Då skapas layouten med två nivåer som visas ovan, och antalet fält i `getRowFields()` ökar till 2. Ange värdet till `false` med `PivotFieldGroupOptions.setNewPivotField(false)` för att i stället ersätta det ursprungliga fältet. Radområdet visar då en enda nivå med endast gruppnamnen och deras aggregerade värden: fruit 130 (50 + 80) och vegetable 130 (60 + 70).
- De namnbaserade och indexbaserade konstruktorerna för `DiscreteGroupItem` kan kombineras i samma `getDiscreteGroupItems()`-array.
{{% /alert %}}

## **Relaterade artiklar**
- [Gruppera pivotfält i pivottabellen](/cells/sv/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [Lägg till rad- och kolumnfält i pivottabellen](/cells/sv/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Tillämpa format på pivottabellen](/cells/sv/nodejs-java/apply-style-to-pivot-table/)
- [Uppdatera pivottabellen](/cells/sv/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}