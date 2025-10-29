---
title: Создайте график акций High Low Close (HLC) с помощью JavaScript через C++
linktitle: Создание диаграммы акций HLC (High Low Close)
description: Узнайте, как создать график акций с максимума, минимума и закрытия с помощью Aspose.Cells for JavaScript через C++. Наше пошаговое руководство покажет, как построить данные фондового рынка, включая максимальные, минимальные и закрывающие цены, для лучшего анализа и визуализации.
keywords: Aspose.Cells for JavaScript через C++, График акций High Low Close, Данные фондового рынка, Анализ, Визуализация.
type: docs
weight: 181
url: /ru/javascript-cpp/create-high-low-close-stock-chart/
---

## **Возможные сценарии использования**  
График акций High-Low-Close (HLC) использует четыре столбца данных. Первый столбец — категория, обычно дата, но можно использовать и имена акций. Далее идут три столбца для высоких, низких и закрывающих цен. Диапазон цен для каждой категории обозначается вертикальной линией от низкого до высокого, а цена закрытия отображается с помощью метки, простирающейся вправо от этой линии.  

![todo:image_alt_text](sample.png)  
## **Улучшения видимости на графике**  
Иногда, чтобы сделать график более интуитивно понятным, мы можем изменить внешний вид маркера (закрытия) или отображать его на вторичной оси.  

![todo:image_alt_text](sample2.png)  
## **Образец кода**  
Нижеприведенный образец кода загружает [образец файла Excel](High-Low-Close.xlsx) и генерирует [файл Excel вывода](out.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>High-Low-Close Stock Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Create an instance of Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockHighLowClose, 5, 6, 20, 12);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);

            // Set the legend can be showed
            chart.showLegend = true;

            // Set the chart title name 
            chart.title.text = "High-Low-Close Stock";

            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set data range (range and orientation)
            chart.chartDataRange = ["A1:D9", true];

            // Set category data 
            chart.nSeries.categoryData = "A2:A9";

            // Set the marker with the built-in data for the 3rd series (index 2)
            const series2 = chart.nSeries.get(2);
            const marker = series2.marker;
            marker.markerStyle = AsposeCells.ChartMarkerType.Dash;
            marker.markerSize = 20;
            marker.area.formatting = AsposeCells.FormattingType.Custom;
            marker.area.foregroundColor = AsposeCells.Color.Maroon;

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
