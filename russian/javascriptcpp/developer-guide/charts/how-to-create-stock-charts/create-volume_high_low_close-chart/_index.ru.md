---
title: Создайте график акций Volume High Low Close (VHLC) с помощью JavaScript через C++
linktitle: Создание графика цен акций по объему  высоким, низким и закрывающим(VHLC)
description: Узнайте, как создать график акций с объемом, максимумом, минимумом и закрытием с помощью Aspose.Cells for JavaScript через C++. Наше руководство покажет, как построить данные фондового рынка, включая объем, максимальные, минимальные и закрывающие цены, для лучшего анализа и визуализации.
keywords: Aspose.Cells for JavaScript через C++, График акций Volume High Low Close, Данные фондового рынка, Анализ, Визуализация.
type: docs
weight: 183
url: /ru/javascript-cpp/create-volume-high-low-close-stock-chart/
---

## **Возможные сценарии использования**
Третий график акций, который мы рассмотрим, это график Volume High Low Close. Опять же, важно повторить, что данные должны быть в правильном порядке. Если необходимо переставить таблицу данных, сделайте это до настройки графика.
Этот график включает столбец для объема сразу после первого (категорийного) столбца, а графики включают столбчатую диаграмму по первичной оси, показывающую этот объем, в то время как цены перемещены на вторичную ось.

![todo:image_alt_text](data.png)
## **График акций объем-высокая-низкая-закрытие (VHLC)**

![todo:image_alt_text](sample.png)
## **Образец кода**
Приведенный ниже образец кода загружает [образец файла Excel](Volume-High-Low-Close.xlsx) и генерирует [выходной файл Excel](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Volume-High-Low-Close Stock Chart Example</h1>
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

            // Create an instance of Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockVolumeHighLowClose, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend can be showed
            chart.showLegend = true;
            // Set the chart title name 
            chart.title.text = "Volume-High-Low-Close Stock";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;
            // Set data range (converted from setChartDataRange(range, isVertical))
            chart.chartDataRange = ["A1:E9", true];
            // Set category data 
            chart.nSeries.categoryData = "A2:A9";
            // Set Color for the first series(Volume) data 
            chart.nSeries.get(0).area.foregroundColor = new AsposeCells.Color(79, 129, 189);
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
