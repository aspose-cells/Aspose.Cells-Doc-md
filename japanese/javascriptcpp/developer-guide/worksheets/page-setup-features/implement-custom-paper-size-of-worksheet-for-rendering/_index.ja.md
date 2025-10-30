---
title: JavaScriptをC++経由でレンダリング用にカスタム用紙サイズを設定する方法
linktitle: レンダリング用のワークシートのカスタム用紙サイズを実装する
type: docs
weight: 70
url: /ja/javascript-cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: この記事では、C++を通じてJavaScript APIを利用し、ExcelファイルをPDFにプログラムでレンダリングする際にカスタム用紙サイズを設定する方法を説明します。
keywords: ExcelをPDFに変換する際にカスタム用紙サイズを設定する  C++経由のJavaScript
---

## **可能な使用シナリオ**  

MS Excelには直接カスタム用紙サイズを作成するオプションはありませんが、ExcelファイルをPDFにレンダリングする際に希望のワークシートのカスタム用紙サイズを設定できます。このドキュメントでは、Aspose.Cells APIを使ったワークシートのカスタム用紙サイズの設定方法を説明します。  

## **レンダリングのためのワークシートのカスタム用紙サイズを実装する**  

Aspose.Cellsを使えば、目的の用紙サイズを設定できます。`[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/)`クラスの[**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#customPaperSize-number-number-)メソッドを使ってカスタムページサイズを指定してください。以下のサンプルコードは、ブック内の最初のワークシートにカスタム用紙サイズを指定する例です。参考用に、次のコードで生成された[出力PDF](45056028.pdf)もご覧ください。  

## **スクリーンショット**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Custom PDF Paper Size Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
                // If no file provided, create a new workbook as in the original JavaScript example
                const wb = new Workbook();

                // Access first worksheet
                const ws = wb.worksheets.get(0);

                // Set custom paper size in unit of inches
                ws.pageSetup.customPaperSize(6, 4);

                // Access cell B4
                const b4 = ws.cells.get("B4");

                // Add the message in cell B4
                b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

                // Save the workbook in pdf format
                const outputData = wb.save(SaveFormat.Pdf);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'outputCustomPaperSize.pdf';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download PDF File';

                document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
                return;
            }

            // If a file is provided, open it and apply the same operations
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Set custom paper size in unit of inches
            ws.pageSetup.customPaperSize(6, 4);

            // Access cell B4
            const b4 = ws.cells.get("B4");

            // Add the message in cell B4
            b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

            // Save the workbook in pdf format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCustomPaperSize.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
