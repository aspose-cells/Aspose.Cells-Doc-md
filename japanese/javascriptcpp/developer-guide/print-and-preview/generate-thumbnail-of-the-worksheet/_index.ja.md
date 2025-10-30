---
title: JavaScriptをC++経由で使用して、ワークシートのサムネイルを生成します
linktitle: ワークシートのサムネイルを生成
type: docs
weight: 110
url: /ja/javascript-cpp/generate-thumbnail-of-the-worksheet/
description: Aspose.Cells for JavaScriptをC++で使用して、ワークシートからサムネイル画像を生成する方法を学びます。ドキュメントやプレゼンテーションのプレビュー用に小さな画像を作成します。
---

{{% alert color="primary" %}} 

ワークシートからサムネイルを作成することは便利です。サムネイルは、ワークシートのプレビューを提供するためにWordドキュメントやPowerPointプレゼンテーションに貼り付けることができる小さなイメージです。それは、オリジナルのドキュメントをダウンロードするためのリンクを含むウェブページに追加することができ、その他の用途もたくさんあります。

{{% /alert %}} 

Aspose.Cells for JavaScriptをC++で使用すると、ワークシートを画像ファイルに出力できるため、サムネイルの作成は簡単です。下記のサンプルコードでは、ワークシートを画像ファイルに出力する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Generate Worksheet Thumbnail Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Generate Thumbnail</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, SheetRender, Utils } = AsposeCells;

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

            // Instantiate and open an Excel file from the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Set the vertical and horizontal resolution
            imgOptions.verticalResolution = 200;
            imgOptions.horizontalResolution = 200;

            // One page per sheet is enabled
            imgOptions.onePagePerSheet = true;

            // Set desired thumbnail dimensions (converted to a property assignment)
            imgOptions.desiredSize = [600, 600, true];

            // Get the first worksheet
            const sheet = book.worksheets.get(0);

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Generate the image for the first page (index 0)
            const outputData = sr.toImage(0);

            // Create a blob and provide a download link
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGenerateThumbnailOfWorksheet.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Thumbnail Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Thumbnail generated successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
