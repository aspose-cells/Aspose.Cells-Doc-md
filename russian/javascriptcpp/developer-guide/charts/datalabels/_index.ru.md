---
title: Управление DataLabels диаграмм Excel с помощью JavaScript через C++
description: Научитесь эффективно управлять метками данных в диаграммах Excel с помощью Aspose.Cells for JavaScript через C++. Этот всесторонний гид охватывает различные задачи управления, включая добавление, удаление и изменение меток для повышения читаемости и удобства использования.
keywords: Скрипт Aspose.Cells for Java, диаграммы Excel, метки данных, управление, читаемость, удобство использования, добавление, удаление, изменение.
linktitle: Метки данных
type: docs
weight: 50
url: /ru/javascript-cpp/insert-datalabels-to-chart/
---

{{% alert color="primary" %}}  

Метки данных - важная часть диаграммы.  
Мы легко можем узнать значение, процент и т. д. каждого ряда  

{{% /alert %}}  

## **Опции меток данных**  
Aspose.Cells for JavaScript через C++ также позволяет управлять метками данных диаграммы в реальном времени, с помощью объекта [DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/), легко перемещать, обновлять и форматировать метки данных диаграммы.  

|![todo:image_alt_text](chart_datalabels.png)|  

## **Управление метками данных диаграммы**  
Управление метками данных диаграммы с помощью DataLabels Aspose.Cells [DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/) очень просто.  

Следующий фрагмент кода демонстрирует, как управлять DataLabels:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Data Labels Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        let asposeReady = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeReady = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');
            if (!asposeReady) {
                resultDiv.innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(50);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("B1").putValue(60);
            worksheet.cells.get("B2").putValue(32);
            worksheet.cells.get("B3").putValue(50);

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Show value labels
            chart.nSeries.get(0).dataLabels.showValue = true;
            // Show series name labels
            chart.nSeries.get(1).dataLabels.showSeriesName = true;
            // Move labels to center
            chart.nSeries.get(1).dataLabels.position = AsposeCells.LabelPositionType.Center;

            // Save the file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_datalabels.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Продвинутые темы**  
- [Добавление пользовательских меток к данным точек в серии диаграммы](/cells/ru/javascript-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [Отключение переноса текста для меток данных диаграммы](/cells/ru/javascript-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [Изменение формы метки данных диаграммы для подгонки текста](/cells/ru/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [Настройка метки данных диаграммы точки с использованием разностных стилей](/cells/ru/javascript-cpp/rich-text-custom-data-label-of-chart-point/)  
- [Установка типа формы меток данных диаграммы](/cells/ru/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [Показ диапазона ячеек в качестве меток данных](/cells/ru/javascript-cpp/showing-cell-range-as-the-data-labels/)
