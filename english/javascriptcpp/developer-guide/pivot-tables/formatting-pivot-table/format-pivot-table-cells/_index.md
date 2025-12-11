---
title: Format Pivot Table Cells
type: docs
weight: 30
url: /javascript-cpp/format-pivot-table-cells/
description: How to format pivot table cells with Aspose.Cells for JavaScript via C++.
keywords: Format pivot table cells.
---

{{% alert color="primary" %}}

Sometimes, you want to format pivot table cells. For example, you want to apply background color to pivot table cells. Aspose.Cells for JavaScript via C++ provides two methods [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#formatAll-style-) and [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#format-number-number-style-), which you can use for this purpose.

[**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#formatAll-style-) applies the style to the entire pivot table, while [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#format-number-number-style-) applies the style to a single cell of the pivot table.

{{% /alert %}}
The following sample code loads the [sample Excel file](pivot_format.xlsx) that contains two pivot tables, and **achieves formatting** the entire pivot table and **individual cells** in the pivot table.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Formatting Example</title>
    </head>
    <body>
        <h1>Pivot Table Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the worksheet by its name
            const worksheet = workbook.worksheets.get("Sheet1");

            // Access the pivot table (second pivot table, index 1)
            const pivotTable = worksheet.pivotTables.get(1);

            // Create a style object with background color light blue
            const style = workbook.createStyle();
            style.pattern = AsposeCells.BackgroundType.Solid;
            style.backgroundColor = AsposeCells.Color.LightBlue;

            // Format entire pivot table with light blue color
            pivotTable.formatAll(style);

            // Create another style object with yellow color
            const style2 = workbook.createStyle();
            style2.pattern = AsposeCells.BackgroundType.Solid;
            style2.backgroundColor = AsposeCells.Color.Yellow;

            // Access the first pivot table (index 0)
            const pivotTable2 = worksheet.pivotTables.get(0);

            // Format the cell of the pivot table at row 16, column 5 (0-based indices)
            pivotTable2.format(16, 5, style2);

            // Saving the workbook object and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot tables formatted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## Related Articles

- [Formatting Pivot Table](/cells/javascript-cpp/formatting-pivot-table/)
- [Working with data display formats of DataField in Pivot Table](/cells/javascript-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)