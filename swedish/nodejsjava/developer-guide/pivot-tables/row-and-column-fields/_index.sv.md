---
title: Lägga till rad- och kolumnfält i en pivottabell i Aspose.Cells för .NET
linktitle: Rad- och kolumnfält
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.setSubtotals in Aspose.Cells for Node.js via Java
keywords: Aspose.Cells, Node.js, Java, pivot table, row field, column field, PivotField, setSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /sv/nodejs-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Lägga till ett fält i rad- eller kolumnregionen**

Metoden `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` flyttar ett basfält från källdatan till en av de fyra pivotregionerna. Argumentet `fieldType` accepterar ett av följande `PivotFieldType`-värden.

- `ROW` — fält placerade vertikalt till vänster
- `COLUMN` — fält placerade horisontellt överst
- `DATA` — fält vars värden aggregeras
- `PAGE` — fält som används som rapportfilter

När fälten har lagts till kan du komma åt dem via egenskaperna `PivotTable.getRowFields()` och `PivotTable.getColumnFields()`. Varje egenskap returnerar en `PivotFieldCollection`. Fältet på index 0 i `RowFields` är det yttersta radfältet, och efterföljande index representerar fält som är nästlade inuti det. Samma indexeringskonvention gäller för `ColumnFields`.

Ordningen på fältnästningen är viktig. Att lägga till `Category` i radregionen först och sedan `Item` skapar en pivot vars yttre gruppering är `Category` och vars inre gruppering är `Item`. Att vända ordningen vänder på hierarkin.

## **Pivotfältets delsummor**

Metoden `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` styr vilka delsummerader som visas för ett pivotfält. Varje anrop växlar en enskild delsummatyp oberoende. Att skicka `shown = true` visar delsummen, medan `shown = false` döljer den. Eftersom varje anrop endast påverkar en typ, kan du bygga en anpassad delmängd av delsummor genom att anropa metoden flera gånger med olika `subtotalType`-värden.

Enumerationen `PivotFieldSubtotalType` definierar de tillgängliga delsummatyperna.

- `AUTOMATIC` — Aspose.Cells väljer standardvalet (vanligtvis `SUM` för numeriska fält)
- `NONE` — undertrycker alla delsummerader
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Delsummor renderas endast när det finns två eller flera pivotfält i radregionen (eller i kolumnregionen). Ett enskilt fält har inget meningsfullt att summera mellan, så `setSubtotals`-anrop har ingen synlig effekt i det fallet. Denna artikel placerar därför två radfält (`Category` ytterst, `Item` innerst) i varje exempel så att delsummegränsen mellan varje `Category`-grupp blir synlig.
{{% /alert %}}

## **Scenario 1 — Automatiska (standard) delsummor**

När du inte anropar `setSubtotals` alls tillämpar Aspose.Cells valet `AUTOMATIC` på numeriska fält. Följande exempel bekräftar uttryckligen detta beteende genom att anropa `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` på det yttre `Category`-radfältet.

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

pivotTable.calculateData();

workbook.save("output_automatic.xlsx");
```

## **Scenario 2 — Undertrycka alla delsummor (None)**

Att anropa `setSubtotals(PivotFieldSubtotalType.NONE, true)` tar bort alla delsummerader från pivottabellen och lämnar endast fältraderna och den totala summan längst ner. Detta är användbart när du vill ha den råa grupperade datan utan några sammanfattningsrader.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

let headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

let data = [
    ["Fruit", "Apple", 2020, 100],
    ["Fruit", "Apple", 2021, 150],
    ["Fruit", "Banana", 2020, 80],
    ["Fruit", "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];

for (let i = 0; i < data.length; i++)
{
    for (let j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **Scenario 3 — Anpassad delmängd av delsummor (Sum + Average)**

Du är inte begränsad till en enda delsummatyp. Varje `setSubtotals`-anrop fungerar oberoende på en typ, så att anropa metoden två gånger — en gång med `SUM` och en gång med `AVERAGE` — skapar en anpassad delmängd av två delsummerader för varje `Category`-grupp.

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

pivotTable.calculateData();

workbook.save("output_custom.xlsx");
```
## **Sammanfattning**

De tre scenarierna ovan delar samma dataset och pivottabellstruktur. Den enda skillnaden mellan dem är `setSubtotals`-anropet som tillämpas på det yttre `Category`-radfältet. Kom ihåg regeln om två fält: ett enskilt fält i en region har inget att summera mellan, så placera alltid minst två fält i rad- eller kolumnregionen när du vill att `setSubtotals` ska ha en synlig effekt.
Rad- och kolumnfält är byggstenarna i en pivottabell. Ett fält som placeras i radregionen visas vertikalt till vänster i pivottabellen, medan ett fält som placeras i kolumnregionen visas horisontellt överst. Den här artikeln visar hur du lägger till basfält i dessa regioner programmatiskt och hur du styr delsummorna som renderas mellan fältgrupper med metoden `PivotField.setSubtotals`.

## **Lägga till ett fält i rad- eller kolumnregionen**

Metoden `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` flyttar ett basfält från källdatan till en av de fyra pivotregionerna. Argumentet `fieldType` accepterar ett av följande `PivotFieldType`-värden.

- `ROW` — fält placerade vertikalt till vänster
- `COLUMN` — fält placerade horisontellt överst
- `DATA` — fält vars värden aggregeras
- `PAGE` — fält som används som rapportfilter

När fälten har lagts till kan du komma åt dem via egenskaperna `PivotTable.getRowFields()` och `PivotTable.getColumnFields()`. Varje egenskap returnerar en `PivotFieldCollection`. Fältet på index 0 i `RowFields` är det yttersta radfältet, och efterföljande index representerar fält som är nästlade inuti det. Samma indexeringskonvention gäller för `ColumnFields`.

Ordningen på fältnästningen är viktig. Att lägga till `Category` i radregionen först och sedan `Item` skapar en pivot vars yttre gruppering är `Category` och vars inre gruppering är `Item`. Att vända ordningen vänder på hierarkin.

## **Pivotfältets delsummor**

Metoden `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` styr vilka delsummerader som visas för ett pivotfält. Varje anrop växlar en enskild delsummatyp oberoende. Att skicka `shown = true` visar delsummen, medan `shown = false` döljer den. Eftersom varje anrop endast påverkar en typ kan du bygga en anpassad delmängd av delsummor genom att anropa metoden flera gånger med olika `subtotalType`-värden.

Enumerationen `PivotFieldSubtotalType` definierar de tillgängliga delsummatyperna.

- `AUTOMATIC` — Aspose.Cells väljer standardvalet (vanligtvis `SUM` för numeriska fält)
- `NONE` — undertrycker alla delsummerader
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Delsummor renderas endast när det finns två eller flera pivotfält i radregionen (eller i kolumnregionen). Ett enskilt fält har inget meningsfullt att summera mellan, så `setSubtotals`-anrop har ingen synlig effekt i det fallet. Den här artikeln placerar därför två radfält (`Category` ytterst, `Item` innerst) i varje exempel så att delsummegränsen mellan varje `Category`-grupp blir synlig.
{{% /alert %}}

## **Scenario 1 — Automatiska (standard) delsummor**

När du inte anropar `setSubtotals` alls tillämpar Aspose.Cells valet `AUTOMATIC` på numeriska fält. Följande exempel bekräftar uttryckligen detta beteende genom att anropa `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` på det yttre `Category`-radfältet.## **Scenario 2 — Undertrycka alla delsummor (None)**

Att anropa `setSubtotals(PivotFieldSubtotalType.NONE, true)` tar bort alla delsummerader från pivottabellen och lämnar endast fältraderna och den totala summan längst ner. Detta är användbart när du vill ha den råa grupperade datan utan några sammanfattningsrader.## **Scenario 3 — Anpassad delmängd av delsummor (Sum + Average)**

Du är inte begränsad till en enda delsummatyp. Varje `setSubtotals`-anrop fungerar oberoende på en typ, så att anropa metoden två gånger — en gång med `SUM` och en gång med `AVERAGE` — skapar en anpassad delmängd av två delsummerader för varje `Category`-grupp.## **Sammanfattning**

De tre scenarierna ovan delar samma dataset och pivottabellstruktur. Den enda skillnaden mellan dem är `setSubtotals`-anropet som tillämpas på det yttre `Category`-radfältet. Kom ihåg regeln om två fält: ett enskilt fält i en region har inget att summera mellan, så placera alltid minst två fält i rad- eller kolumnregionen när du vill att `setSubtotals` ska ha en synlig effekt.
{{< app/cells/assistant language="nodejs-java" >}}
