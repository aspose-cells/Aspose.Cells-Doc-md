---
title: Дата оси с помощью JavaScript через C++
description: Узнайте, как управлять датой оси в Aspose.Cells for JavaScript через C++. Наше руководство поможет вам разобраться с различными форматами дат, шкалами времени и частотой меток деления.
keywords: Aspose.Cells for JavaScript через C++, дата ось, управление, форматы дат, шкалы времени, частота меток деления.
type: docs
weight: 200
url: /ru/javascript-cpp/date-axis/
---

## **Возможные сценарии использования**
Когда вы создаете диаграмму из данных листа, использующих даты, и даты отображаются вдоль горизонтальной (категорийной) оси в диаграмме, Aspose.Cells for JavaScript через C++ автоматически преобразует категориальную ось в ось с датой (шкала времени).
Ось дат отображает даты в хронологическом порядке с определенными интервалами или базовыми единицами, такими как количество дней, месяцев или лет, даже если даты на листе не расположены последовательно или в тех же базовых единицах.
 По умолчанию Aspose.Cells определяет базовые единицы для оси даты на основе минимальной разницы между любыми двумя датами в данных листа. Например, если у вас есть данные о ценах акций, где минимальная разница между датами — семь дней, Excel устанавливает базовую единицу в дни, но вы можете изменить её на месяцы или годы, если хотите увидеть динамику акций за более длительный период.

## **Обработка оси дат, подобно Microsoft Excel**
Пожалуйста, посмотрите следующий пример кода, который создает новый Excel файл и помещает значения диаграммы в первый рабочий лист. 
Затем мы добавляем диаграмму и устанавливаем тип [**Axis**](https://reference.aspose.com/cells/javascript-cpp/axis/) 
на [**Axis.categoryType**](https://reference.aspose.com/cells/javascript-cpp/axis/#categoryType--), а затем устанавливаем базовые единицы в Дни.

![todo:image_alt_text](excel.png)

## **Образец кода**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Date Axis Chart Example</title>
    </head>
    <body>
        <h1>Date Axis Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, CategoryType, TimeUnit, ChartTextDirectionType, FillType } = AsposeCells;

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

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Shortcut to cells collection
            const cells = worksheet.cells;

            // Add the sample values to cells
            cells.get("A1").value = "Date";

            // 14 means datetime format
            const style = cells.style;
            style.number = 14;

            // Put values to cells for creating chart
            const cellA2 = cells.get("A2");
            cellA2.style = style;
            cellA2.value = new Date(Date.UTC(2022, 5, 26));

            const cellA3 = cells.get("A3");
            cellA3.style = style;
            cellA3.value = new Date(Date.UTC(2022, 4, 22));

            const cellA4 = cells.get("A4");
            cellA4.style = style;
            cellA4.value = new Date(Date.UTC(2022, 7, 3));

            cells.get("B1").value = "Price";
            cells.get("B2").value = 40;
            cells.get("B3").value = 50;
            cells.get("B4").value = 60;

            // Add a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 9, 6, 21, 13);
            // Access the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            // Converted setter to property assignment (range and boolean passed as array)
            chart.chartDataRange = ["A1:B4", true];

            // Set the Axis type to Date time
            chart.categoryAxis.categoryType = CategoryType.TimeScale;
            // Set the base unit for CategoryAxis to days
            chart.categoryAxis.baseUnitScale = TimeUnit.Days;
            // Set the direction for the axis text to be vertical
            chart.categoryAxis.tickLabels.directionType = ChartTextDirectionType.Vertical;
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = FillType.None;
            // Set max value of Y axis.
            chart.valueAxis.maxValue = 70;
            // Set major unit.
            chart.valueAxis.majorUnit = 10;

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DateAxis.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
