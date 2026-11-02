---
title: Lägg till rad- och kolumnfält i en pivottabell i Aspose.Cells for JavaScript via C++
linktitle: Lägg till rad- och kolumnfält i en pivottabell i Aspose.Cells for JavaScript via C++
description: Lär dig hur du lägger till rad- och kolumnfält i en pivottabell och styr delsummer för pivotfält med PivotField.SetSubtotals och PivotFieldSubtotalType i Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, JavaScript via C++, pivottabell, radfält, kolumnfält, PivotField, setSubtotals, PivotFieldSubtotalType, delsummor, JavaScript, Excel-pivottabell
type: docs
weight: 220
url: /sv/javascript-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Lägga till ett fält i rad- eller kolumnområdet**
Metoden `pivotTable.addFieldToArea(fieldType, fieldName)` flyttar ett basfält från källdatan till ett av de fyra pivotområdena. Argumentet `fieldType` accepterar ett av följande `PivotFieldType`-värden.
- `Row` – fält som placeras lodrätt till vänster
- `Column` – fält som placeras horisontellt överst
- `Data` – fält vars värden aggregeras
- `Page` – fält som används som rapportfilter
Fältens nästlingsordning spelar roll. När du lägger till `Category` i radområdet och därefter `Item` skapas en pivottabell där `Category` utgör den yttre grupperingen och `Item` den inre. Om ordningen vänds blir hierarkin omvänd.

## **Delsummor för pivotfält**
Metoden `pivotField.setSubtotals(subtotalType, shown)` styr vilka delsummorader som visas för ett pivotfält. Varje anrop växlar en enda delsummotyp utan att påverka de andra typerna. När du anger `shown = true` visas delsumman, medan `shown = false` döljer den. Eftersom varje anrop endast påverkar en typ leder upprepade anrop med olika `subtotalType`-värden till ett anpassat urval delsummor.
Enumet `PivotFieldSubtotalType` definierar de tillgängliga delsummetyperna.
- `Automatic` – Aspose.Cells väljer standardinställningen (vanligtvis `Sum` för numeriska fält)
- `None` – undertrycker alla delsummorader
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
Delsummor visas endast om det finns två eller fler pivotfält i radområdet (eller i kolumnområdet). Med ett enda fält finns det inget mellan grupperna som kan delsummeras på ett meningsfullt sätt, så anrop till `setSubtotals` får då ingen synlig effekt. Den här artikeln använder därför två radfält (`Category` som yttre och `Item` som inre) i varje exempel, så att gränsen mellan varje `Category`-grupp och dess delsumma blir synlig.
{{% /alert %}}

## **Scenario 1 – Automatiska delsummor (standard)**
När du inte anropar `setSubtotals` alls tillämpar Aspose.Cells valet `Automatic` på numeriska fält. Följande exempel bekräftar uttryckligen detta beteende genom att anropa `setSubtotals(PivotFieldSubtotalType.Automatic, true)` på det yttre radfältet `Category`.

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
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get(0, 0).value = "Category";
            cells.get(0, 1).value = "Item";
            cells.get(0, 2).value = "Year";
            cells.get(0, 3).value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTableIndex = worksheet.pivotTables.add("=A1:D9", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);
            pivotTable.calculateData();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_automatic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Scenario 2 – Undertrycka alla delsummor (None)**
Att anropa `setSubtotals(PivotFieldSubtotalType.None, true)` tar bort alla delsummorader från pivottabellen och lämnar endast fältraderna och totalsumman längst ned. Detta är användbart när du vill ha den grupperade rådatan utan några sammanfattningsrader.

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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const headers = ["Category", "Item", "Year", "Amount"];
            for (let j = 0; j < headers.length; j++) {
                worksheet.cells.get(0, j).value = headers[j];
            }
            const data = [
                ["Fruit", "Apple", 2020, 100],
                ["Fruit", "Apple", 2021, 150],
                ["Fruit", "Banana", 2020, 80],
                ["Fruit", "Banana", 2021, 90],
                ["Vegetable", "Carrot", 2020, 50],
                ["Vegetable", "Carrot", 2021, 60],
                ["Vegetable", "Daikon", 2020, 40],
                ["Vegetable", "Daikon", 2021, 45]
            ];
            for (let i = 0; i < data.length; i++) {
                for (let j = 0; j < data[i].length; j++) {
                    worksheet.cells.get(i + 1, j).value = data[i][j];
                }
            }
            const pivotTableIndex = worksheet.pivotTables.add("=A1:D9", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_none.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Scenario 3 – Anpassat urval av delsummor (Sum + Average)**
Du är inte begränsad till en enda delsummotyp. Varje anrop till `setSubtotals` påverkar oberoende en enda typ, så att två anrop till metoden – en gång med `Sum` och en gång med `Average` – skapar ett anpassat urval med två delsummorader för varje `Category`-grupp.

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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get("A1").value = "Category";
            cells.get("B1").value = "Item";
            cells.get("C1").value = "Year";
            cells.get("D1").value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTables = worksheet.pivotTables;
            const i = pivotTables.add("=A1:D9", "F3", "PivotTable1");
            const pivotTable = pivotTables.get(i);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_custom.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Sammanfattning**
De tre scenarierna skiljer sig endast åt i ett avseende: anropen till `setSubtotals`. Allt annat – datamängden, fälten och de områden som de tilldelas – är identiskt, vilket gör att layouterna är direkt jämförbara.
- **Placera fält.** `pivotTable.addFieldToArea(PivotFieldType.Row, fieldName)` flyttar en kolumn i källdatan till ett område. Inom ett område är anropsordningen visningsordningen, så att det första anropet blir den yttersta gruppen. Delsummor kräver två eller fler fält i samma område: med ett enda fält finns det inget mellan grupperna att delsummera.
- **Scenario 1 – automatiska delsummor.** Om `setSubtotals` inte anropas överlåts valet till Excel, som tillämpar sin egen standarddelsumma på numeriska fält. Att anropa `setSubtotals` med `PivotFieldSubtotalType.Automatic` registrerar valet uttryckligen i stället för att lämna det implicit.
- **Scenario 2 – inga delsummor.** `setSubtotals` med `PivotFieldSubtotalType.None` stänger av standarddelsumman, så att pivottabellen behåller fältraderna och totalsumman men tar bort de delsummorader Excel annars skulle infoga mellan fältraderna och totalsumman.
- **Scenario 3 – ett valt urval.** Varje anrop växlar exakt en delsummotyp, och anropen ackumuleras utan att återställa varandra. Att anropa metoden en gång med `PivotFieldSubtotalType.Sum` och en gång med `PivotFieldSubtotalType.Average` lämnar därför båda aktiverade, och pivottabellen visar en delsumma av typen `Sum`, en delsumma av typen `Average` och en totalsumma.

{{% alert color="primary" %}}
Delsummorna är inte specifika för radområdet. Samma anrop till `setSubtotals` på ett fält som hämtats från `pivotTable.getColumnFields()` ger samma tre layouter på kolumnaxeln, eftersom inställningen tillhör pivotfältet och inte den axel där fältet placeras.
{{% /alert %}}

## **Relaterade artiklar**
- [Sidfält i pivottabeller](/cells/sv/javascript-cpp/add-page-field-in-pivot-table/)
- [Uppdatera pivottabeller i Aspose.Cells for JavaScript via C++](/cells/sv/javascript-cpp/refresh-pivot-table/)
- [Tillämpa stilar på pivottabeller](/cells/sv/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}