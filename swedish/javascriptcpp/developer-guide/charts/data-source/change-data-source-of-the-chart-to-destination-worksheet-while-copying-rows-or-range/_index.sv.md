---
title: Ändra datakälla till diagrammet till destinationsbladet vid kopiering av rader eller område med JavaScript via C++
linktitle: Ändra datakällan för diagrammet till destinationskalkylbladet samtidigt som du kopierar rader eller område
description: Lär dig hur du ändrar datakällan för ett diagram till ett destinationsblad medan du kopierar rader eller ett område i Aspose.Cells for JavaScript via C++. Denna guide visar hur du uppdaterar diagrammets dataintervall och länkar det till destinationsbladet.
keywords: Aspose.Cells for JavaScript via C++, diagram, datakälla, destinationsblad, rader, område, kopiera, uppdatera, dataintervall, länkning.
type: docs
weight: 440
url: /sv/javascript-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Möjliga användningsscenario**

När du kopierar rader eller område som innehåller diagram till ett nytt blad, ändras inte datakällan för diagrammet. Till exempel, om datakällan för diagrammet är `=Sheet1!$A$1:$B$4`, kommer datakällan att förbli densamma, dvs `=Sheet1!$A$1:$B$4`, även efter kopiering. Den refererar fortfarande till det gamla bladet, dvs Sheet1. Detta är också beteendet i Microsoft Excel. Men om du vill att den ska referera till det nya destinationsbladet, använd då [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--)-egendomen och ställ in den på **true** när du anropar [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-)-metoden. Om ditt destinationsblad är DestSheet, kommer datakällan för ditt diagram att ändras från `=Sheet1!$A$1:$B$4` till `=DestSheet!$A$1:$B$4`.

## **Ändra datakällan för diagrammet till destinationskalkylbladet samtidigt som du kopierar rader eller område**

Följande exempel kod förklarar användningen av [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--)-egendomen vid kopiering av rader eller område som innehåller diagram till ett nytt blad. Koden använder filen [exempel Excel-fil](5113699.xlsx) och genererar [output Excel-fil](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Worksheet with Charts</title>
    </head>
    <body>
        <h1>Copy Worksheet with Charts Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first sheet which contains chart
            const source = wb.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = wb.worksheets.add("DestSheet");

            // Set CopyOptions.referToDestinationSheet to true
            const options = new AsposeCells.CopyOptions();
            options.referToDestinationSheet = true;

            // Copy all the rows of source worksheet to destination worksheet which includes chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options);

            // Save workbook in xlsx format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
