---
title: JavaScriptを介したC++で指定したワークシートをPDFに保存
linktitle: 指定されたワークシートをPDFに保存する
type: docs
weight: 140
url: /ja/javascript-cpp/save-specified-worksheets-to-pdf/
description: C++を使用したAspose.Cells for JavaScriptで指定したワークシートをPDFに保存する方法を学びます。 
---

デフォルトでは、Aspose.Cellsはブック内のすべての**表示されている**ワークシートをPDFに保存します。[**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--) オプションを使用して、特定のワークシートだけをPDFに保存できます。例：アクティブなワークシートをPDFに保存、すべてのワークシート（表示および非表示）をPDFに保存、複数のカスタムワークシートをPDFに保存など。

## **アクティブワークシートをPDFに保存する**

アクティブシートのみをPDFにエクスポートしたい場合は、[**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--)に[**SheetSet.active**](https://reference.aspose.com/cells/javascript-cpp/sheetset/#active--)を渡すことで実現できます。

シート「Sheet2」は、ソースファイル[sheetset-example.xlsx](sheetset-example.xlsx)のアクティブシートです。

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

## **すべてのワークシートをPDFに保存**

[**SheetSet.visible**](https://reference.aspose.com/cells/javascript-cpp/sheetset/#visible--)はブック内の表示されているシートを示し、[**SheetSet.all**](https://reference.aspose.com/cells/javascript-cpp/sheetset/#all--)は表示・非表示に関わらずすべてのシートを含むものを示します。すべてのシートをPDFにエクスポートしたい場合は、[**SheetSet.all**](https://reference.aspose.com/cells/javascript-cpp/sheetset/#all--) を [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--) オプションに渡すだけです。

ソースファイル [sheetset-example.xlsx](sheetset-example.xlsx) には、非表示シート `Sheet3` を含むすべての4つのシートが含まれています。

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

## **指定されたワークシートをPDFに保存**

複数の目的のシートやカスタムシートをPDFにエクスポートしたい場合は、複数のシートインデックスを[**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--)に渡すことで実現できます。

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

## **ワークシートを並べ替えてPDFに変換**

ソースファイルを変更せずにシートの順序（例：逆順）を変更してPDFに出力したい場合は、並び替えたシートインデックスを [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--) オプションに渡すことで実現できます。

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

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
