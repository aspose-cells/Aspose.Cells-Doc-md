---
title: JavaScriptをC++経由で使用し、ImageOrPrintOptionsを使ってワークシートから画像を抽出します。
linktitle: ImageOrPrintOptionsを使用してワークシートからイメージを抽出する
type: docs
weight: 140
url: /ja/javascript-cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Excelワークシートから画像を抽出し、Aspose.Cells for JavaScriptをC++経由で保存する方法を学びます。
---

{{% alert color="primary" %}} 

Microsoft Excelのユーザーは、スプレッドシートに画像を追加できます。Aspose.Cells for JavaScriptをC++で使用すれば、Microsoft Excelファイルから画像を読み取り、ローカルドライブに保存することが可能です。この記事ではその方法を紹介します。

{{% /alert %}} 

以下のサンプルコードは、Excelファイルから画像を抽出して保存する方法を示しています。



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Image from Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, Utils } = AsposeCells;

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

            // Open the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the first Picture in the first worksheet
            const pic = worksheet.pictures.get(0);

            // Determine picture format
            const picformat = pic.imageType.toString();

            // Define ImageOrPrintOptions
            const printoption = new ImageOrPrintOptions();

            // Specify the image format (use JPEG as in original code)
            printoption.imageType = ImageType.Jpeg;

            // Export picture to image bytes (browser version returns image bytes when path is not used)
            const outputData = pic.toImage(printoption);

            // Determine file extension and MIME type
            let ext = picformat.toLowerCase();
            if (ext === 'jpeg') ext = 'jpg';
            let mime = 'image/jpeg';
            if (ext === 'png') mime = 'image/png';
            if (ext === 'gif') mime = 'image/gif';

            const filename = 'outputExtractImagesFromWorksheets.' + ext;

            const blob = new Blob([outputData], { type: mime });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = filename;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Extracted Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image extracted successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
