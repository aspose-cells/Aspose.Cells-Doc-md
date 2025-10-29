---
title: 在数据透视表中处理数据字段的数据显示格式
type: docs
weight: 140
url: /zh/javascript-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript通过C++支持所有DataField的数据展示格式。

{{% /alert %}}

## **“从最小到最大的排名”和“从最大到最小的排名”显示格式选项**

ASpose.Cells提供了设置数据透视字段显示格式选项的功能。为此，API提供了[**PivotShowValuesSetting.calculationType**](https://reference.aspose.com/cells/javascript-cpp/pivotshowvaluessetting/#calculationType-pivotfielddatadisplayformat-)属性。为了从最大到最小排名，您可以将[**PivotShowValuesSetting.calculationType**](https://reference.aspose.com/cells/javascript-cpp/pivotshowvaluessetting/#calculationType-pivotfielddatadisplayformat-)属性设置为[**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/javascript-cpp/pivotfielddatadisplayformat/)。以下代码片段演示了设置显示格式选项。

可从此处下载示例源文件和输出文件以测试示例代码:

【源 Excel 文件】（101089332.xlsx）

【输出 Excel 文件】（101089333.xlsx）

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
