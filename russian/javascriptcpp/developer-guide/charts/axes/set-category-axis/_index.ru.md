---
title: Как установить категориальную ось с помощью JavaScript через C++
linktitle: Как настроить категориальную ось
description: Узнайте, как установить категориальную ось в Aspose.Cells for JavaScript через C++. Наш гид поможет вам понять, как определить диапазон категории, настроить ее свойства и форматировать метки.
keywords: Aspose.Cells for JavaScript через C++, категориальная ось, настройка, диапазон, свойства, форматирование.
type: docs
weight: 205
url: /ru/javascript-cpp/how-to-set-category-axis/
---

## **Возможные сценарии использования**
После создания графика в рабочем листе, вы можете задать категориальную ось. В этой статье мы покажем, как установить категориальную ось для графика Excel с помощью Aspose.Cells for JavaScript через C++ на примере кода.

## **Шаги в примерном коде**

1. Создайте новую книгу.

2. Создайте новую диаграмму на первом листе.

3. Добавьте некоторые значения в ячейки на первом листе.

4. Теперь вы можете установить категориальную ось; есть два способа: используя данные из ячейки или используя строки напрямую, оба показаны в примере кода.

5. Установите значение оси и сохраните рабочую книгу, чтобы просмотреть результат.

## **Образец кода**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, LegendPositionType, Utils } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CHART";

            // Add a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 8, 0, 20, 10);
            const chart = worksheet.charts.get(chartIndex);

            // Add some values to cells
            worksheet.cells.get("A1").putValue("Sales");
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("A4").putValue(130);
            worksheet.cells.get("A5").putValue(160);
            worksheet.cells.get("A6").putValue(150);
            worksheet.cells.get("B1").putValue("Days");
            worksheet.cells.get("B2").putValue(1);
            worksheet.cells.get("B3").putValue(2);
            worksheet.cells.get("B4").putValue(3);
            worksheet.cells.get("B5").putValue(4);
            worksheet.cells.get("B6").putValue(5);

            // Some values in string
            const Sales = "100,150,130,160,150";
            const Days = "1,2,3,4,5";

            // Set Category Axis Data with string
            chart.nSeries.categoryData = `{${Days}}`;
            // Or you can set Category Axis Data with data in cells
            // chart.nSeries.categoryData = "B2:B6";

            // Add Series to the chart
            chart.nSeries.add("Demand1", true);
            // Set value axis with string 
            chart.nSeries.get(0).values = `{${Sales}}`;
            chart.nSeries.add("Demand2", true);
            // Set value axis with data in cells
            chart.nSeries.get(1).values = "A2:A6";

            // Set some Category Axis properties
            chart.categoryAxis.tickLabels.rotationAngle = 45;
            chart.categoryAxis.tickLabels.font.size = 8;
            chart.legend.position = LegendPositionType.Bottom;

            // Save the workbook to view the result file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
