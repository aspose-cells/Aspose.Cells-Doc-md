---
title: 数据透视表隐藏和排序数据
type: docs
weight: 120
url: /zh/javascript-cpp/pivot-table-hide-and-sort-data/
---

## **数据透视表隐藏和排序数据**
Aspose.Cells for JavaScript通过C++支持隐藏和排序数据透视表。以下代码片段演示了此功能：按降序排序Score列，然后隐藏得分低于60的行。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Hide and Sort Example</title>
    </head>
    <body>
        <h1>PivotTable Hide and Sort Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first pivot table in the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Getting data body range and determining rows used
            const dataBodyRange = pivotTable.dataBodyRange;
            let currentRow = 3;
            const rowsUsed = dataBodyRange.endRow;

            // Sorting score in descending
            const field = pivotTable.rowFields.get(0);
            field.isAutoSort = true;
            field.isAscendSort = false;
            field.autoSortField = 0;
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Hiding rows with score less than 60
            while (currentRow < rowsUsed) {
                const cell = worksheet.cells.get(currentRow, 1);
                const score = cell.floatValue;
                if (score < 60) {
                    worksheet.cells.hideRow(currentRow);
                }
                currentRow = currentRow + 1;
            }

            pivotTable.refreshData();
            pivotTable.calculateData();

            // Saving the modified Excel file and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PivotTableHideAndSort_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

示例代码中使用的源和输出Excel文件已附上供参考。

[源文件](96928093.xlsx)

[输出文件](96928094.xlsx)
