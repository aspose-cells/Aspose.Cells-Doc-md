---
title: 单元格名称和行/列索引之间的转换
linktitle: 单元格名称和索引转换
type: docs
weight: 10
url: /zh/javascript-cpp/names-and-indices/
description: 学习如何通过C++的Aspose.Cells for JavaScript实现单元格名称与行/列索引的转换。
keywords: 用C++的JavaScript从行列索引获取单元格名称，从单元格名称获取行列索引，创建安全的工作表名称，添加安全的工作表名称
---

## **从行和列索引获取单元格名称**
可以通过给定行和列索引来查找单元格的名称。 本文解释了如何操作。
Aspose.Cells for Java脚本通过C++提供CellsHelper.cellIndexToName方法，允许开发者通过提供行和列索引来获取单元格的名称。

{{% alert color="primary" %}} 

Microsoft Excel从1开始计算行列索引。不同于Microsoft Excel，Aspose.Cells for Java脚本通过C++从0开始计算行列索引。

{{% /alert %}} 

以下示例代码说明了如何使用CellsHelper.cellIndexToName在已知行和列索引的情况下访问单元格名称。代码生成以下输出。



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            // Original logic converted to browser JavaScript
            var row = 3;
            var column = 5;
            var name = AsposeCells.CellsHelper.cellIndexToName(row, column);
            console.log("Cell name: " + name);
            document.getElementById('result').innerHTML = '<p>Cell name: ' + name + '</p>';
        });
    </script>
</html>
```
## **从单元格名称获取行和列索引**
可以从单元格名称中找到单元格的行和列索引。 本文解释了如何操作。
Aspose.Cells for Java脚本通过C++提供CellsHelper.cellNameToIndex方法，允许开发者通过单元格名称获取行和列索引。

{{% alert color="primary" %}} 

Microsoft Excel从1开始计算行列索引。不同于Microsoft Excel，Aspose.Cells for Java脚本通过C++从0开始计算行列索引。

{{% /alert %}} 

以下示例代码说明了如何使用CellsHelper.cellNameToIndex根据单元格名称获取行和列索引。代码生成以下输出。



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Row and Column from Cell Name</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <div>
            <label for="cellName">Cell Name:</label>
            <input type="text" id="cellName" value="C4" />
        </div>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

        let asposeInitialized = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeInitialized = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', () => {
            if (!asposeInitialized) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const name = document.getElementById('cellName').value || "C4";

            const rowCol = CellsHelper.cellNameToIndex(name);
            const currRow = rowCol[0];
            const currCol = rowCol[1];
            console.log("Row: " + currRow + " , Column: " + currCol);

            document.getElementById('result').innerHTML = `<p>Row: ${currRow} , Column: ${currCol}</p>`;
        });
    </script>
</html>
```

## **创建安全的工作表名称**
有时需要在运行时分配工作表名称。在这种情况下，可能存在包含一些额外字符如<>+(?”的工作表名称。需要用用户提供的预设字符替换任何此类不允许作为工作表名的字符。同样，长度可能超过31个字符，需要截断。Apache POI提供创建安全名称的某些功能，因此Aspose.Cells for Java脚本通过C++也提供类似功能，以处理所有这些问题。以下示例代码演示了此功能：



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Create Safe Sheet Name</title>
    </head>
    <body>
        <h1>Create Safe Sheet Name Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', () => {
            // Long name will be truncated to 31 characters
            var name1 = AsposeCells.CellsHelper.createSafeSheetName("this is first name which is created using CellsHelper.CreateSafeSheetName and truncated to 31 characters");

            // Any invalid character will be replaced with _
            var name2 = AsposeCells.CellsHelper.createSafeSheetName(' <> + (adj.Private ? " Private" : ")', '_');

            // Display results in the page
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p><strong>Safe Name 1:</strong> ' + name1 + '</p>' +
                                  '<p><strong>Safe Name 2:</strong> ' + name2 + '</p>';
        });
    </script>
</html>
```

输出:

这是第一个名字，它是特别私人的

` ``<> + (adj.Private _ " 私有"
