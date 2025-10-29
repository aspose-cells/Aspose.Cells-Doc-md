---
title: Игнорировать ошибки при рендеринге Excel в PDF с помощью JavaScript через C++
linktitle: Игнорировать ошибки при преобразовании Excel в PDF
type: docs
weight: 80
url: /ru/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Узнайте, как игнорировать ошибки при конвертации файлов Excel в PDF с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**  

 Иногда при конвертации файла Excel в PDF возникают ошибки или исключения, и процесс конвертации прекращается. Вы можете игнорировать все такие ошибки во время конвертации, используя свойство [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--). Таким образом, процесс конвертации завершится гладко без выброса ошибок или исключений, но возможна потеря данных. Поэтому используйте это свойство только в случае, если потеря данных для вас не критична.  

## **Игнорировать ошибки при преобразовании Excel в PDF**  

Следующий код загружает [образец файла Excel](55541778.xlsx), но этот файл содержит ошибки и вызывает ошибку при [преобразовании в PDF](55541779.pdf) в 17.11. Однако, поскольку мы используем свойство [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--), ошибка не возникает. Однако одна *округлая красная стрелка*, как показано на скриншоте, теряется.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Excel to PDF (Ignore Errors) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF (Ignore Errors)</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Pdf Save Options - Ignore Error
            const opts = new PdfSaveOptions();
            opts.ignoreError = true;

            // Save the Workbook in Pdf with Pdf Save Options
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputErrorExcel2Pdf.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
