---
title: PdfSaveOptionsとImageOrPrintOptionsのDefaultFontプロパティをJavaScriptを使ってC++経由で優先的に設定する
linktitle: PdfSaveOptionsおよびImageOrPrintOptionsのDefaultFontプロパティを設定し、優先度を持たせます。
type: docs
weight: 30
url: /ja/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Aspose.Cells for JavaScriptを用いてC++でPdfSaveOptionsとImageOrPrintOptionsのDefaultFontプロパティを設定する方法を発見し、フォントの欠落時の適切なレンダリングを確保します。
---

## **可能な使用シナリオ**

[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) および [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) の **DefaultFont** プロパティを設定する際には、フォントが見つからない（インストールされていない）場合に、ワークブック全体のテキストにそのDefaultFontを設定すると期待されるかもしれません。

一般的に、PDFまたは画像に保存する場合、C++を通じてAspose.Cells for JavaScriptは最初にワークブックのデフォルトフォント（`Workbook.DefaultStyle.Font`）を設定しようとします。ワークブックのデフォルトフォントが依然としてテキストを正しく表示/レンダリングできない場合、Aspose.Cellsは[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions)のDefaultFont属性に記載されたフォントでレンダリングを試みます。 

この期待に対処するために、[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) には "**CheckWorkbookDefaultFont**" というブール型のプロパティがあります。このプロパティを **false** に設定すると、ワークブックのデフォルトのフォントを試行しないようになり、また [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) のDefaultFont設定が優先されます。

## **PdfSaveOptions/ImageOrPrintOptionsのDefaultFontプロパティを設定します**

次のサンプルコードはExcelファイルを開きます。最初のシートのセルA1には"Christmas Time Font text"というテキストが設定されており、フォント名は"Christmas Time Personal Use"ですが、これはインストールされていません。[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/)の**DefaultFont**属性を"Times New Roman"に設定し、**CheckWorkbookDefaultFont**ブール型プロパティを**"false"**に設定することで、A1セルのテキストを"Times New Roman"フォントでレンダリングし、Workbookのデフォルトフォント（"Calibri"）を使用しないようにします。このコードは最初のシートをPNGとTIFF画像フォーマットにレンダリングし、最後にPDFに出力します。

{{% alert color="primary" %}}

**CheckWorkbookDefaultFont**属性のデフォルト値は**true**です。

{{% /alert %}}

これは、例コードで使用されている [テンプレートファイル](49446913.xlsx)のスクリーンショットです。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

[**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--)プロパティを"Times New Roman"に設定した後の出力PNG画像例です。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

[**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--)プロパティを"Times New Roman"に設定した後の出力[TIF](48496672.tiff)画像を確認してください。

[**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--)プロパティを「Times New Roman」に設定した後の出力[PDF](48496673.pdf)ファイルを参照してください。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Default Font for Export (PNG, TIFF, PDF)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadPng" style="display: none;">Download PNG</a><br/>
            <a id="downloadTiff" style="display: none;">Download TIFF</a><br/>
            <a id="downloadPdf" style="display: none;">Download PDF</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, ImageType, SheetRender, WorkbookRender, PdfSaveOptions } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Rendering to PNG while setting checkWorkbookDefaultFont = false and defaultFont to Times New Roman
            const imgOpt = new ImageOrPrintOptions();
            imgOpt.imageType = ImageType.Png;
            imgOpt.checkWorkbookDefaultFont = false;
            imgOpt.defaultFont = "Times New Roman";

            const sr = new SheetRender(workbook.worksheets.get(0), imgOpt);
            const pngData = sr.toImage(0);
            const pngBlob = new Blob([pngData], { type: 'image/png' });
            const downloadPng = document.getElementById('downloadPng');
            downloadPng.href = URL.createObjectURL(pngBlob);
            downloadPng.download = 'out1_imagePNG.png';
            downloadPng.style.display = 'inline-block';
            downloadPng.textContent = 'Download PNG';

            // Rendering to TIFF while setting checkWorkbookDefaultFont = false and defaultFont to Times New Roman
            imgOpt.imageType = ImageType.Tiff;
            const wr = new WorkbookRender(workbook, imgOpt);
            const tiffData = wr.toImage();
            const tiffBlob = new Blob([tiffData], { type: 'image/tiff' });
            const downloadTiff = document.getElementById('downloadTiff');
            downloadTiff.href = URL.createObjectURL(tiffBlob);
            downloadTiff.download = 'out1_imageTIFF.tiff';
            downloadTiff.style.display = 'inline-block';
            downloadTiff.textContent = 'Download TIFF';

            // Rendering to PDF while setting the default font and checkWorkbookDefaultFont
            const saveOptions = new PdfSaveOptions();
            saveOptions.defaultFont = "Times New Roman";
            saveOptions.checkWorkbookDefaultFont = false;
            const pdfData = workbook.save(SaveFormat.Pdf, saveOptions);
            const pdfBlob = new Blob([pdfData], { type: 'application/pdf' });
            const downloadPdf = document.getElementById('downloadPdf');
            downloadPdf.href = URL.createObjectURL(pdfBlob);
            downloadPdf.download = 'out1_pdf.pdf';
            downloadPdf.style.display = 'inline-block';
            downloadPdf.textContent = 'Download PDF';

            resultEl.innerHTML = '<p style="color: green;">Export completed. Click the links above to download the generated files.</p>';
        });
    </script>
</html>
```
