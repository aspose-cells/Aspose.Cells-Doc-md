---
title: C++経由でJavaScriptを使用してWorkbookのアンマネージドリソースを解放する
linktitle: ブックのアンマネージリソースを解放する
type: docs
weight: 310
url: /ja/javascript-cpp/release-unmanaged-resources-of-the-workbook/
description: C++経由でAspose.Cells for JavaScriptを使用してWorkbookオブジェクトのアンマネージドリソースを解放する方法を学習します。 
---

{{% alert color="primary" %}}

Aspose.Cellsは[**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--)メソッドを提供し、[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)オブジェクトの未管理リソースを解放します。このdisposeパターンは、ファイルやパイプハンドル、レジストリハンドル、待機ハンドル、または未管理メモリブロックへのポインタなどの未管理リソースにアクセスするオブジェクトにのみ使われます。これは、ガベージコレクターは未管理オブジェクトの再回収に非常に効率的ですが、未管理オブジェクトの回収はできないためです。

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)オブジェクトは現在、*System.IDisposable*インターフェースを実装しており、単一のメソッド[**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--)を持ちます。直接[**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--)メソッドを呼び出すか、*Using*ステートメントを使って自動的にこのメソッドを呼び出すことも可能です。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Dispose Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create workbook object
            const wb1 = new Workbook();

            // Call Dispose method
            wb1.dispose();

            // Call Dispose method via a scoped approach
            (async () => {
                const wb2 = new Workbook();
                // Any other code goes here
                wb2.dispose();
            })();

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully!</p>';
        });
    </script>
</html>
```
