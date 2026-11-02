---
title: Visa eller filtrera topp 10 i pivottabell
linktitle: Visa eller filtrera topp 10 i pivottabell
description: Lär dig att endast visa de högst eller lägst rangordnade objekten i ett pivotfält i Aspose.Cells for .NET. Den här artikeln behandlar metoden Top10AutoShow i Excel 97-2003, hur du läser inställningar med Top10AutoShowSettings och filtret för topp 10 i Excel 2007-365 via FilterTop10.
keywords: Aspose.Cells, .NET, pivottabell, topp 10, automatisk visning, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, C#
type: docs
weight: 20
url: /sv/net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell som listar alla objekt i ett radfält kan vara svårläst när fältet har dussintals medlemmar. En topp 10-rapport behåller endast de högst eller lägst rangordnade objekten, vilket är precis vad rapporter med rangordning behöver – "topp 5 produkter efter intäkt" eller "de tre lägsta regionerna efter antal försäljningar". Aspose.Cells stöder två mekanismer för detta, som motsvarar två generationer av Microsoft Excel.
- **Automatisk visning i Excel 97-2003** – metoden `PivotField.Top10AutoShow()`. Detta är den klassiska inställningen "Visa de översta/understa N objekten" som lagras direkt i pivotfältet. Den fungerar i alla Excel-versioner, både äldre och nyare, eftersom den ingår i det ursprungliga pivottabellformatet.
- **Topp 10-filter i Excel 2007-365** – metoden `PivotField.FilterTop10()`. Detta är det moderna värdefiltret för topp 10 som finns under fältmenyns värdefilter. Det lagras som ett `PivotFilter`-objekt som är kopplat till fältet och erbjuder rangordning baserad på antal objekt respektive procent.

## **Visa topp 10 i Excel 97-2003 (Top10AutoShow)**
Den klassiska funktionen för automatisk visning konfigureras med ett enda anrop till `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int count, int rankBy)`:
- `isAutoShow` – aktiverar eller inaktiverar inställningen för automatisk visning i fältet.
- `isTop` – `true` behåller de högst rangordnade objekten (Topp), medan `false` behåller de lägst rangordnade objekten (Botten).
- `count` – hur många objekt som ska behållas, till exempel 10 för en klassisk topp 10-rapport.
- `rankBy` – det nollbaserade indexet för **datfältet** vars värden rangordnar objekten. Ange -1 för att rangordna objekten efter fältet självt.
Rangordningen kan baseras på ett värdefält eller på fältet självt. Det finns två vanliga varianter, som visas nedan.

### **Rangordna efter ett värdefält**
Rangordna radfältets objekt efter ett vanligt värdefält, till exempel "Sum of Sales". Följande exempel skapar en pivottabell med ett radfält (`Sport`) och ett datfält (`Sales`) och visar sedan de två högst rangordnade sportgrupperna efter försäljning. `rankBy` är 0 eftersom "Sum of Sales" är datfältet på index 0.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Visa de 2 högsta objekten, rankade efter "Sum of Sales" (datafältets index 0)
sportField.Top10AutoShow(true, true, 2, 0);
pivotTable.CalculateData();
workbook.Save("output-top10-by-value-field.xlsx");
```

### **Rangordna efter fältet självt**
Ett fält kan också rangordnas utifrån sina egna värden – ange -1 som `rankBy`. För denna variant behövs inget extra datfält; fältet behöver endast finnas i rad- eller kolumnområdet. Följande exempel visar de tre lägst rangordnade sportgrupperna, rangordnade efter fältet självt. När inställningen sparas utelämnas attributet `rankBy` från pivottabellens XML eftersom -1 är formatets standardvärde, och `Top10AutoShowSettings.RankBy` läser tillbaka värdet -1.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Visa de 3 lägsta objekten rankade efter fältet självt (rankBy = -1)
sportField.Top10AutoShow(true, false, 3, -1);
pivotTable.CalculateData();
workbook.Save("output-top10-by-field-itself.xlsx");
```

## **Läsa de aktuella inställningarna (Top10AutoShowSettings)**
Egenskapen `PivotField.Top10AutoShowSettings` returnerar ett `PivotFieldTop10AutoShowSettings`-objekt som exponerar de inställningar för automatisk visning som för närvarande lagras i fältet. Använd den för att kontrollera hur objekt presenteras i en befintlig arbetsbok eller i en pivottabell som du nyss konfigurerat – även när arbetsboken har lästs in från en fil.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
PivotField sportField = pivotTable.RowFields[0];
PivotFieldTop10AutoShowSettings settings = sportField.Top10AutoShowSettings;
Console.WriteLine("AutoShow enabled: " + settings.IsAutoShow);
Console.WriteLine("Direction: " + (settings.IsTop ? "Top" : "Bottom"));
Console.WriteLine("Item count: " + settings.AutoShowCount);
Console.WriteLine("Ranking data field index: " + settings.RankBy);
```

De fyra egenskaperna motsvarar de klassiska AutoShow-attributen som skrivs till pivottabellens XML (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), och värdena som läses tillbaka är därför de värden som alla Excel-versioner tillämpar.

## **Obs!**

{{% alert color="primary" %}}
- De direkta egenskaperna i `PivotField` – `IsAutoShow`, `IsAscendShow`, `AutoShowCount` och `AutoShowField` – är markerade som föråldrade. Använd objektet `Top10AutoShowSettings` i stället: `IsAutoShow` motsvarar `Top10AutoShowSettings.IsAutoShow`, `IsAscendShow` motsvarar `Top10AutoShowSettings.IsTop`, `AutoShowCount` motsvarar `Top10AutoShowSettings.AutoShowCount` och `AutoShowField` motsvarar `Top10AutoShowSettings.RankBy`. Ändra inställningarna med metoden `Top10AutoShow()`, som är det sätt som stöds.
- `Top10AutoShow` fungerar med rad- och kolumnfält. Ett fält som endast finns i sidoområdet (filterområdet) kan inte rangordnas på det här sättet eftersom dess objekt inte placeras i pivottabellens huvuddel.
{{% /alert %}}

## **Excel 2007-365: topp 10-filter (FilterTop10)**
Moderna Excel-versioner erbjuder topp 10 som ett värdefilter i fältmenyn (Värdefilter, Topp 10...). Aspose.Cells implementerar det med metoden `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`, som returnerar det skapade `PivotFilter`-objektet:
- `valueFieldIndex` – det nollbaserade indexet för det datfält vars aggregerade värden används för att rangordna objekten.
- `type` – vad `itemCount` betyder. `PivotFilterType.Count` behåller ett bestämt antal objekt (dialogens alternativ Objekt). `PivotFilterType.Percent` behåller en procentandel av objekten, så `itemCount` är procentandelen i sig – 30 behåller de översta 30 procenten. `PivotFilterType.Sum` rangordnar efter den kumulativa andelen av det totala värdet.
- `isTop` – `true` för Topp, `false` för Botten.
- `itemCount` – N i Topp N; enheten beror på `type`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Top 10-filter — behåll de 2 främsta objekten enligt "Sum of Sales" (datafältsindex 0)
PivotFilter filter = sportField.FilterTop10(0, PivotFilterType.Count, true, 2);
// För ett procentbaserat filter i stället, behåll de främsta 30 procenten av objekten:
// sportField.FilterTop10(0, PivotFilterType.Percent, true, 30);
pivotTable.PivotCache.Refresh();
pivotTable.CalculateData();
workbook.Save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`Top10AutoShow` och `FilterTop10` är två separata funktioner. Funktionen för automatisk visning skriver det klassiska attributet `autoShow` till pivotfältet och stöds av alla Excel-versioner från Excel 97 och framåt. `FilterTop10` skriver en modern `PivotFilter`-post, som kräver Excel 2007 eller senare. När en arbetsbok öppnas i en äldre Excel-version visar en pivottabell som använder det moderna filtret alla objekt. För dokument som måste överföras fram och tillbaka via äldre verktyg bör du använda `Top10AutoShow`; för moderna arbetsböcker bör du använda `FilterTop10` eftersom det kan kombineras med de andra värdefiltren.
{{% /alert %}}

## **Relaterade artiklar**
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/net/filter-by-label-or-value-of-pivot-table/)
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/net/pivot-table-add-row-and-column-fields/)
- [Gruppera pivotfält i pivottabellen](/cells/sv/net/group-pivot-fields-in-the-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/net/refresh-pivot-table/)
- [Lägg till sidfält i pivottabell](/cells/sv/net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="csharp" >}}