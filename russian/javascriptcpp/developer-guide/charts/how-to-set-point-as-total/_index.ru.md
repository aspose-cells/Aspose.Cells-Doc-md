---
title: Как установить точку как общую с помощью JavaScript через C++
linktitle: Как установить точку как сумму
description: Узнайте, как установить точки как общие в водопадах с помощью Aspose.Cells for JavaScript через C++.
keywords: Водопадный график, точка, установка как общая, JavaScript через C++
type: docs
weight: 72
url: /ru/javascript-cpp/how-to-set-point-as-total/
---

## Что означает "Установить точку как сумму" в диаграмме Excel

В некоторых диаграммах Excel, например, водопадных, некоторые данные точек являются суммой предыдущих точек, и может понадобиться "установить точку как сумму". Мы покажем пример кода и иллюстрацию ниже.

## Водопадная диаграмма должна иметь функцию "Установить точку как сумму" 

![todo:image_alt_text](set-as-total1.png)

На этой картинке показан водопадный график в Excel. Видно, что есть четыре точки данных, начинающиеся с "Итого", предназначенные для подсчёта всех предыдущих данных. В настройках этой картинки что-то не так. Когда выбираешь точку "Итого 2024", видно, что опция "Установить как итог" в Excel не отмечена. Ниже приложен [пробный файл Excel](SampleSheet.xlsx), который нужно настроить, и мы используем Aspose.Cells for JavaScript через C++ для правильной настройки.

## Используйте Aspose.Cells for JavaScript через C++, чтобы "Установить точку как итог" 

Мы используем следующий код для правильной настройки файла:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Chart Subtotals Example</title>
    </head>
    <body>
        <h1>Set Chart Subtotals Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the chart named "Graphiq5"
            const chart = worksheet.charts.get("Graphiq5");

            // set some points as total column 
            // In this example, we set points 0, 4, 8, 12 as total
            chart.nSeries.get(0).layoutProperties.subtotals = [0, 4, 8, 12];

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Вы можете получить следующий исправленный [выходной файл](output.xlsx)

Как видно на рисунке ниже, четыре точки "Total" настроены правильно, и вы можете заметить различия с предыдущей диаграммой.

![todo:image_alt_text](set-as-total2.png)
