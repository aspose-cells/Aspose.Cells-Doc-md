---
title: 使用JavaScript通过C++进行JSON
linktitle: Json
type: docs
weight: 300
url: /zh/javascript-cpp/convert-workbook-to-json/
description: 学习如何使用Aspose.Cells for JavaScript通过C++将Excel工作簿转换为JSON。
---

{{% alert color="primary" %}}
Aspose.Cells 支持将工作簿转换为 Json（JavaScript 对象表示法）文件。
{{% /alert %}}

## **将Excel工作簿转换为JSON**

Aspose.Cells API 提供了将电子表格转换为 JSON 格式的支持。要导出工作簿到 JSON，请将 [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat) 作为 [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) 方法的第二个参数传递。你还可以使用 [**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions) 类来指定导出工作表到 JSON 的其他设置。

以下代码示例演示如何使用 [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/#json) 枚举成员将活动工作表导出为 JSON。请参阅代码，将 [source file](book1.xlsx) 转换为 [输出 JSON 文件](book1.Json)。以作参考。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Workbook to JSON</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook as JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook converted to JSON successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```

## **高级主题**
- [将CSV转换为JSON](/cells/zh/javascript-cpp/convert-csv-to-json/)
- [将Excel转换为JSON](/cells/zh/javascript-cpp/convert-excel-to-json/)
- [将JSON转换为CSV](/cells/zh/javascript-cpp/convert-json-to-csv/)
- [将JSON转换为Excel](/cells/zh/javascript-cpp/convert-json-to-excel/)
