---
title: ワークシートを画像に変換  JavaScript（C++）を使用してデータ周囲の空白を取り除く
linktitle: ワークシートを画像に変換  データ周りの余白を削除する
type: docs
weight: 40
url: /ja/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Microsoft Excelのワークシートを画像に変換し、データ周囲の空白を除去する方法をAspose.Cells for JavaScriptをC++経由で学びます。 
---

{{% alert color="primary" %}}

時には、ワークシートの画像をアプリケーションやWebページで表示する必要があります。たとえば、画像をWord文書、PDFファイル、PowerPointプレゼンテーション、あるいは他のドキュメントに挿入する必要があるかもしれません。基本的に、ワークシートを画像としてレンダリングして、他のアプリケーションに貼り付けられるようにしたいと思うでしょう。Aspose.Cellsを使用すると、Microsoft Excelのワークシートを画像に変換することができます。

{{% /alert %}}

## **データ周りの余白を削除してください**

[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender)APIは、ワークシートを指定された属性（たとえば、画像形式、ページ化されたシートなど）で画像ファイルに変換します。いくつかの画像形式がサポートされており、BMP、GIF、JPG、TIFF、EMFなどが含まれています。

シートを画像化する際、出力画像にはデフォルトで余白（ボーダー）があります。これを削除するには、元のワークシートの上部、下部、左側、右側のページ設定のマージンを0に設定し、それに応じて[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions)属性を指定してください。

次のコードスニペットは、出力画像のデータ周りの余白を削除します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Sheet to EMF</title>
    </head>
    <body>
        <h1>Convert Worksheet to EMF Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to EMF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFilter, LoadDataFilterOptions, ImageOrPrintOptions, ImageType, PrintingPageType, SheetRender, Utils } = AsposeCells;

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

            // Prepare load options and filters
            const loadOptions = new LoadOptions();
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.All);

            // Instantiate workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // To remove the white border around the image.
            sheet.pageSetup.leftMargin = 0;
            sheet.pageSetup.rightMargin = 0;
            sheet.pageSetup.bottomMargin = 0;
            sheet.pageSetup.topMargin = 0;

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.imageType = ImageType.Emf;

            // Set only one page would be rendered for the image
            imgOptions.onePagePerSheet = true;
            imgOptions.printingPage = PrintingPageType.IgnoreBlank;

            // Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
            const sr = new SheetRender(sheet, imgOptions);

            // Convert the image (returns image data in browser environment)
            const imageData = sr.toImage(0);

            // Create a blob and provide download link
            const blob = new Blob([imageData], { type: 'image/emf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRemoveWhitespaceAroundData.emf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download EMF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image conversion completed successfully! Click the download link to get the EMF file.</p>';
        });
    </script>
</html>
```
