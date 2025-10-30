---
title: JavaScriptをC++で使用してVBAコードに署名があるかどうかを確認する
linktitle: VBAコードが署名されているかどうかをチェック
type: docs
weight: 100
url: /ja/javascript-cpp/check-if-vba-code-is-signed/
description: Aspose.Cells for JavaScriptを使用して、VBAコードプロジェクトに署名されているかどうかをC++で確認する方法を学びます。 
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、VBAコードプロジェクトが署名されているかどうかを確認できます。VBAコードプロジェクトが署名されているかどうかを確認するには、[**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--)プロパティを使用してください。

{{% /alert %}}

以下のコードは、[**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--)プロパティを使用してVBAコードに署名されているかどうかを確認する方法を示しています。このコードは任意のExcelファイルでテストできます。テスト用に、このコードで使用されているExcelファイル（[このExcelファイル](5115032.xlsm)）を使用可能です。

## **JavaScriptでVBAコードに署名されているか確認する**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VBA Signed Check Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the VBA project and checking if it's signed
            const vbaProject = workbook.vbaProject;
            const isSigned = vbaProject.isSigned();

            resultDiv.innerHTML = `<p>Is VBA Code Project Signed: ${isSigned}</p>`;
        });
    </script>
</html>
```

## コンソール出力

上記のコードのコンソール出力は、提供された[サンプルExcelファイル](5115032.xlsm)を使用して以下のようになります。

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
