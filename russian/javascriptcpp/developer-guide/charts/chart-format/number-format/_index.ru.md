---
title: Установите код формата значений серии графика с помощью JavaScript через C++
description: Узнайте, как установить код формата значений серии графика в Aspose.Cells for JavaScript через C++. Это руководство поможет вам понять, как форматировать данные вашей серии графика с помощью соответствующего кода формата, что позволит вам точно и профессионально представлять ваши данные.
keywords: Aspose.Cells for JavaScript через C++, серия графика, код формата значений, форматирование, представление данных, точность, профессионализм.
linktitle: Формат числа
type: docs
weight: 100
url: /ru/javascript-cpp/set-the-values-format-code-of-chart-series/
---

## **Возможные сценарии использования**
Вы можете установить код формата значений серии графика, используя свойство [Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--). Это свойство полезно не только для серии, основанной на диапазоне внутри листа, но и для серии, созданной с помощью массива значений.

## **Установить код формата значений серии графика**
Следующий пример кода добавляет серию в пустой график, у которого ранее не было серий. Он добавляет серию с помощью массива значений. После добавления серия форматируется с помощью кода $#,##0, используя свойство [Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--), и число 10000 превращается в $10 000. Скриншот показывает эффект этого кода на [пример Excel файла](51740712.xlsx) и [выходной Excel файл](51740713.xlsx) после выполнения.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Образец кода**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Series Example</h1>
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

                // Access first worksheet
                const worksheet = workbook.worksheets.get(0);

                // Access first chart
                const chart = worksheet.charts.get(0);

                // Add series using an array of values
                chart.nSeries.add("{10000, 20000, 30000, 40000}", true);

                // Access the series and set its values format code
                const series = chart.nSeries.get(0);
                series.valuesFormatCode = "$#,##0";

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = '51740713.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```
