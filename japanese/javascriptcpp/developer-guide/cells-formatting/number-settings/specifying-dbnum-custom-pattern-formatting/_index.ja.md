---
title: DBNumのカスタムパターン書式を指定する
linktitle: DBNumのカスタムパターン書式を指定する
description: Aspose.Cellsは、C++を使用したJavaScript用のライブラリで、カスタムフォーマットパターンを使用した日付と数字の書式設定をサポートします。この記事では、数値表示をよりコントロールするための dbnum カスタムフォーマットパターンの指定方法を示します。
keywords: Aspose.Cells、C++を使用したJavaScript、電子スプレッドシート、カスタムフォーマットパターン、書式設定、 dbnum 、表示コントロール
type: docs
weight: 110
url: /ja/javascript-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **可能な使用シナリオ**

C++を使用したAspose.Cells for JavaScriptは *DBNum* カスタムパターン書式設定をサポートします。例えば、セルの値が123で、そのセルの書式設定を [DBNum2][$-804]General と指定すると、壱佰弐拾参のように表示されます。セルのカスタム書式は [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) メソッドと [**Style.custom(string)**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) メソッドを使用して指定できます。

## **サンプルコード**

以下のサンプルコードは、「*DBNum*」カスタムパターンの書式設定を指定する方法を示しています。[出力PDF](43352081.pdf)もご確認ください。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - DBNum Custom Formatting Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Access cell A1 and put value 123.
            const cell = ws.cells.get("A1");
            cell.value = 123;

            // Access cell style.
            const st = cell.style;

            // Specifying DBNum custom pattern formatting.
            st.custom = "[DBNum2][$-804]General";

            // Set the cell style.
            cell.style = st;

            // Set the first column width.
            ws.cells.columns.get(0).width = 30;

            // Save the workbook in output pdf format.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDBNumCustomFormatting.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
