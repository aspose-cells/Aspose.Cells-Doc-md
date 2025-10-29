---
title: 查找单元格值是否以单引号开始
type: docs
weight: 270
url: /zh/javascript-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: 学习如何通过Aspose.Cells for JavaScript通过C++ API查找单元格值是否以单引号开头。
keywords: 通过C++的JavaScript查找单元格值以单引号开头，搜索以单引号开头的单元格 JavaScript via C++
---

{{% alert color="primary" %}}

Aspose.Cells 现在提供了属性 [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-) 来查找单元格值是否以单引号标记开始。在此属性之前，无法区分类似 sample 和 'sample 等字符串。

{{% /alert %}}

以下示例代码说明，像sample和'sample'这样的字符串无法通过[**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--)属性区分，因此必须使用[**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-)属性进行区分。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            // Creating a new workbook
            const wb = new Workbook();

            // Accessing the first worksheet in the workbook
            const sheet = wb.worksheets.get(0);

            // Access cell A1 and A2
            const a1 = sheet.cells.get("A1");
            const a2 = sheet.cells.get("A2");

            // Add sample in A1 and sample with quote prefix in A2
            a1.putValue("sample");
            a2.putValue("'sample");

            // Read their string values, A1 and A2 both are same when read as stringValue
            const a1String = a1.stringValue;
            const a2String = a2.stringValue;

            // Access styles of A1 and A2
            const s1 = a1.style;
            const s2 = a2.style;

            // Check if A1 and A2 has a quote prefix
            const a1Quote = s1.quotePrefix;
            const a2Quote = s2.quotePrefix;

            // Display results
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = `
                <p>String value of A1: ${a1String}</p>
                <p>String value of A2: ${a2String}</p>
                <p>A1 has a quote prefix: ${a1Quote}</p>
                <p>A2 has a quote prefix: ${a2Quote}</p>
            `;

            // Save the workbook and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```
