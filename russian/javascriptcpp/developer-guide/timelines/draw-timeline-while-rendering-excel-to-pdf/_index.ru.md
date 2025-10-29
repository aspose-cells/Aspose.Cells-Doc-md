---
title: Отрисовка временной шкалы при отображении Excel в PDF с помощью JavaScript через C++
linktitle: Отображение временной шкалы при преобразовании Excel в PDF
type: docs
weight: 60
url: /ru/javascript-cpp/draw-timeline-while-rendering-excel-to-pdf/
description: Управление временными шкалами Excel файлов с помощью Aspose.Cells for JavaScript через C++.
keywords: Отрисовка временной шкалы в PDF без Office 2013, Office 2016, Office 2019 и Office 365 JavaScript через C++
---

## **Отображение временной шкалы при преобразовании Excel в PDF**
Если у вас есть Excel-файл с примененной временной шкалой, и вы хотите экспортировать его в PDF с сохранением настроек временной шкалы, Aspose.Cells for JavaScript через C++ это теперь поддерживает по умолчанию. Просто экспортируйте Excel-файл с временной шкалой в PDF, и созданный PDF будет отображать временную шкалу.

Приведенный ниже образец кода загружает [образец Excel-файла](input.xlsx), содержащий существующую временную шкалу. Затем он сохраняет книгу как [файл PDF на выходе](out.pdf). На следующем снимке экрана сравниваются исходный файл Excel и сгенерированный PDF-файл.

<img src="out.png" width="60%">

## **Образец кода**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Saving the workbook to PDF format (browser)
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
