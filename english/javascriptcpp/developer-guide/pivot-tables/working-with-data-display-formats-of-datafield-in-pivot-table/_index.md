---
title: Working with data display formats of DataField in Pivot Table
type: docs
weight: 140
url: /javascript-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ supports all the data display formats of DataField.

{{% /alert %}}

## **"Rank Smallest to Largest" and "Rank Largest to Smallest" display format option**

Aspose.Cells provides the ability to set the display format option for pivot fields. For this, the API provides the [**PivotShowValuesSetting.calculationType**](https://reference.aspose.com/cells/javascript-cpp/pivotshowvaluessetting/#calculationType-pivotfielddatadisplayformat-) property. To rank largest to smallest, you may set the [**PivotShowValuesSetting.calculationType**](https://reference.aspose.com/cells/javascript-cpp/pivotshowvaluessetting/#calculationType-pivotfielddatadisplayformat-) property to [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/javascript-cpp/pivotfielddatadisplayformat/). The following code snippet demonstrates setting the display format options.

Sample source and output files can be downloaded from here for testing the sample code:

[Source Excel File](101089332.xlsx)

[Output Excel File](101089333.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PivotTable Data Display Format</title>
    </head>
    <body>
        <h1>PivotTable Data Display Format Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils, PivotFieldDataDisplayFormat } = AsposeCells;
        
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const pivotIndex = 0;

            // Accessing the PivotTable
            const pivotTable = worksheet.pivotTables.get(pivotIndex);

            // Accessing the data fields.
            const pivotFields = pivotTable.dataFields;

            // Accessing the first data field in the data fields.
            const pivotField = pivotFields.get(0);

            // Setting data display format (convert getters/setters to properties)
            pivotField.showValuesSetting.calculationType = PivotFieldDataDisplayFormat.RankLargestToSmallest;

            pivotTable.calculateData();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PivotTableDataDisplayFormatRanking_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```