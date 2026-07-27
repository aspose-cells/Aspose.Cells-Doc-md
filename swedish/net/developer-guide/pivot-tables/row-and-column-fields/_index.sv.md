---
title: Lägga till rad- och kolumnfält i en pivottabell i Aspose.Cells för .NET
linktitle: Rad- och kolumnfält
description: Lär dig hur du lägger till basfält i rad- och kolumnregionerna i en pivottabell och styr pivotfältets delsummor med PivotField.SetSubtotals i Aspose.Cells for .NET.
keywords: Aspose.Cells, .NET, pivottabell, radfält, kolumnfält, PivotField, SetSubtotals, PivotFieldSubtotalType, delsummor
type: docs
weight: 220
url: /sv/net/pivot-table-add-row-column-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Rad- och kolumnfält är byggstenarna i en pivottabell. Ett fält som placeras i radregionen visas vertikalt till vänster i pivottabellen, medan ett fält som placeras i kolumnregionen visas horisontellt överst. Den här artikeln visar hur du lägger till basfält i dessa regioner programmässigt och hur du styr delsummorna som renderas mellan fältgrupper med hjälp av metoden `PivotField.SetSubtotals`.

## **Lägga till ett fält i rad- eller kolumnregionen**

Metoden `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` flyttar ett basfält från källdatan till en av de fyra pivotregionerna. Argumentet `fieldType` accepterar ett av följande `PivotFieldType`-värden.

- `Row` — fält som placeras vertikalt till vänster
- `Column` — fält som placeras horisontellt överst
- `Data` — fält vars värden aggregeras
- `Page` — fält som används som rapportfilter

När fälten har lagts till kan du komma åt dem via egenskaperna `PivotTable.RowFields` och `PivotTable.ColumnFields`. Varje egenskap returnerar en `PivotFieldCollection`. Fältet på index 0 i `RowFields` är det yttersta radfältet, och efterföljande index representerar fält som är nästlade inuti det. Samma indexeringskonvention gäller för `ColumnFields`.

Ordningen på fältnästningen är viktig. Att lägga till `Category` i radregionen först och sedan `Item` skapar en pivot vars yttre gruppering är `Category` och vars inre gruppering är `Item`. Om du vänder på ordningen vänds hierarkin.

## **Pivotfältets delsummor**

Metoden `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` styr vilka delsummarader som visas för ett pivotfält. Varje anrop växlar en enskild delsummatyp oberoende. Genom att skicka `shown = true` visas delsummaraden, medan `shown = false` döljer den. Eftersom varje anrop endast påverkar en typ, bygger upprepade anrop med olika `subtotalType`-värden en anpassad delmängd av delsummor.

Enumen `PivotFieldSubtotalType` definierar de tillgängliga delsummatyperna.

- `Automatic` — Aspose.Cells väljer standardvalet (vanligtvis `Sum` för numeriska fält)
- `None` — undertrycker varje delsummarad
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
Delsummor renderas endast när det finns två eller fler pivotfält i radregionen (eller i kolumnregionen). Ett enskilt fält har inget meningsfullt att subtotala mellan, så `SetSubtotals`-anrop har ingen synlig effekt i det fallet. Den här artikeln placerar därför två radfält (`Category` yttre, `Item` inre) i varje exempel så att delsummegränsen mellan varje `Category`-grupp syns.
{{% /alert %}}

## **Scenario 1 — Automatiska (standard) delsummor**

När du inte anropar `SetSubtotals` alls tillämpar Aspose.Cells valet `Automatic` på numeriska fält. Följande exempel bekräftar uttryckligen detta beteende genom att anropa `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` på det yttre `Category`-radfältet.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);

worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);

worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);

worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);

worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);

worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);

worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);

worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Automatic, true);

pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output_automatic.xlsx");
```

## **Scenario 2 — Undertrycka alla delsummor (None)**

Att anropa `SetSubtotals(PivotFieldSubtotalType.None, true)` tar bort varje delsummarad från pivottabellen och lämnar bara fältraderna och totalsumman längst ner. Detta är användbart när du vill ha den råa grupperade datan utan några sammanfattningsrader.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

string[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.Length; j++)
{
    worksheet.Cells[0, j].PutValue(headers[j]);
}

object[,] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020, 80  },
    { "Fruit",     "Banana", 2021, 90  },
    { "Vegetable", "Carrot", 2020, 50  },
    { "Vegetable", "Carrot", 2021, 60  },
    { "Vegetable", "Daikon", 2020, 40  },
    { "Vegetable", "Daikon", 2021, 45  }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.None, true);
pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output_none.xlsx");
```

## **Scenario 3 — Anpassad delsummaundergrupp (Sum + Average)**

Du är inte begränsad till en enda delsummatyp. Varje `SetSubtotals`-anrop verkar oberoende på en typ, så att anropa metoden två gånger — en gång med `Sum` och en gång med `Average` — skapar en anpassad delmängd av två delsummarader för varje `Category`-grupp.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells["A1"].PutValue("Category");
worksheet.Cells["B1"].PutValue("Item");
worksheet.Cells["C1"].PutValue("Year");
worksheet.Cells["D1"].PutValue("Amount");

worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);

worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);

worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);

worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);

worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);

worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);

worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);

worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);

PivotTableCollection pivotTables = worksheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Sum, true);
categoryField.SetSubtotals(PivotFieldSubtotalType.Average, true);

pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output_custom.xlsx");
```

## **Sammanfattning**

De tre scenarierna ovan delar samma dataset och pivottabellstruktur. Den enda skillnaden mellan dem är `SetSubtotals`-anropet som tillämpas på det yttre `Category`-radfältet. Kom ihåg tvåfältsregeln: ett enskilt fält i en region har inget att subtotala mellan, så placera alltid minst två fält i rad- eller kolumnregionen när du vill att `SetSubtotals` ska ha en synlig effekt.

## **Relaterade artiklar**

- [Sidfält i pivottabeller](/cells/sv/net/add-page-field-in-pivot-table/)
- [Uppdatera pivottabeller i Aspose.Cells for .NET](/cells/sv/net/refresh-pivot-table/)
- [Tillämpa stilar på pivottabeller](/cells/sv/net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
