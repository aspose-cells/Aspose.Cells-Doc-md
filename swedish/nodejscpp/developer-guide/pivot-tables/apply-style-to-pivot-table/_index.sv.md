---
title: Tillämpa stilar på pivottabeller i Aspose.Cells for Node.js via C++
linktitle: Tillämpa stilar på pivottabeller i Aspose.Cells for Node.js via C++
description: Lär dig hur du tillämpar inbyggda och anpassade stilar på pivottabeller med Aspose.Cells for Node.js via C++, inklusive äldre XLS-autoformat, moderna namngivna stilar för Excel 2007+, anpassade pivottabellstilar och FormatAll-genvägen.
keywords: Aspose.Cells Node.js via C++ pivottabellstil, PivotTableStyleType, AutoFormatType, FormatAll, anpassad stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /sv/nodejs-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder både äldre pivot-autoformat (avsedda för `.xls`-filer) och moderna namngivna eller anpassade pivottabellstilar (avsedda för `.xlsx`-, `.xlsm`- och `.xlsb`-filer). Vilket API du ska anropa beror på det filformat som arbetsboken sparas i, inte det format den lästes in från.
{{% /alert %}}

## **Introduktion**
Aspose.Cells exponerar två parallella stil-API:er för pivottabeller. Valet mellan dem styrs av det filformat du sparar arbetsboken till, inte av det format du läser in den från. En arbetsbok som lästs in från en `.xls`-fil kan sparas om som `.xlsx`, och i det fallet gäller det moderna stil-API:t istället för det äldre.
- `PivotTable.PivotTableStyleType` väljer en av de inbyggda namngivna stilarna (ljust och mörkt tema, inklusive de stilar som lades till i Excel 2017). Dessa förinställningar är skrivskyddade.
- `PivotTable.PivotTableStyleName` väljer en anpassad stil som du definierar själv via `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. Anpassade stilar krävs när du vill ändra färger, kanter eller typsnitt utöver vad förinställningarna erbjuder.
Dessutom är `PivotTable.FormatAll(Style)` en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivottabellen och åsidosätter det som ställts in via något av stilnamns-API:erna ovan. Detta är användbart när ett enhetligt utseende krävs oavsett underliggande tema.

## **Tillämpa ett äldre XLS-förinställt autoformat**
`PivotTable.AutoFormatType` accepterar ett värde från enumerationen `Aspose.Cells.Pivot.PivotTableAutoFormatType`. De tillgängliga värdena är `Report1` till `Report10`, `Classic` och `Table1` till `Table10`.
Följande exempel läser in en ny arbetsbok, fyller i exempeldata för Fruit/Year/Amount, lägger till en pivottabell, tillämpar `PivotTableAutoFormatType.Report5` och sparar resultatet som `.xls`.

{{% alert color="primary" %}}
**Varför inga kolumnfält?** Autoformat i Report-serien (`Report1` till `Report10`, `Table1` till `Table10`) designades i klassisk Excel för **endimensionella pivottabeller** med endast radfält och värden — de har ingen inbyggd formatering för kolumnfältsrubriker. Om din pivottabell behöver kolumnfält, använd de moderna `PivotTableStyleType`-förinställningarna från [Scenario 2](#apply-a-modern-named-preset-pivot-table-style) istället, vilka är designade för den tvådimensionella layout som modern Excel använder.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
// Scenario 1: Tillämpa ett äldre XLS-förinställt autoformat
// API som används: PivotTable.AutoFormatType
// Målfilformat: .xls (äldre)
// För fullständiga exempel och datafiler, gå till https://github.com/aspose-cells/Aspose.Cells-for-.NET
// Skapa en ny arbetsbok
const workbook = new AsposeCells.Workbook();
// Hämta det första kalkylbladet
const sheet = workbook.getWorksheets().get(0);
// Fyll källdatan med rubrikrad (Fruit, Year, Amount)
// och 9 datarader som täcker druva, blåbär, kiwi, körsbär under 2020 och 2021
sheet.getCells().get(0, 0).putValue("Fruit");
sheet.getCells().get(0, 1).putValue("Year");
sheet.getCells().get(0, 2).putValue("Amount");
sheet.getCells().get(1, 0).putValue("grape");
sheet.getCells().get(1, 1).putValue(2020);
sheet.getCells().get(1, 2).putValue(50);
sheet.getCells().get(2, 0).putValue("blueberry");
sheet.getCells().get(2, 1).putValue(2020);
sheet.getCells().get(2, 2).putValue(30);
sheet.getCells().get(3, 0).putValue("kiwi");
sheet.getCells().get(3, 1).putValue(2020);
sheet.getCells().get(3, 2).putValue(25);
sheet.getCells().get(4, 0).putValue("cherry");
sheet.getCells().get(4, 1).putValue(2020);
sheet.getCells().get(4, 2).putValue(40);
sheet.getCells().get(5, 0).putValue("grape");
sheet.getCells().get(5, 1).putValue(2021);
sheet.getCells().get(5, 2).putValue(60);
sheet.getCells().get(6, 0).putValue("blueberry");
sheet.getCells().get(6, 1).putValue(2021);
sheet.getCells().get(6, 2).putValue(35);
sheet.getCells().get(7, 0).putValue("kiwi");
sheet.getCells().get(7, 1).putValue(2021);
sheet.getCells().get(7, 2).putValue(28);
sheet.getCells().get(8, 0).putValue("cherry");
sheet.getCells().get(8, 1).putValue(2021);
sheet.getCells().get(8, 2).putValue(45);
sheet.getCells().get(9, 0).putValue("grape");
sheet.getCells().get(9, 1).putValue(2020);
sheet.getCells().get(9, 2).putValue(45);
// Lägg till en pivottabell vid destinationscell E3, namngiven "Pivot1", med källintervall A1:C10
const pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
const pivotTable = sheet.getPivotTables().get(pivotIndex);
// Tilldela fält: Fruit -> Rader, Amount -> Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Tillämpa det äldre XLS-förinställda autoformatet "Report5"
// Obs: Den här egenskapen är endast meningsfull när den sparas som .xls.
// När den sparas som .xlsx/.xlsm/.xlsb ignorerar Excel AutoFormatType
// och använder det som PivotTableStyleType / PivotTableStyleName anger.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);
// Spara arbetsboken i äldre .xls-format
workbook.save("output.xls");
```

## **Tillämpa en modern namngiven förinställd pivottabellstil**

## **Definiera och tillämpa en anpassad pivottabellstil**
De inbyggda förinställningarna kan inte ändras. När du behöver åsidosätta färger, kanter eller typsnitt måste du definiera en anpassad pivotstil. Arbetsflödet har tre steg:
1. Lägg till en anpassad stil i arbetsbokens `TableStyles`-samling via `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. Detta returnerar indexet för den nyskapade stilen.
2. Konfigurera stilen genom att lägga till element (till exempel `WholeTable` eller `GrandTotalRow`) via `TableStyle.TableStyleElements.Add(TableStyleElementType)`, och tilldela sedan en `Style` till varje element via `TableStyleElement.SetElementStyle(Style)`.
3. Tillämpa den anpassade stilen på pivottabellen genom att sätta `PivotTable.PivotTableStyleName` till stilens namn. Använd inte `PivotTableStyleType` här, eftersom den egenskapen väljer inbyggda förinställningar.

{{% alert color="primary" %}}
`PivotTableStyleName` och `PivotTableStyleType` är inte utbytbara. Använd `PivotTableStyleType` för inbyggda förinställningar och `PivotTableStyleName` för anpassade stilar som du har definierat via `AddPivotTableStyle`. Att ange båda är ofarligt, men endast den som matchar den avsedda källan renderas.
{{% /alert %}}

De tillgängliga värdena för `TableStyleElementType` inkluderar `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` och `PageFieldValues`.
Följande exempel definierar en anpassad pivotstil med en tunn svart kant på `WholeTable` och ett fetstilt rött typsnitt på `GrandTotalRow`, och tillämpar den sedan via `PivotTableStyleName` och sparar som `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Fyll i källdata: rubrikrad + 9 datarader (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);
// Lägg till pivottabell från A1:C10, förankrad vid E3, med namnet "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Steg 1: registrera en ny anpassad pivottabellstil och spara dess index
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Steg 2: lägg till ett WholeTable-element och tillämpa tunna svarta kanter på alla fyra sidor
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WholeTable);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);
wholeTableElement.setElementStyle(wholeTableStyle);
// Steg 3: lägg till ett GrandTotalRow-element och tillämpa fet röd text
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GrandTotalRow);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setIsBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.Red);
grandTotalElement.setElementStyle(grandTotalStyle);
// Steg 4: tillämpa den anpassade stilen efter namn (INTE via PivotTableStyleType, som är för inbyggda förinställningar)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **Tillämpa en stil på varje pivotcell med FormatAll**
`PivotTable.FormatAll(Style)` är en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivottabellen, inklusive dataområdet, rad- och kolumnrubriker samt totaler. Det som tidigare ställts in via `PivotTableStyleType` eller `PivotTableStyleName` åsidosätts.

{{% alert color="primary" %}}
`FormatAll` åsidosätter både `PivotTableStyleType` och `PivotTableStyleName`. Använd det endast när ett enhetligt, temaoberoende utseende krävs för hela pivottabellen.
{{% /alert %}}

Följande exempel skapar en `Style` med gul solid fyllning, ett fetstilt mörkblått typsnitt och tunna svarta kanter på alla sidor, och tillämpar den sedan med `FormatAll` och sparar som `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Populera källdata: rubrikrad (rad 1) + 9 datarader (raderna 2-10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(5000);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(3000);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(4000);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(2000);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(6000);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(3500);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(4500);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(2500);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(5500);
// Lägg till pivottabell: källområde A1:C10, destinationscell E3, namn "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Tilldela pivotfält: Fruit -> Rad-område, Year -> Kolumn-område, Amount -> Data-område
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Bygg en stil som kommer att tvingas på varje cell i pivottabellen
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.DarkBlue);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);
// Applicera FormatAll: tvingar denna enda stil på varje cell i pivottabellen,
// och åsidosätter eventuell PivotTableStyleType / PivotTableStyleName som tidigare ställts in
pivotTable.formatAll(style);
// Spara arbetsboken i det moderna .xlsx-formatet
workbook.save("output.xlsx");
```

## **Vilket stil-API ska jag använda?**
Valet av stil-API beror på det filformat du sparar till. Använd tabellen nedan som en snabbreferens.
| Målfilformat | API att använda | Anteckningar |
|---|---|---|
| `.xls` (äldre) | `PivotTable.AutoFormatType` | Värden från `Aspose.Cells.Pivot.PivotTableAutoFormatType` (t.ex. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignoreras vid sparning i moderna format. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, inbyggd stil) | `PivotTable.PivotTableStyleType` | Värden från `Aspose.Cells.PivotTableStyleType` (ljust/mörkt tema, inklusive tillägg i Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, anpassad stil) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Använd när de inbyggda förinställningarna inte räcker. Konfigurera via `TableStyleElement.SetElementStyle(...)`. |
| Valfritt format (enhetlig åsidosättning) | `PivotTable.FormatAll(Style)` | Genväg som åsidosätter alla andra stilinställningar i hela pivottabellen. |
Vid tveksamhet, spara som `.xlsx` och använd `PivotTableStyleType` för inbyggda teman, eller `PivotTableStyleName` för anpassade teman.

{{< app/cells/assistant language="nodejs-cpp" >}}