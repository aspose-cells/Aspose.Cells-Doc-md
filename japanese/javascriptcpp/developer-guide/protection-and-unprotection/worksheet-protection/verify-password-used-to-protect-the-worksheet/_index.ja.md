---
title: JavaScriptを利用したC++でのワークシートのパスワード保護解除状況の確認
linktitle: ワークシートを保護するために使用されたパスワードの検証
type: docs
weight: 370
url: /ja/javascript-cpp/verify-password-used-to-protect-the-worksheet/
description: C++を利用してAspose.Cells for JavaScriptを使用し、ワークシートの保護に使用されたパスワードを検証する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cells APIは、便利なプロパティとメソッドを導入して[**Protection**](https://reference.aspose.com/cells/javascript-cpp/protection)クラスを強化しました。その一つが[**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-)であり、パスワードを*string*として指定し、同じパスワードがシートの保護に使用されたかどうかを検証します。

{{% /alert %}}

[**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-)メソッドは、指定されたパスワードが対象のワークシートを保護するために使用されたパスワードと一致すれば**true**を返し、一致しなければ**false**を返します。次のコード例は、[**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-)メソッドと[**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--)プロパティを併用してパスワード保護を検出し、パスワードを確認します。

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
