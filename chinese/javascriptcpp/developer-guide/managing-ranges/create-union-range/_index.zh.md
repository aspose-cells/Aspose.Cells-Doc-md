---
title: 使用 JavaScript 通过 C++ 创建联合范围
linktitle: 创建联合范围
type: docs
weight: 360
url: /zh/javascript-cpp/create-union-range/
description: 学习如何使用 C++ 创建联合范围。
keywords: 使用 C++ 通过 JavaScript 创建联合范围，Aspose.Cells JavaScript 通过 C++ 实现联合范围，WorksheetCollection 使用 JavaScript via C++ 创建联合范围
---

## **创建联合范围**
Aspose.Cells 提供通过 [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#createUnionRange-string-number-) 方法创建联合范围的能力。该方法接受两个参数：用于创建联合范围的地址和工作表的索引。该方法返回一个 [UnionRange](https://reference.aspose.com/cells/javascript-cpp/unionrange) 对象。  

以下代码片段演示了如何使用 [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#createUnionRange-string-number-) 方法创建联合范围。生成的输出文件已附上供参考。  

- [输出文件](106364952.xlsx)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Create Union Range Example</title>
    </head>
    <body>
        <h1>Create Union Range Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create union range
            const unionRange = workbook.worksheets.createUnionRange("sheet1!A1:A10,sheet1!C1:C10", 0);

            // Put value "ABCD" in the range (converted setter to property)
            unionRange.value = "ABCD";

            // Save the output workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CreateUnionRange_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Union range created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
