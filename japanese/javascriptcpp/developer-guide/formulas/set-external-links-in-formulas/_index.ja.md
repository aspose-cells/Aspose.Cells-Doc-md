---
title: 外部リンクを数式に設定する方法（JavaScript を C++ で使用）
linktitle: 数式で外部リンクを設定する
type: docs
weight: 20
url: /ja/javascript-cpp/set-external-links-in-formulas/
description: JavaScript を C++ 経由で使用して、数式内に外部リンクを設定する方法を学びます。 
keywords: JavaScript を C++ 経由で使用して、数式内に外部リンクを設定したり、外部ファイルを含めたりする方法。 
---

{{% alert color="primary" %}} 

Sometimes, it is necessary to include links to external files in formulas, for example, to evaluate a cell or range value against them. Aspose.Cells for JavaScript via C++ provides this feature and this document explains how to use it.

{{% /alert %}} 

以下のサンプルコードは、数式に外部ファイルを含める方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example - Set External Formulas</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            // Use selected file name for external link reference, or default to 'book1.xlsx'
            const externalFileName = fileInput.files.length ? fileInput.files[0].name : "book1.xlsx";

            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Get first Worksheet
            const sheet = workbook.worksheets.get(0);

            // Get Cells collection
            const cells = sheet.cells;

            // Set formula with external links
            cells.get("A1").formula = `=SUM('[${externalFileName}]Sheet1'!A2, '[${externalFileName}]Sheet1'!A4)`;

            // Set formula with external links
            cells.get("A2").formula = `='[${externalFileName}]Sheet1'!A8`;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and formulas set. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
