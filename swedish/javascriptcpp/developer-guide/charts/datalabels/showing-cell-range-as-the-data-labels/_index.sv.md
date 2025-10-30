---
title: Visa cellrange som datalabel med JavaScript via C++
linktitle: Visar cellområdet som datamärken
description: Lär dig hur man visar ett cellområde som datalabels i diagram med Aspose.Cells for JavaScript via C++. Vår guide visar hur man länkar etiketterna till din datakälla och formaterar dem för att ge korrekt och meningsfull information i dina diagram.
keywords: Aspose.Cells for JavaScript via C++, diagram, datalabels, cellområde, datakälla, formatering, noggrannhet, meningsfull information.
type: docs
weight: 130
url: /sv/javascript-cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}
I Microsoft Excel 2013 kan du visa ett cellområde för datalabels. Aspose.Cells for JavaScript via C++ stöder denna funktion.
{{% /alert %}}

## **Kryssrutan för att visa cellområde som datamärken**

Att visa cellområdet som datamärken i Microsoft Excel:

1. Välj seriens datamärken och högerklicka för att öppna snabbmenyn.  
1. Välj **Formatera datamärken**. Etikettalternativ visas.  
1. Välj eller avmarkera alternativet **Etiketten innehåller - Värde från celler**.  

Koden nedan ger tillgång till en diagramserie datamärkningar och ställer in [**DataLabels.showCellRange**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#showCellRange--)-egenskapen till **true** för att välja alternativet **Label Contains - Value From Cells**.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Show Range in Data Labels</title>
    </head>
    <body>
        <h1>Show Range in Data Labels Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook from the source Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Check the "Label Contains - Value From Cells"
            const dataLabels = chart.nSeries.get(0).dataLabels;
            dataLabels.showCellRange = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
