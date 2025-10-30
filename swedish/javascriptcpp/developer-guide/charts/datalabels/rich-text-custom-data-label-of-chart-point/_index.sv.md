---
title: Rich Text anpassad datalabel för diagrampunkt med JavaScript via C++
description: Lär dig hur man lägger till rik text anpassade datalabels till diagrampunkter i Aspose.Cells for JavaScript via C++. Vår guide visar hur man formaterar etiketterna med olika typsnitt, färger och justeringsalternativ för att förbättra utseendet och läsbarheten på dina diagram.
keywords: Aspose.Cells for JavaScript via C++, diagram, rik text, anpassade datalabels, typsnitt, färger, justering, utseende, läsbarhet.
type: docs
weight: 10
url: /sv/javascript-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att skapa rik text anpassade datalabels för diagrampunkter. Aspose.Cells tillhandahåller metoden [**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#characters-number-number-) för att returnera [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting)-objektet som kan användas för att ställa in teckenfärger, fetstil etc.

{{% /alert %}}

## Anpassat riktmärke för diagram punkt

Följande kod kommer åt den första diagrampunkten i den första serien, ställer in dess text och sedan formaterar teckensnittet för de första 10 tecknen genom att ställa in dess färg till röd och fetstil till **true**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the sheet
            const chart = worksheet.charts.get(0);

            // Access the data label of first series first point
            const dlbls = chart.nSeries.get(0).points.get(0).dataLabels;

            // Set data label text
            dlbls.text = "Rich Text Label";

            // Set the font setting of the first 10 characters
            const fntSetting = dlbls.characters(0, 10);
            const font = fntSetting.font;
            font.color = AsposeCells.Color.Red;
            font.isBold = true;

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Data label updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
