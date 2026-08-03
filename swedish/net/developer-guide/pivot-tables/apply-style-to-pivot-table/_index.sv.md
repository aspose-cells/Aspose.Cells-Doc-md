---
title: Tillämpa stilar på pivottabeller i Aspose.Cells för .NET
linktitle: Tillämpa pivottabellstilar
description: Lär dig hur du tillämpar inbyggda och anpassade stilar på pivottabeller i Aspose.Cells for .NET, inklusive äldre XLS-autoformat, moderna namngivna stilar från Excel 2007+, anpassade pivottabellstilar och genvägen FormatAll.
keywords: Aspose.Cells .NET pivottabell stil, PivotTableStyleType, AutoFormatType, FormatAll, anpassad stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /sv/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder både äldre pivot-autoformat (avsedda för `.xls`-filer) och moderna namngivna eller anpassade pivottabellstilar (avsedda för `.xlsx`-, `.xlsm`- och `.xlsb`-filer). Vilket API du ska anropa beror på det filformat som arbetsboken sparas till, inte det format den lästes in från.

{{% /alert %}}

## **Introduktion**

Aspose.Cells exponerar två parallella stil-API:er för pivottabeller. Valet mellan dem styrs av det filformat du sparar arbetsboken till, inte av det format du läser in den från. En arbetsbok som lästs in från en `.xls`-fil kan sparas om som `.xlsx`, och i det fallet gäller det moderna stil-API:t snarare än det äldre.

För äldre `.xls`-utdata använder du egenskapen `PivotTable.AutoFormatType` tillsammans med enumerationen `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Detta API motsvarar den autoformatväljare som klassisk Excel erbjöd för pivottabeller.

För modern `.xlsx`-, `.xlsm`- och `.xlsb`-utdata finns två varianter av stil-API:t:

- `PivotTable.PivotTableStyleType` väljer en av de inbyggda namngivna stilarna (ljust och mörkt tema, inklusive de stilar som lades till i Excel 2017). Dessa förinställningar är skrivskyddade.
- `PivotTable.PivotTableStyleName` väljer en anpassad stil som du själv definierar via `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. Anpassade stilar krävs när du vill ändra färger, kantlinjer eller teckensnitt utöver vad förinställningarna erbjuder.

Dessutom är `PivotTable.FormatAll(Style)` en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivottabellen och åsidosätter det som har ställts in via någon av ovanstående stilnamns-API:er. Detta är användbart när ett enhetligt utseende krävs oavsett det underliggande temat.

## **Tillämpa ett äldre XLS-förinställt autoformat**

`PivotTable.AutoFormatType` accepterar ett värde från enumerationen `Aspose.Cells.Pivot.PivotTableAutoFormatType`. De tillgängliga värdena är `Report1` till `Report10`, `Classic` och `Table1` till `Table10`.

{{% alert color="primary" %}}

`AutoFormatType` respekteras endast när arbetsboken sparas som `.xls`. När samma arbetsbok sparas som `.xlsx`, `.xlsm` eller `.xlsb` ignorerar Excel den här egenskapen och faller tillbaka på inställningarna `PivotTableStyleType` och `PivotTableStyleName`.

{{% /alert %}}

Följande exempel laddar en ny arbetsbok, fyller i exempeldata för Fruit/Year/Amount, lägger till en pivottabell, tillämpar `PivotTableAutoFormatType.Report5` och sparar resultatet som `.xls`.

{{% alert color="primary" %}}

**Varför inga kolumnfält?** Autoformaten i Report-serien (`Report1` till `Report10`, `Table1` till `Table10`) designades i klassiska Excel för **endimensionella pivottabeller** med endast radfält och värden — de har ingen inbyggd formatering för kolumnfält-rubriker. Om din pivottabell behöver kolumnfält, använd de moderna `PivotTableStyleType`-förinställningarna från Scenario 2 nedan istället, som är designade för den tvådimensionella layout som moderna Excel använder.

{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Scenario 1: Tillämpa ett äldre XLS-förinställt automatiskt format
// API in use: PivotTable.AutoFormatType
// Target file format: .xls (legacy)
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

// Create a new workbook
Workbook workbook = new Workbook();

// Get the first worksheet
Worksheet sheet = workbook.Worksheets[0];

// Populate the source data with header row (Fruit, Year, Amount)
// and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
sheet.Cells[0, 0].PutValue("Fruit");
sheet.Cells[0, 1].PutValue("Year");
sheet.Cells[0, 2].PutValue("Amount");

sheet.Cells[1, 0].PutValue("grape");
sheet.Cells[1, 1].PutValue(2020);
sheet.Cells[1, 2].PutValue(50);

sheet.Cells[2, 0].PutValue("blueberry");
sheet.Cells[2, 1].PutValue(2020);
sheet.Cells[2, 2].PutValue(30);

sheet.Cells[3, 0].PutValue("kiwi");
sheet.Cells[3, 1].PutValue(2020);
sheet.Cells[3, 2].PutValue(25);

sheet.Cells[4, 0].PutValue("cherry");
sheet.Cells[4, 1].PutValue(2020);
sheet.Cells[4, 2].PutValue(40);

sheet.Cells[5, 0].PutValue("grape");
sheet.Cells[5, 1].PutValue(2021);
sheet.Cells[5, 2].PutValue(60);

sheet.Cells[6, 0].PutValue("blueberry");
sheet.Cells[6, 1].PutValue(2021);
sheet.Cells[6, 2].PutValue(35);

sheet.Cells[7, 0].PutValue("kiwi");
sheet.Cells[7, 1].PutValue(2021);
sheet.Cells[7, 2].PutValue(28);

sheet.Cells[8, 0].PutValue("cherry");
sheet.Cells[8, 1].PutValue(2021);
sheet.Cells[8, 2].PutValue(45);

sheet.Cells[9, 0].PutValue("grape");
sheet.Cells[9, 1].PutValue(2020);
sheet.Cells[9, 2].PutValue(45);

// Add a pivot table at destination cell E3, named "Pivot1", using source range A1:C10
int pivotIndex = sheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// Assign fields: Fruit -> Rows, Year -> Columns, Amount -> Data
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Apply the legacy XLS preset autoformat "Report5"
// Note: This property is only meaningful when saving as .xls.
// When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
// and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;

// Save the workbook in legacy .xls format
workbook.Save("output.xls");
```

## **Tillämpa en modern namngiven förinställd pivottabellstil**

`PivotTable.PivotTableStyleType` accepterar ett värde från enumerationen `Aspose.Cells.PivotTableStyleType`. Enumerationen täcker ljusa teman `PivotTableStyleLight1` till `PivotTableStyleLight28` och mörka teman `PivotTableStyleDark1` till `PivotTableStyleDark28`. Stilarna som lades till i Excel 2017 (den andra omgången av ljusa och mörka teman) kan nås via samma enumeration.

Detta är det rekommenderade API:t för alla moderna filformat. Till skillnad från det äldre autoformatet återges stilen som väljs här troget av Excel och överlever rundresor genom andra Office-verktyg.

Följande exempel använder samma Fruit/Year/Amount-data, skapar en identisk pivottabell, tillämpar `PivotTableStyleDark1` och sparar arbetsboken som `.xlsx`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Scenario 2: Tillämpa en modern Excel 2007+ namngiven förinställd stil med PivotTableStyleType.
// Målfilformat: .xlsx. PivotTableStyleType-uppräkningen finns i Aspose.Cells-namnrymden
// (inte i Aspose.Cells.Pivot) — det är därför vi inte behöver någon extra using för den.
// GitHub-referens: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Rubrikrad: Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 9 datarader med Fruit / Year / Amount
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(150);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(180);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(120);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(170);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(210);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(190);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(130);

// Lägg till en pivottabell vid E3 med namnet "Pivot1", med källa från A1:C10
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Tilldela pivotfält: Fruit -> Radområde, Year -> Kolumnområde, Amount -> Dataområde
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Tillämpa en modern Excel 2007+ namngiven förinställd pivotstil.
// PivotTableStyleType är det korrekta API:et för .xlsx / .xlsm / .xlsb-filer; AutoFormatType
// ignoreras av Excel för dessa format. PivotTableStyleDark1 tillhör den mörka temafamiljen
// (PivotTableStyleDark1..PivotTableStyleDark28), och samma uppräkning exponerar också de
// nyare Excel 2017 ljus/mörk-teman (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1;

// Spara som modern .xlsx — detta är formatet för vilket PivotTableStyleType är meningsfullt.
workbook.Save("output.xlsx");
```

## **Definiera och tillämpa en anpassad pivottabellstil**

De inbyggda förinställningarna kan inte modifieras. När du behöver åsidosätta färger, kantlinjer eller teckensnitt måste du definiera en anpassad pivotstil. Arbetsflödet har tre steg:

1. Lägg till en anpassad stil i arbetsbokens `TableStyles`-samling via `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. Detta returnerar indexet för den nyskapade stilen.
2. Konfigurera stilen genom att lägga till element (t.ex. `WholeTable` eller `GrandTotalRow`) via `TableStyle.TableStyleElements.Add(TableStyleElementType)`, och tilldela sedan en `Style` till varje element via `TableStyleElement.SetElementStyle(Style)`.
3. Tillämpa den anpassade stilen på pivottabellen genom att sätta `PivotTable.PivotTableStyleName` till stilens namn. Använd inte `PivotTableStyleType` här, eftersom den egenskapen väljer inbyggda förinställningar.

{{% alert color="primary" %}}

`PivotTableStyleName` och `PivotTableStyleType` är inte utbytbara. Använd `PivotTableStyleType` för inbyggda förinställningar, och `PivotTableStyleName` för anpassade stilar som du har definierat via `AddPivotTableStyle`. Att sätta båda är ofarligt, men det är bara den som matchar den avsedda källan som återges.

{{% /alert %}}

De tillgängliga `TableStyleElementType`-värdena inkluderar `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` och `PageFieldValues`.

Följande exempel definierar en anpassad pivotstil med en tunn svart kantlinje på `WholeTable` och ett fetstilt rött teckensnitt på `GrandTotalRow`, och tillämpar den sedan via `PivotTableStyleName` och sparar som `.xlsx`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using System.Drawing;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Populera källdata: rubrikrad + 9 datarader (A1:C10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);

// Lägg till pivottabell med källa från A1:C10, förankrad vid E3, namngiven "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Steg 1: registrera en ny anpassad pivottabellstil och fånga dess index
int styleIndex = workbook.Worksheets.TableStyles.AddPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.Worksheets.TableStyles[styleIndex];

// Steg 2: lägg till ett WholeTable-element och tillämpa tunna svarta kanter på alla fyra sidor
int wholeTableElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.WholeTable);
TableStyleElement wholeTableElement = tableStyle.TableStyleElements[wholeTableElementIndex];
Style wholeTableStyle = workbook.CreateStyle();
wholeTableStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.TopBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.BottomBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.LeftBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.RightBorder].Color = Color.Black;
wholeTableElement.SetElementStyle(wholeTableStyle);

// Steg 3: lägg till ett GrandTotalRow-element och tillämpa fet röd teckensnitt
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);

// Steg 4: tillämpa den anpassade stilen efter namn (INTE efter PivotTableStyleType, vilket är för inbyggda förinställningar)
pivotTable.PivotTableStyleName = "CustomPivotStyle";

workbook.Save("output.xlsx");
```

## **Tillämpa en stil på varje pivotcell med FormatAll**

`PivotTable.FormatAll(Style)` är en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivottabellen, inklusive dataområdet, rad- och kolumnrubriker samt summor. Det som tidigare ställts in via `PivotTableStyleType` eller `PivotTableStyleName` åsidosätts.

{{% alert color="primary" %}}

`FormatAll` åsidosätter både `PivotTableStyleType` och `PivotTableStyleName`. Använd det endast när ett enhetligt, temaoberoende utseende krävs över hela pivottabellen.

{{% /alert %}}

Följande exempel skapar en `Style` med gul solid fyllning, ett fetstilt mörkblått teckensnitt och tunna svarta kantlinjer på alla sidor, och tillämpar den sedan med `FormatAll` och sparar som `.xlsx`.

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Scenario 4: Tillämpa en enda Stil på varje pivottabellcell med FormatAll
// API som används: PivotTable.FormatAll(Style)
// Målformat: .xlsx
// GitHub-referens: se Aspose.Cells-for-.NET repository — pivottabellformateringsexempel

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Fylla källdata: rubrikrad (rad 1) + 9 datarader (raderna 2-10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(5000);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(3000);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(4000);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(2000);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(6000);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(3500);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(4500);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(2500);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(5500);

// Lägg till pivottabell: källområde A1:C10, målcell E3, namn "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Tilldela pivotfält: Fruit -> Rad-område, Year -> Kolumn-område, Amount -> Data-område
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Bygg en Stil som tvingas på varje cell i pivottabellen
Style style = workbook.CreateStyle();
style.ForegroundColor = Color.Yellow;
style.Pattern = BackgroundType.Solid;
style.Font.IsBold = true;
style.Font.Color = Color.DarkBlue;
style.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.TopBorder].Color = Color.Black;
style.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.BottomBorder].Color = Color.Black;
style.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.LeftBorder].Color = Color.Black;
style.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.RightBorder].Color = Color.Black;

// Tillämpa FormatAll: tvingar denna enda stil på varje cell i pivottabellen,
// och åsidosätter alla PivotTableStyleType / PivotTableStyleName som tidigare ställts in
pivotTable.FormatAll(style);

// Spara arbetsboken i det moderna .xlsx-formatet
workbook.Save("output.xlsx");
```

## **Vilket stil-API ska jag använda?**

Valet av stil-API beror på det filformat du sparar till. Använd tabellen nedan som en snabbreferens.

| Målfilformat | API att använda | Anteckningar |
|---|---|---|
| `.xls` (äldre) | `PivotTable.AutoFormatType` | Värden från `Aspose.Cells.Pivot.PivotTableAutoFormatType` (t.ex. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignoreras vid sparning som moderna format. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, inbyggd stil) | `PivotTable.PivotTableStyleType` | Värden från `Aspose.Cells.PivotTableStyleType` (ljust/mörkt tema, inklusive tillägg från Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, anpassad stil) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Använd när de inbyggda förinställningarna inte räcker. Konfigurera via `TableStyleElement.SetElementStyle(...)`. |
| Valfritt format (enhetlig åsidosättning) | `PivotTable.FormatAll(Style)` | Genväg som åsidosätter alla andra stilinställningar över hela pivottabellen. |

Vid tveksamhet, spara som `.xlsx` och använd `PivotTableStyleType` för inbyggda teman, eller `PivotTableStyleName` för anpassade teman.

{{< app/cells/assistant language="csharp" >}}