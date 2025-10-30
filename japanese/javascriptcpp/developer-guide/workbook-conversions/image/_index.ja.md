---
title: JavaScriptを使った画像処理 via C++
linktitle: 画像
type: docs
weight: 300
url: /ja/javascript-cpp/convert-excel-to-image/
---

{{% alert color="primary" %}}  
Aspose.Cellsでは、ワークブックからワークシートをエクスポートし、異なる形式に変換することができます。この記事ではワークシートを異なる形式に変換する方法について説明します。  
{{% /alert %}}  

## ワークブックをTIFF形式に変換  

 Excelファイルは複数のシートとページを含むことができます。[**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender)を使用してExcelをTIFFに変換し、複数ページを作成します。また、[ImageOrPrintOptions.tiffCompression](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#tiffCompression--)、[ImageOrPrintOptions.tiffColorDepth](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#tiffColorDepth--)、解像度（[ImageOrPrintOptions.horizontalResolution](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#horizontalResolution--)、[ImageOrPrintOptions.verticalResolution](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#verticalResolution--)）などのTIFF設定を制御できます。  

次のコードスニペットは、Excelを複数ページのTIFFに変換する方法を示しています。[元のExcelファイル](workbook-to-tiff-with-mulitiple-pages.xlsx)と[生成されたTIFF画像](workbook-to-tiff-with-mulitiple-pages.tiff)を参照できます。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Workbook to TIFF (Multiple Pages) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, TiffCompression, WorkbookRender } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Configure image/print options
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.imageType = ImageType.Tiff;
            imgOptions.horizontalResolution = 200;
            imgOptions.verticalResolution = 200;
            imgOptions.tiffCompression = TiffCompression.CompressionLZW;

            // Render workbook to image (TIFF)
            const workbookRender = new WorkbookRender(wb, imgOptions);

            // Obtain image data (multi-page TIFF)
            const outputData = workbookRender.toImage();

            const blob = new Blob([outputData], { type: "image/tiff" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'workbook-to-tiff-with-mulitiple-pages.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">TIFF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **ワークシートをイメージに変換**  

ワークシートには分析したいデータが含まれています。 例えば、ワークシートにはパラメータ、合計、パーセンテージ、例外、計算などが含まれることがあります。  

開発者として、ワークシートを画像として表示する必要があるかもしれません。例えば、アプリケーションやウェブページで画像として使用することができます。Microsoft Word文書、PDFファイル、PowerPointプレゼンテーション、または他のドキュメントタイプに画像を挿入したい場合です。要するに、ワークシートを画像としてレンダリングし、別の場所で使用したいのです。  

[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender)
[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions)
[**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender)

[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender)クラスは、画像としてレンダリングするワークシートを表します。異なる属性やオプションを持つワークシートを画像ファイルに変換できるオーバーロードされた[**SheetRender.toImage(number, string)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-string-)メソッドがあります。バッファーオブジェクトを返し、画像ファイルをディスクに保存したりストリームしたりできます。サポートされている画像フォーマットにはBMP、PNG、GIF、JPG、JPEG、TIFF、EMFがあります。  

次のコードスニペットは、Excelファイルのワークシートを画像ファイルに変換する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Worksheet To Images By Page</title>
    </head>
    <body>
        <h1>Convert Worksheet To Images By Page</h1>
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
            const resultDiv = document.getElementById('result');
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

            // Preparing image/print options
            const options = new ImageOrPrintOptions();
            options.horizontalResolution = 200;
            options.verticalResolution = 200;
            options.imageType = ImageType.Tiff;

            // Sheet to Image By Page conversion
            const sr = new SheetRender(sheet, options);
            const pageCount = sr.pageCount;

            if (pageCount === 0) {
                resultDiv.innerHTML = '<p style="color: red;">No pages found to render.</p>';
                return;
            }

            const linksContainer = document.createElement('div');
            linksContainer.innerHTML = '<p style="color: green;">Conversion completed. Download the generated images below:</p>';
            for (let j = 0; j < pageCount; j++) 
            {
                // sr.toImage(pageIndex) returns image bytes in browser build
                const imageData = sr.toImage(j);
                const blob = new Blob([imageData], { type: 'image/tiff' });
                const url = URL.createObjectURL(blob);

                const link = document.createElement('a');
                link.href = url;
                link.download = "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif";
                link.textContent = "Download Image Page " + (j + 1);
                link.style.display = 'block';
                linksContainer.appendChild(link);
            }

            resultDiv.appendChild(linksContainer);
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
現在、ワークシートを画像に変換するAPIは3Dバブルチャートをサポートしていません。  
{{% /alert %}}  

## **ワークシートをSVGに変換**  

SVGはScalable Vector Graphicsの略です。 SVGは、二次元ベクトルグラフィックのためのXML標準に基づいた仕様です。 1999年以来、World Wide Web Consortium（W3C）によって開発されてきたオープンな標準です。  

C++を使用したAspose.Cells for JavaScriptは、バージョン7.1.0以降、ワークシートをSVG画像に変換できるようになりました。以下のコードスニペットは、Excelファイル内のワークシートをSVG画像ファイルに変換する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Worksheet to SVG Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SheetType } = AsposeCells;

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
            // Instantiate a workbook
            const workbook = new Workbook();

            // Put sample text in the first cell of the first worksheet in the newly created workbook
            workbook.worksheets.get(0).cells.get("A1").putValue("DEMO TEXT ON SHEET1");

            // Add second worksheet in the workbook
            workbook.worksheets.add(SheetType.Worksheet);

            // Set text in the first cell of the second sheet
            workbook.worksheets.get(1).cells.get("A1").putValue("DEMO TEXT ON SHEET2");

            // Set currently active sheet index to 1 i.e. Sheet2
            workbook.worksheets.activeSheetIndex = 1;

            // Save workbook to SVG. It shall render the active sheet only to SVG
            const outputData = workbook.save(SaveFormat.Svg);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertWorksheetToSVG_out.svg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download SVG File';

            document.getElementById('result').innerHTML = '<p style="color: green;">SVG generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **高度なトピック**  
- [Excelのチャートを画像に変換](/cells/ja/javascript-cpp/convert-an-excel-chart-to-image/)  
- [SVG形式でチャートを画像に変換](/cells/ja/javascript-cpp/converting-chart-to-image-in-svg-format/)  
- [viewBox属性を使用してチャートをSVGにエクスポート](/cells/ja/javascript-cpp/export-chart-to-svg-with-viewbox-attribute/)  
- [ExcelからTIFFへの変換の進行状況を追跡](/cells/ja/javascript-cpp/track-conversion-progress-of-excel-to-tiff/)
