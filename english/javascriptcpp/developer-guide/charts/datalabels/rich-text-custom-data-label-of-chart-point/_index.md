---
title: Rich Text Custom Data Label of Chart Point with JavaScript via C++
description: Learn how to add rich text custom data labels to chart points in Aspose.Cells for JavaScript via C++. Our guide will show you how to format the labels with different fonts, colors, and alignment options to enhance the appearance and readability of your charts.
keywords: Aspose.Cells for JavaScript via C++, charting, rich text, custom data labels, fonts, colors, alignment, appearance, readability.
type: docs
weight: 10
url: /javascript-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

You can use Aspose.Cells to create rich text custom data labels for chart points. Aspose.Cells provides the [**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#characters-number-number-) method to return the [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) object, which can be used to set the font properties of the text, such as its color, boldness, etc.

{{% /alert %}}

## Rich Text Custom Data Label of Chart Point

The following code accesses the first chart point of the first series, sets its text, and then sets the font of the first 10 characters by changing its color to red and making it bold.

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

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the sheet
            const chart = worksheet.charts.get(0);

            // Access the data label of the first series' first point
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