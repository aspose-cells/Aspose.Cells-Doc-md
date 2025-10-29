---
title: Установка источника данных для графика с помощью JavaScript через C++
description: Узнайте о различных поддерживаемых источниках данных в Aspose.Cells for JavaScript на C++. Наше руководство проведет вас по различным типам источников данных и покажет, как подключать и извлекать данные из них для заполнения ваших таблиц.
keywords: Скрипт по C++ для диаграмм, отображения, форматирования данных, меток, цветов, шрифтов, внешнего вида, удобства использования.
linktitle: Источник данных
type: docs
weight: 10
url: /ru/javascript-cpp/data-formatting-in-charts/
---

В наших предыдущих темах мы уже предоставили много примеров, демонстрирующих, как можно установить источник данных для вашего графика, но в этой теме мы расскажем подробнее о типах данных, которые можно установить для графика.

## **Установка данных графика**

При работе с графиками с использованием Aspose.Cells есть два типа данных, с которыми нужно работать, следующие:

- Данные графика.
- Данные категорий.

### **Данные графика**

Данные для графика — это данные, которые мы используем в качестве источника данных для построения графиков. Мы можем добавить диапазон ячеек (с содержащими данными для графика), вызвав метод [**add(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/seriescollection/#add-string-boolean-) объекта [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Worksheet and Chart Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 170;
            worksheet.cells.get("A4").value = 300;
            worksheet.cells.get("B1").value = 160;
            worksheet.cells.get("B2").value = 32;
            worksheet.cells.get("B3").value = 50;
            worksheet.cells.get("B4").value = 40;

            // Adding sample values to cells as category data
            worksheet.cells.get("C1").value = "Q1";
            worksheet.cells.get("C2").value = "Q2";
            worksheet.cells.get("C3").value = "Y1";
            worksheet.cells.get("C4").value = "Y2";

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.nSeries.add("A1:B4", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Данные категорий**

Категорийные данные используются для подписи данных графика и могут быть добавлены к [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection) с помощью его свойства [**categoryData**](https://reference.aspose.com/cells/javascript-cpp/seriescollection/#categoryData--). Ниже приведен полный пример, демонстрирующий использование данных графика и категорий. После выполнения приведенного выше кода будет добавлен столбчатый график на лист.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Create Workbook with Chart Example</h1>
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

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files.length) {
                const arrayBuffer = await fileInput.files[0].arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(10);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(170);
            worksheet.cells.get("A4").putValue(200);
            worksheet.cells.get("B1").putValue(120);
            worksheet.cells.get("B2").putValue(320);
            worksheet.cells.get("B3").putValue(50);
            worksheet.cells.get("B4").putValue(40);

            // Adding sample values to cells as category data
            worksheet.cells.get("C1").putValue("Q1");
            worksheet.cells.get("C2").putValue("Q2");
            worksheet.cells.get("C3").putValue("Y1");
            worksheet.cells.get("C4").putValue("Y2");

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.nSeries.add("A1:B4", true);

            // Setting the data source for the category data of SeriesCollection
            chart.nSeries.categoryData = "C1:C4";

            // Saving the Excel file and creating a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**  
- [Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона](/cells/ru/javascript-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)  
- [Создание динамических диаграмм](/cells/ru/javascript-cpp/create-dynamic-charts/)  
- [Легкий способ настройки диаграмм с помощью метода Chart.chartDataRange](/cells/ru/javascript-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)  
- [Найдите тип значений X и Y точек в серии графика](/cells/ru/javascript-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
