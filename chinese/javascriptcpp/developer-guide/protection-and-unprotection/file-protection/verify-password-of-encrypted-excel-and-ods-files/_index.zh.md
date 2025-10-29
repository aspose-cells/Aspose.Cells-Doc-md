---
title: 通过 C++ 及 JavaScript 验证加密文件的密码
linktitle: 验证加密文件的密码
type: docs
weight: 10
url: /zh/javascript-cpp/verify-password-of-encrypted-excel-and-ods-files/
description: 使用 C++ 及 Aspose.Cells for JavaScript 通过 JavaScript 验证加密的 Excel（xlsx、xlsb、xls、xlsm）和 Open Office（ODS）文件的密码
---

{{% alert color="primary" %}}  
 如果Excel（xlsx、xlsb、xls、xlsm）和Open Office（ODS）文件被密码锁定，Aspose支持简单的密码验证，无需解析文件的具体数据。  
{{% /alert %}}  

## **验证加密文件的密码**  

 为验证加密文件密码，C++ 通过 Aspose.Cells for JavaScript 提供 [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-) 方法。此方法接受两个参数，文件流和需要验证的密码  
以下代码片段演示了使用[**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-)方法来验证提供的密码是否有效。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Verify Excel Password Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Verify Password</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FileFormatUtil, Utils } = AsposeCells;

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
            const bytes = new Uint8Array(arrayBuffer);

            const isPasswordValid = FileFormatUtil.verifyPassword(bytes, "1234");

            document.getElementById('result').innerHTML = '<p>Password is Valid: ' + isPasswordValid + '</p>';
        });
    </script>
</html>
```
