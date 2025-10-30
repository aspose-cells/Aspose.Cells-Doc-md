---
title: JavaScriptを用いた暗号化ファイルのパスワード検証（C++）
linktitle: 暗号化されたファイルのパスワードを確認する
type: docs
weight: 10
url: /ja/javascript-cpp/verify-password-of-encrypted-excel-and-ods-files/
description: C++を通じてAspose.Cells for JavaScriptを用いた暗号化されたExcel（xlsx、xlsb、xls、xlsm）およびOpen Office（ODS）ファイルのパスワードを検証する
---

{{% alert color="primary" %}}  
Excel（xlsx、xlsb、xls、xlsm）とOpen Office（ODS）ファイルがパスワードでロックされている場合、Asposeはファイルの特定のデータを解析せずに簡単なパスワード検証をサポートします。  
{{% /alert %}}  

## **暗号化されたファイルのパスワードを確認します**  

暗号化されたファイルのパスワードを検証するために、Aspose.Cells for JavaScriptは[**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-)メソッドを提供します。このメソッドは2つのパラメータ、ファイルストリームと検証する必要があるパスワードを受け取ります。  
以下のコードスニペットは、提供されたパスワードが有効かどうかを確認する[**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-)メソッドの使用を示しています。  

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
