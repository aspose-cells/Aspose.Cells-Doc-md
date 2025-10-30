---
title: 条件付き書式のデータバー画像を生成
linktitle: 条件付き書式のデータバー画像を生成
description: Aspose.Cellsはスプレッドシートファイルを操作するためのJavaScriptライブラリです。条件付き書式付きのデータバーや画像の生成をサポートしており、セルの値に基づいてスプレッドシートの表示をカスタマイズすることができます。この記事では、Aspose.Cellsライブラリを使用して条件付き書式付きのデータバーと画像を生成する方法を紹介します。
keywords: Aspose.Cells、条件付き書式、データバー、画像、スプレッドシート、JavaScript via C++
type: docs
weight: 40
url: /ja/javascript-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

時折、条件付き書式のデータバーの画像を生成する必要があります。Aspose.Cellsの [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/javascript-cpp/databar/#toImage-cell-imageorprintoptions-) メソッドを使用して、これらの画像を生成できます。この記事では、Aspose.Cellsを使用してデータバーの画像を生成する方法について説明します。

{{% /alert %}}

以下のサンプルコードは、セルC1のDataBar画像を生成します。まず、そのセルの書式条件オブジェクトにアクセスし、そのオブジェクトから[**DataBar**](https://reference.aspose.com/cells/javascript-cpp/databar)オブジェクトを取得、その[**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/javascript-cpp/databar/#toImage-cell-imageorprintoptions-)メソッドを使用してセルの画像を生成します。最後に、その画像をディスクに保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Generate DataBar Image</title>
    </head>
    <body>
        <h1>Generate DataBar Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Creating a workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell which contains conditional formatting databar
            const cell = worksheet.cells.get("C1");

            // Create and get the conditional formatting of the worksheet
            const idx = worksheet.conditionalFormattings.add();
            const fcc = worksheet.conditionalFormattings.get(idx);
            fcc.addCondition(AsposeCells.FormatConditionType.DataBar);
            fcc.addArea(AsposeCells.CellArea.createCellArea("C1", "C4"));

            // Access the conditional formatting databar
            const dbar = fcc.get(0).dataBar;

            // Create image or print options
            const opts = new AsposeCells.ImageOrPrintOptions();
            opts.imageType = AsposeCells.ImageType.Png;

            // Get the image bytes of the databar
            const imgBytes = dbar.toImage(cell, opts);

            // Create a blob and provide download link
            const blob = new Blob([imgBytes], { type: "image/png" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGenerateDatabarImage.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Generated DataBar Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image generated successfully! Click the download link to save the PNG file.</p>';
        });
    </script>
</html>
```
