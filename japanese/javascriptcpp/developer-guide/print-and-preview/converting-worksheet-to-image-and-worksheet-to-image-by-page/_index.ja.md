---
title: JavaScriptをC++経由で使用して、ワークシートを画像に変換およびページごとに画像化します。
linktitle: ワークシートを画像に変換し、ページごとにワークシートを画像に変換
type: docs
weight: 80
url: /ja/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}
このドキュメントは、開発者に対し、ワークシートを画像ファイルに変換し、複数ページのワークシートをページごとに画像化する方法について詳しく解説します。

時には、アプリケーションやWebページでワークシートを画像として表示する必要があります。たとえば、その画像をWord文書、PDFファイル、PowerPointプレゼンテーションに挿入したり、他のシナリオで使用する必要があるかもしれません。単純に言えば、ワークシートを画像としてレンダリングしたいと思います。Aspose.Cellsは、Microsoft Excelファイルのワークシートを画像に変換することをサポートしています。また、Aspose.Cellsは、ワークブックを複数のページごとに1つの画像ファイルに変換することもサポートしています。

これを達成するためには、Office Automationを使用することができますが、Office Automationには独自の欠点があります。セキュリティ、安定性、拡張性/処理速度、価格、機能など、いくつかの理由や問題があります。簡単に言えば、多くの理由がありますが、その中でも主な理由の1つは、Microsoft自体がOffice Automationを強く推奨していないことです。
{{% /alert %}}

## **Aspose.Cells for JavaScriptをC++経由で使用してワークシートを画像ファイルに変換します。**

この解説では、シンプルなコード行数でAspose.Cells APIを使用して、コンソールアプリケーションを作成し、ワークシートを画像に変換し、各ワークシートを一つの画像に変換する方法を示します。

レンダリング機能に関連するいくつかの価値のあるクラスをプログラムまたはプロジェクトにインポートする必要があります。例として[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/)、[**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender/)などがあります。[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/)クラスは画像をレンダリングするワークシートを表し、オーバーロードされた[**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)メソッドを持ち、任意の属性やオプションを設定してワークシートを画像ファイルに直接変換できます。画像オブジェクトを返し、画像ファイルをディスクまたはストリームに保存可能です。サポートされる画像形式にはBMP、PNG、GIF、JPG、JPEG、TIFF、EMFなどがあります。

この記事では以下の方法について説明します:

- ワークシートを画像に変換する
- ワークシートの各ページを画像に変換する

このタスクでは、Aspose.Cellsを使用して、テンプレートワークブックからワークシートを画像ファイルに変換する方法を示します。

### **プロジェクトのセットアップ**

1. まず、[Aspose.Cells for JavaScriptをC++経由でダウンロード](https://downloads.aspose.com/cells/javascript-cpp)します。
1. 開発コンピュータにインストールします。すべての[Aspose](http://www.aspose.com/)コンポーネントは、インストール時に評価モードで動作します。評価モードには時間制限がなく、生成されたドキュメントにウォーターマークのみが挿入されます。次に開発環境を起動し、新しいコンソールアプリケーションを作成します。この例はJavaScriptコンソールアプリケーションですが、JavaScriptと連携する任意の環境を使用できます。作成したプロジェクトにAspose.Cellsを参照として追加してください。

### **ワークシートを画像ファイルに変換**

Microsoft Excelで新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました：**Testbook.xlsx**（1つのワークシート）。次に、テンプレートファイルのワークシートSheet1をSheetImage.jpgという画像ファイルに変換します。

コンポーネントがタスクを達成するために使用したコードは以下の通りです。**Testbook.xlsx**のSheet1を画像ファイルに変換し、この変換がどれほど簡単であるかを説明します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Convert Worksheet to Image Example</title>
    </head>
    <body>
        <h1>Convert Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

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

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.onePagePerSheet = true;

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Generate the image data for the first page (index 0)
            const outputData = sr.toImage(0);

            // Create a blob and provide a download link
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputConvertWorksheettoImageFile.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet converted to image successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```

## **Aspose.Cells for JavaScriptをC++経由で使用し、ページごとのワークシートを画像ファイルに変換します。**

この例では、Aspose.Cellsを使用して、複数のページを持つテンプレートワークブックからワークシートを1つの画像ファイルに変換する方法を示します。

### **ページ単位でシートを画像に変換**

私はMicrosoft Excelで新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました: **Testbook2.xlsx** (1 ワークシート)。

これで、テンプレートファイルのワークシート Sheet1 を画像ファイルに変換します（1ページごとのファイル）。すでにコンソールアプリケーションを作成してコピー作業を行う準備ができているため、コンソールアプリケーションの作成手順をスキップして、直接ワークシートの変換手順に移ります。

以下は、そのタスクを実現するためにコンポーネントが使用するコードです。Testbook2.xlsxのSheet1をページごとに画像ファイルに変換します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Worksheet to Images By Page</title>
    </head>
    <body>
        <h1>Convert Worksheet to Images By Page</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div id="downloadLinks"></div>
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
            const resultDiv = document.getElementById('result');
            const linksDiv = document.getElementById('downloadLinks');
            linksDiv.innerHTML = '';
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Create image/print options and set properties
            const options = new ImageOrPrintOptions();
            options.horizontalResolution = 200;
            options.verticalResolution = 200;
            options.imageType = ImageType.Tiff;

            // Sheet to Image By Page conversion
            const sr = new SheetRender(sheet, options);

            const pageCount = sr.pageCount;
            const createdLinks = [];

            for (let j = 0; j < pageCount; j++) 
            {
                // toImage returns image data for the specified page
                const outputData = sr.toImage(j);
                const blob = new Blob([outputData], { type: 'image/tiff' });
                const url = URL.createObjectURL(blob);
                const link = document.createElement('a');
                const pageNumber = j + 1;
                const fileName = 'outputConvertWorksheetToImageByPage_' + pageNumber + '.tif';
                link.href = url;
                link.download = fileName;
                link.textContent = 'Download ' + fileName;
                link.style.display = 'block';
                linksDiv.appendChild(link);
                createdLinks.push(url);
            }

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed! Click the links below to download the generated TIFF images.</p>';
        });
    </script>
</html>
```
