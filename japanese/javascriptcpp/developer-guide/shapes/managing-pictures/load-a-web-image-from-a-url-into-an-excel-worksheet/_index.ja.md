---
title: JavaScriptを使用したC++経由でURLからExcelワークシートに画像をロード
linktitle: ExcelワークシートにURLからのWeb画像をロードする
type: docs
weight: 30
url: /ja/javascript-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: Aspose.Cells for JavaScriptをC++経由で使用し、URLからの画像を実際のExcel画像に変換する方法。
keywords: ExcelでURLから画像を表示、Excel URLから画像を表示、URLからExcelに画像を挿入、ExcelでURLを画像に変換、ExcelのURLから画像を読み込む、JavaScriptとExcel
---

## ExcelワークシートにURLからの画像をロードする

C++経由のAspose.Cells for JavaScriptは、URLからExcelワークシートに画像を簡単かつ便利にロードできる方法を提供します。この記事では、画像データをストリームにダウンロードし、Aspose.Cells APIを使用してワークシートに挿入する方法を説明します。この方法を使用すると、画像がExcelファイルの一部となり、ワークシートを開くたびに再ダウンロードされません。

## サンプルコード

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert Web Image</title>
    </head>
    <body>
        <h1>Insert Web Image into Excel</h1>
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
                // If no file provided, create a new workbook
                document.getElementById('result').innerHTML = '<p style="color: orange;">No input workbook selected. A new workbook will be created.</p>';
            }

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Ensure at least one worksheet exists
            if (workbook.worksheets.count === 0) {
                workbook.worksheets.add("Sheet1");
            }
            const worksheet = workbook.worksheets.get(0);

            // Download the image from the web
            const url = "https://www.aspose.com/Images/aspose-logo.jpg";
            const response = await fetch(url);
            if (!response.ok) {
                document.getElementById('result').innerHTML = `<p style="color: red;">Failed to download image: ${response.status} ${response.statusText}</p>`;
                return;
            }
            const imgArrayBuffer = await response.arrayBuffer();
            const imgBytes = new Uint8Array(imgArrayBuffer);

            // Insert the image into the worksheet at row 0, column 0
            worksheet.pictures.add(0, 0, imgBytes);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'webimagebook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
URLから常に最新の画像を取得したい場合があります。その場合は、[Webアドレスからリンクされた画像を挿入](/cells/ja/javascript-cpp/insert-a-linked-picture-from-web-address/)の記事の指示に従うことができます。この方法を使用すると、ワークシートを開くたびにURLから画像が読み込まれます。
{{% /alert %}}
