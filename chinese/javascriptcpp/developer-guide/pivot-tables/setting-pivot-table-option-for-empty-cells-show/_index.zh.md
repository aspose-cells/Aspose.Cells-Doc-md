---
title: 设置数据透视表选项  对空单元格显示
type: docs
weight: 40
url: /zh/javascript-cpp/setting-pivot-table-option-for-empty-cells-show/
---

{{% alert color="primary" %}}

你可以使用Aspose.Cells for JavaScript通过C++设置不同的Pivot表选项。其中一个选项是“空单元格显示”。通过设置此选项，Pivot表中的所有空单元格将显示为指定的字符串。

{{% /alert %}}

## **在Microsoft Excel中设置数据透视表选项**

要在Microsoft Excel中查找并设置此选项：

1. 选择数据透视表，右键单击。
2. 选择**数据透视表选项**。
3. 选择**布局和格式**选项卡。
4. 选择**对空单元格显示**选项并指定字符串。

## **使用Aspose.Cells for JavaScript通过C++设置Pivot表选项**

Aspose.Cells for JavaScript通过C++提供[**PivotTable.displayNullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#displayNullString-boolean-)和[**PivotTable.nullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#nullString-string-)属性，用于设置“空单元格显示”Pivot表选项。

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

## 相关文章

- [格式化数据透视表](/cells/zh/javascript-cpp/formatting-pivot-table/)
