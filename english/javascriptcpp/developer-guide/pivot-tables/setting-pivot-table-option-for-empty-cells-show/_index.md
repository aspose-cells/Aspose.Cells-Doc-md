---
title: Setting Pivot Table Option - For Empty Cells Show
type: docs
weight: 40
url: /javascript-cpp/setting-pivot-table-option-for-empty-cells-show/
---

{{% alert color="primary" %}}

You can set different pivot table options using Aspose.Cells for JavaScript via C++. One such option is "For empty cells show". By setting this option, all empty cells in a pivot table are displayed as a specified string.

{{% /alert %}}

## **Setting Pivot Table Option in Microsoft Excel**

To find and set this option in Microsoft Excel:

1. Select a pivot table and right-click.
1. Select **PivotTable Options**.
1. Select the **Layout & Format** tab.
1. Select the **For empty cells show** option and specify a string.

## **Setting Pivot Table Option Using Aspose.Cells for JavaScript via C++**

Aspose.Cells for JavaScript via C++ provides the [**PivotTable.displayNullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#displayNullString-boolean-) and [**PivotTable.nullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#nullString-string-) properties for setting the "For empty cells show" pivot table option.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Update Example</title>
    </head>
    <body>
        <h1>Update PivotTable Null Display Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            await AsposeCells.onReady();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and its first pivot table
            const worksheet = workbook.worksheets.get(0);
            const pt = worksheet.pivotTables.get(0);

            // Indicating if or not display the empty cell value
            pt.displayNullString = true;
            // Indicating the null string
            pt.nullString = "null";

            // Recalculate pivot table data
            pt.calculateData();

            // Do not refresh data on opening file
            pt.refreshDataOnOpeningFile = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Pivot table updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## Related Articles

- [Formatting Pivot Table](/cells/javascript-cpp/formatting-pivot-table/)