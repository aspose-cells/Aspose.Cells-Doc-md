---
title: 使用C++通过JavaScript设置公式中的外部链接
linktitle: 设置公式中的外部链接
type: docs
weight: 20
url: /zh/javascript-cpp/set-external-links-in-formulas/
description: 学习如何用C++通过Aspose.Cells for JavaScript在公式中设置外部链接。 
keywords: 用C++通过JavaScript设置公式中的外部链接，或在公式中包含外部文件 
---

{{% alert color="primary" %}} 

有时需要在公式中包含对外部文件的链接，例如，为了根据外部文件评估单元格或区域的值。C++通过Aspose.Cells for JavaScript提供了此功能，本文档说明了如何使用它。

{{% /alert %}} 

下面的示例代码显示了如何在公式中包含外部文件。

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
