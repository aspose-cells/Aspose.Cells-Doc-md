---
title: Tillämpa stilar på pivottabeller
linktitle: Tillämpa stilar på pivottabeller
description: Lär dig hur du tillämpar inbyggda och anpassade stilar på pivottabeller i Aspose.Cells for Node.js via Java, inklusive äldre XLS-autoformat, moderna namngivna stilar från Excel 2007+, anpassade pivottabellstilar och genvägen FormatAll.
keywords: Aspose.Cells Node.js via Java pivot table style, PivotTableStyleType, AutoFormatType, FormatAll, custom style, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /sv/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder tillämpning av både äldre pivot-autoformat (avsedda för `.xls`-filer) och moderna namngivna eller anpassade pivottabellstilar (avsedda för `.xlsx`-, `.xlsm`- och `.xlsb`-filer). Vilket API du bör anropa beror på det filformat som arbetsboken sparas till, inte det format den lästes in från.

{{% /alert %}}

## **Introduktion**

Aspose.Cells exponerar två parallella stil-API:er för pivottabeller. Valet mellan dem styrs av det filformat du sparar arbetsboken till, inte av det format du läser in den från. En arbetsbok som lästs in från en `.xls`-fil kan sparas om som `.xlsx`, och i det fallet gäller det moderna stil-API:et snarare än det äldre.

För äldre `.xls`-utdata använder du egenskapen `PivotTable.autoFormatType` tillsammans med enumerationen `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Detta API motsvarar den autoformatväljare som klassisk Excel erbjöd för pivottabeller.

För moderna `.xlsx`-, `.xlsm`- och `.xlsb`-utdata finns två varianter av stil-API:er tillgängliga:

- `PivotTable.pivotTableStyleType` väljer en av de inbyggda namngivna stilarna (ljusa och mörka teman, inklusive de stilar som lades till i Excel 2017). Dessa förinställningar är skrivskyddade.
- `PivotTable.pivotTableStyleName` väljer en anpassad stil som du definierar själv via `Worksheets.getTableStyles().addPivotTableStyle(...)`. Anpassade stilar krävs när du vill ändra färger, kantlinjer eller teckensnitt utöver vad förinställningarna erbjuder.

Dessutom är `PivotTable.formatAll(Style)` en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivoten och åsidosätter vad som än har ställts in via något av ovanstående stilnamns-API:er. Detta är användbart när ett enhetligt utseende krävs oavsett underliggande tema.

## **Tillämpa ett äldre XLS-förinställt autoformat**

`PivotTable.autoFormatType` accepterar ett värde från enumerationen `Aspose.Cells.Pivot.PivotTableAutoFormatType`. De tillgängliga värdena är `Report1` till `Report10`, `Classic` och `Table1` till `Table10`.

{{% alert color="primary" %}}

`autoFormatType` respekteras endast när arbetsboken sparas som `.xls`. När samma arbetsbok sparas som `.xlsx`, `.xlsm` eller `.xlsb` ignorerar Excel denna egenskap och faller tillbaka på inställningarna `pivotTableStyleType` och `pivotTableStyleName`.

{{% /alert %}}

Följande exempel läser in en ny arbetsbok, fyller i exempeldata för Fruit/Year/Amount, lägger till en pivottabell, tillämpar `PivotTableAutoFormatType.Report5` och sparar resultatet som `.xls`.

{{% alert color="primary" %}}

**Varför inga kolumnfält?** Autoformaten i Report-serien (`Report1` till `Report10`, `Table1` till `Table10`) designades i klassiska Excel för **endimensionella pivottabeller** med endast radfält och värden — de har ingen inbyggd formatering för kolumnfält-rubriker. Om din pivottabell behöver kolumnfält, använd de moderna `PivotTableStyleType`-förinställningarna från Scenario 2 nedan istället, som är designade för den tvådimensionella layout som moderna Excel använder.

{{% /alert %}}

```javascript
let workbook = new AsposeCells.Workbook();

// Hämta det första kalkylbladet
let sheet = workbook.getWorksheets().get(0);

// Fylla källdatan med rubrikrad (Fruit, Year, Amount)
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

// Lägg till en pivottabell vid destinationscell E3, med namnet "Pivot1", med källintervallet A1:C10
let pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Tilldela fält: Fruit -> Rader, Year -> Kolumner, Amount -> Data
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

`PivotTable.pivotTableStyleType` accepterar ett värde från enumerationen `Aspose.Cells.PivotTableStyleType`. Enumerationen täcker ljusa teman `PivotTableStyleLight1` till `PivotTableStyleLight28` och mörka teman `PivotTableStyleDark1` till `PivotTableStyleDark28`. Stilarna som lades till i Excel 2017 (den andra vågen av ljusa och mörka teman) nås via samma enumeration.

Detta är det rekommenderade API:et för alla moderna filformat. Till skillnad från det äldre autoformatet återges stilen som väljs här troget av Excel och överlever rundresor genom andra Office-verktyg.

Följande exempel använder samma Fruit/Year/Amount-data, skapar en identisk pivottabell, tillämpar `PivotTableStyleDark1` och sparar arbetsboken som `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Rubrikrad: Frukt / År / Belopp
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 datarader med Frukt / År / Belopp
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

// Lägg till en pivottabell vid E3 med namnet "Pivot1", hämtad från A1:C10
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Tilldela pivotfält: Frukt -> Radområde, År -> Kolumnområde, Belopp -> Dataområde
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Tillämpa en modern Excel 2007+ namngiven förinställd pivotstil.
// PivotTableStyleType är det korrekta API:et för .xlsx / .xlsm / .xlsb-filer; AutoFormatType
// ignoreras av Excel för dessa format. PivotTableStyleDark1 tillhör det mörka temat
// familjen (PivotTableStyleDark1..PivotTableStyleDark28), och samma enum exponerar också de
// nyare Excel 2017 ljusa/mörka teman (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);

// Spara som modern .xlsx — detta är formatet för vilket PivotTableStyleType är meningsfullt.
workbook.save("output.xlsx");
```

## **Definiera och tillämpa en anpassad pivottabellsstil**

De inbyggda förinställningarna kan inte modifieras. När du behöver åsidosätta färger, kantlinjer eller teckensnitt måste du definiera en anpassad pivotstil. Arbetsflödet har tre steg:

1. Lägg till en anpassad stil i arbetsbokens `TableStyles`-samling via `Worksheets.getTableStyles().addPivotTableStyle(String name)`. Detta returnerar indexet för den nyskapade stilen.
2. Konfigurera stilen genom att lägga till element (såsom `WholeTable` eller `GrandTotalRow`) via `TableStyle.tableStyleElements.add(TableStyleElementType)`, och tilldela sedan en `Style` till varje element via `TableStyleElement.setElementStyle(Style)`.
3. Tillämpa den anpassade stilen på pivoten genom att sätta `PivotTable.pivotTableStyleName` till stilens namn. Använd inte `pivotTableStyleType` här, eftersom den egenskapen väljer inbyggda förinställningar.

{{% alert color="primary" %}}

`pivotTableStyleName` och `pivotTableStyleType` är inte utbytbara. Använd `pivotTableStyleType` för inbyggda förinställningar och `pivotTableStyleName` för anpassade stilar som du har definierat via `addPivotTableStyle`. Att ställa in båda är ofarligt, men endast den som matchar den avsedda källan återges.

{{% /alert %}}

De tillgängliga `TableStyleElementType`-värdena inkluderar `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` och `PageFieldValues`.

Följande exempel definierar en anpassad pivotstil med en tunn svart kantlinje på `WholeTable` och ett fet rött teckensnitt på `GrandTotalRow`, och tillämpar den sedan via `pivotTableStyleName` och sparar som `.xlsx`.

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

// Lägg till pivottabell med källa från A1:C10, förankrad vid E3, namngiven "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Steg 1: registrera en ny anpassad pivottabellstil och fånga dess index
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// Steg 2: lägg till ett WholeTable-element och applicera tunna svarta kanter på alla fyra sidor
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WHOLE_TABLE);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
let topBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.BLACK);

let bottomBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.BLACK);

let leftBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.BLACK);

let rightBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.BLACK);

wholeTableElement.setElementStyle(wholeTableStyle);

// Steg 3: lägg till ett GrandTotalRow-element och applicera fet röd text
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.RED);
grandTotalElement.setElementStyle(grandTotalStyle);

// Steg 4: applicera den anpassade stilen via namn (INTE via PivotTableStyleType, vilket är för inbyggda förinställningar)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **Tillämpa en stil på varje pivotcell med FormatAll**

`PivotTable.formatAll(Style)` är en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivottabellen, inklusive dataområdet, rad- och kolumnrubriker samt totaler. Vad som tidigare ställts in via `pivotTableStyleType` eller `pivotTableStyleName` åsidosätts.

{{% alert color="primary" %}}

`formatAll` åsidosätter både `pivotTableStyleType` och `pivotTableStyleName`. Använd det endast när ett enhetligt, temaoberoende utseende krävs över hela pivoten.

{{% /alert %}}

Följande exempel skapar en `Style` med en gul heldragen fyllning, ett fet mörkblått teckensnitt och tunna svarta kantlinjer på alla sidor, och tillämpar den sedan med `formatAll` och sparar som `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Fyll i källdata: rubrikrad (rad 1) + 9 datarader (raderna 2-10)
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

// Lägg till pivottabell: källintervall A1:C10, målcell E3, namn "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Tilldela pivotfält: Fruit -> Rad-område, Year -> Kolumn-område, Amount -> Data-område
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Bygg en stil som tvingas på varje cell i pivottabellen
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

// Tillämpa FormatAll: tvingar denna enda stil på varje cell i pivottabellen,
// och åsidosätter eventuell PivotTableStyleType / PivotTableStyleName som tidigare ställts in
pivotTable.formatAll(style);

// Spara arbetsboken i det moderna .xlsx-formatet
workbook.save("output.xlsx");
```

## **Vilket stil-API bör jag använda?**

Valet av stil-API beror på det filformat du sparar till. Använd tabellen nedan som en snabbreferens.

| Målfilformat | API att använda | Anteckningar |
|---|---|---|
| `.xls` (äldre) | `PivotTable.autoFormatType` | Värden från `Aspose.Cells.Pivot.PivotTableAutoFormatType` (t.ex. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignoreras vid sparning som moderna format. |
| `.xlsx` / `.xlsm` / `.xlsb` (modernt, inbyggd stil) | `PivotTable.pivotTableStyleType` | Värden från `Aspose.Cells.PivotTableStyleType` (ljusa/mörka teman, inklusive tillägg från Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modernt, anpassad stil) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | Använd när de inbyggda förinställningarna inte räcker. Konfigurera via `TableStyleElement.setElementStyle(...)`. |
| Alla format (enhetlig åsidosättning) | `PivotTable.formatAll(Style)` | Genväg som åsidosätter alla andra stilinställningar över hela pivoten. |

Vid tveksamhet, spara som `.xlsx` och använd `pivotTableStyleType` för inbyggda teman, eller `pivotTableStyleName` för anpassade teman.

{{< app/cells/assistant language="javascript" >}}