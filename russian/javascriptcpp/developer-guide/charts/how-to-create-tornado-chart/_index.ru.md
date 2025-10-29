---
title: Как создать торнадо график с помощью JavaScript через C++
linktitle: Как создать диаграмму торнадо
type: docs
weight: 73
url: /ru/javascript-cpp/create-tornado-chart/
description: Узнайте, как создать торнадо график с помощью Aspose.Cells for JavaScript через API C++.
keywords: Создавайте торнадо графики на JavaScript, добавляйте их, вставляйте торнадо график
---

## **Введение**
Гистограмма торнадо, также известная как диаграмма торнадо или торнадо-график, является видом визуализации данных, который часто используется для анализа чувствительности в Excel. Она помогает понять влияние изменения переменных на конкретный результат или результат.

## **Как создать гистограмму торнадо в Excel**
Вы можете создать гистограмму торнадо в Excel, следуя этим шагам:
1. Выберите данные и перейдите во вкладку Вставка --> Диаграммы --> Вставить столбцовую или гистограмму --> Столбчатая гистограмма. Нажмите на неё.
<br>
<img src="1.png" width=70% />
2. Измените ось Y: Щелкните правой кнопкой мыши по оси Y. Нажмите на формат оси. В метках нажмите на выпадающий список позиции метки и выберите Положение Лоу.
<br>
<img src="2.png" width=70% />
3. Выберите любой столбец и перейдите к форматированию. установите соответствующую ширину промежутка.
<br>
<img src="3.png" width=70% />
4. Удалим знак минус(-) с гистограммы торнадо. Выберите ось X. Перейдите к форматированию. В параметрах оси нажмите на номер. В категории выберите пользовательское. В поле формата напишите ###0,###0. Нажмите добавить.
<br>
<img src="4.png" width=70% />
5. нажмите на ось Y и перейдите к параметрам оси. В параметрах оси отметьте Категории в обратном порядке.
<br>
<img src="5.png" width=70% />

## ** Как добавить торнадо-график в Aspose.Cells for JavaScript через C++**
Пожалуйста, ознакомьтесь с следующим образцом кода. Он загружает [образец электронной таблицы](sample.xlsx), который содержит некоторые тестовые данные. Затем он создает столбчатую диаграмму на основе исходных данных и настраивает соответствующие свойства. Наконец, он сохраняет книгу в [формате XLSX](out.xlsx). На следующем скриншоте показана гистограмма торнадо, созданная Aspose.Cells в выходном файле Excel.
<br>
<img src="6.png" width=70% />

### **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const charts = sheet.charts;

            // Add bar chart
            const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
            const chart = charts.get(index);

            // Set data for bar chart
            chart.chartDataRange = "A1:C7";

            // Set properties for bar chart
            chart.title.text = "Tornado chart";
            chart.style = 2;
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;
            chart.plotArea.border.color = AsposeCells.Color.White;
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            chart.categoryAxis.tickLabelPosition = AsposeCells.TickLabelPositionType.Low;
            chart.category```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const charts = sheet.charts;

            // Add bar chart
            const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
            const chart = charts.get(index);

            // Set data for bar chart
            chart.chartDataRange = "A1:C7";

            // Set properties for bar chart
            chart.title.text = "Tornado chart";
            chart.style = 2;
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;
            chart.plotArea.border.color = AsposeCells.Color.White;
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            chart.categoryAxis.tickLabelPosition = AsposeCells.TickLabelPositionType.Low;
            chart.categoryAxis.isPlotOrderReversed = true;

            chart.gapWidth = 10;

            const valueAxis = chart.valueAxis;
            valueAxis.tickLabels.numberFormat = "#,##0;#,##0";

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
