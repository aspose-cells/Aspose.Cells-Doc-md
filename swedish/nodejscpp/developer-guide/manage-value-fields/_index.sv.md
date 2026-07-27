---
title: Värdefält i Aspose.Cells for Node.js via C++
linktitle: Värdefält i Aspose.Cells for Node.js via C++
description: Lär dig hur du lägger till basfält i dataområdet i en pivottabell, ändrar sammanfattningsfunktionen med PivotField.Function och visar värdefältet på Rad- eller Kolumn-axeln i Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Node.js, C++, pivottabell, värdefält, PivotField, PivotField.Function, datafält, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /sv/nodejs-cpp/manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Värdefält är kärnan i varje pivottabell, de numeriska aggregat som sammanfattar källdatan. I Aspose.Cells for Node.js via C++ fylls dataområdet i en pivottabell genom att lägga till basfält via `PivotTable.addFieldToArea`, och varje fält som placeras i det området kan ha sin egen sammanfattningsfunktion. När två eller flera datafält finns, exponerar Aspose.Cells ett speciellt aggregatfält, `PivotTable.ValuesField`, som kan visas på Rad- eller Kolumn-axeln som ett basfält, vilket ger dig finare kontroll över hur värdefälten visas i layouten.

## Lägga till ett fält i dataområdet

Att lägga till ett basfält i data(värde)området är det första steget för att forma hur en pivottabell aggregerar din källdata. Aspose.Cells exponerar `PivotTable.addFieldToArea(PivotFieldType, string)`, en överlagring som accepterar konstanten `PivotFieldType.Data` och namnet på källkolumnen. När ett fält har lagts till i dataområdet exponerar API:et det via samlingen `PivotTable.DataFields`, i den ordning som fälten lades till. Som standard sammanfattas en numerisk källkolumn med `ConsolidationFunction.Sum`, medan en icke-numerisk kolumn som standard är `Count`.

## Ändra sammanfattningsfunktionen

Varje fält som placeras i dataområdet är internt förpackat som en `PivotField`-instans, och dess egenskap `Function` returnerar ett värde från enum-typen `ConsolidationFunction`. Samma `Function`-setter låter dig växla mellan de tillgängliga aggregaten, inklusive `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` och `Varp`.

{{% alert color="primary" %}}
Att ändra `Function` påverkar bara aggregatet, källkolumnen ändras inte.
{{% /alert %}}

Du kan därför lämna ett datafält som `Sum` medan du lägger till ett andra datafält som riktar sig mot samma källkolumn men använder `Count` eller `Average`, allt i en enda pivot.

## Visa värdefält på Rad- eller Kolumn-axeln

När en pivottabell innehåller två eller flera datafält, exponerar Aspose.Cells ytterligare ett virtuellt fält som kallas `PivotTable.ValuesField`. Detta virtuella fält representerar aggregatet av varje datafält som finns i dataområdet. Du kan dra det till Rad- eller Kolumn-området som ett baspivotfält, vilket är användbart för att lägga ut flera mått sida vid sida.

{{% alert color="primary" %}}
`PivotTable.ValuesField` fungerar inte om det inte finns något eller bara ett värdefält.
{{% /alert %}}

Scenarierna nedan går igenom tre kompletta exempel som demonstrerar varje funktion som beskrivs ovan mot samma pivotstruktur.

## Scenario 1 — Dra ett basfält till värdeområdet

Detta scenario visar hur man placerar ett enskilt basfält (`Amount`) i dataområdet för en befintlig pivottabell. Den delade pivotstrukturen placerar `Category` och `Item` på Rad-axeln och `Year` på Kolumn-axeln. Efter operationen visas `Amount` i dataområdet och beräknas som `Sum` av `Amount` som standard.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Rubriker i A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// Datarader A2:D9 med nästlade loopar som förgrenar sig på j
for (let i = 1; i <= 8; i++) {
  for (let j = 0; j < 4; j++) {
    switch (j) {
      case 0:
        worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
        break;
      case 1:
        if (i == 1 || i == 2) worksheet.getCells().get(i, j).putValue("Apple");
        else if (i == 3 || i == 4) worksheet.getCells().get(i, j).putValue("Banana");
        else if (i == 5 || i == 6) worksheet.getCells().get(i, j).putValue("Carrot");
        else worksheet.getCells().get(i, j).putValue("Daikon");
        break;
      case 2:
        worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
        break;
      case 3:
        if (i == 1) worksheet.getCells().get(i, j).putValue(100);
        else if (i == 2) worksheet.getCells().get(i, j).putValue(150);
        else if (i == 3) worksheet.getCells().get(i, j).putValue(80);
        else if (i == 4) worksheet.getCells().get(i, j).putValue(90);
        else if (i == 5) worksheet.getCells().get(i, j).putValue(50);
        else if (i == 6) worksheet.getCells().get(i, j).putValue(60);
        else if (i == 7) worksheet.getCells().get(i, j).putValue(40);
        else worksheet.getCells().get(i, j).putValue(45);
        break;
    }
  }
}

// Lägg till pivottabell vid F3 med namnet PivotTable1
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivotlayout: Kategori och Vara på Rad, År på Kolumn, Belopp som datafält
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Scenario 2 — Ändra sammanfattningsfunktionen

Detta scenario utgår från samma pivotstruktur som Scenario 1 men lägger till `Amount`-fältet i dataområdet två gånger. Båda datafälten refererar till samma källkolumn, men det andra fältet åsidosätts med hjälp av `PivotField.Function`-settern så att det blir `Count` istället för standardvärdet `Sum`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

for (let i = 1; i <= 8; i++)
{
    for (let j = 0; j <= 3; j++)
    {
        if (j == 0)
        {
            worksheet.getCells().get(i, j).putValue(i <= 5 ? "Fruit" : "Vegetable");
        }
        else if (j == 1)
        {
            let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
            worksheet.getCells().get(i, j).putValue(items[i - 1]);
        }
        else if (j == 2)
        {
            let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
            worksheet.getCells().get(i, j).putValue(years[i - 1]);
        }
        else
        {
            let amounts = [100, 150, 80, 90, 50, 60, 40, 45];
            worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
        }
    }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let countField = pivotTable.getDataFields().get(1);
countField.setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_function.xlsx");
```

## Scenario 3 — Visa värdefält på Rad- eller Kolumn-axeln

Med två datafält på plats blir `PivotTable.ValuesField` användbart. Detta scenario drar det virtuella aggregatfältet till Kolumn-området så att varje mått i dataområdet visas som sitt eget kolumnblock bredvid `Year`.

<!-- CODE_BLOCK:2:Build a complete end-to-end sample that starts with a require statement to load the Aspose.Cells Node.js module, then creates a Workbook instance, calls workbook.getWorksheets().get(0) to obtain the first worksheet, assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual worksheet.getCells().get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.Data, "Amount") twice. Assign pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.Count) so the second data field becomes Count while the first remains Sum. Finally call pivotTable.addFieldToArea(PivotFieldType.Column, pivotTable.getValuesField().getName()) to plot the value fields onto the Column axis. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_plot.xlsx"). The final layout has Row region (Category, Item), Column region (Year + ValuesField), and Data region (Sum-of-Amount, Count-of-Amount). -->

Tillsammans täcker dessa tre scenarier varje aspekt av värdefältshantering i Aspose.Cells for Node.js via C++, från ett enskilt datafält med standardvärdet `Sum` till en pivot med flera mått där det virtuella `ValuesField` styr layouten på Rad- eller Kolumn-axeln.

## Relaterade artiklar

- [Pivot Table Row and Column Fields in Aspose.Cells for Node.js via C++](/cells/sv/nodejs-cpp/row-and-column-fields/)
- [Page Fields in Pivot Tables](/cells/sv/nodejs-cpp/add-page-field-in-pivot-table/)
- [Refreshing Pivot Tables in Aspose.Cells for Node.js via C++](/cells/sv/nodejs-cpp/refresh-pivot-table/)
- [Applying Styles to Pivot Tables](/cells/sv/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript" >}}