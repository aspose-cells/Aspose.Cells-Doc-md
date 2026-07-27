---
title: Lägga till rad- och kolumnfält i en pivottabell i Aspose.Cells för .NET
linktitle: Rad- och kolumnfält
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.SetSubtotals in Aspose.Cells for Node.js via C++
keywords: Aspose.Cells, Node.js, C++, pivot table, row field, column field, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /sv/nodejs-cpp/pivot-table-add-row-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


Rad- och kolumnfält är byggstenarna i en pivottabell. Ett fält som placeras i radområdet visas vertikalt till vänster i pivoten, medan ett fält som placeras i kolumnområdet visas horisontellt överst. Den här artikeln visar hur du lägger till basfält i dessa områden programmatiskt och hur du styr de subtotaler som visas mellan fältgrupper med hjälp av metoden `PivotField.SetSubtotals`.

## **Lägga till ett fält i rad- eller kolumnområdet**

Metoden `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` flyttar ett basfält från källdatan till ett av de fyra pivotområdena. Argumentet `fieldType` accepterar ett av följande `PivotFieldType`-värden.

- `Row` — fält placerade vertikalt till vänster
- `Column` — fält placerade horisontellt överst
- `Data` — fält vars värden aggregeras
- `Page` — fält som används som rapportfilter

När fälten har lagts till kan du komma åt dem via egenskaperna `PivotTable.RowFields` och `PivotTable.ColumnFields`. Varje egenskap returnerar en `PivotFieldCollection`. Fältet vid index 0 i `RowFields` är det yttersta radfältet, och efterföljande index representerar fält som är kapslade inuti det. Samma indexeringskonvention gäller för `ColumnFields`.

Ordningen på fältens kapsling är viktig. Om du lägger till `Category` i radområdet först och sedan `Item` skapas en pivot vars yttre gruppering är `Category` och vars inre gruppering är `Item`. Om du vänder på ordningen vänds hierarkin.

## **Pivotfältssubtotaler**

Metoden `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` styr vilka subtotalrader som visas för ett pivotfält. Varje anrop växlar en enskild subtotaltyp oberoende. Om du skickar `shown = true` visas subtotalen, medan `shown = false` döljer den. Eftersom varje anrop endast påverkar en typ, kan du bygga en anpassad delmängd av subtotaler genom att anropa metoden flera gånger med olika `subtotalType`-värden.

Enum `PivotFieldSubtotalType` definierar de tillgängliga subtotaltyperna.

- `Automatic` — Aspose.Cells väljer standardvalet (vanligtvis `Sum` för numeriska fält)
- `None` — undertryck alla subtotalrader
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
Subtotaler renderas endast när det finns två eller flera pivotfält i radområdet (eller i kolumnområdet). Ett enskilt fält har inget meningsfullt att subtotalera mellan, så `SetSubtotals`-anrop har ingen synlig effekt i det fallet. Den här artikeln placerar därför två radfält (`Category` ytter, `Item` inre) i varje exempel så att subtotalgränsen mellan varje `Category`-grupp syns.
{{% /alert %}}

## **Scenario 1 — Automatiska (standard) subtotaler**

När du inte anropar `SetSubtotals` alls tillämpar Aspose.Cells `Automatic`-valet på numeriska fält. Följande exempel bekräftar uttryckligen detta beteende genom att anropa `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` på det yttre `Category`-radfältet.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_automatic.xlsx");
```

## **Scenario 2 — Undertrycka alla subtotaler (None)**

Om du anropar `SetSubtotals(PivotFieldSubtotalType.None, true)` tas varje subtotalrad bort från pivoten, vilket bara lämnar fältraderna och den totala summan längst ner. Detta är användbart när du vill ha den råa grupperade datan utan några sammanfattningsrader.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];

for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

const categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **Scenario 3 — Anpassad uppsättning av subtotaler (Sum + Average)**

Du är inte begränsad till en enskild subtotaltyp. Varje `SetSubtotals`-anrop fungerar oberoende på en typ, så om du anropar metoden två gånger — en gång med `Sum` och en gång med `Average` — skapas en anpassad uppsättning av två subtotalrader för varje `Category`-grupp.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get("A1").putValue("Category");
worksheet.getCells().get("B1").putValue("Item");
worksheet.getCells().get("C1").putValue("Year");
worksheet.getCells().get("D1").putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

let pivotTables = worksheet.getPivotTables();
let pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_custom.xlsx");
## **Sammanfattning**

De tre scenarierna ovan delar samma dataset och pivottabellstruktur. Den enda skillnaden mellan dem är `SetSubtotals`-anropet som tillämpas på det yttre `Category`-radfältet. Kom ihåg regeln om två fält: ett enskilt fält i ett område har inget att subtotalera mellan, så placera alltid minst två fält i rad- eller kolumnområdet när du vill att `SetSubtotals` ska ha en synlig effekt.

## **Relaterade artiklar**

- [Sidfält i pivottabeller](/cells/sv/nodejs-cpp/add-page-field-in-pivot-table/)
- [Uppdatera pivottabeller i Aspose.Cells for Node.js via C++](/cells/sv/nodejs-cpp/refresh-pivot-table/)
- [Tillämpa stilar på pivottabeller](/cells/sv/nodejs-cpp/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
