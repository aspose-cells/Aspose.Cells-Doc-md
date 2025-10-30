---
title: JavaScriptを介してC++でWorkbook内のVBAプロジェクトに署名されているか確認する
linktitle: ブックのVBAプロジェクトが署名されているかどうかを確認
type: docs
weight: 70
url: /ja/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: C++を通じてAspose.Cells for JavaScriptを使用して、Workbook内のVBAプロジェクトが署名されているかどうかを確認する方法を学びます。
---

{{% alert color="primary" %}}

Microsoft Excelでは、**ツール > デジタル署名...**メニューコマンドを使用してVBAプロジェクトが署名されているかどうかを確認できます。同様に、Aspose.Cellsの[**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--)プロパティを使用してプログラムで確認することも可能です。

{{% /alert %}}

## **JavaScriptでWorkbook内のVBAプロジェクトに署名されているか確認する**

以下のコードは、ワークブックをロードし、そのVBAプロジェクトが署名されているかどうかを [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--)プロパティを使用して判定します。署名されている場合は **true** を返し、そうでなければ**false**を返します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VBA Signed Check</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
        <button id="runExample">Run Example</button>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the VBA project and checking if it's signed
            const isSigned = workbook.vbaProject.isSigned;

            console.log("VBA Project is Signed: " + isSigned);
            document.getElementById('result').innerHTML = `<p>VBA Project is Signed: ${isSigned}</p>`;
        });
    </script>
</html>
```
