---
title: 使用JavaScript通过C++检测工作表是否密码保护
linktitle: 检测工作表是否受密码保护
type: docs
weight: 360
url: /zh/javascript-cpp/detect-if-worksheet-is-password-protected/
description: 学习如何使用Aspose.Cells for Java脚本通过C++检测工作表是否密码保护。 
keywords: 通过C++使用JavaScript检测工作表密码保护，根据密码保护状态检测JavaScript，使用C++脚本检测密码保护状态，Aspose.Cells for Java脚本通过C++
---

{{% alert color="primary" %}}

可以单独保护工作簿和工作表。例如，电子表格可能包含一个或多个受密码保护的工作表，但电子表格本身可能受保护，也可能不受保护。Aspose.Cells API提供检测特定工作表是否受密码保护的方法。本文演示如何使用Aspose.Cells for Java脚本通过C++实现相同的功能。

{{% /alert %}}

Aspose.Cells for Java脚本通过C++已暴露[**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--)属性，用于检测工作表是否受密码保护。布尔类型[**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--)属性如果[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)受密码保护，则返回**true**，否则返回**false**。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Worksheet Password Protection</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create an instance of Workbook and load a spreadsheet
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Access the protected Worksheet
            const sheet = book.worksheets.get(0);

            // Check if Worksheet is password protected
            if (sheet.protection.isProtectedWithPassword()) {
                resultDiv.innerHTML = '<p>Worksheet is password protected</p>';
                console.log("Worksheet is password protected");
            } else {
                resultDiv.innerHTML = '<p>Worksheet is not password protected</p>';
                console.log("Worksheet is not password protected");
            }
        });
    </script>
</html>
```
