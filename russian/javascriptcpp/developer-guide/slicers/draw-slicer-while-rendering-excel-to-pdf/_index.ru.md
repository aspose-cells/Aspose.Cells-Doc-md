---
title: Нарисуйте фильтр при рендеринге Excel в PDF
type: docs
weight: 60
url: /ru/javascript-cpp/draw-slicer-while-rendering-excel-to-pdf/
---

## **Нарисуйте фильтр при рендеринге Excel в PDF**
Если у вас есть файл Excel, в котором применяется фильтр с помощью слайсера, и вы хотите экспортировать Excel в PDF с учетом настроек слайсера, Aspose.Cells for JavaScript через C++ теперь поддерживает это по умолчанию. Просто экспортируйте файл Excel с слайсером в PDF, и сгенерированный PDF покажет примененный слайсер.

Следующий образец кода загружает [образец файла Excel](94044165.xlsx), содержащий существующую срезку. Затем он сохраняет книгу как [выходной файл PDF](94044166.pdf). На следующем скриншоте сравниваются исходный файл Excel и сгенерированный файл PDF.

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **Образец кода**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as PDF</title>
    </head>
    <body>
        <h1>Save Excel as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleSlicerChart.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
