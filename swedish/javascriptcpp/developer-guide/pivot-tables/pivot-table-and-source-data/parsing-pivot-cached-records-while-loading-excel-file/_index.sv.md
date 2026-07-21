---
title: Dekodning Pivot Cache poster vid inläsning av Excel fil
type: docs
weight: 70
url: /sv/javascript-cpp/parsing-pivot-cached-records-while-loading-excel-file/
---

## **Möjliga användningsscenario**

När du skapar en pivottabell tar Microsoft Excel en kopia av källdata och lagrar den i Pivot Cache. Pivot Cache hålls i minnet i Microsoft Excel. Du kan inte se den, men det är datan som pivottabellen hänvisar till när du bygger din pivottabell eller ändrar en Slicer-val eller flyttar rader/kolumner. Detta gör att Microsoft Excel kan vara mycket reaktivt på förändringar i pivottabellen, men det kan också dubbla storleken på din fil. Trots allt är Pivot Cache bara en kopia av din källdata så det är logiskt att din filstorlek kommer att vara potentiellt dubblerad.

När du laddar din Excel-fil i Workbook-objektet kan du bestämma om du också vill ladda posterna i Pivot Cache eller inte, med hjälp av egenskapen [**LoadOptions.parsingPivotCachedRecords**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#parsingPivotCachedRecords-boolean-). Standardvärdet för denna egenskap är **false**. Om Pivot Cache är ganska stor kan det förbättra prestanda. Men om du också vill ladda posterna i Pivot Cache bör du ställa in denna egenskap till **true**.

## **Dekodning Pivot Cache-poster vid inläsning av Excel-fil**

Följande exempel förklarar användningen av egenskapen [**LoadOptions.parsingPivotCachedRecords**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#parsingPivotCachedRecords-boolean-). Det laddar [exempelfilen Excel](61767773.xlsx) medan det parsar pivot-cacheade poster. Sedan uppdaterar det pivottabellen och sparar den som [utdata Excel-fil](61767774.xlsx).

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Parsing Pivot Cached Records While Loading Example</title>
    </head>
    <body>
        <h1>Parsing Pivot Cached Records While Loading Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options
            const options = new LoadOptions();
            // Set ParsingPivotCachedRecords true, default value is false
            options.parsingPivotCachedRecords = true;

            // Load the Excel file with load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), options);

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access first pivot table
            const pt = ws.pivotTables.get(0);

            // Set refresh data flag true
            pt.refreshDataFlag = true;

            // Refresh and calculate pivot table
            pt.refreshData();
            pt.calculateData();

            // Set refresh data flag false
            pt.refreshDataFlag = false;

            // Save the output Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
