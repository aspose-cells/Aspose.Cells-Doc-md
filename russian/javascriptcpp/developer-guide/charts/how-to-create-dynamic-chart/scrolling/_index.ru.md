---
title: Как создать динамическую диаграмму прокрутки с помощью JavaScript через C++
linktitle: Как создать динамическую прокручивающуюся диаграмму
description: Узнайте, как создать динамическую диаграмму прокрутки с помощью Aspose.Cells for JavaScript через C++. Наше пошаговое руководство продемонстрирует, как реализовать плавные переходы данных и автоматическую прокрутку на вашей диаграмме для непрерывного и обновляемого отображения.
keywords: Aspose.Cells for JavaScript через C++, Динамическая диаграмма прокрутки, Переходы данных, Плавная прокрутка, Непрерывное отображение, Обновление визуализации.
type: docs
weight: 75
url: /ru/javascript-cpp/create-dynamic-scrolling-chart/
---

## **Возможные сценарии использования**
Динамическая прокручивающаяся диаграмма - это тип графического представления, используемого для отображения данных, меняющихся со временем. Она предназначена для предоставления видео в реальном времени данных, позволяя пользователям отслеживать непрерывные обновления и тренды. Диаграмма непрерывно обновляется при добавлении новых данных, автоматически прокручиваясь, чтобы показывать самую последнюю информацию.

Динамические прокручивающиеся диаграммы широко используются в различных отраслях, таких как финансы, анализ фондового рынка, отслеживание погоды и аналитика социальных медиа. Они позволяют пользователям визуализировать и анализировать паттерны данных и принимать обоснованные решения на основе информации в реальном времени.

Эти диаграммы обычно интерактивны, позволяя пользователю увеличивать или уменьшать масштаб, прокручивать исторические данные и регулировать временные интервалы. Они часто поддерживают несколько серий данных, обеспечивая комплексный обзор различных метрик и их взаимосвязей.

В целом, динамические прокручивающиеся диаграммы - это ценные инструменты для мониторинга и анализа временных рядов данных, способствуя принятию решений в реальном времени и улучшая возможности визуализации данных.

## **Используйте Aspose.Cells для создания динамической прокручиваемой диаграммы**
В следующих параграфах мы покажем, как создать динамическую диаграмму прокрутки с помощью Aspose.Cells for JavaScript через C++. Мы покажем пример кода и созданный с этим кодом файл Excel.

## **Образец кода**
Приведенный ниже образец кода сгенерирует файл [Динамической Прокручивающейся Диаграммы](DynamicScrollingChart.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Scrolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils, ChartType } = AsposeCells;

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
            // Create a new workbook and access the first worksheet.
            const workbook = new Workbook();
            const sheets = workbook.worksheets;
            const sheet = sheets.get(0);

            // Populate the data for the chart. Add values to cells and set series names.
            sheet.cells.get("A1").value = "Day";
            sheet.cells.get("B1").value = "Sales";
            // In this example, we will add 30 days of data
            const allDays = 30;
            const showDays = 10;
            let currentDay = 1;

            for (let i = 0; i < allDays; i++) {
                const cellA = `A${i + 2}`;
                const cellB = `B${i + 2}`;
                sheet.cells.get(cellA).value = i + 1;
                sheet.cells.get(cellB).value = 50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3);
            }

            // This is the Dynamic Scrolling Control Data
            sheet.cells.get("G19").value = "Start Day";
            sheet.cells.get("G20").value = currentDay;
            sheet.cells.get("H19").value = "Show Days";
            sheet.cells.get("H20").value = showDays;

            // Set the dynamic range for the chart's data source. 
            let index = sheets.names.add("Sheet1!ChtScrollData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)";

            // Set the dynamic range for the chart's data labels. 
            index = sheets.names.add("Sheet1!ChtScrollLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)";

            // Add a ScrollBar for the Dynamic Scrolling Chart
            const bar = sheet.shapes.addScrollBar(2, 0, 3, 0, 200, 30);
            bar.min = 0;
            bar.max = allDays - showDays;
            bar.currentValue = currentDay;
            bar.linkedCell = "$G$20";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 2, 4, 15, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtScrollData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtScrollLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicScrollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Примечания**
В сгенерированном файле вы можете работать со строкой прокрутки, в то время как диаграмма динамически подсчитывает последние 10 наборов данных. Это делается с использованием формулы "СМЕЩЕНИЕ" в образцовом коде:
