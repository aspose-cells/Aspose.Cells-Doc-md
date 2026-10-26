---
title: Lägg till rad- och kolumnfält i pivottabeller med Aspose.Cells for Node.js via C++
linktitle: Lägg till rad- och kolumnfält i pivottabeller med Aspose.Cells for Node.js via C++
description: Lär dig att lägga till basfält i rad- och kolumnområdena i en pivottabell och styra delsummor för pivotfält med hjälp av PivotField.setSubtotals i Aspose.Cells for Node.js via C++
keywords: Aspose.Cells, Node.js, C++, pivottabell, radfält, kolumnfält, PivotField, SetSubtotals, PivotFieldSubtotalType, delsummor
type: docs
weight: 220
url: /sv/nodejs-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Lägga till ett fält i rad- eller kolumnområdet**
Metoden `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` flyttar ett basfält från källdatan till ett av pivottabellens fyra områden. Parametern `fieldType` accepterar ett av följande `PivotFieldType`-värden.
- `Row` – fält som placeras vertikalt till vänster
- `Column` – fält som placeras horisontellt överst
- `Data` – fält vars värden aggregeras
- `Page` – fält som används som rapportfilter
Fältens nästlingsordning är viktig. Om `Category` läggs till i radområdet före `Item` skapas en pivottabell där `Category` utgör den yttre grupperingen och `Item` den inre. Om ordningen är omvänd byter fältens inre och yttre gruppering plats.

## **Delsummor för pivotfält**
Metoden `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` styr vilka rader med delsummor som visas för ett pivotfält. Varje anrop styr om en enda typ av delsumma visas eller döljs, oberoende av övriga typer. Att ange `shown = true` visar delsumman, medan `shown = false` döljer den. Eftersom varje anrop endast påverkar en typ skapar upprepade anrop med olika `subtotalType`-värden ett anpassat urval av delsummor.
Enumet `PivotFieldSubtotalType` definierar de tillgängliga typerna av delsummor.
- `Automatic` – Aspose.Cells väljer den förvalda delsumtypen (vanligtvis `Sum` för numeriska fält)
- `None` – döljer alla rader med delsummor
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
Delsummor visas endast när radområdet eller kolumnområdet innehåller två eller fler pivotfält. För ett enda fält finns det inga grupper mellan vilka det är meningsfullt att visa delsummor, så anrop till `setSubtotals` får då ingen synlig effekt. I varje exempel placeras därför två radfält (`Category` ytterst, `Item` innerst), så att gränsen mellan varje `Category`-grupp och dess delsummor blir tydlig.
{{% /alert %}}

## **Scenario 1 – Automatiska delsummor (standardval)**
När `setSubtotals` inte anropas alls väljer Aspose.Cells `Automatic` för numeriska fält. Följande exempel bekräftar detta beteende uttryckligen genom att anropa `setSubtotals(PivotFieldSubtotalType.Automatic, true)` på det yttre radfältet `Category`.

```javascript
const AsposeCells = require("aspose.cells.node");
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
let pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **Scenario 2 – Dölja alla delsummor (None)**
När `setSubtotals(PivotFieldSubtotalType.None, true)` anropas tas alla rader med delsummor bort från pivottabellen, så att endast fältraderna och totalsumman längst ned återstår. Detta är användbart när du vill visa den grupperade rådatan utan några sammanfattningsrader.

```javascript
const AsposeCells = require("aspose.cells.node");
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
const pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
const categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **Scenario 3 – Anpassat urval av delsummor (Sum + Average)**
Du kan använda fler än en typ av delsumma. Varje anrop till `setSubtotals` påverkar en enda typ, oberoende av övriga typer. Därför skapar två anrop till metoden – en gång med `Sum` och en gång med `Average` – ett anpassat urval med två rader med delsummor för varje `Category`-grupp.

```javascript
const AsposeCells = require("aspose.cells.node");
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
let pivotTable = pivotTables.add("A1:D9", 2, 5);
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
De tre scenario skiljer sig åt i en sak endast: anroppen till `setSubtotals`. Allt annat — datasetet, fälten och de områden de tilldelas till — är identiskt, vilket gör att layouterna kan jämföras direkt.
- **Placering av fält.** `PivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, fieldName)` flyttar en källkolumn till ett område. Inom ett och samma område är kallordningen den visuella ordningen, så det första anropet blir det yttre gruppdjupet. Subtotaler kräver två eller fler fält i samma område: med ett enda fält finns det inget mellan grupperna att summera.
- **Scenario 1 — automatiska subtotaler.** Om `setSubtotals` inte anropas lämnas valet till Excel, som tillämpar sin egen standardsubtotal på numeriska fält. Att anropa `setSubtotals` med `AsposeCells.PivotFieldSubtotalType.Automatic` uttryckligen registrerar detta val istället för att lämna det implicit.
- **Scenario 2 — inga subtotaler.** `setSubtotals` med `AsposeCells.PivotFieldSubtotalType.None` inaktiverar standardsubtotallen, så pivottabellen behåller fältraderna och slutsumman men hinner inte in subtotalrader som Excel annars skulle infoga mellan dem.
- **Scenario 3 — ett valt urval.** Varje anrop växlar exakt en subtotaltyp, och anropen ackumulerar snarare än återställer varandra. Att anropa den en gång med `AsposeCells.PivotFieldSubtotalType.Sum` och en gång med `AsposeCells.PivotFieldSubtotalType.Average` lämnar båda aktiverade, och pivottabellen visar en Subtotal för Summa, en Subtotal för Medelvärde och en slutsumma.

{{% alert color="primary" %}}
Ingenting angående subtotaler är specifikt för radområdet. Samma anrop till `setSubtotals` på ett fält hämtat från `PivotTable.ColumnFields` producerar samma tre layouter på kolumnaxeln, eftersom inställningen hör till pivottabellfältet och inte till axeln det sitter på.
{{% /alert %}}

## **Relaterade artiklar**
- [Sidfält i pivottabeller](/cells/sv/nodejs-cpp/add-page-field-in-pivot-table/)
- [Uppdatera pivottabeller i Aspose.Cells for Node.js via C++](/cells/sv/nodejs-cpp/refresh-pivot-table/)
- [Tillämpa format på pivottabeller](/cells/sv/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}