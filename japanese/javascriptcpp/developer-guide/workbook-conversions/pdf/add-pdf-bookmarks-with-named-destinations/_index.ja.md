---
title: JavaScript経由のC++を使用してPDFのしおりに名前付きリンク先を追加
linktitle: 名前付き目次でPDFブックマークを追加する
type: docs
weight: 20
url: /ja/javascript-cpp/add-pdf-bookmarks-with-named-destinations/
description: Aspose.Cells for JavaScriptを使用して、名前付きリンク先付きのPDFブックマークの追加方法を学ぶ。ページの変更に関係なくブックマークが維持されることを確認してください。
---

## **可能な使用シナリオ**

名前付き目次はPDFページに依存しないPDF内のブックマークまたはリンクの特別な種類です。つまり、PDFにページが追加または削除されても、ブックマークは無効になる可能性がありますが、名前付き目次はそのままです。名前付き目次を作成するには、[**PdfBookmarkEntry.destinationName**](https://reference.aspose.com/cells/javascript-cpp/pdfbookmarkentry/#destinationName--)プロパティを設定してください。

## **名前付き目次でPDFブックマークを追加する**

以下のサンプルコードとその[ソースExcelファイル](50528348.xlsx)、[出力PDFファイル](50528349.pdf)を参照してください。スクリーンショットには、出力PDF内のブックマークと名前付きデスティネーションが表示されます。スクリーンショットには、名前付きデスティネーションの表示方法と、Acrobat Readerのプロフェッショナルバージョンが必要であることが記載されています。

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PDF Bookmark Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PDF Bookmark Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfBookmarkEntry, PdfSaveOptions } = AsposeCells;

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

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell C5
            let cell = worksheet.cells.get("C5");

            // Create Bookmark and Destination for this cell
            const bookmarkEntry = new PdfBookmarkEntry();
            bookmarkEntry.text = "Text";
            bookmarkEntry.destination = cell;
            bookmarkEntry.destinationName = "AsposeCells--" + cell.name;

            // Access cell G56
            cell = worksheet.cells.get("G56");

            // Create Sub-Bookmark and Destination for this cell
            const subbookmarkEntry1 = new PdfBookmarkEntry();
            subbookmarkEntry1.text = "Text1";
            subbookmarkEntry1.destination = cell;
            subbookmarkEntry1.destinationName = "AsposeCells--" + cell.name;

            // Access cell L4
            cell = worksheet.cells.get("L4");

            // Create Sub-Bookmark and Destination for this cell
            const subbookmarkEntry2 = new PdfBookmarkEntry();
            subbookmarkEntry2.text = "Text2";
            subbookmarkEntry2.destination = cell;
            subbookmarkEntry2.destinationName = "AsposeCells--" + cell.name;

            // Add Sub-Bookmarks in list
            const list = [];
            list.push(subbookmarkEntry1);
            list.push(subbookmarkEntry2);

            // Assign Sub-Bookmarks list to Bookmark Sub-Entry
            bookmarkEntry.subEntries = bookmarkEntry.subEntries || [];
            bookmarkEntry.subEntries.push(...list);

            // Create PdfSaveOptions and assign Bookmark to it
            const opts = new PdfSaveOptions();
            opts.bookmark = bookmarkEntry;

            // Save the workbook in Pdf format with given pdf save options
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputPdfBookmarkEntry_DestinationName.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to download the file.</p>';
        });
    </script>
</html>
```
