---
title: Ограничение количества страниц при преобразовании Excel в PDF с помощью JavaScript через C++
linktitle: Ограничение количества сгенерированных страниц при преобразовании Excel в PDF
type: docs
weight: 180
url: /ru/javascript-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Узнайте, как ограничить количество создаваемых страниц при конвертации электронной таблицы Excel в PDF с помощью Aspose.Cells for JavaScript через C++. 
---

{{% alert color="primary" %}}

 Иногда вы хотите распечатать диапазон страниц в выводящий PDF-файл. Aspose.Cells for JavaScript через C++ обеспечивает возможность установки лимита на количество страниц при конвертации электронной таблицы Excel в формат PDF.

{{% /alert %}}

## **Ограничение количества сгенерированных страниц**

В следующем примере показано, как отображать диапазон страниц (3 и 4) в файле Microsoft Excel в формате PDF.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PDF Export Example</title>
    </head>
    <body>
        <h1>Export Specific Pages to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Open an Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate the PdfSaveOption
            const options = new PdfSaveOptions();

            // Print only Page 3 and Page 4 in the output PDF
            // Starting page index (0-based index)
            options.pageIndex = 3;
            // Number of pages to be printed
            options.pageCount = 2;

            // Save the PDF file
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outPDF1.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

 Если в таблице есть формулы, лучше всего вызвать [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) непосредственно перед рендерингом в PDF. Это гарантирует, что значения, зависящие от формул, будут перерасчитаны, и в выходном файле будут отображаться правильные значения.

{{% /alert %}}
