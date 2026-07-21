---
title: Tillämpa stilar på pivottabeller
linktitle: Tillämpa stilar på pivottabeller
description: Lär dig hur du tillämpar inbyggda och anpassade stilar på pivottabeller i Aspose.Cells for Node.js via C++, inklusive äldre XLS-autoformat, moderna namngivna stilar från Excel 2007+, anpassade pivottabellstilar och genvägen FormatAll.
keywords: Aspose.Cells Node.js via C++ pivottabell stil, PivotTableStyleType, AutoFormatType, FormatAll, anpassad stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /sv/nodejs-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_nodejs_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells stöder tillämpning av både äldre pivot-autoformat (avsedda för `.xls`-filer) och moderna namngivna eller anpassade pivottabellstilar (avsedda för `.xlsx`-, `.xlsm`- och `.xlsb`-filer). Vilken API du bör anropa beror på filformatet som arbetsboken sparas till, inte formatet den laddades från.

{{% /alert %}}

## **Introduktion**

Aspose.Cells exponerar två parallella stil-API:er för pivottabeller. Valet mellan dem styrs av filformatet du sparar arbetsboken till, inte av formatet du läser den från. En arbetsbok som laddats från en `.xls`-fil kan sparas om som `.xlsx`, och i det fallet gäller det moderna stil-API:et snarare än det äldre.

För äldre `.xls`-utdata, använd egenskapen `PivotTable.AutoFormatType` tillsammans med enumerationen `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Detta API motsvarar autoformatväljaren som klassisk Excel erbjöd för pivottabeller.

För moderna `.xlsx`-, `.xlsm`- och `.xlsb`-utdata finns två varianter av stil-API tillgängliga:

- `PivotTable.PivotTableStyleType` väljer en av de inbyggda namngivna stilarna (ljusa och mörka teman, inklusive stilarna som lades till i Excel 2017). Dessa förinställningar är skrivskyddade.
- `PivotTable.PivotTableStyleName` väljer en anpassad stil som du definierar själv genom `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. Anpassade stilar krävs när du vill ändra färger, kantlinjer eller teckensnitt utöver vad förinställningarna erbjuder.

Dessutom är `PivotTable.FormatAll(Style)` en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivoten, och åsidosätter det som är inställt genom någon av stilinamns-API:erna ovan. Detta är användbart när ett enhetligt utseende krävs oavsett det underliggande temat.

## **Tillämpa en äldre XLS-förinställd autoformat**

`PivotTable.AutoFormatType` accepterar ett värde från enumerationen `Aspose.Cells.Pivot.PivotTableAutoFormatType`. De tillgängliga värdena är `Report1` till `Report10`, `Classic`, och `Table1` till `Table10`.

{{% alert color="primary" %}}

`AutoFormatType` respekteras endast när arbetsboken sparas som `.xls`. När samma arbetsbok sparas som `.xlsx`, `.xlsm` eller `.xlsb`, ignorerar Excel denna egenskap och faller tillbaka på inställningarna `PivotTableStyleType` och `PivotTableStyleName`.

{{% /alert %}}

Följande exempel laddar en ny arbetsbok, fyller i Fruit/Year/Amount-exempeldata, lägger till en pivottabell, tillämpar `PivotTableAutoFormatType.Report5`, och sparar resultatet som `.xls`.

```javascript
const AsposeCells = require("aspose.cells");

// Scenario 1: Tillämpa ett äldre XLS-förinställt autoformat
// API som används: PivotTable.AutoFormatType
// Målfilsformat: .xls (äldre)
// För fullständiga exempel och datafiler, gå till https://github.com/aspose-cells/Aspose.Cells-for-.NET

// Skapa en ny arbetsbok
const workbook = new AsposeCells.Workbook();

// Hämta det första kalkylbladet
const sheet = workbook.getWorksheets().get(0);

// Fyll källdatan med rubrikrad (Fruit, Year, Amount)
// och 9 datarader som täcker grape, blueberry, kiwi, cherry över 2020 och 2021
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

// Lägg till en pivottabell vid destinationscell E3, med namnet "Pivot1", med hjälp av källintervall A1:C10
const pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
const pivotTable = sheet.getPivotTables().get(pivotIndex);

// Tilldela fält: Fruit -> Rader, Year -> Kolumner, Amount -> Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Tillämpa det äldre XLS-förinställda autoformatet "Report5"
// Obs: Den här egenskapen är endast meningsfull när man sparar som .xls.
// När man sparar som .xlsx/.xlsm/.xlsb ignorerar Excel AutoFormatType
// och använder det som PivotTableStyleType / PivotTableStyleName anger.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);

// Spara arbetsboken i äldre .xls-format
workbook.save("output.xls");
```

## **Tillämpa en modern namngiven förinställd pivottabellstil**

`PivotTable.PivotTableStyleType` accepterar ett värde från enumerationen `Aspose.Cells.PivotTableStyleType`. Enumerationen täcker ljusa teman `PivotTableStyleLight1` till `PivotTableStyleLight28` och mörka teman `PivotTableStyleDark1` till `PivotTableStyleDark28`. Stilarna som lades till i Excel 2017 (den andra vågen av ljusa och mörka teman) nås genom samma enumeration.

Detta är det rekommenderade API:et för alla moderna filformat. Till skillnad från den äldre autoformaten renderas stilen som väljs här troget av Excel och överlever rundresor genom andra Office-verktyg.

Följande exempel använder samma Fruit/Year/Amount-data, skapar en identisk pivottabell, tillämpar `PivotTableStyleDark1`, och sparar arbetsboken som `.xlsx`.

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
```

## **Definiera och tillämpa en anpassad pivottabellstil**

De inbyggda förinställningarna kan inte modifieras. Närhelst du behöver åsidosätta färger, kantlinjer eller teckensnitt, måste du definiera en anpassad pivotstil. Arbetsflödet har tre steg:

1. Lägg till en anpassad stil i arbetsbokens `TableStyles`-samling via `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. Detta returnerar indexet för den nyskapade stilen.
2. Konfigurera stilen genom att lägga till element (såsom `WholeTable` eller `GrandTotalRow`) genom `TableStyle.TableStyleElements.Add(TableStyleElementType)`, tilldela sedan en `Style` till varje element via `TableStyleElement.SetElementStyle(Style)`.
3. Tillämpa den anpassade stilen på pivoten genom att sätta `PivotTable.PivotTableStyleName` till stilens namn. Använd inte `PivotTableStyleType` här, eftersom den egenskapen väljer inbyggda förinställningar.

{{% alert color="primary" %}}

`PivotTableStyleName` och `PivotTableStyleType` är inte utbytbara. Använd `PivotTableStyleType` för inbyggda förinställningar, och `PivotTableStyleName` för anpassade stilar som du har definierat genom `AddPivotTableStyle`. Att sätta båda är ofarligt, men endast den som matchar den avsedda källan renderas.

{{% /alert %}}

De tillgängliga `TableStyleElementType`-värdena inkluderar `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` och `PageFieldValues`.

Följande exempel definierar en anpassad pivotstil med en tunn svart kantlinje på `WholeTable` och ett fetstilt rött teckensnitt på `GrandTotalRow`, tillämpar den sedan via `PivotTableStyleName` och sparar som `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Fyll i källdata: rubrikrad + 9 datarader (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
```

## **Tillämpa en stil på varje pivotcell med FormatAll**

`PivotTable.FormatAll(Style)` är en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivottabellen, inklusive dataområdet, rad- och kolumnrubriker samt totaler. Det som tidigare ställts in genom `PivotTableStyleType` eller `PivotTableStyleName` åsidosätts.

{{% alert color="primary" %}}

`FormatAll` åsidosätter både `PivotTableStyleType` och `PivotTableStyleName`. Använd den endast när ett enhetligt, temaneutralt utseende krävs över hela pivoten.

{{% /alert %}}

Följande exempel skapar en `Style` med gul solid fyllning, ett fetstilt mörkblått teckensnitt och tunna svarta kantlinjer på alla sidor, tillämpar den sedan med `FormatAll` och sparar som `.xlsx`.

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

// Bygg en stil som kommer att tvingas på varje cell i pivottabellen
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.Yellow);</think>
```

## **Vilket stil-API ska jag använda?**

Valet av stil-API beror på filformatet du sparar till. Använd tabellen nedan som en snabbreferens.

| Målfilformat | API att använda | Anteckningar |
|---|---|---|
| `.xls` (äldre) | `PivotTable.AutoFormatType` | Värden från `Aspose.Cells.Pivot.PivotTableAutoFormatType` (t.ex. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignoreras vid sparande i moderna format. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, inbyggd stil) | `PivotTable.PivotTableStyleType` | Värden från `Aspose.Cells.PivotTableStyleType` (ljusa/mörka teman, inklusive tillägg i Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, anpassad stil) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Använd när de inbyggda förinställningarna inte räcker. Konfigurera via `TableStyleElement.SetElementStyle(...)`. |
| Alla format (enhetlig åsidosättning) | `PivotTable.FormatAll(Style)` | Genväg som åsidosätter alla andra stilinställningar över hela pivoten. |

Vid tvivel, spara som `.xlsx` och använd `PivotTableStyleType` för inbyggda teman, eller `PivotTableStyleName` för anpassade teman.

{{< app/cells/assistant language="javascript" >}}
