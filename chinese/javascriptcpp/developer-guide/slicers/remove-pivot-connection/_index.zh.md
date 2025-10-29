---
title: 用JavaScript和C++移除数据透视连接
linktitle: 删除数据透视连接
type: docs
weight: 30
url: /zh/javascript-cpp/remove-pivot-connection/
description: 学习如何使用Aspose.Cells for JavaScript通过C++移除数据透视连接。
keywords: 移除没有 Office 2013、Office 2016、Office 2019 和 Office 365 JavaScript 连接的枢纽。
---

## **可能的使用场景**

如果您想在 Excel 中解除切片器与数据透视表的关联，需右键点击切片器并选择“报告连接...”。在选项列表中，您可以操作复选框。类似的，如果您想通过 C++ 脚本使用 Aspose.Cells for JavaScript API 编程解除切片器与数据透视表的关系，请使用 [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#removePivotConnection-pivottable-) 方法。它会解除切片器与数据透视表的关联。

## **取消切片器与数据透视表的关联**

以下示例代码加载了包含现有切片器的[示例Excel文件](remove-pivot-connection.xlsx)。它访问切片器，然后解除切片器与数据透视表的关联，最后将工作簿保存为[输出Excel文件](remove-pivot-connection-out.xlsx)。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Connection</title>
    </head>
    <body>
        <h1>Remove Pivot Connection Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access the first PivotTable inside the PivotTable collection.
            const pivotTable = worksheet.pivotTables.get(0);

            // Access the first slicer inside the slicer collection.
            const slicer = worksheet.slicers.get(0);

            // Remove PivotTable connection.
            slicer.removePivotConnection(pivotTable);

            // Save the workbook in output XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'remove-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
