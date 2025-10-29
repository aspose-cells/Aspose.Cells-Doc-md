---
title: Управление заголовками диаграмм Excel с помощью JavaScript через C++
description: Узнайте, как использовать Aspose.Cells for JavaScript через C++ для добавления и форматирования заголовков диаграмм и осей в Microsoft Excel. Наше руководство покажет, как задавать различные типы заголовков, настраивать их внешний вид и изменять заголовки осей для лучшего отображения данных и ясности.
keywords: Aspose.Cells for JavaScript через C++, заголовки диаграмм, заголовки осей, Microsoft Excel, отображение данных, внешний вид.
linktitle: Заголовки
type: docs
weight: 50
url: /ru/javascript-cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

В диаграммах Excel существует 2 вида заголовков:
1. Заголовок диаграммы 
1. Заголовки осей

{{% /alert %}}

## **Параметры заголовка**
Aspose.Cells for JavaScript через C++ также позволяет управлять заголовками диаграмм во время выполнения. С помощью объекта [Title](https://reference.aspose.com/cells/javascript-cpp/title/) вы можете изменять текст, шрифт и формат заливки для заголовков.

|![todo:image_alt_text](chart_title.png)|

## **Настройка заголовков диаграмм или осей**
Вы можете использовать Microsoft Excel для установки заголовков диаграмм и осей в WYSIWYG-режиме. Aspose.Cells for JavaScript через C++ также позволяет разработчикам устанавливать заголовки диаграмм и их осей во время выполнения. Все диаграммы и их оси содержат свойство [Title](https://reference.aspose.com/cells/javascript-cpp/title/), которое можно использовать для установки их заголовков, как показано в примере ниже.

 Следующий фрагмент кода демонстрирует, как задавать названия диаграмм и осей.

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
            // Instantiate a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 60;
            worksheet.cells.get("B2").value = 32;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = AsposeCells.Color.Blue;

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = AsposeCells.Color.Red;

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = AsposeCells.Color.Cyan;

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

            // Setting the title of a chart
            chart.title.text = "Title";

            // Setting the font color of the chart title to blue
            chart.title.font.color = AsposeCells.Color.Blue;

            // Setting the title of category axis of the chart
            chart.categoryAxis.title.text = "Category";

            // Setting the title of value axis of the chart
            chart.valueAxis.title.text = "Value";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Чтение подзаголовка диаграммы из файла ODS](/cells/ru/javascript-cpp/read-chart-subtitle-from-ods-file/)
