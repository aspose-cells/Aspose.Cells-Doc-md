---
title: Визуализировать сплошные линий сетки при преобразовании Excel в PDF с помощью JavaScript через C++
linktitle: Отрисовка сплошной сетки при преобразовании Excel в PDF
type: docs
weight: 390
url: /ru/javascript-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Узнайте, как отображать сплошные линии сетки при преобразовании Excel в PDF с использованием Script Aspose.Cells for Java через C++. 
keywords: Визуализировать сплошные линии сетки в PDF JavaScript через C++, преобразовать Excel в PDF со сплошной линией сетки JavaScript через C++, PdfSaveOptions для сплошных линий сетки JavaScript через C++ 
---

Для совместимости с более старыми версиями Aspose.Cells по умолчанию рисует сетки пунктирными линиями при преобразовании Excel в PDF. Однако современные Excel отображают сетки как сплошные линии.

С опцией [PdfSaveOptions.gridlineTypes](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions), Script Aspose.Cells for Java через C++ может также отображать линии сетки как сплошные линии.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Generate PDF with Gridlines</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
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

            // Loads the workbook which contains hidden external links (as in original JavaScript example)
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an empty Workbook
            const wb = new Workbook();

            // Prepare data
            const worksheet = wb.worksheets.get(0);
            const cell = worksheet.cells.get("D9");
            cell.value = "gridline";

            // Enable to print gridline
            worksheet.pageSetup.printGridlines = true;

            // Set to render gridline as solid line
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.gridlineType = AsposeCells.GridlineType.Hair;

            // Save the pdf file with PdfSaveOptions
            const outputData = wb.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'test_Cs.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

![solid-gridline.png](solid-gridline.png)
