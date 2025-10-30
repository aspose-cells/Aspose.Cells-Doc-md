---
title: JavaScriptを使用したドキュメント変換進行状況の追跡
linktitle: ドキュメント変換の進行状況を追跡
type: docs
weight: 970
url: /ja/javascript-cpp/track-document-conversion-progress/
description: Excelファイルのドキュメント変換進行状況をAspose.Cells for JavaScript via C++で追跡する方法を学びましょう。
---

## **可能な使用シナリオ**  

大きなExcelファイルの変換には時間がかかる場合があります。その間、単なるローディング画面の代わりにドキュメント変換の進行状況を表示して、アプリケーションの usability を向上させたい場合があります。Aspose.Cells for JavaScript via C++は、[**IPageSavingCallback**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback)インターフェースを提供することでドキュメント変換の進行状況追跡をサポートします。[**IPageSavingCallback**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback)インターフェースは、[**IPageSavingCallback.pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-)および[**IPageSavingCallback.pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-)メソッドを提供し、カスタムクラスに実装できます。また、どのページをレンダリングするか制御することも可能です（*TestPageSavingCallback* カスタムクラスの例も参考にしてください）。  

## **文書変換の進行状況を追跡する**  

次のコード例は、[ソースExcelファイル](94896151.xlsx)を読み込み、[**IPageSavingCallback**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback)インターフェースを実装した*TestPageSavingCallback*カスタムクラスを使用して、その変換進行状況をコンソールに表示するものです。  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Pages to PDF with Progress Callback</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SaveFormat } = AsposeCells;

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

        // Define TestPageSavingCallback class
        class TestPageSavingCallback {
            onPageSaving(pageIndex, fileName) {
                console.log(`Saving page ${pageIndex} to ${fileName}`);
            }
        }

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PdfSaveOptions and assign the page saving callback
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.pageSavingCallback = new TestPageSavingCallback();

            // Save workbook as PDF with options
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DocumentConversionProgress.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF conversion started/completed. Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```  

以下は、*TestPageSavingCallback*カスタムクラスのコードです。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Saving Callback Example</title>
    </head>
    <body>
        <h1>Page Saving Callback Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example (Save as PDF with Callback)</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

        class TestPageSavingCallback {
            pageStartSaving(args) {
                console.log(`Start saving page index ${args.pageIndex} of pages ${args.pageCount}`);

                // don't output pages before page index 2.
                if (args.pageIndex < 2) {
                    args.isToOutput = false;
                }
            }

            pageEndSaving(args) {
                console.log(`End saving page index ${args.pageIndex} of pages ${args.pageCount}`);

                // don't output pages after page index 8.
                if (args.pageIndex >= 8) {
                    args.hasMorePages = false;
                }
            }
        }

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

            // Create PDF save options and attach the page saving callback
            const options = new PdfSaveOptions();
            options.pageSavingCallback = new TestPageSavingCallback();

            // Save workbook as PDF with the callback applied
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **コンソール出力**  

{{< highlight java >}}  

Start saving page index 0 of pages 11</br>  
End saving page index 0 of pages 11</br>  
Start saving page index 1 of pages 11</br>  
End saving page index 1 of pages 11</br>  
Start saving page index 2 of pages 11</br>  
End saving page index 2 of pages 11</br>  
Start saving page index 3 of pages 11</br>  
End saving page index 3 of pages 11</br>  
Start saving page index 4 of pages 11</br>  
End saving page index 4 of pages 11</br>  
Start saving page index 5 of pages 11</br>  
End saving page index 5 of pages 11</br>  
Start saving page index 6 of pages 11</br>  
End saving page index 6 of pages 11</br>  
Start saving page index 7 of pages 11</br>  
End saving page index 7 of pages 11</br>  
Start saving page index 8 of pages 11</br>  
End saving page index 8 of pages 11  

{{< /highlight >}}
