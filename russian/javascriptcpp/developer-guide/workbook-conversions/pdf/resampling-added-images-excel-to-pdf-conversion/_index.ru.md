---
title: Пересэмплирование добавленных изображений — преобразование Excel в PDF с помощью JavaScript через C++
linktitle: Повторное изменение размера добавленных изображений
type: docs
weight: 150
url: /ru/javascript-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Узнайте, как сжать добавленные изображения в Excel файлах для уменьшения размера PDF и повышения производительности преобразования с помощью Script Aspose.Cells for Java через C++.
---

{{% alert color="primary" %}}

При работе с крупными файлами Microsoft Excel с множеством изображений, возможно, потребуется сжать изображения, чтобы уменьшить размер конечного файла PDF и повысить производительность преобразования. Script Aspose.Cells for Java через C++ поддерживает пересэмплирование добавленных изображений для уменьшения размера PDF и немного улучшения производительности.

{{% /alert %}}

Пожалуйста, ознакомьтесь с приведенным ниже образцом кода, описывающим, как выполнить задачу с использованием API Aspose.Cells. В примере происходит преобразование файла Microsoft Excel в файл PDF с одновременным сжатием изображений в файле.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Excel to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Initialize a new Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate the PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set Image Resample properties (converted from setImageResample(300, 70))
            // Universal setter->property conversion: setImageResample(...) -> imageResample = [...]
            pdfSaveOptions.imageResample = [300, 70];

            // Save the PDF file (returns binary data)
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile_out_pdf.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Использование опции [**imageResample(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#imageResample-number-number-) минимизирует размер выходного PDF, но может немного повлиять на качество изображения.

{{% /alert %}} {{% alert color="primary" %}}

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}
