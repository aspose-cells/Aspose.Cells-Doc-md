---
title: Tillämpa stilar på pivottabeller i Aspose.Cells for JavaScript via C++
linktitle: Tillämpa stilar på pivottabeller i Aspose.Cells for JavaScript via C++
description: Lär dig hur du tillämpar inbyggda och anpassade stilar på pivottabeller i Aspose.Cells for JavaScript via C++, inklusive äldre XLS-autoformat, moderna namngivna pivottabellstilar från Excel 2007+, anpassade pivottabellstilar och genvägen FormatAll.
keywords: Aspose.Cells for JavaScript via C++ pivottabellstil, PivotTableStyleType, AutoFormatType, FormatAll, anpassad stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /sv/javascript-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder både äldre pivottabellsautoformat (avsedda för `.xls`-filer) och moderna namngivna eller anpassade pivottabellstilar (avsedda för `.xlsx`-, `.xlsm`- och `.xlsb`-filer). Det API du ska anropa beror på vilket filformat arbetsboken sparas i, inte på vilket format den läses in från.
{{% /alert %}}

## **Introduktion**
Aspose.Cells exponerar två parallella stil-API:er för pivottabeller. Valet mellan dem avgörs av vilket filformat arbetsboken sparas i, inte av vilket format den läses in från. En arbetsbok som har lästs in från en `.xls`-fil kan sparas om som `.xlsx`, och då gäller det moderna stil-API:et i stället för det äldre.
- `pivotTable.pivotTableStyleType` väljer en av de inbyggda namngivna stilarna (ljusa och mörka teman, inklusive de stilar som lades till i Excel 2017). Dessa förinställningar är skrivskyddade.
- `pivotTable.pivotTableStyleName` väljer en anpassad stil som du själv definierar via `workbook.worksheets.tableStyles.addPivotTableStyle(...)`. Anpassade stilar krävs när du vill ändra färger, ramar eller teckensnitt utöver vad förinställningarna erbjuder.
Utöver detta är `pivotTable.formatAll(style)` en genväg som tillämpar ett enda `style`-objekt på varje cell i pivottabellen och åsidosätter de inställningar som har angetts via någon av de två API:erna ovan. Det är användbart när ett enhetligt utseende krävs oavsett det underliggande temat.

## **Tillämpa ett förinställt autoformat för äldre XLS**
`pivotTable.autoFormatType` accepterar ett värde från enumerationen `Aspose.Cells.Pivot.PivotTableAutoFormatType`. De tillgängliga värdena är `Report1` till `Report10`, `Classic` och `Table1` till `Table10`.
Följande exempel läser in en ny arbetsbok, fyller i exempeldata för `Fruit`/`Year`/`Amount`, lägger till en pivottabell, tillämpar `PivotTableAutoFormatType.Report5` och sparar resultatet som `.xls`.

{{% alert color="primary" %}}
**Varför inga kolumnfält?** Autoformattyperna `Report1` till `Report10` och `Table1` till `Table10` utformades i klassisk Excel för **pivottabeller med en enda dimension** med enbart radfält och värden – de saknar inbyggd formatering för rubriker till kolumnfält. Om pivottabellen behöver kolumnfält använder du i stället de moderna förinställningarna för `PivotTableStyleType` i [Scenario 2](#apply-a-modern-named-preset-pivot-table-style), som är utformade för den tvådimensionella layouten som används i modern Excel.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Scenario 1: Använd ett förinställt autoformat för äldre XLS
            // API som används: PivotTable.AutoFormatType
            // Målfilformat: .xls (äldre format)
            // För fullständiga exempel och datafiler, gå till https://github.com/aspose-cells/Aspose.Cells-for-.NET
            // Skapa en ny arbetsbok
            const workbook = new Workbook();
            // Hämta det första kalkylbladet
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Fyll källdatan med en rubrikrad (Fruit, Year, Amount)
            // och 9 datarader som täcker grape, blueberry, kiwi, cherry under 2020 och 2021
            cells.get(0, 0).value = "Fruit";
            cells.get(0, 1).value = "Year";
            cells.get(0, 2).value = "Amount";
            cells.get(1, 0).value = "grape";
            cells.get(1, 1).value = 2020;
            cells.get(1, 2).value = 50;
            cells.get(2, 0).value = "blueberry";
            cells.get(2, 1).value = 2020;
            cells.get(2, 2).value = 30;
            cells.get(3, 0).value = "kiwi";
            cells.get(3, 1).value = 2020;
            cells.get(3, 2).value = 25;
            cells.get(4, 0).value = "cherry";
            cells.get(4, 1).value = 2020;
            cells.get(4, 2).value = 40;
            cells.get(5, 0).value = "grape";
            cells.get(5, 1).value = 2021;
            cells.get(5, 2).value = 60;
            cells.get(6, 0).value = "blueberry";
            cells.get(6, 1).value = 2021;
            cells.get(6, 2).value = 35;
            cells.get(7, 0).value = "kiwi";
            cells.get(7, 1).value = 2021;
            cells.get(7, 2).value = 28;
            cells.get(8, 0).value = "cherry";
            cells.get(8, 1).value = 2021;
            cells.get(8, 2).value = 45;
            cells.get(9, 0).value = "grape";
            cells.get(9, 1).value = 2020;
            cells.get(9, 2).value = 45;
            // Lägg till en pivottabell vid destinationscellen E3, med källintervallet A1:C10
            const pivotTableIndex = sheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = sheet.pivotTables.get(pivotTableIndex);
            // Tilldela fält: Fruit -> Rader, Amount -> Data
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Använd det förinställda autoformatet "Report5" för äldre XLS
            // Obs! Den här egenskapen har betydelse endast när filen sparas som .xls.
            // När filen sparas som .xlsx/.xlsm/.xlsb ignorerar Excel AutoFormatType
            // och använder det som PivotTableStyleType / PivotTableStyleName anger.
            pivotTable.autoFormatType = AsposeCells.PivotTableAutoFormatType.Report5;
            // Spara arbetsboken i det äldre .xls-formatet
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xls";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Tillämpa en modern namngiven förinställningsstil för pivottabeller**
`pivotTable.pivotTableStyleType` väljer en av de inbyggda namngivna stilar som Excel 2007 introducerade för pivottabeller. Enumerationen `PivotTableStyleType` exponerar tre temafamiljer: `PivotTableStyleLight1` till `PivotTableStyleLight28` (ljus), `PivotTableStyleMedium1` till `PivotTableStyleMedium28` (medel) och `PivotTableStyleDark1` till `PivotTableStyleDark28` (mörk). Den definierar också `None` och `Custom`. De högst numrerade medlemmarna i varje familj är de stilar som lades till i Excel 2017.
Dessa förinställningar är skrivskyddade. När du behöver ändra färger, ramar eller teckensnitt utöver vad en förinställning erbjuder måste du i stället definiera en anpassad pivottabellstil, som visas i [Scenario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**Varför använda moderna förinställningar i stället för autoformaten i rapportserierna?** Värdena `Report1` till `Report10` och `Table1` till `Table10` i `PivotTableAutoFormatType` fanns innan kolumnfält för pivottabeller infördes och innehåller därför ingen formatering för rubriker till kolumnfält, så Excel återger de rubrikerna utan formatering. Förinställningarna i `PivotTableStyleType` utformades för den tvådimensionella layouten som används i modern Excel och formaterar både rubriker till radfält och rubriker till kolumnfält.
{{% /alert %}}

Det här scenariot återanvänder exempeldata med `Fruit`/`Year`/`Amount` från Scenario 1, lägger till `Year` i kolumnområdet bredvid radfältet `Fruit` via `PivotFieldType.Column`, tillämpar den mörka temaförinställningen `PivotTableStyleDark1` med `pivotTable.pivotTableStyleType` och sparar resultatet som `.xlsx` – det format som `PivotTableStyleType` gäller för.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Scenario 2: Applicera en modern, namngiven förinställningsstil för Excel 2007+ med PivotTableStyleType.
            // Målfilformat: .xlsx. Enumereringen PivotTableStyleType finns i Aspose.Cells-namnrymden
            // (inte i Aspose.Cells.Pivot) -- därför behöver vi ingen extra using-deklaration för den.
            // GitHub-referens: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Rubrikrad: Fruit / Year / Amount
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // 9 datarader med Fruit / Year / Amount
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 150;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 200;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 180;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 120;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 170;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 210;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 190;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 130;
            // Lägg till en pivottabell vid E3 med A1:C10 som datakälla
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // Tilldela pivotfält: Fruit -> radområde, Year -> kolumnområde, Amount -> dataområde
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Applicera en modern, namngiven förinställningsstil för pivottabell i Excel 2007+.
            // PivotTableStyleType är rätt API för .xlsx / .xlsm / .xlsb-filer; AutoFormatType
            // ignoreras av Excel för dessa format. PivotTableStyleDark1 tillhör gruppen med mörka teman
            // (PivotTableStyleDark1..PivotTableStyleDark28), och samma enum exponerar även de nyare
            // ljusa/mörka temana i Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
            pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleDark1;
            // Spara som modern .xlsx -- detta är formatet för vilket PivotTableStyleType har betydelse.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
        </script>
    </body>
</html>
```

## **Definiera och tillämpa en anpassad pivottabellstil**
De inbyggda förinställningarna kan inte ändras. När du behöver åsidosätta färger, ramar eller teckensnitt måste du därför definiera en anpassad pivottabellstil. Arbetsflödet har tre steg:
1. Lägg till en anpassad stil i arbetsbokens `tableStyles`-samling via `workbook.worksheets.tableStyles.addPivotTableStyle(name)`. Detta returnerar indexet för den nyskapade stilen.
2. Konfigurera stilen genom att lägga till element (såsom `WholeTable` eller `GrandTotalRow`) via `tableStyle.tableStyleElements.add(tableStyleElementType)` och tilldela sedan en `style` till varje element via `tableStyleElement.setElementStyle(style)`.
3. Tillämpa den anpassade stilen på pivottabellen genom att ange stilnamnet i `pivotTable.pivotTableStyleName`. Använd inte `pivotTable.pivotTableStyleType` här, eftersom den egenskapen väljer inbyggda förinställningar.

{{% alert color="primary" %}}
`pivotTable.pivotTableStyleName` och `pivotTable.pivotTableStyleType` är inte utbytbara. Använd `pivotTable.pivotTableStyleType` för inbyggda förinställningar och `pivotTable.pivotTableStyleName` för anpassade stilar som du har definierat via `addPivotTableStyle`. Att ange båda är harmlöst, men endast den egenskap som motsvarar den avsedda källan används vid återgivningen.
De tillgängliga värdena i `TableStyleElementType` omfattar `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` och `PageFieldValues`.
Följande exempel definierar en anpassad pivottabellstil med en tunn svart ram runt `WholeTable` och ett fett och rött teckensnitt på `GrandTotalRow`, tillämpar den sedan via `pivotTable.pivotTableStyleName` och sparar som `.xlsx`.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Fyll i källdata: rubrikrad + 9 datarader (A1:C10)
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 200;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 300;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 400;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 500;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 600;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 700;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 800;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 900;
            // Lägg till pivottabell med data från A1:C10, förankrad vid E3
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Steg 1: registrera en ny anpassad pivottabellstil och spara dess index
            const styleIndex = workbook.worksheets.tableStyles.addPivotTableStyle("CustomPivotStyle");
            const tableStyle = workbook.worksheets.tableStyles.get(styleIndex);
            // Steg 2: lägg till ett WholeTable-element och applicera tunna svarta ramar på alla fyra sidor
            const wholeTableElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.WholeTable);
            const wholeTableElement = tableStyle.tableStyleElements.get(wholeTableElementIndex);
            const wholeTableStyle = workbook.createStyle();
            const topBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.TopBorder);
            topBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            topBorder.color = "black";
            const bottomBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.BottomBorder);
            bottomBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            bottomBorder.color = "black";
            const leftBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.LeftBorder);
            leftBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            leftBorder.color = "black";
            const rightBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.RightBorder);
            rightBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            rightBorder.color = "black";
            wholeTableElement.setElementStyle(wholeTableStyle);
            // Steg 3: lägg till ett GrandTotalRow-element och applicera röd fetstil
            const grandTotalElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.GrandTotalRow);
            const grandTotalElement = tableStyle.tableStyleElements.get(grandTotalElementIndex);
            const grandTotalStyle = workbook.createStyle();
            grandTotalStyle.font.isBold = true;
            grandTotalStyle.font.color = "red";
            grandTotalElement.setElementStyle(grandTotalStyle);
            // Steg 4: applicera den anpassade stilen efter namn (INTE via PivotTableStyleType, som är avsedd för inbyggda förinställningar)
            pivotTable.pivotTableStyleName = "CustomPivotStyle";
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Tillämpa en stil på varje pivottabellscell med `formatAll`**
`pivotTable.formatAll(style)` är en genväg som tillämpar ett enda `style`-objekt på varje cell i pivottabellen, inklusive dataområdet, rad- och kolumnrubriker samt totalsummor. Allt som tidigare angetts via `pivotTable.pivotTableStyleType` eller `pivotTable.pivotTableStyleName` åsidosätts.

{{% alert color="primary" %}}
`formatAll` åsidosätter både `pivotTable.pivotTableStyleType` och `pivotTable.pivotTableStyleName`. Använd det endast när du behöver ett enhetligt utseende i hela pivottabellen, oberoende av temat.
Följande exempel skapar en `style` med en gul solidfyllning, ett fett och mörkblått teckensnitt och tunna svarta ramar på alla sidor, tillämpar den sedan med `formatAll` och sparar som `.xlsx`.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Scenario 4: Använd en enda Style för varje cell i pivottabellen med FormatAll
            // API som används: PivotTable.FormatAll(Style)
            // Målformat: .xlsx
            // GitHub-referens: se Aspose.Cells-for-.NET-repositoriet – exempel på pivottabellformatering
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // Fyll i källdatan: rubrikrad (rad 1) + 9 datarader (raderna 2–10)
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 5000;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 3000;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 4000;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 2000;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 6000;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 3500;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 4500;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 2500;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 5500;
            // Lägg till pivottabell: källområde A1:C10, destinationscell E3
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // Tilldela pivotfält: Fruit -> radområde, Year -> kolumnområde, Amount -> dataområde
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Skapa en Style som tvingas på varje cell i pivottabellen
            const style = workbook.createStyle();
            style.foregroundColor = AsposeCells.Color.Yellow;
            style.pattern = AsposeCells.BackgroundType.Solid;
            style.font.isBold = true;
            style.font.color = AsposeCells.Color.DarkBlue;
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;
            // Använd FormatAll: tvingar denna enda stil på varje cell i pivottabellen
            // och åsidosätter eventuell tidigare angiven PivotTableStyleType / PivotTableStyleName
            pivotTable.formatAll(style);
            // Spara arbetsboken i det moderna .xlsx-formatet
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Vilket stil-API ska jag använda?**
Valet av stil-API beror på vilket filformat du sparar i. Använd tabellen nedan som snabbreferens.
| Målfilformat | API som ska användas | Anmärkningar |
|---|---|---|
| `.xls` (äldre) | `pivotTable.autoFormatType` | Värden från `Aspose.Cells.Pivot.PivotTableAutoFormatType` (t.ex. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignoreras vid sparande i moderna format. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, inbyggd stil) | `pivotTable.pivotTableStyleType` | Värden från `Aspose.Cells.PivotTableStyleType` (ljusa/mörka teman, inklusive de stilar som lades till i Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, anpassad stil) | `pivotTable.pivotTableStyleName` + `workbook.worksheets.tableStyles.addPivotTableStyle(...)` | Använd när de inbyggda förinställningarna inte räcker. Konfigurera via `tableStyleElement.setElementStyle(...)`. |
| Alla format (enhetlig åsidosättning) | `pivotTable.formatAll(style)` | Genväg som åsidosätter alla andra stilinställningar i hela pivottabellen. |
I tveksamma fall sparar du som `.xlsx` och använder `pivotTable.pivotTableStyleType` för inbyggda teman, eller `pivotTable.pivotTableStyleName` för anpassade pivottabellstilar.

{{< app/cells/assistant language="javascript-cpp" >}}