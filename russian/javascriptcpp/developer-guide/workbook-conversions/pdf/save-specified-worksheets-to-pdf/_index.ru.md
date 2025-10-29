---
title: Сохраните указанные листы в PDF с помощью JavaScript на C++
linktitle: Сохранить указанные листы в формат PDF
type: docs
weight: 140
url: /ru/javascript-cpp/save-specified-worksheets-to-pdf/
description: Узнайте, как сохранить указанные листы в PDF с помощью Script Aspose.Cells for Java на C++. 
---

По умолчанию, Aspose.Cells сохраняет все **видимые** листы книги в PDF-файл. С помощью [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--) можно сохранить указанные листы в PDF. Например, можно сохранить активный лист в PDF, все листы (и видимые, и скрытые) в PDF, или выбрать несколько листов для сохранения в PDF.

## **Сохранить активный лист в формат PDF**

Если нужно сохранить только активный лист, это можно сделать, передав [**SheetSet.active**](https://reference.aspose.com/cells/javascript-cpp/sheetset/#active--) в опцию [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--).

Лист `Sheet2` является активным листом исходного файла [sheetset-example.xlsx](sheetset-example.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells SheetSet to PDF Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>SheetSet to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, SheetSet } = AsposeCells;

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

            // Prepare PdfSaveOptions and set active sheet set
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.sheetSet = SheetSet.active;

            // Save workbook to PDF using PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

## **Сохранить все листы в PDF**

[**SheetSet.visible**](https://reference.aspose.com/cells/javascript-cpp/sheetset/#visible--) обозначает видимые листы в книге, а [**SheetSet.all**](https://reference.aspose.com/cells/javascript-cpp/sheetset/#all--) — все листы, включая скрытые/невидимые. Если хотите экспортировать все листы в PDF, просто передайте  [**SheetSet.all**](https://reference.aspose.com/cells/javascript-cpp/sheetset/#all--) в опцию [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--).

Исходный файл [sheetset-example.xlsx](sheetset-example.xlsx) содержит все четыре листа с скрытым листом `Sheet3`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: SheetSet to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, SheetSet, Utils } = AsposeCells;

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

            // Open the template excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set all sheets to output
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.sheetSet = SheetSet.all;

            // Save the pdf file with PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

## **Сохранить указанные листы в формат PDF**

Для экспорта нужных/кастомных нескольких листов в PDF, передайте несколько индексов листов в опцию [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Specific Sheets to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SheetSet, SaveFormat, Utils } = AsposeCells;

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

            // Opening the Excel file through the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set custom multiple sheets (Sheet1, Sheet3) to output
            const sheetSet = new SheetSet([0, 2]);
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.sheetSet = sheetSet;

            // Save the pdf file with PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

## **Переупорядочить листы в PDF**

Если хотите упорядочить листы (например, в обратном порядке) для экспорта в PDF без изменения исходного файла, сделайте это, передав переупорядоченные индексы листов в опцию [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>SheetSet to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, SheetSet, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Reorder sheets(Sheet1, Sheet2, Sheet3, Sheet4) to sheets(Sheet4, Sheet3, Sheet2, Sheet1)
            const sheetSet = new SheetSet([3, 2, 1, 0]);
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.sheetSet = sheetSet;

            // Save the pdf file with PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}} 

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}
