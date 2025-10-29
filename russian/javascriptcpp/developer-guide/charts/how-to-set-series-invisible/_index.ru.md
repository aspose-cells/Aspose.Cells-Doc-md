---
title: Как скрыть серию с помощью JavaScript через C++
linktitle: Как сделать серию невидимой
description: Узнайте, как сделать серию невидимой в диаграмме Excel с помощью Script Aspose.Cells for Java через C++. 
keywords: Диаграмма Excel, Серия, Невидимая, IsFiltered JavaScript через C++.
type: docs
weight: 74
url: /ru/javascript-cpp/how-to-set-series-invisible/
---

## Как сделать серию невидимой в диаграмме Excel

В Excel можно щёлкнуть правой кнопкой по диаграмме, выбрать "Выбрать данные", и в появившемся окне проверить или снять выделение с серии, чтобы сделать её невидимой. Вы можете скачать [пример файла](SeriesFiltered.xlsx) и работать с ним в Excel, как показано на рисунке, чтобы реализовать эту функцию. Далее мы расскажем, как достичь этого с помощью библиотеки Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## Как сделать серию невидимой с помощью Aspose.Cells 

Мы используем следующий код, чтобы сделать серию невидимой с помощью Aspose.Cells:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Modify Chart Series Color Variation</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet and its charts
            const charts = workbook.worksheets.get(0).charts;
            const chart = charts.get("Chart 1");

            // Access filtered NSeries and NSeries collections (properties instead of getters)
            const nSeriesFiltered = chart.filteredNSeries;
            const nSeries = chart.nSeries;

            // Set IsColorVaried on series (converted from setIsColorVaried to property assignment)
            nSeries.get(1).isColorVaried = true;
            nSeries.get(0).isColorVaried = true;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Вы можете получить следующий [входной файл](SeriesFiltered.xlsx) и [выходной файл](output.xlsx).

Как показано на рисунке ниже, первые две серии, которые изначально были видимы, стали невидимыми в выходном файле.
![todo:image_alt_text](output.png)
