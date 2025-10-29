---
title: 用JavaScript via C++添加数据透视连接
linktitle: 添加数据透视连接
type: docs
weight: 30
url: /zh/javascript-cpp/add-pivot-connection/
description: 学习如何使用Aspose.Cells for JavaScript通过C++添加数据透视连接。
keywords: 无需Office 2013、2016、2019和365 JavaScript via C++添加数据透视连接
---

## **可能的使用场景**

如果您想在Excel中关联切片器和数据透视表，右键点击切片器并选择“报告连接...”项。在选项列表中，您可以操作复选框。同样地，如果您想通过Aspose.Cells API编程方式关联切片器和数据透视表，请使用[**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#addPivotConnection-PivotTable-)方法。它将关联切片器和数据透视表。

## **关联切片器和数据透视表**

以下示例代码加载了包含现有切片器的[示例Excel文件](add-pivot-connection.xlsx)。它访问切片器，然后将切片器与数据透视表关联，最后将工作簿保存为[输出Excel文件](add-pivot-connection-out.xlsx)。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add Pivot Connection Example</title>
    </head>
    <body>
        <h1>Add Pivot Connection Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            const pivotTable = worksheet.pivotTables.get(0);

            const slicer = worksheet.slicers.get(0);

            slicer.addPivotConnection(pivotTable);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'add-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
