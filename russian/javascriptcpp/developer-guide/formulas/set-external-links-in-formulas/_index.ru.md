---
title: Установка внешних связей в формулах с помощью JavaScript через C++
linktitle: Установка внешних ссылок в формулах
type: docs
weight: 20
url: /ru/javascript-cpp/set-external-links-in-formulas/
description: Узнайте, как задавать внешние связи в формулах с помощью Aspose.Cells for JavaScript через C++. 
keywords: Установка внешних связей в формулах JavaScript через C++, включение внешних файлов в формулы JavaScript через C++ 
---

{{% alert color="primary" %}} 

Иногда необходимо включать ссылки на внешние файлы в формулы, например, для оценки значения ячейки или диапазона по ним. Aspose.Cells for JavaScript через C++ предоставляет эту функцию, и в этом документе объясняется, как её использовать.

{{% /alert %}} 

Ниже приведен пример кода, показывающий, как включить внешние файлы в формулы.

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
