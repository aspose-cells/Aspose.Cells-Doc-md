---
title: 使用JavaScript通过C++在范围内搜索和替换数据
linktitle: 在 Excel 中使用 C# 代码搜索和替换范围内的数据
type: docs
weight: 170
url: /zh/javascript-cpp/search-and-replace-data-in-a-range/
description: 本文展示如何使用JavaScript通过C++在Excel中搜索和替换范围内的数据。
keywords: 使用JavaScript搜索和替换Excel中的数据，使用JavaScript搜索Excel中的数据，使用JavaScript在范围内搜索和替换数据，使用JavaScript搜索范围内的数据，JavaScript在范围内搜索数据，JavaScript在Excel中搜索数据，JavaScript搜索范围内的数据，使用JavaScript在Excel中搜索数据，使用JavaScript在范围内搜索和替换数据，使用JavaScript在范围内搜索和替换数据。
---

{{% alert color="primary" %}}

 有时需要在忽略范围外任何单元格值的情况下，搜索并替换范围内的特定数据。8647720447Script通过C++允许你限制搜索到特定的范围。本文解释了此方法。

{{% /alert %}}

 8647720447Script通过C++提供了在搜索数据时指定范围的[**FindOptions.range(CellArea)**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#range-cellarea-)方法。以下的代码示例在范围内搜索和替换数据。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Find and Replace Example</title>
    </head>
    <body>
        <h1>Find and Replace Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, FindOptions, LookInType, LookAtType } = AsposeCells;

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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Define the search range (E9:H15)
            const area = CellArea.createCellArea("E9", "H15");

            // Configure find options
            const opts = new FindOptions();
            opts.lookInType = LookInType.Values;
            opts.lookAtType = LookAtType.EntireContent;
            opts.range = area;

            let cell = null;

            do {
                cell = worksheet.cells.find("search", cell, opts);
                if (cell === null || cell.isNull()) {
                    break;
                }
                // Replace found cell's value
                cell.value = "replace";
            } while (true);

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Find and replace completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
