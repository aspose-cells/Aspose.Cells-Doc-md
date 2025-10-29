---
title: Управление осями диаграмм Excel с помощью JavaScript через C++
description: Узнайте, как настраивать оси диаграмм в Script Aspose.Cells for Java через C++. Наше руководство покажет, как настраивать основные и вспомогательные оси, устанавливать их диапазоны и изменять их свойства для улучшения ваших диаграмм.
keywords: Aspose.Cells for JavaСкрипт на C++, оси графика, конфигурация, основные оси, вторичные оси, диапазон, свойства.
linktitle: Оси
type: docs
weight: 50
url: /ru/javascript-cpp/chart-axes/
---

{{% alert color="primary" %}}  

В диаграммах Excel существует 3 вида осей:  
1. Горизонтальная (Категориальная) ось: OX  
1. Вертикальная(значения) ось: ось Y  
1. Глубина(серии) ось: ось Z  

{{% /alert %}}  

## **Опции оси**  
Aspose.Cells for JavaСкрипт на C++ также позволяет управлять осями графика во время выполнения. С помощью объекта [Axis](https://reference.aspose.com/cells/javascript-cpp/axis/) вы можете изменять все параметры оси, как это делается в Excel.  

|![todo:image_alt_text](chart_axes.png)|  

## **Управление осью X и Y**  
В графике Excel горизонтальные и вертикальные оси — это две наиболее популярные оси.  

Следующий фрагмент кода демонстрирует, как установить параметры осей X и Y.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Chart Axes</title>
    </head>
    <body>
        <h1>Chart Axes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = "Series1";
            worksheet.cells.get("A2").value = 50;
            worksheet.cells.get("A3").value = 100;
            worksheet.cells.get("A4").value = 150;
            worksheet.cells.get("B1").value = "Series2";
            worksheet.cells.get("B2").value = 60;
            worksheet.cells.get("B3").value = 32;
            worksheet.cells.get("B4").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.chartDataRange = ["A1:B4", true];

            // Hiding X axis
            chart.categoryAxis.isVisible = false;

            // Setting max value of Y axis
            chart.valueAxis.maxValue = 200;
            // Setting major unit
            chart.valueAxis.majorUnit = 50;

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_axes.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```  

## **Продвинутые темы**  
- [Изменение направления меток делений](/cells/ru/javascript-cpp/change-tick-label-direction/)  
- [Определение существующих осей на графике](/cells/ru/javascript-cpp/determine-which-axis-exists-in-the-chart/)  
- [Обработка автоматических единиц оси диаграммы, как в Microsoft Excel](/cells/ru/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [Чтение меток оси после вычисления диаграммы](/cells/ru/javascript-cpp/read-axis-labels-after-calculating-the-chart/)  
- [Как установить ось категорий в графике Excel](/cells/ru/javascript-cpp/how-to-set-category-axis/)
