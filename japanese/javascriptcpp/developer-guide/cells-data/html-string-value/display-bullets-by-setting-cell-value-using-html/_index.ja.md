---
title: HTML を使用してセルの値を設定して箇条書きを表示
type: docs
weight: 130
url: /ja/javascript-cpp/display-bullets-by-setting-cell-value-using/
description: HTMLを使用してExcelセルに箇条書きを追加する、使いやすいAspose.Cells for JavaScriptをC++ API経由で使用します。
keywords: Excel JavaScriptで箇条書きを追加、表示するためにC++を使って箇条書きを追加、HTML JavaScriptを使ってExcelに箇条書きを追加、Excelで箇条書きを表示、HTML JavaScriptを使ってExcelに箇条書きを追加、HTML JavaScriptを使ってExcelで箇条書きを表示、C++を使ってExcelで箇条書きを追加します。
---

{{% alert color="primary" %}}

Aspose.CellsはHTMLコードを使用した箇条書き表示をサポートしています。この記事では、HTMLを使用してセルの値を設定することで箇条書きを表示する方法を説明します。[**Cell.htmlString(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-)メソッドを使用してHTMLを設定します。

{{% /alert %}}

## HTMLを使ってセルの値を設定し、箇条書きを表示するJavaScriptコード

以下のコードはHTMLコードを使用してセルの値を設定します。このコードを実行すると、以下の画像のような出力が得られます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Bullets In Cells</title>
    </head>
    <body>
        <h1>Bullets In Cells Example</h1>
        <p>Select an existing Excel file to modify or leave empty to create a new workbook.</p>
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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set the HTML string (converted from setHtmlString -> htmlString property)
            cell.htmlString = "<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'>Text 1 </font><font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font><font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 2 </font><font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font><font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 3 </font><font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font><font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 4 </font>";

            // Auto fit the Columns
            worksheet.autoFitColumns();

            // Save the workbook to a Blob and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'BulletsInCells_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File: BulletsInCells_out.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## サンプルコードによって生成された出力

上記のサンプルコードの出力を以下のスクリーンショットで示します。

![todo:image_alt_text](display-bullets-by-setting-cell-value-using-html_1.png)
