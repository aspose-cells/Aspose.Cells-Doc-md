---
title: Вычисление функций MINIFS и MAXIFS в Excel 2016 с помощью JavaScript через C++
description: Эта статья рассказывает о том, как с помощью библиотеки Aspose.Cells вычислять функции MINIFS и MAXIFS в Microsoft Excel 2016 с помощью JavaScript через C++. Загрузите существующий Excel файл или создайте новый, затем используйте методы Aspose.Cells для вычисления этих функций и сохранения результатов на диск.
keywords: Aspose.Cells, Excel, 2016, функция MINIFS, функция MAXIFS, вычисления JavaScript через C++
type: docs
weight: 300
url: /ru/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Возможные сценарии использования**
Microsoft Excel 2016 поддерживает функции MINIFS и MAXIFS. Эти функции не поддерживаются в Excel 2013 или более ранних версиях. Скрипт Aspose.Cells for JavaScript через C++ также поддерживает вычисление этих функций. Следующий скриншот иллюстрирует использование этих функций. Пожалуйста, прочтите красные комментарии внутри скриншота, чтобы понять, как работают эти функции.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Расчет функций MINIFS и MAXIFS Excel 2016**
Следующий пример кода загружает [пример файла Excel](5115149.xlsx) и вызывает метод [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) для выполнения вычислений формулы через Aspose.Cells for JavaScript с помощью C++, а затем сохраняет результаты в [выходном PDF](5115154.pdf).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>MINIFS and MAXIFS Calculation to PDF</h1>
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

            // Load your source workbook containing MINIFS and MAXIFS functions
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Perform Aspose.Cells formula calculation
            workbook.calculateFormula();

            // Save the calculations result in pdf format
            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputMINIFSAndMAXIFS.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculation and conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
