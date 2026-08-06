---
title: Ändra sidfältslayout i pivottabell
linktitle: Ändra sidfältslayout i pivottabell
description: Lär dig hur du styr layouten för sidfältsområdet i en pivottabell med Aspose.Cells for .NET, inklusive inställning av visningsordning, omslagsantal och fältordning för sidfälten överst i pivottabellen.
keywords: Aspose.Cells, NET-bibliotek, kalkylblad, pivottabell, sidfält, sidfältsordning, sidfältets omslagsantal, flytta sidfält
type: docs
weight: 191
url: /sv/net/change-page-field-layout/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Den här artikeln är en fortsättning på ämnet **Lägg till sidfält i pivottabell**. Den visar hur man styr layouten för sidfältsområdet — remsan med filterkontroller överst i en pivottabell — inklusive visningsordning, omslagsantal och omordning av fält.

{{% /alert %}}

## **Introduktion**

En pivottabell i Microsoft Excel har ett dedikerat **sidfältsområde** som sitter ovanför rad-/kolumn-/datakroppen i tabellen. Det här området renderas som en remsa med rullmenyer för filter (en per sidfält) och är det som slutanvändare klickar på för att skära pivoten efter kriterier som år eller region. Aspose.Cells modellerar detta område genom samlingen `PivotTable.PageFields` och exponerar tre egenskaper som styr hur remsan visas visuellt:

- `PivotTable.PageFieldOrder` (ett värde av typen `Aspose.Cells.PrintOrderType`) avgör om ytterligare sidfält placeras *bredvid* de befintliga eller *under* dem.
- `PivotTable.PageFieldWrapCount` anger hur många sidfält som placeras per rad eller kolumn innan omslag sker.
- `PivotTable.PageFields.Move(currIndex, destIndex)` omordnar sidfälten utan att ändra ordningsläget.

Den här artikeln går igenom tre kodexempel som demonstrerar var och en av dessa operationer på en delad datamängd, så att du kan jämföra de resulterande layouterna sida vid sida.

## **Källdata**

Alla tre exempel nedan läser in dessa åtta rader med försäljningsdata till ett kalkylblad som heter `PivotData`. Informationen innehåller två kandidater för sidfält (`Year`, `Region`), en kandidat för radfält (`Fruit`) och ett mått (`Amount`), vilket gör att sidfältsremsan blir meningsfull att granska.

| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |

Alla åtta rader fylls i i varje kodexempel, i identisk ordning, så att källdata aldrig skiljer sig mellan scenarierna — det är bara egenskaperna för sidfältslayouten som gör det.

## **Exempel 1: Över sedan ned**

I det första scenariot konfigurerar vi de två sidfälten (`Year`, `Region`) så att de visas **sida vid sida i en enda rad** överst i pivottabellen. Vi tilldelar `Fruit` till radaxeln, placerar `Year` först och `Region` sedan på sidaxeln (ordningen på anropen till `AddFieldToArea` bestämmer startindexet), lägger till `Amount` (Sum) som datafält och anger sedan `PageFieldOrder` till `PrintOrderType.OverThenDown` med `PageFieldWrapCount = 2`. Med `OverThenDown` och ett omslagsantal på 2 läggs de två sidfälten ut horisontellt sida vid sida i en enda rad överst i pivottabellen, så att remsan upptar en rad med bredden två.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string dataDir = "output";
if (!Directory.Exists(dataDir)) Directory.CreateDirectory(dataDir);

Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.Worksheets;

int pivotDataIdx = worksheets.Add("PivotData");
Worksheet pivotDataSheet = worksheets[pivotDataIdx];
Cells pivotDataCells = pivotDataSheet.Cells;

// Rubriker (rad 0)
pivotDataCells[0, 0].PutValue("Fruit");
pivotDataCells[0, 1].PutValue("Year");
pivotDataCells[0, 2].PutValue("Region");
pivotDataCells[0, 3].PutValue("Amount");

// Rad 1: Apple, 2022, North, 150
pivotDataCells[1, 0].PutValue("Apple");
pivotDataCells[1, 1].PutValue(2022);
pivotDataCells[1, 2].PutValue("North");
pivotDataCells[1, 3].PutValue(150);

// Rad 2: Apple, 2023, North, 180
pivotDataCells[2, 0].PutValue("Apple");
pivotDataCells[2, 1].PutValue(2023);
pivotDataCells[2, 2].PutValue("North");
pivotDataCells[2, 3].PutValue(180);

// Rad 3: Banana, 2022, South, 120
pivotDataCells[3, 0].PutValue("Banana");
pivotDataCells[3, 1].PutValue(2022);
pivotDataCells[3, 2].PutValue("South");
pivotDataCells[3, 3].PutValue(120);

// Rad 4: Banana, 2023, South, 140
pivotDataCells[4, 0].PutValue("Banana");
pivotDataCells[4, 1].PutValue(2023);
pivotDataCells[4, 2].PutValue("South");
pivotDataCells[4, 3].PutValue(140);

// Rad 5: Cherry, 2022, East, 200
pivotDataCells[5, 0].PutValue("Cherry");
pivotDataCells[5, 1].PutValue(2022);
pivotDataCells[5, 2].PutValue("East");
pivotDataCells[5, 3].PutValue(200);

// Rad 6: Cherry, 2023, East, 220
pivotDataCells[6, 0].PutValue("Cherry");
pivotDataCells[6, 1].PutValue(2023);
pivotDataCells[6, 2].PutValue("East");
pivotDataCells[6, 3].PutValue(220);

// Rad 7: Grape, 2022, West, 90
pivotDataCells[7, 0].PutValue("Grape");
pivotDataCells[7, 1].PutValue(2022);
pivotDataCells[7, 2].PutValue("West");
pivotDataCells[7, 3].PutValue(90);

// Rad 8: Grape, 2023, West, 110
pivotDataCells[8, 0].PutValue("Grape");
pivotDataCells[8, 1].PutValue(2023);
pivotDataCells[8, 2].PutValue("West");
pivotDataCells[8, 3].PutValue(110);

// Lägg till PivotTableReport-arket
int pivotTableSheetIdx = worksheets.Add("PivotTableReport");
Worksheet pivotTableSheet = worksheets[pivotTableSheetIdx];
PivotTableCollection pivotTables = pivotTableSheet.PivotTables;

// Skapa pivottabell med källa från PivotData!A1:D9 placerad vid A1 på PivotTableReport
int pivotIndex = pivotTables.Add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

// Lägg till fält
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);   // Frukt
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);  // År
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);  // Region
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);  // Belopp
pivotTable.DataFields[0].Function = ConsolidationFunction.Sum;

// Konfigurera layout för sidfältsområdet: placera sidfält först horisontellt, radbryt efter var 2:a
pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

// Uppdatera och beräkna
pivotTable.CalculateData();

// Spara
workbook.Save(Path.Combine(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Exempel 2: Ned sedan över**

I det här exemplet placerar vi `Fruit` på radaxeln, `Year` och `Region` på sidaxeln (med `Year` först) och `Amount` (Sum) som datafält — exakt som i Exempel 1. Vi anger sedan `PageFieldOrder` till `PrintOrderType.DownThenOver` och `PageFieldWrapCount` till `2`. Med `DownThenOver` och ett omslagsantal på 2 staplas de två sidfälten vertikalt — `Year` överst, `Region` direkt under — och bildar en enda kolumn överst i pivottabellen. Remsan upptar alltså två rader med bredden ett, till skillnad från Exempel 1.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var pivotData = workbook.Worksheets[0];
pivotData.Name = "PivotData";
int pivotReportIdx = workbook.Worksheets.Add("PivotTableReport");
var pivotReport = workbook.Worksheets[pivotReportIdx];

var headers = new[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.Length; c++)
{
    pivotData.Cells[0, c].PutValue(headers[c]);
}

var data = new object[,]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};

for (int r = 0; r < data.GetLength(0); r++)
{
    for (int c = 0; c < data.GetLength(1); c++)
    {
        pivotData.Cells[r + 1, c].PutValue(data[r, c]);
    }
}

int idx = pivotReport.PivotTables.Add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.PivotTables[idx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.DownThenOver;
pivotTable.PageFieldWrapCount = 2;

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_downThenOver.xlsx");
```

## **Exempel 3: Flytta ett sidfält**

I det tredje scenariot behåller vi denna datamängd och fälttilldelning, anger en neutral layout (`OverThenDown` med omslagsantal `2`) och demonstrerar sedan operationen `PageFields.Move`. Anropet `Move(0, 1)` flyttar sidfältet på index 0 (`Year`) till position 1, och sidfältet som var på position 1 (`Region`) flyttas till position 0. Efter detta anrop är `Region` det första sidfältet och `Year` det andra. Omslaget och ordningsläget är oförändrade, så remsan renderas fortfarande horisontellt sida vid sida — det är bara ordningen på de två rullmenyerna som har bytts ut.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();

Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Name = "PivotData";

dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Year");
dataSheet.Cells["C1"].PutValue("Region");
dataSheet.Cells["D1"].PutValue("Amount");

dataSheet.Cells["A2"].PutValue("Apple");
dataSheet.Cells["B2"].PutValue(2022);
dataSheet.Cells["C2"].PutValue("North");
dataSheet.Cells["D2"].PutValue(150);

dataSheet.Cells["A3"].PutValue("Apple");
dataSheet.Cells["B3"].PutValue(2023);
dataSheet.Cells["C3"].PutValue("North");
dataSheet.Cells["D3"].PutValue(180);

dataSheet.Cells["A4"].PutValue("Banana");
dataSheet.Cells["B4"].PutValue(2022);
dataSheet.Cells["C4"].PutValue("South");
dataSheet.Cells["D4"].PutValue(120);

dataSheet.Cells["A5"].PutValue("Banana");
dataSheet.Cells["B5"].PutValue(2023);
dataSheet.Cells["C5"].PutValue("South");
dataSheet.Cells["D5"].PutValue(140);

dataSheet.Cells["A6"].PutValue("Cherry");
dataSheet.Cells["B6"].PutValue(2022);
dataSheet.Cells["C6"].PutValue("East");
dataSheet.Cells["D6"].PutValue(200);

dataSheet.Cells["A7"].PutValue("Cherry");
dataSheet.Cells["B7"].PutValue(2023);
dataSheet.Cells["C7"].PutValue("East");
dataSheet.Cells["D7"].PutValue(220);

dataSheet.Cells["A8"].PutValue("Grape");
dataSheet.Cells["B8"].PutValue(2022);
dataSheet.Cells["C8"].PutValue("West");
dataSheet.Cells["D8"].PutValue(90);

dataSheet.Cells["A9"].PutValue("Grape");
dataSheet.Cells["B9"].PutValue(2023);
dataSheet.Cells["C9"].PutValue("West");
dataSheet.Cells["D9"].PutValue(110);

int pivotSheetIdx = workbook.Worksheets.Add("PivotTableReport");
Worksheet pivotSheet = workbook.Worksheets[pivotSheetIdx];

int pivotIdx = pivotSheet.PivotTables.Add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.PivotTables[pivotIdx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

pivotTable.PageFields.Move(0, 1);

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_move.xlsx");
```

## **Relaterade artiklar**

- [Lägg till sidfält i pivottabell](/cells/sv/net/add-page-field-in-pivot-table/) — sidan som introducerar hur sidfält läggs till i en pivottabell.
- [Rad- och kolumnfält i pivottabell](/cells/sv/net/pivot-table-add-row-and-column-fields/) — täcker allokering av fält till rad- och kolumnaxlarna och kompletterar arbetet med sidaxeln som visas här.
- [Hantera värdefält i pivottabell](/cells/sv/net/manage-value-fields/) — beskriver hur man konfigurerar dataområdet (värde), inklusive `Sum`-aggregeringen som används i den här artikeln.
- [Uppdatera pivottabell](/cells/sv/net/refresh-pivot-table/) — förklarar `RefreshData` och `CalculateData`, vilka krävs efter omordning av sidfält.
- [Tillämpa stil på pivottabell](/cells/sv/net/apply-style-to-pivot-table/) — visar hur man formaterar den renderade pivottabellen efter att sidfältsremsan har lagts ut.

{{< app/cells/assistant language="csharp" >}}