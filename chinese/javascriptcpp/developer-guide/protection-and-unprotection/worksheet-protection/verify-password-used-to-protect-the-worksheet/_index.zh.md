---
title: 验证用于保护工作表的密码，使用JavaScript通过C++
linktitle: 验证用于保护工作表的密码
type: docs
weight: 370
url: /zh/javascript-cpp/verify-password-used-to-protect-the-worksheet/
description: 学习如何使用Aspose.Cells for Java脚本通过C++验证用于保护工作表的密码。
---

{{% alert color="primary" %}}

Aspose.Cells API增强了[**Protection**](https://reference.aspose.com/cells/javascript-cpp/protection)类，新增了一些有用的属性和方法。其中一个方法是[**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-)，它允许指定密码（字符串实例）并验证是否用该密码保护了[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)。

{{% /alert %}}

如果指定的密码与用于保护工作表的密码匹配，则[**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-)方法返回**true**，否则返回**false**。以下代码结合使用[**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-)方法和[**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--)属性来检测密码保护状态并验证密码。

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

            // Instantiate Workbook with file bytes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Check if Worksheet is password protected
            if (sheet.protection.isProtectedWithPassword()) {
                // Verify the password used to protect the Worksheet
                if (sheet.protection.verifyPassword("1234")) {
                    resultDiv.innerHTML = '<p style="color: green;">Specified password has matched</p>';
                } else {
                    resultDiv.innerHTML = '<p style="color: red;">Specified password has not matched</p>';
                }
            } else {
                resultDiv.innerHTML = '<p style="color: blue;">Worksheet is not password protected</p>';
            }
        });
    </script>
</html>
```
