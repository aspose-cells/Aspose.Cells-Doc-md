---
title: Автоматическая подгонка строк при рендеринге с помощью JavaScript через C++
linktitle: Автонастройка строк для визуализации
type: docs
weight: 130
url: /ru/javascript-cpp/autofit-rows-for-rendering/
description: узнайте, как автоматически подгонять строки для рендеринга в Excel с помощью Aspose.Cells for JavaScript через C++. Предотвратите обрезку текста в сохраненных PDF файлах.
---

Обычно, чтобы отображать весь текст в ячейке, можно автоподогнать строку в нормальном режиме с масштабом 100% в Microsoft Excel. Это позволяет полностью видеть текст в обычном режиме, а при печати или сохранении файла как PDF текст отображается правильно.

Однако в некоторых случаях автоподгонка строки хорошо работает в нормальном режиме, но при переключении на режим печати или сохранении файла как PDF, текст обрезается. Проверьте исходный файл [Book1.xlsx](Book1.xlsx) и скриншоты.

![текст обрезан в виде для печати](text_clipped_in_printview.png)

Если вы хотите предотвратить обрезание текста в сохраненном PDF-файле, вы можете автоматически подогнать строку с помощью опции [AutoFitterOptions.forRendering](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#forRendering--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows and Save as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, AutoFitterOptions, SaveFormat, Utils } = AsposeCells;

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

            // Init workbook instance from uploaded file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set autofit options for rendering.
            const autoFitterOptions = new AutoFitterOptions();
            autoFitterOptions.forRendering = true;

            // Autofit rows with options on first worksheet.
            const worksheet = workbook.worksheets.get(0);
            worksheet.autoFitRows(autoFitterOptions);

            // Save to pdf.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

Теперь текст не обрезается в сохраненном файле PDF.

![текст не обрезается в сохраненном pdf](text_not_clipped_in_saved_pdf.png)
