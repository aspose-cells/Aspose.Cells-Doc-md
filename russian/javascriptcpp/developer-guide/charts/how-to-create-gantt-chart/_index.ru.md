---
title: Как создать диаграмму Ганта с помощью JavaScript через C++
linktitle: Как создать диаграмму Ганта
type: docs
weight: 72
url: /ru/javascript-cpp/how-to-create-gantt-chart/
description: Узнайте, как создать диаграмму Ганта с помощью Aspose.Cells for JavaScript через API C++.
keywords: Создавайте диаграмму Ганта на JavaScript, добавляйте ее, вставляйте диаграмму Ганта
---

## **Что такое диаграмма Ганта**

Диаграмма Ганта — это тип графика в виде столбцовой диаграммы, которая иллюстрирует график проекта. Она показывает даты начала и окончания различных элементов проекта. Каждый элемент или задача представлена столбцом, длина которого соответствует его продолжительности. Диаграммы Ганта также показывают зависимости между задачами, позволяя менеджерам видеть последовательность выполнения задач. Они широко используются в управлении проектами для планирования, расписания и отслеживания проектов.

## **Как создать диаграмму Ганта в Excel**

Вы можете создать диаграмму Ганта в Excel, следуя этим шагам:
1. Добавьте данные для диаграммы Ганта. 
<br>
<img src="00.png" width=50% />
1. Выберите данные и перейдите в Вставка -> Графики -> Вставить столбчатую или линейчатую диаграмму -> Сложенная гистограмма. В нашем примере это B1:B7, затем вставьте **Сложенную гистограмму**.
<br>
<img src="1.png" width=50% />

1. Выберите диаграмму, **Выберите данные** -> **Добавить**, установите **Название ряда** и **Значения ряда** согласно примеру.
<br>
<img src="2.png" width=50% />

1. Выберите диаграмму, отредактируйте **Метки горизонтальной (категорийной) оси**.
<br>
<img src="3.png" width=50% />

1. **Форматировать ось** по оси Y, выберите **Обратный порядок категорий**.
1. Выберите **синие серии** и установите **Заливка -> Нет заливки**.
1. **Форматировать ось** по оси X, установите **Минимум** и **Максимум** (1/5/2019:43470, 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **Добавьте метки данных** для диаграммы, и вы получите диаграмму Ганта.
<br>
<img src="0.png" width=50% />


## **Как добавить диаграмму Ганта в Aspose.Cells**
Пожалуйста, посмотрите следующий пример кода. Он загружает [пробный Excel-файл](sample.xlsx), содержащий некоторые данные. Затем он создает сложенную столбчатую диаграмму на основе исходных данных и устанавливает соответствующие свойства. В конце он сохраняет рабочую книгу в [формате XLSX](result.xlsx). Следующий скриншот показывает созданную с помощью Aspose.Cells диаграмму Ганта в выходном Excel-файле.
<br>
<img src="5.png" width=60% />

### **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Chart Example</title>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create BarStacked Chart
            const i = worksheet.charts.add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(i);

            // Set the chart title name 
            chart.title.text = "Gantt Chart";

            // Set the chart title is Visible
            chart.title.isVisible = true;

            // Set data range
            chart.chartDataRange = "B1:B6";

            // Add series data range
            chart.nSeries.add("C2:C6", true);

            // No fill for one serie
            chart.nSeries.get(0).area.fillFormat.fillType = AsposeCells.FillType.None;

            // Set the Horizontal(Category) Axis
            chart.nSeries.setCategoryData("A2:A6");

            // Reverse the Horizontal(Category) Axis
            chart.categoryAxis.isPlotOrderReversed = true;

            // Set the value axis's MinValue and MaxValue
            const minValue = parseFloat(worksheet.cells.get("B2").value);
            const maxValue = parseFloat(worksheet.cells.get("D6").value);
            chart.valueAxis.minValue = isNaN(minValue) ? 0 : minValue;
            chart.valueAxis.maxValue = isNaN(maxValue) ? 0 : maxValue;

            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Show the DataLabels
            chart.nSeries.get(1).dataLabels.showValue = true;

            // Disable the Legend
            chart.showLegend = false;

            // Save the result
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
