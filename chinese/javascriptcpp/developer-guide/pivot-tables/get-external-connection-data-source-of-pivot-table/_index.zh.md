---
title: 获取数据透视表的外部连接数据源
type: docs
weight: 150
url: /zh/javascript-cpp/get-external-connection-data-source-of-pivot-table/
description: 如何用Aspose.Cells for JavaScript通过C++获取数据透视表的外部连接数据源。
keywords: Aspose.Cells for JavaScript Excel、Excel JavaScript库，使用C++通过Aspose.Cells for JavaScript获取数据透视表的外部连接数据源。
---

## **如何获取数据透视表的外部连接数据源**

Aspose.Cells for JavaScript通过C++提供了获取数据透视表外部连接数据源的功能。API提供了[**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--)属性，属于[**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable/)类。[**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--)属性返回[**ExternalConnection**](https://reference.aspose.com/cells/javascript-cpp/externalconnection/)对象。以下代码片段演示了如何使用[**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--)属性获取数据透视表的外部连接数据源。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Pivot Table External Connection Example</title>
    </head>
    <body>
        <h1>Pivot Table External Connection Example</h1>
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

            // Instantiating a Workbook object by opening the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get the pivot table
            const pivotTable = worksheet.pivotTables.get(0);

            // Get external connection data source
            const externalConnection = pivotTable.externalConnectionDataSource;

            const name = externalConnection.name;
            const type = externalConnection.type;

            console.log("External Connection Data Source");
            console.log("Name: " + name);
            console.log("Type: " + type);

            resultDiv.innerHTML = `<p style="color: green;">External Connection Data Source</p>
                                   <p>Name: ${name}</p>
                                   <p>Type: ${type}</p>`;
        });
    </script>
</html>
```

代码片段中使用的源文件已附上供参考。

[源文件](104398862.xlsx)
