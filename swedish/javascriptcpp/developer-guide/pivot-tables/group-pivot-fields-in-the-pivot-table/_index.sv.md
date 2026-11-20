---
title: Gruppera pivotfält i pivottabellen
linktitle: Gruppera pivotfält i pivottabellen
description: Lär dig hur du grupperar rad- och kolumnfält i en pivottabell till datumperioder, såsom månader och kvartal, och numeriska intervall med hjälp av PivotField.group och PivotFieldGroupOptions i Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, pivottabell, gruppering av pivotfält, PivotField.group, PivotFieldGroupOptions, datumgruppering, talgruppering, månader, kvartal, numeriskt intervall, JavaScript via C++
type: docs
weight: 80
url: /sv/javascript-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
- Gruppering av pivotfält är användbart när ett rad- eller kolumnfält i en pivottabell innehåller många olika poster, till exempel ett datumfält med hundratals datum eller ett numeriskt fält med många spridda värden. Grupperingen samlar posterna i meningsfulla avsnitt: datum i månader, kvartal och år samt tal i intervall som 0-1, 2-3, 4-5. På så sätt blir en stor pivottabell kompakt och lättare att analysera. Aspose.Cells tillhandahåller den här funktionen med hjälp av metoden `PivotField.group()` (automatisk gruppering efter datatyp) och `PivotField.group(PivotFieldGroupOptions)` (anpassade grupperingsalternativ).
- Datumgruppering samlar enskilda datum i perioder som dagar, månader, kvartal och år och skapar en tidshierarki (till exempel År, Kvartal, Månader). Trender över tid blir tydliga direkt, och varje periodsnivå blir ett eget pivotfält i pivottabellens rad- eller kolumnområde.
- Gruppering är endast tillgänglig för fält som har placerats i pivottabellens rad- eller kolumnområde. Ett datafält (värdefält) kan inte grupperas direkt. Om ett sådant fält ska grupperas måste det först läggas till i pivottabellens rad- eller kolumnområde.

## **Gruppera pivotfält automatiskt**
Överlagringen av `PivotField.group()` utan parametrar granskar fältets datatyp och grupperar fältet automatiskt. Ett fält som endast innehåller datum och tomma celler grupperas efter månader. Ett fält som endast innehåller tal och tomma celler grupperas i numeriska intervall med hjälp av ett automatiskt intervall.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Pivot Fields Automatically</title>
    </head>
    <body>
        <h1>Auto-Group a Pivot Field</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the second worksheet and its pivot table
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the first row field automatically by its data type
                pt.rowFields.get(0).group();
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputAutoGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **Gruppera pivotfält med anpassade alternativ**
Klassen `PivotFieldGroupOptions` erbjuder konfigurationsinställelser för anpassad gruppering. För datumfält anger du `startDate`, `endDate` och `groupTypes`. För numeriska fält anger du `startNumber`, `endNumber` och `interval`. Egenskapen `newPivotField` styr om gruppering skapar nya pivotfält bredvid det ursprungliga fältet (se avsnittet Obs i slutet av den här artikeln).

### **Gruppera ett datumfält efter månader och kvartal**
Exemplet nedan grupperar datumradfältet i pivottabellen i exemplet efter månader och kvartal mellan ett startdatum och ett slutdatum. Koden läser in [exempelfilen i Excel](sampleGroupPivotFieldsInPivotTable.xlsx), utför grupperingen, beräknar data i pivottabellen och sparar det grupperade resultatet. Skärmbilden visar resultatet: datumradfältet är nu grupperat efter kvartal och månader.
Observera att ordningen på värdena i `options.groupTypes` inte spelar roll. Oavsett i vilken ordning grupperingstyperna anges visas de grupperade fälten alltid från den största till den minsta perioden: år, kvartal, månader, dagar, timmar, minuter, sekunder. I det här exemplet anges månaderna före kvartalen i `options.groupTypes`, men kvartalen visas som den yttre nivån och månaderna som den inre nivån.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Date Field by Months and Quarters</title>
    </head>
    <body>
        <h1>Group a Date Pivot Field</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the date row field by months and quarters between the given dates
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startDate = new Date(2008, 1, 1);
                options.endDate = new Date(2008, 9, 5);
                options.groupTypes = [AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters];
                pt.rowFields.get(0).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputGroupPivotFieldsInPivotTable.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

![Pivottabell grupperad efter månader och kvartal](group-pivot-fields-in-the-pivot-table_1.png)

### **Gruppera ett numeriskt fält i intervall**
`FieldTwo` i pivottabellen i exemplet är ursprungligen ett datafält (värdefält). Eftersom endast rad- eller kolumnfält kan grupperas anropar koden först `PivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` för att flytta `FieldTwo` till radområdet. Därefter uppdaterar koden pivottabellen och grupperar det numeriska fältet i intervallen 0-1, 2-3 och 4-5 med hjälp av `startNumber = 0`, `endNumber = 5` och `interval = 2`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Numeric Field into Ranges</title>
    </head>
    <body>
        <h1>Group a Numeric Pivot Field</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // FieldTwo is a data field: move it to the row area first,
                // because only row/column fields can be grouped
                pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
                pt.calculateData();
                // Group the numeric field into the ranges 0-1, 2-3, 4-5
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startNumber = 0;
                options.endNumber = 5;
                options.interval = 2;
                pt.rowFields.get(1).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputNumberGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **Obs**

{{% alert color="primary" %}}
- Metodöverlagringarna för `PivotField.groupBy()` är föråldrade och har tagits bort från API:et. De ersätts av `PivotField.group()` och `PivotField.group(PivotFieldGroupOptions)`.
- I Microsoft Excel ersätter gruppering av ett numeriskt fält det ursprungliga pivotfältet med de grupperade intervallen, medan gruppering av ett datumfält skapar nya pivotfält (ett per grupperingsnivå, till exempel kvartal och månader) bredvid det ursprungliga fältet. Från och med Aspose.Cells 26.10 följer metoderna `PivotField.group()` samma beteende som i Excel. Egenskapen `PivotFieldGroupOptions.newPivotField` finns för kompatibilitet med äldre versioner: den har standardvärdet `false` för numerisk gruppering och `true` för gruppering av datum och tid. Ange `false` om du vill att datumgruppering ska ersätta det ursprungliga pivotfältet i stället för att skapa nya pivotfält.
- Egenskapen `PivotFieldGroupOptions.interval` har endast effekt vid numerisk gruppering och vid gruppering av datum per dag (till exempel när datum grupperas i perioder på sju dagar). Den ignoreras när datum grupperas per månad, kvartal eller år.
{{% /alert %}}

## **Relaterade artiklar**
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [Lägg till sidfält i pivottabell](/cells/sv/javascript-cpp/add-page-field-in-pivot-table/)
- [Använd format på pivottabell](/cells/sv/javascript-cpp/apply-style-to-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/javascript-cpp/refresh-pivot-table/)
- [Diskret gruppering av objekt i pivotfält](/cells/sv/javascript-cpp/discrete-group-pivot-fields/)

{{< app/cells/assistant language="javascript-cpp" >}}