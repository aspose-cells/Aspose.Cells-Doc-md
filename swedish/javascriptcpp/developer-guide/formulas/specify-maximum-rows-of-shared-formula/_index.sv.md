---
title: Ange maximala rader för delad formel med JavaScript via C++
linktitle: Ange maximala rader för delad formel
type: docs
weight: 40
url: /sv/javascript-cpp/specify-maximum-rows-of-shared-formula/
description: Lär dig hur du anger maximala rader för delade formler med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

Standardmaximalt antal rader för delad formel är 64. Det kan vara vilket tal som helst, t.ex. 1000. Prestandan för delad formel förändras med ett annat antal rader. Därför ger Aspose.Cells egenskapen [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--) som kan användas för att specificera det maximala antalet rader för den delade formeln. Den delade formeln delas upp i flera delade formler om det totala antalet rader för den delade formeln överstiger detta värde, vilket visas i följande skärmbild.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **Ange maximala rader för delad formel**  

Följande exempel förklarar användningen av egenskapen [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--). Den sätter det maximala antalet rader för den delade formeln till 5 och lägger till den delade formeln i cell D1 för 100 rader och sparar till [utgångs-Excel fil](61767856.xlsx). Om du extraherar innehållet i utgångs-Excel-filen och kontrollerar *sheet1.xml*, kommer du att se att den delade formeln delas efter varje 5 rader som markerats i skärmbilden ovan.  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Maximum Rows Of Shared Formula Example</title>
    </head>
    <body>
        <h1>Specify Maximum Rows Of Shared Formula Example</h1>
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Set the max rows of shared formula to 5
            workbook.settings.maxRowsOfSharedFormula = 5;

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access cell D1
            const cell = ws.cells.get("D1");

            // Set the shared formula in 100 rows
            cell.sharedFormula = ["=Sum(A1:A2)", 100, 1];

            // Save the output Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyMaximumRowsOfSharedFormula.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
