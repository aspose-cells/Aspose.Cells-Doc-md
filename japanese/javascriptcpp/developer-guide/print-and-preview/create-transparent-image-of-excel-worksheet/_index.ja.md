---
title: Excelワークシートの透明な画像をJavaScriptをC++経由で作成します。
linktitle: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /ja/javascript-cpp/create-transparent-image-of-excel-worksheet/
description: Aspose.Cells for JavaScriptをC++経由で使用して、Excelワークシートの透明な画像を生成する方法を学びます。
---

{{% alert color="primary" %}}

時々、ワークシートの画像を透明なイメージとして生成する必要があります。埋められていないセルに透明性を適用したい場合があります。Aspose.Cellsは透明性をワークシートイメージに適用するための[**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#transparent--)プロパティを提供しています。このプロパティが **false** の場合、埋められていないセルは白色で描画され、 **true** の場合、埋められていないセルは透明に描画されます。

{{% /alert %}}

以下のワークシートイメージでは、透明性が適用されていません。埋められていないセルは白色で描画されます。

|**透明度なしの出力: セルの背景は白です**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

以下のワークシート画像では、透明度が適用されました。塗りつぶしのないセルは透明です。

|**透明度を有効にした出力**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

次のサンプルコードは、Excelワークシートから透明な画像を生成します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Create Transparent Image Example</title>
    </head>
    <body>
        <h1>Create Transparent Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Create Transparent PNG</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType } = AsposeCells;

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

            // Create workbook object from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = wb.worksheets.get(0);

            // Apply different image or print options
            const imgOption = new ImageOrPrintOptions();
            imgOption.imageType = ImageType.Png;
            imgOption.horizontalResolution = 200;
            imgOption.verticalResolution = 200;
            imgOption.onePagePerSheet = true;

            // Apply transparency to the output image
            imgOption.transparent = true;

            // Create image after applying image or print options
            const sr = new SheetRender(sheet, imgOption);
            const outputData = await sr.toImage(0);

            const blob = new Blob([outputData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCreateTransparentImage.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PNG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image created successfully! Click the download link to get the PNG file.</p>';
        });
    </script>
</html>
```
