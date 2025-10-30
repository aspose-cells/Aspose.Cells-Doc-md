---
title: JavaScriptをC++経由でワークシートのページ設定の用紙の幅と高さを取得する
linktitle: ワークシートのページ設定の用紙幅と用紙高さを取得する方法
type: docs
weight: 50
url: /ja/javascript-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: JavaScriptをC++で使用して、Excelワークシートのページ設定の用紙の幅と高さをプログラムで取得する方法を探ります。
keywords: JavaScriptをC++で使用してExcelのページ設定の用紙の幅を取得、または用紙の高さを取得。
---

## **可能な使用シナリオ**

シートのページ設定に設定された用紙幅と高さを知る必要がある場合、このために[**PageSetup.paperWidth**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperWidth--)と[**PageSetup.paperHeight**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperHeight--)のプロパティを使用してください。

## **ワークシートのページ設定の用紙の幅と高さを取得**

次のサンプルコードは、[**PageSetup.paperWidth**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperWidth--)と[**PageSetup.paperHeight**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperHeight--)の使い方を例示しています。最初に用紙サイズを*A2*に設定し、その後用紙の幅と高さを取得します。次に*A3*、*A4*、*Letter*に変更し、それぞれの用紙の幅と高さを取得します。

### **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Paper Size Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // If a file is selected, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Set paper size to A2 and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA2;
            console.log("PaperA2: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            // Set paper size to A3 and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA3;
            console.log("PaperA3: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            // Set paper size to A4 and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA4;
            console.log("PaperA4: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            // Set paper size to Letter and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperLetter;
            console.log("PaperLetter: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            const outputLines = [
                "PaperA2: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight,
                "PaperA3: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight,
                "PaperA4: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight,
                "PaperLetter: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight
            ];

            document.getElementById('result').innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
        });
    </script>
</html>
```

### **コンソール出力**



{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
