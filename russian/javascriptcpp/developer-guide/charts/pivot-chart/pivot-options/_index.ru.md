---
title: Как управлять PivotChart с помощью PivotOptions для JavaScript через C++
linktitle: Опции сводной таблицы
type: docs
weight: 10
url: /ru/javascript-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Как управлять PivotChart с помощью PivotOptions в JavaScript через C++.
keywords: PivotChart JavaScript через C++
---

## Что такое сводная диаграмма

Сводная диаграмма в Excel - это графическое представление данных, созданное на основе сводной таблицы. Она позволяет пользователям визуализировать и анализировать данные динамически, суммируя и отображая информацию в виде диаграммы. Сводные диаграммы интерактивны и их легко изменять, чтобы показать различные перспективы данных, что делает их мощным инструментом для анализа и презентации данных в Excel.

## Как управлять сводной диаграммой с опциями сводной таблицы

Используя Aspose.Cells for JavaScript через C++, вы можете использовать [**PivotOptions**](https://reference.aspose.com/cells/javascript-cpp/pivotoptions/) для управления PivotChart.

Пример файла и кода:
[Образец файла](Sample.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide PivotChart ZoneFilter Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and the first chart
            const worksheet = workbook.worksheets.get(0);
            const chart = worksheet.charts.get(0);
            const opt = chart.pivotOptions;

            // Hide ZoneFilter in PivotChart
            opt.dropZoneFilter = false; // HideZoneFilter

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HideZoneFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">ZoneFilter hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

С помощью вышеуказанного примера кода вы можете проверить результатный файл с следующим эффектом, как показано на рисунке:

**![Вывод](Output.png)**
