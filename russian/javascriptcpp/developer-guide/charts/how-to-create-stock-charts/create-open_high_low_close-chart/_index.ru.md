---
title: Создайте график акций Open High Low Close (OHLC) с помощью JavaScript через C++
description: Узнайте, как создать график акций с открытием, максимумом, минимумом и закрытием с помощью Aspose.Cells for JavaScript через C++. Наше руководство покажет, как построить данные фондового рынка, включая цены открытия, максимума, минимума и закрытия, для лучшего анализа и визуализации.
keywords: Aspose.Cells for JavaScript через C++, График акций Open High Low Close, Данные фондового рынка, Анализ, Визуализация.
type: docs
weight: 182
url: /ru/javascript-cpp/create-open-high-low-close-stock-chart/
---

## **Возможные сценарии использования**
График цен акций Open-High-Low-Close (OHLC) использует пять столбцов данных по порядку: категория, открытие, максимум, минимум и закрытие. Диапазон цен в каждой категории снова указан вертикальной линией, а интервал между открытием и закрытием отображается более широким плавающим баром; если цена увеличивается в категории (закрытие выше открытия), бар заполняется одним цветом, а если цена уменьшается, бар заполняется другим. Этот тип графика часто называется графиком свечей.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Улучшения видимости на графике**
Мы часто используем цвета, а не черно-белую палитру, чтобы обозначить рост и снижение цен. В первом наборе свечей ниже красный показывает рост, а зеленый — снижение цен.

![todo:image_alt_text](sample2.png)
## **Образец кода**
Нижеприведенный образец кода загружает [образец файла Excel](Open-High-Low-Close.xlsx) и генерирует [файл Excel вывода](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open-High-Low-Close Stock Chart Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockOpenHighLowClose, 5, 6, 20, 12);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);

            // Set the legend can be showed
            chart.showLegend = true;

            // Set the chart title name 
            chart.title.text = "Open-High-Low-Close Stock";

            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set data range
            chart.chartDataRange = ["A1:E9", true];

            // Set category data 
            chart.nSeries.categoryData = "A2:A9";

            // Set the DownBars and UpBars with different color
            chart.nSeries.get(0).downBars.area.foregroundColor = AsposeCells.Color.Green;
            chart.nSeries.get(0).upBars.area.foregroundColor = AsposeCells.Color.Red;

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
