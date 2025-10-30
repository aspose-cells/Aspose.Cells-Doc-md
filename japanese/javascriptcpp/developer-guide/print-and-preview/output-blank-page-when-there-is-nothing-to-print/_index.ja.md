---
title: JavaScriptをC++経由で使用して、印刷する内容がない場合に空白ページを出力します
linktitle: 空白ページを出力する。印刷するものがない場合
type: docs
weight: 90
url: /ja/javascript-cpp/output-blank-page-when-there-is-nothing-to-print/
---

## **可能な使用シナリオ**

シートが空の場合、Aspose.Cellsは何も印刷しません。この挙動を変更するには、[**ImageOrPrintOptions.outputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#outputBlankPageWhenNothingToPrint--)プロパティを使用します。これを**true**に設定すると、空白ページが印刷されます。

## **印刷するものがない場合、空白ページを出力**

以下のサンプルコードは、空のワークブックと空のワークシートを作成し、[**ImageOrPrintOptions.outputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#outputBlankPageWhenNothingToPrint--)プロパティを**true**に設定した後、空のワークシートを画像にレンダリングします。その結果、何も印刷するものがないため空白ページが生成されます。これは以下の画像で確認できます。

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render Blank Sheet to PNG</title>
    </head>
    <body>
        <h1>Render Blank Sheet to PNG</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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

            // Create or load workbook: if a file is provided, open it; otherwise create a new blank workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet - it is empty sheet for a new workbook or first sheet of provided workbook
            const ws = workbook.worksheets.get(0);

            // Specify image or print options
            // Since the sheet may be blank, set outputBlankPageWhenNothingToPrint to true
            const opts = new ImageOrPrintOptions();
            opts.imageType = ImageType.Png;
            opts.outputBlankPageWhenNothingToPrint = true;

            // Render empty sheet to png image
            const sr = new SheetRender(ws, opts);
            const imgData = sr.toImage(0);

            // Create downloadable blob and link
            const blob = new Blob([imgData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputBlankPageWhenNothingToPrint.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PNG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the PNG file.</p>';
        });
    </script>
</html>
```
