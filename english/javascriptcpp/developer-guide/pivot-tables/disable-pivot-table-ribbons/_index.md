---
title: Disable Pivot Table Ribbons
type: docs
weight: 90
url: /javascript-cpp/disable-pivot-table-ribbons/
description: How to disable Pivot Table Ribbons with Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript via C++ Excel, Excel JavaScript via C++ library, Disable Pivot Table Ribbons Using Aspose.Cells for JavaScript via C++ Excel Library.
---

{{% alert color="primary" %}}

Pivot table based reports are useful but prone to error if target users do not have detailed knowledge of Excel to configure these reports. In these circumstances, organizations will want to restrict users from being able to change a pivot table based report. Common pivot table features like adding additional filters, slicers, fields, or changing the order of certain things in the report are mostly not recommended for every user. On the other hand, these users shall also be able to refresh the report and use existing filters or slicers. Aspose.Cells for JavaScript via C++ has provided this ability to developers for restricting users from changing these reports while creating these reports. For this purpose, Excel provides a feature to disable the pivot table ribbon and the same is provided by Aspose.Cells for JavaScript via C++, i.e. developer can disable the ribbon which contains controls to modify these reports.

{{% /alert %}}

## **How to Disable Pivot Table Ribbon Using Aspose.Cells for JavaScript via C++**

Following code demonstrates this feature by accessing a pivot table from a sheet and then setting [**enableWizard**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#enableWizard-boolean-) to **false**. Sample pivot table file can be downloaded from this [link](pivot_table_test.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Pivot Table Wizard Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the pivot table in the first sheet
            const pt = workbook.worksheets.get(0).pivotTables.get(0);

            // Disable ribbon for this pivot table
            pt.enableWizard = false;

            // Save output file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table wizard disabled successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```