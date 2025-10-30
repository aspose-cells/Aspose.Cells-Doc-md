---
title: Sätt texten för diagramlegendens fyllning till ingen med Aspose.Cells for JavaScript via C++
linktitle: Ställ in text för diagrammets legendpostfyllnad till none med hjälp av Aspose.Cells
description: Lär dig hur du använder Aspose.Cells for JavaScript via C++ för att sätta texten för fyllningen i legendens fält till ingen. Denna guide visar hur man ändrar fyllningsfärgen på legendposter i Microsoft Excel diagram för bättre visualisering och anpassning.
keywords: Aspose.Cells for JavaScript via C++, Fälts fyllning för diagramlegend, Microsoft Excel, Visualisering, Anpassning.
type: docs
weight: 320
url: /sv/javascript-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Om du vill att texten på diagrammets legendarepresentant ska vara tom så att den inte visas inom diagramlegenden, ställ in [**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/javascript-cpp/legendentry/#isTextNoFill--) till **true**.

{{% /alert %}}

Följande exempelkod ställer in texten för diagrammets andra legendpostfyllnad till none. Vänligen ladda ner den [exempelfil för Excel](5115219.xlsx) som används i denna kod och den [utfärdade Excelfilen](5115217.xlsx) som genererats av den som referens.

Följande skärmbild visar effekten av denna kod på den [exempelfilen i Excel](5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Legend Entry Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the first chart inside the sheet
            const chart = sheet.charts.get(0);

            // Set text of second legend entry fill to none
            const legendEntry = chart.legend.legendEntries.get(1);
            legendEntry.isTextNoFill = true;

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ChartLegendEntry_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
