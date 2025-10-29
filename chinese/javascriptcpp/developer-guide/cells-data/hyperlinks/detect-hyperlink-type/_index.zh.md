---
title: 检测超链接类型
type: docs
weight: 160
url: /zh/javascript-cpp/detect-hyperlink-type/
description: 了解如何通过Aspose.Cells for JavaScript在C++ API中检测超链接类型。
keywords: 通过C++检测超链接类型JavaScript，检测超链接类型JavaScript，通过C++获取超链接类型JavaScript
---

## **检测超链接类型**

Excel文件可以具有不同类型的超链接，如外部、单元格引用、文件路径等。Aspose.Cells for JavaScript通过C++支持检测超链接类型的功能。超链接的类型由[**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype)枚举表示，[**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype)枚举具有以下成员。

- External：外部链接
- FilePath：本地文件/文件夹的完整路径。
- Email：电子邮件
- CellReference：链接到单元格或命名区域。

要检查超链接的类型，[**Hyperlink**](https://reference.aspose.com/cells/javascript-cpp/hyperlink)类提供一个[**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--)属性，其返回类型为[**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype)。以下代码片段演示了如何使用[**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--)属性，使用此[源Excel文件](94896195.xlsx)。

### 源代码

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Link Types Example</title>
    </head>
    <body>
        <h1>Link Types Example</h1>
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

                // Get the first (default) worksheet
                const worksheet = workbook.worksheets.get(0);

                // Create a range A1:A7 (original code created A1:B7 but used A1 to A7 in parameters)
                const range = worksheet.cells.createRange("A1", "A7");

                // Get Hyperlinks in range
                const hyperlinks = range.hyperlinks;

                let outputHtml = '<p>Hyperlinks found:</p><ul>';
                if (typeof hyperlinks.forEach === 'function') {
                    hyperlinks.forEach(link => {
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    });
                } else {
                    for (let i = 0; i < hyperlinks.count; i++) {
                        const link = hyperlinks.get(i);
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    }
                }
                outputHtml += '</ul>';

                resultDiv.innerHTML = outputHtml;
            });
        });
    </script>
</html>
```


以下是上述代码片段生成的输出。

### 控制台输出
