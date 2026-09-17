---
title: Hantera värdefält i pivottabeller i Aspose.Cells for .NET
linktitle: Hantera värdefält i pivottabeller i Aspose.Cells for .NET
description: Lär dig hur du lägger till basfält i dataregionen i en pivottabell, ändrar summeringsfunktionen med PivotField.Function och placerar värdefältet på rad- eller kolumnaxeln i Aspose.Cells for .NET.
keywords: Aspose.Cells, .NET, pivottabell, värdefält, PivotField, PivotField.Function, datafält, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /sv/net/manage-value-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Lägga till ett fält i dataregionen
Att lägga till ett basfält i data- (värde-)regionen är det första steget när man formar hur en pivottabell aggregerar källdatan. Aspose.Cells exponerar `PivotTable.AddFieldToArea(PivotFieldType, string)`, en överlagring som accepterar konstanten `PivotFieldType.Data` och källkolumnens namn. När ett fält har lagts till i dataregionen exponerar API:et det via samlingen `PivotTable.DataFields`, i den ordning som fälten lades till. Som standard sammanfattas en numerisk källkolumn med `ConsolidationFunction.Sum`, medan en icke-numerisk kolumn som standard får värdet `Count`.

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
    { "Fruit",     "Banana", 2020,  80 },
    { "Fruit",     "Banana", 2021,  90 },
    { "Vegetable", "Carrot", 2020,  50 },
    { "Vegetable", "Carrot", 2021,  60 },
    { "Vegetable", "Daikon", 2020,  40 },
    { "Vegetable", "Daikon", 2021,  45 }
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
pivotTable.CalculateData();
workbook.Save("output_drag.xlsx");
```

## Ändra summeringsfunktionen
När ett fält finns i dataregionen exponerar Aspose.Cells det via `PivotField`-objektet på `PivotTable.DataFields`. Varje `PivotField` har en skrivbar egenskap `Function` av typen `ConsolidationFunction`, som styr den aggregering som tillämpas på fältets underliggande värden. `ConsolidationFunction` är en enum med medlemmarna `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` och `Varp` — de första sex täcker de allra flesta verkliga användningsfallen, medan de fyra sista är statistiska aggregeringar som är användbara för variansanalys.

{{% alert color="primary" %}}
Att ändra `Function` påverkar endast aggregeringen; källkolumnen och pivotens rad-/kolumnstruktur ändras inte. För att byta aggregering för ett befintligt datafält anger du `pivotTable.DataFields[i].Function = ConsolidationFunction.<X>;` och anropar sedan `pivotTable.CalculateData()` för att rendera om pivoten.
{{% /alert %}}

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
    { "Fruit",     "Banana", 2020,  80 },
    { "Fruit",     "Banana", 2021,  90 },
    { "Vegetable", "Carrot", 2020,  50 },
    { "Vegetable", "Carrot", 2021,  60 },
    { "Vegetable", "Daikon", 2020,  40 },
    { "Vegetable", "Daikon", 2021,  45 }
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
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
PivotField countField = pivotTable.DataFields[1];
countField.Function = ConsolidationFunction.Count;
pivotTable.CalculateData();
workbook.Save("output_function.xlsx");
```

## Plotta värdefält på rad- eller kolumnaxeln
När en pivottabell innehåller två eller flera datafält exponerar Aspose.Cells ett ytterligare virtuellt fält som kallas `PivotTable.ValuesField`. Detta virtuella fält representerar aggregeringen av alla datafält som finns i dataregionen. Du kan dra det till rad- eller kolumnregionen som ett baspivotfält, vilket är användbart när du vill lägga ut flera mått sida vid sida.

{{% alert color="primary" %}}
`PivotTable.ValuesField` fungerar inte om det inte finns något värdefält eller endast ett enda värdefält.
{{% /alert %}}

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
    { "Fruit",     "Banana", 2020,  80 },
    { "Fruit",     "Banana", 2021,  90 },
    { "Vegetable", "Carrot", 2020,  50 },
    { "Vegetable", "Carrot", 2021,  60 },
    { "Vegetable", "Daikon", 2020,  40 },
    { "Vegetable", "Daikon", 2021,  45 }
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
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.DataFields[1].Function = ConsolidationFunction.Count;
pivotTable.AddFieldToArea(PivotFieldType.Column, pivotTable.ValuesField.Name);
pivotTable.CalculateData();
workbook.Save("output_plot.xlsx");
```

{{< app/cells/assistant language="csharp" >}}