---
title: JavaScriptをC++経由で使用して、画像または印刷オプションを指定してワークシートを画像に変換します。
linktitle: ImageOrPrintオプションを使用してワークシートを画像に変換する
type: docs
weight: 90
url: /ja/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Aspose.Cells for JavaScriptをC++経由で使用し、ワークシートを画像ファイルに変換し、さまざまな画像および印刷オプションを適用する方法を学びます。   
---

{{% alert color="primary" %}}  
このドキュメントは、ワークシートを画像ファイルに変換し、画像と印刷オプションを適用し、解像度、TIFF圧縮、画像形式、ページ品質などのオプションを適用する方法について詳しく説明します。  
{{% /alert %}}  

## **ワークシートをイメージとして保存する - 異なるアプローチ**  

時々、ワークシートを図解的に表示する必要があります。ワークシートの画像をアプリケーションやWebページに挿入する必要があります。画像をWord文書、PDFファイル、PowerPointプレゼンテーションに挿入したり、他のシナリオで使用する必要があります。別の場所で使用するためにワークシートを画像としてレンダリングしたいと思うだけです。Aspose.CellsはExcelファイルのワークシートを画像に変換することをサポートしています。また、Aspose.Cellsは画像形式、解像度（縦と横の両方）、画像品質、およびその他の画像および印刷オプションを設定することをサポートしています。  

Office Automationを試すかもしれませんが、Office Automationには欠点もあります。その理由や問題点はいくつかあります：たとえば、セキュリティ、安定性、スケーラビリティと速度、価格、機能などです。要するに、多くの理由がありますが、その中でも最も重要なのは、Microsoft自身がソフトウェアソリューションからのOffice Automationを強く推奨していない点です。  

この記事は、Aspose.Cells APIを使用して、C#コンソールアプリケーションを作成し、わずかなコード行でさまざまなイメージと印刷オプションを使用してワークシートをイメージに変換する方法を示しています。  

[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/)クラスはワークシートの画像レンダリング用のワークシートを表し、オーバーロードされた[**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)メソッドを持ち、これを直接使ってワークシートを画像ファイルに変換し、希望の属性やオプションを指定できます。画像ファイルをディスクまたはストリームに保存できるオブジェクトを返します。サポートされる画像形式にはBMP、PNG、GIF、JPEG、TIFF、EMFなどがあります。  

## **ImageOrPrintオプションを使用して、Aspose.Cellsを使用してワークシートをイメージに変換する。**  

### **Microsoft Excelでテンプレートワークブックを作成する**  

私はMS Excelで新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました。これで、テンプレートファイルのワークシート **Sheet1** を画像ファイル **SheetImage.tiff** に変換し、水平および垂直解像度、TiffCompressionなどの異なるイメージオプションを適用します。  

### **Aspose.Cellsをダウンロードしてインストールする**  

まず、[Aspose.Cells for JavaScriptをC++経由でダウンロード](https://downloads.aspose.com/cells/javascript-cpp)します。開発コンピュータにインストールします。すべての[Aspose](http://www.aspose.com/)コンポーネントは、評価モードで動作し、制限時間がありません。評価モードでは、生成されたドキュメントにウォーターマークのみが挿入されます。  

### **プロジェクトを作成する**  

お好みの開発環境（例：Visual Studio）を起動します。新しいコンソールアプリケーションを作成します。  

### **参照の追加**  

このプロジェクトではAspose.Cellsを使用します。ですので、プロジェクトにAspose.Cellsコンポーネントへの参照を追加する必要があります。例として、…\Program Files\Aspose\Aspose.Cells for JavaScriptをC++\Bin\Aspose.Cells.nodeへの参照を追加します。  

### **ワークシートを画像ファイルに変換**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType, TiffCompression, PrintingPageType, Utils } = AsposeCells;

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

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Apply different Image and Print options
            const options = new ImageOrPrintOptions();

            // Set Horizontal Resolution
            options.horizontalResolution = 300;

            // Set Vertical Resolution
            options.verticalResolution = 300;

            // Set TiffCompression
            options.tiffCompression = TiffCompression.CompressionLZW;

            // Set Image Format
            options.imageType = ImageType.Tiff;

            // Set printing page type
            options.printingPage = PrintingPageType.Default;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, options);

            // Render/save the image for the sheet (pageIndex is zero-based)
            const pageIndex = 3;
            const imageData = sr.toImage(pageIndex);

            const blob = new Blob([imageData], { type: 'image/tiff' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `outputWorksheetToAnImage_${pageIndex + 1}.tiff`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF Image';

            resultDiv.innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```  

## **変換オプション**  

特定のページを画像に保存することが可能です。次のコードは、ワークブック内の最初と2番目のワークシートをJPG画像に変換します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Specific Pages To Images</title>
    </head>
    <body>
        <h1>Specific Pages To Images Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Specify page index to be rendered
            const idxPage = 3;

            // Render the third image for the sheet
            const bitmap = sr.toImage(idxPage);

            // Save the image file as a downloadable blob
            const blob = new Blob([bitmap], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `outputSpecificPagesToImage_${idxPage + 1}.jpg`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```  

## **WorkbookRenderを使用した画像変換**  

TIFF画像は複数のフレームを含むことができます。ワークブック全体を複数のフレームまたはページを持つ単一のTIFF画像に保存できます。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Use WorkbookRender for Image Conversion Example</title>
    </head>
    <body>
        <h1>Use WorkbookRender for Image Conversion Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, WorkbookRender, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare image/print options
            const opts = new ImageOrPrintOptions();
            opts.imageType = AsposeCells.ImageType.Tiff;

            // Create WorkbookRender and convert to image
            const workbookRender = new WorkbookRender(workbook, opts);

            // toImage may return a single Uint8Array or an array of Uint8Array pages
            const imageResult = await workbookRender.toImage();

            let imageData = imageResult;
            if (Array.isArray(imageResult) && imageResult.length > 0) {
                imageData = imageResult[0];
            }

            // Ensure imageData is a Uint8Array or ArrayBuffer
            let blob;
            if (imageData instanceof Uint8Array || imageData instanceof ArrayBuffer) {
                blob = new Blob([imageData], { type: 'image/tiff' });
            } else {
                // Fallback: try to stringify/convert if possible
                blob = new Blob([imageData], { type: 'application/octet-stream' });
            }

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputUseWorkbookRenderForImageConversion.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted TIFF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image conversion completed! Click the download link to get the TIFF file.</p>';
        });
    </script>
</html>
```
