---
title: Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range with JavaScript via C++
linktitle: Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range
description: Learn how to change the data source of a chart to a destination worksheet while copying rows or a range in Aspose.Cells for JavaScript via C++. This guide demonstrates how to update the chart's data range and link it to the destination worksheet.
keywords: Aspose.Cells for JavaScript via C++, charting, data source, destination worksheet, rows, range, copy, update, data range, linkage.
type: docs
weight: 440
url: /javascript-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Possible Usage Scenarios**

When you copy rows or a range that contains charts to a new worksheet, the data source of the chart does not change. For example, if the data source of the chart is `=Sheet1!$A$1:$B$4`, then after copying rows or a range to a new worksheet, the data source will remain the same, i.e., `=Sheet1!$A$1:$B$4`. It still refers to the old worksheet, i.e., Sheet1. This is also the behavior in Microsoft Excel. However, if you want it to refer to the new destination worksheet, use the [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--) property and set it to **true** while calling the [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) method. Now, if your destination worksheet is **DestSheet**, the data source of your chart will change from `=Sheet1!$A$1:$B$4` to `=DestSheet!$A$1:$B$4`.

## **Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range**

The following sample code demonstrates the usage of the [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--) property while copying rows or a range containing charts to a new worksheet. The code uses the [sample Excel file](5113699.xlsx) and generates the [output Excel file](5113697.xlsx).

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

            // Access the first sheet which contains the chart
            const source = wb.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = wb.worksheets.add("DestSheet");

            // Set CopyOptions.referToDestinationSheet to true
            const options = new AsposeCells.CopyOptions();
            options.referToDestinationSheet = true;

            // Copy all the rows of the source worksheet to the destination worksheet, which includes the chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options);

            // Save workbook in XLSX format and provide download link
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