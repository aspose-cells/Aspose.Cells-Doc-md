---
title: ワークシートがパスワード保護されているかどうかをJavaScriptを使用してC++で検出
linktitle: ワークシートがパスワードで保護されているかどうかを検出する
type: docs
weight: 360
url: /ja/javascript-cpp/detect-if-worksheet-is-password-protected/
description: Aspose.Cells for JavaScriptをC++で使用して、ワークシートがパスワード保護されているかどうかを検出する方法を学びます。 
keywords: JavaScriptを使用してワークシートのパスワード保護を検出する方法、パスワード保護されているかどうかをC++を使って確認する方法、Aspose.Cells for JavaScriptをC++で使用します。
---

{{% alert color="primary" %}}

ワークブックとワークシートを個別に保護することが可能です。例えば、スプレッドシートにパスワード保護された1つまたは複数のワークシートが含まれている場合でも、スプレッドシート自体は保護されているかどうか異なる場合があります。Aspose.Cells APIは、特定のワークシートがパスワード保護されているかどうかを検出する方法を提供します。この記事では、Aspose.Cells for JavaScriptをC++ APIで使用して同じことを実現する方法を示します。

{{% /alert %}}

C++経由のAspose.Cells for JavaScriptは、[**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--)プロパティを公開して、ワークシートがパスワード保護されているかどうかを検出します。 Boolean型の[**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--)プロパティは、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)がパスワード保護されている場合は**true**を返し、そうでない場合は**false**を返します。

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
