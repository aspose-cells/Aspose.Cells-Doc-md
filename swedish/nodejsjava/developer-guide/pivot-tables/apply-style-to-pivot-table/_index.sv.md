---
title: Tillämpa stilar på pivottabeller i Aspose.Cells for Node.js via Java
linktitle: Tillämpa stilar på pivottabeller i Aspose.Cells for Node.js via Java
description: Lär dig hur du tillämpar inbyggda och anpassade stilar på pivottabeller i Aspose.Cells for Node.js via Java, inklusive äldre XLS-autoformat, moderna namngivna stilar för Excel 2007+, anpassade pivottabellsstilar och genvägen formatAll.
keywords: Aspose.Cells Node.js via Java pivottabellsstil, PivotTableStyleType, AutoFormatType, FormatAll, anpassad stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /sv/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder tillämpning av både äldre pivotautoformat (avsedda för `.xls`-filer) och moderna namngivna eller anpassade pivottabellsstilar (avsedda för `.xlsx`-, `.xlsm`- och `.xlsb`-filer). Vilket API du ska anropa beror på det filformat som arbetsboken sparas till, inte det format den laddades från.
{{% /alert %}}

## **Introduktion**
Aspose.Cells exponerar två parallella stil-API:er för pivottabeller. Valet mellan dem styrs av det filformat du sparar arbetsboken till, inte av det format du läser den från. En arbetsbok som laddats från en `.xls`-fil kan sparas om som `.xlsx`, och i det fallet gäller det moderna stil-API:et istället för det äldre.
- `PivotTable.pivotTableStyleType` väljer en av de inbyggda namngivna stilarna (ljusa och mörka teman, inklusive de stilar som lades till i Excel 2017). Dessa förinställningar är skrivskyddade.
- `PivotTable.pivotTableStyleName` väljer en anpassad stil som du själv definierar via `Worksheets.getTableStyles().addPivotTableStyle(...)`. Anpassade stilar krävs när du vill ändra färger, kantlinjer eller teckensnitt utöver vad förinställningarna erbjuder.
Dessutom är `PivotTable.formatAll(Style)` en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivoten och åsidosätter det som anges via något av stilnamns-API:erna ovan. Detta är användbart när ett enhetligt utseende krävs oavsett underliggande tema.

## **Tillämpa ett äldre XLS-förinställt autoformat**
`PivotTable.autoFormatType` accepterar ett värde från enumerationen `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Tillgängliga värden är `Report1` till `Report10`, `Classic` och `Table1` till `Table10`.
Följande exempel laddar en ny arbetsbok, fyller i exempeldata för Fruit/Year/Amount, lägger till en pivottabell, tillämpar `PivotTableAutoFormatType.Report5` och sparar resultatet som `.xls`.

{{% alert color="primary" %}}
**Varför inga kolumnfält?** Autoformat i Report-serien (`Report1` till `Report10`, `Table1` till `Table10`) designades i klassisk Excel för **endimensionella pivottabeller** med endast radfält och värden — de har ingen inbyggd formatering för kolumnfältsrubriker. Om din pivot behöver kolumnfält, använd de moderna `PivotTableStyleType`-förinställningarna från [Scenario 2](#apply-a-modern-named-preset-pivot-table-style) istället, vilka är designade för den tvådimensionella layout som moderna Excel använder.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// Hämta det första kalkylbladet
let sheet = workbook.getWorksheets().get(0);
// Fyll källdata med rubrikrad (Frukt, År, Mängd)
// och 9 datarader som täcker druva, blåbär, kiwi, körsbär över 2020 och 2021
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
// Lägg till en pivottabell vid målcell E3, med namnet, med källintervall A1:C10
let pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// Tilldela fält: Frukt -> Rader, Mängd -> Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Tillämpa det äldre XLS-förinställda autoformatet "Report5"
// Obs: Den här egenskapen är endast meningsfull när den sparas som .xls.
// När den sparas som .xlsx/.xlsm/.xlsb ignorerar Excel AutoFormatType
// och använder det som PivotTableStyleType / PivotTableStyleName anger.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);
// Spara arbetsboken i äldre .xls-format
workbook.save("output.xls");
```

## **Tillämpa en modern namngiven förinställd pivottabellsstil**
`PivotTable.setPivotTableStyleType(int)` väljer någon av de inbyggda, namngivna stilar som Excel 2007 införde för pivottabeller. `PivotTableStyleType`-enumerationen exponerar tre temafamiljer: den ljusa familjen från `PIVOT_TABLE_STYLE_LIGHT1` till `PIVOT_TABLE_STYLE_LIGHT28`, den medelmåliga familjen från `PIVOT_TABLE_STYLE_MEDIUM1` till `PIVOT_TABLE_STYLE_MEDIUM28` och den mörka familjen från `PIVOT_TABLE_STYLE_DARK1` till `PIVOT_TABLE_STYLE_DARK_28`. Den definierar även `None` och `Custom`. Medlemmarna med högre nummer i varje familj är de stilar som lades till i Excel 2017.
Dessa förinställningar är skrivskyddade. Så snart du behöver ändra färger, ramar eller teckensnitt utöver vad en förinställning erbjuder, måste du i stället definiera en anpassad pivotstil, som visas i [Scenario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**Varför de moderna förinställningarna och inte rapportseriens autoformat?** Värdena `Report1` till `Report10` och `Table1` till `Table10` i `PivotTableAutoFormatType` härstammar från tiden före pivotkolumnfält, så de innehåller ingen formatering för kolumnfältsrubriker och Excel renderar dessa rubriker utan formatering. Förinställningarna i `PivotTableStyleType` utformades för den tvådimensionella layout som modern Excel använder och formaterar rubriker för både radfält och kolumnfält på samma sätt.
{{% /alert %}}

Det här scenariot återanvänder Fruit/Year/Amount-datasetet från Scenario 1, lägger till `Year` i kolumnområdet bredvid radfältet `Fruit` via `PivotFieldType.COLUMN`, tillämpar den mörka temaförinställningen `PIVOT_TABLE_STYLE_DARK1` med `pivotTable.setPivotTableStyleType` och sparar resultatet som `.xlsx` — det format som `PivotTableStyleType` är relevant för.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// 9 data rows of Fruit / Year / Amount
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(150);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(180);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(120);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(170);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(210);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(190);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(130);
// Add a pivot table at E3, sourced from A1:C10
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);
// Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx");
```

## **Definiera och tillämpa en anpassad pivottabellsstil**
De inbyggda förinställningarna kan inte ändras. Närhelst du behöver åsidosätta färger, kantlinjer eller teckensnitt måste du definiera en anpassad pivotstil. Arbetsflödet har tre steg:
1. Lägg till en anpassad stil i arbetsbokens `TableStyles`-samling via `Worksheets.getTableStyles().addPivotTableStyle(String name)`. Detta returnerar indexet för den nyskapade stilen.
2. Konfigurera stilen genom att lägga till element (såsom `WholeTable` eller `GrandTotalRow`) via `TableStyle.tableStyleElements.add(TableStyleElementType)`, och tilldela sedan en `Style` till varje element via `TableStyleElement.setElementStyle(Style)`.
3. Tillämpa den anpassade stilen på pivoten genom att sätta `PivotTable.pivotTableStyleName` till stilens namn. Använd inte `pivotTableStyleType` här, eftersom den egenskapen väljer inbyggda förinställningar.

{{% alert color="primary" %}}
`pivotTableStyleName` och `pivotTableStyleType` är inte utbytbara. Använd `pivotTableStyleType` för inbyggda förinställningar, och `pivotTableStyleName` för anpassade stilar som du har definierat via `addPivotTableStyle`. Att sätta båda är ofarligt, men bara den som matchar den avsedda källan renderas.
Tillgängliga `TableStyleElementType`-värden inkluderar `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` och `PageFieldValues`.
Följande exempel definierar en anpassad pivotstil med en tunn svart kantlinje på `WholeTable` och ett fetstil rött teckensnitt på `GrandTotalRow`, och tillämpar den sedan via `pivotTableStyleName` och sparar som `.xlsx`.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
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
// Lägg till pivottabell med källa från A1:C10, förankrad vid E3, namngiven
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Steg 1: registrera en ny anpassad pivottabellstil och fånga dess index
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Steg 2: lägg till ett WholeTable-element och tillämpa tunna svarta kanter på alla fyra sidor
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WHOLE_TABLE);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
let topBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.getBlack());
let bottomBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.getBlack());
let leftBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.getBlack());
let rightBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);
// Steg 3: lägg till ett GrandTotalRow-element och tillämpa fet röd text
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);
// Steg 4: tillämpa den anpassade stilen med namn (INTE med PivotTableStyleType, vilket är för inbyggda förinställningar)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **Tillämpa en stil på varje pivotcell med formatAll**
`PivotTable.formatAll(Style)` är en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivottabellen, inklusive dataområdet, rad- och kolumnrubriker samt totaler. Det som tidigare ställts in via `pivotTableStyleType` eller `pivotTableStyleName` åsidosätts.

{{% alert color="primary" %}}
`formatAll` åsidosätter både `pivotTableStyleType` och `pivotTableStyleName`. Använd det endast när ett enhetligt, temaoberoende utseende krävs över hela pivoten.
Följande exempel skapar en `Style` med gul solid fyllning, ett fetstil mörkblått teckensnitt och tunna svarta kantlinjer på alla sidor, och tillämpar den sedan med `formatAll` och sparar som `.xlsx`.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Fylla på källdata: rubrikrad (rad 1) + 9 datarader (raderna 2-10)
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
// Lägg till pivottabell: källintervall A1:C10, destinationscell E3, namn
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Tilldela pivotfält: Fruit -> radområde, Year -> kolumnområde, Amount -> dataområde
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Bygg en stil som kommer att tvingas på varje cell i pivottabellen
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.getYellow());
style.setPattern(AsposeCells.BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getDarkBlue());
style.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER).setColor(AsposeCells.Color.getBlack());
// Tillämpa formatAll: tvingar denna enda stil på varje cell i pivottabellen,
// och åsidosätter alla PivotTableStyleType / PivotTableStyleName som tidigare satts
pivotTable.formatAll(style);
// Spara arbetsboken i det moderna .xlsx-formatet
workbook.save("output.xlsx");
```

## **Vilket stil-API ska jag använda?**
Valet av stil-API beror på det filformat du sparar till. Använd tabellen nedan som en snabbreferens.
| Målfilformat | API att använda | Anteckningar |
|---|---|---|
| `.xls` (äldre) | `PivotTable.autoFormatType` | Värden från `Aspose.Cells.Pivot.PivotTableAutoFormatType` (t.ex. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignoreras vid sparande till moderna format. |
| `.xlsx` / `.xlsm` / `.xlsb` (modernt, inbyggd stil) | `PivotTable.pivotTableStyleType` | Värden från `Aspose.Cells.PivotTableStyleType` (ljusa/mörka teman, inklusive tillägg från Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modernt, anpassad stil) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | Använd när de inbyggda förinställningarna inte räcker. Konfigurera via `TableStyleElement.setElementStyle(...)`. |
| Valfritt format (enhetlig åsidosättning) | `PivotTable.formatAll(Style)` | Genväg som åsidosätter alla andra stilinställningar över hela pivoten. |
Vid tveksamhet, spara som `.xlsx` och använd `pivotTableStyleType` för inbyggda teman, eller `pivotTableStyleName` för anpassade teman.

{{< app/cells/assistant language="nodejs-java" >}}