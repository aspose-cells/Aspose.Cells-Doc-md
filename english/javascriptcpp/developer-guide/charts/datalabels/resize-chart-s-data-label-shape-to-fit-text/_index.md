---
title: Resize Chart's Data Label Shape To Fit Text with JavaScript via C++
linktitle: Resize Chart's Data Label Shape To Fit Text
description: Learn how to resize the data label shape in a chart to fit the text in Aspose.Cells for JavaScript via C++. Our guide will show you how to adjust the size and shape of the label container to ensure that the text is displayed correctly without any truncation or overlapping.
keywords: Aspose.Cells for JavaScript via C++, charting, data labels, shape resizing, text fitting, truncation, overlapping.
type: docs
weight: 220
url: /javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}  
Excel application provides the **Resize shape to fit text** option for Chart's DataLabels in order to increase the size of the shape so that the text fits inside of it.  
{{% /alert %}}  

## **How to Resize Chart's Data Label Shape To Fit Text in Microsoft Excel**  

This option can be accessed on the Excel interface by selecting any of the data labels on the chart. Right‑click and select the **Format DataLabels** menu. On the **Size & Properties** tab, expand **Alignment** to reveal the related properties, including the **Resize shape to fit text** option.  

## **How to Resize Chart's Data Label Shape To Fit Text Using Aspose.Cells for JavaScript via C++**  

In order to mimic Excel's feature of resizing data label shapes to fit the text, the Aspose.Cells APIs expose the Boolean property **DataLabels.isResizeShapeToFitText**. The following piece of code shows a simple usage scenario of this property.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Data Labels Resize Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet that contains the Chart
            const sheet = workbook.worksheets.get(0);

            for (let c = 0; c < sheet.charts.count; c++) {
                // Access the Chart
                const chart = sheet.charts.get(c);

                for (let index = 0; index < chart.nSeries.count; index++) {
                    // Access the DataLabels of indexed NSeries
                    const labels = chart.nSeries.get(index).dataLabels;

                    // Set ResizeShapeToFitText property to true
                    labels.isResizeShapeToFitText = true;
                }

                // Calculate Chart
                chart.calculate();
            }

            // Save the result
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