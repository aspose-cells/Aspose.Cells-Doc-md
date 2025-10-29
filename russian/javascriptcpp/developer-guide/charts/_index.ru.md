---
title: Создание и управление графиками с помощью JavaScript через C++
linktitle: Диаграммы
description: Узнайте, как использовать Aspose.Cells for JavaScript через C++ для создания графиков в Microsoft Excel. Наше руководство продемонстрирует различные типы графиков и способы настройки их внешнего вида и форматирования.
keywords: Aspose.Cells for JavaScript через C++, создание графиков, Microsoft Excel, типы графиков, настройка, внешний вид, форматирование.
type: docs
weight: 130
url: /ru/javascript-cpp/creating-charts/
---

{{% alert color="primary" %}}

С помощью Aspose.Cells можно добавлять различные типы диаграмм в электронные таблицы. Aspose.Cells предоставляет множество гибких объектов диаграмм. В этой теме обсуждаются объекты диаграмм Aspose.Cells.

{{% /alert %}}

## **Создание диаграмм**

### **Простое создание диаграммы**
Создание диаграммы с Aspose.Cells с помощью следующих примеров кода:
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding sample values to cells
            worksheet.cells.get("A2").value = "Category1";
            worksheet.cells.get("A3").value = "Category2";
            worksheet.cells.get("A4").value = "Category3";

            worksheet.cells.get("B1").value = "Column1";
            worksheet.cells.get("B2").value = 4;
            worksheet.cells.get("B3").value = 20;
            worksheet.cells.get("B4").value = 50;

            worksheet.cells.get("C1").value = "Column2";
            worksheet.cells.get("C2").value = 50;
            worksheet.cells.get("C3").value = 100;
            worksheet.cells.get("C4").value = 150;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Setting chart data source as the range "A1:C4"
            chart.chartDataRange = { range: "A1:C4", isSeriesInRows: true };

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Вещи, которые нужно знать для создания диаграммы**

Перед созданием диаграмм важно понять некоторые базовые концепции, которые помогают при создании диаграмм с помощью Aspose.Cells.

#### **Объекты диаграммирования**

Ниже перечислены объекты для построения диаграмм:

- Series, один набор данных в диаграмме.
- Axis, ось диаграммы.
- Chart, одна диаграмма Excel.
- ChartArea, область диаграммы на листе.
- ChartDataTable, таблица данных диаграммы.
- ChartFrame, объект рамки в диаграмме.
- ChartPoint, одна точка в наборе данных диаграммы.
- ChartPointCollection, коллекция, содержащая все точки в одном наборе данных.
- Charts, коллекция объектов Chart.
- DataLabels, коллекция всех объектов DataLabel для указанного набора данных.
- FillFormat, формат заливки для формы.
- Floor, основание 3D-диаграммы.
- Legend, легенда диаграммы.
- Line, линия диаграммы.
- SeriesCollection, коллекция объектов Series.
- TickLabels, метки делений, связанные с метками делений на оси диаграммы.
- Название, заголовок диаграммы или оси.
- Линия тренда, линия тренда на диаграмме.
- Коллекция линий тренда, коллекция всех объектов линии тренда для указанной серии данных.
- Стены, стены 3D-диаграммы.

#### **Использование объектов построения диаграмм**

Как уже упоминалось, все объекты построения диаграмм являются экземплярами соответствующих классов и обладают конкретными свойствами и методами для выполнения определенных задач. Используйте объекты построения диаграмм для создания диаграмм.

Добавьте любую диаграмму на лист с помощью коллекции [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--). Каждый элемент коллекции [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--) представляет объект [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/). Объект [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) инкапсулирует все другие объекты для настройки внешнего вида диаграммы. Следующий раздел показывает, как использовать несколько базовых объектов диаграмм для создания простой диаграммы.

### **Создание диаграммы с использованием Aspose.Cells**



1. Добавьте данные в ячейки листа с помощью метода [**putValue(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-string-) объекта [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/).
   Это будет использоваться в качестве источника данных для диаграммы.
2. Добавьте график на лист, вызвав метод [**add**](https://reference.aspose.com/cells/javascript-cpp/chartcollection/#add-charttype-number-number-number-number-) коллекции [**ChartCollection**](https://reference.aspose.com/cells/javascript-cpp/chartcollection), заключённый в объект [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/).
3. Укажите тип графика с помощью перечисления [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/).
   Например, ниже используется значение [**ChartType.Pyramid**](https://reference.aspose.com/cells/javascript-cpp/charttype) как тип диаграммы.
4. Получите новый объект [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) из коллекции [**Charts**](https://reference.aspose.com/cells/javascript-cpp/chartcollection), передав его индекс.
5. Используйте любой объект построения графика, заключённый в объект [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/), для управления графиком.
   Ниже используется объект [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection/) для указания источника данных диаграммы.

При добавлении исходных данных в диаграмму источник данных может быть диапазоном ячеек (например, "A1:C3"), последовательностью несмежных ячеек (например, "A1, A3, A5") или последовательностью значений (например, "1,2,3").

Эти общие шаги позволяют создать любой тип диаграммы. Используйте различные объекты построения диаграмм для создания различных диаграмм.

С помощью Aspose.Cells можно создать множество различных типов диаграмм. Все стандартные диаграммы, поддерживаемые Aspose.Cells, предварительно определены в перечислении с именем [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/).

Предопределенные типы графиков:

|**Типы графиков**|**Описание**|
| :- | :- |
|Column|Представляет гистограмму с кластеризацией
|ColumnStacked|Представляет стопку гистограмму
|Column100PercentStacked|Представляет 100% стопку гистограмму
|Column3DClustered|Представляет 3D гистограмму с кластеризацией
|Column3DStacked|Представляет 3D стопку гистограмму
|Column3D100PercentStacked|Представляет 3D 100% стопку гистограмму
|Column3D|Представляет 3D гистограмму
|Bar|Представляет гистограмму с кластеризацией по горизонтали
|BarStacked|Представляет стопку гистограмму по горизонтали
|Bar100PercentStacked|Представляет 100% стопку гистограмму по горизонтали
|Bar3DClustered|Представляет 3D гистограмму с кластеризацией по горизонтали
|Bar3DStacked|Представляет 3D стопку гистограмму по горизонтали
|Bar3D100PercentStacked|Представляет 3D 100% стопку гистограмму по горизонтали
|Line|Представляет линейный график
|LineStacked|Представляет стопку линейный график
|Line100PercentStacked|Представляет 100% стопку линейный график
|LineWithDataMarkers|Представляет линейный график с маркерами данных
|LineStackedWithDataMarkers|Представляет стопку линейный график с маркерами данных
|Line100PercentStackedWithDataMarkers|Представляет собой 100% столбчатую диаграмму с маркерами данных|
|Line3D|Представляет собой 3D линейную диаграмму|
|Pie|Представляет собой круговую диаграмму|
|Pie3D|Представляет собой 3D круговую диаграмму|
|PiePie|Представляет собой круговую диаграмму с вложенной круговой диаграммой|
|PieExploded|Представляет собой взорванную круговую диаграмму|
|Pie3DExploded|Представляет собой 3D взорванную круговую диаграмму|
|PieBar|Представляет собой столбчатую диаграмму с вложенной круговой диаграммой|
|Scatter|Представляет собой точечную диаграмму|
|ScatterConnectedByCurvesWithDataMarker|Представляет собой точечную диаграмму, соединенную кривыми, с маркерами данных|
|ScatterConnectedByCurvesWithoutDataMarker|Представляет собой точечную диаграмму, соединенную кривыми, без маркеров данных|
|ScatterConnectedByLinesWithDataMarker|Представляет собой точечную диаграмму, соединенную линиями, с маркерами данных|
|ScatterConnectedByLinesWithoutDataMarker|Представляет собой точечную диаграмму, соединенную линиями, без маркеров данных|
|Area|Представляет собой зонную диаграмму|
|AreaStacked|Представляет собой стопку зонную диаграмму|
|Area100PercentStacked|Представляет собой 100% стопку зонную диаграмму|
|Area3D|Представляет собой 3D зонную диаграмму|
|Area3DStacked|Представляет собой 3D стопку зонную диаграмму|
|Area3D100PercentStacked|Представляет собой 3D 100% стопку зонную диаграмму|
|Doughnut|Представляет собой донат-диаграмму|
|DoughnutExploded|Представляет круговую диаграмму со сдвоенной дугой|
|Radar|Представляет радарную диаграмму|
|RadarWithDataMarkers|Представляет радарную диаграмму с маркерами данных|
|RadarFilled|Представляет заполненную радарную диаграмму|
|Surface3D|Представляет трехмерную поверхностную диаграмму|
|SurfaceWireframe3D|Представляет проволочную трехмерную поверхностную диаграмму|
|SurfaceContour|Представляет контурную диаграмму|
|SurfaceContourWireframe|Представляет проволочную контурную диаграмму|
|Bubble|Представляет диаграмму пузырьков|
|Bubble3D|Представляет трехмерную диаграмму пузырьков|
|Cylinder|Представляет цилиндрическую диаграмму|
|CylinderStacked|Представляет стопку цилиндрических диаграмм|
|Cylinder100PercentStacked|Представляет 100% стопку цилиндрических диаграмм|
|CylindericalBar|Представляет цилиндрическую столбчатую диаграмму|
|CylindericalBarStacked|Представляет стопку цилиндрических столбчатых диаграмм|
|CylindericalBar100PercentStacked|Представляет 100% стопку цилиндрических столбчатых диаграмм|
|CylindericalColumn3D|Представляет трехмерную цилиндрическую колоночную диаграмму|
|Cone|Представляет конусную диаграмму|
|ConeStacked|Представляет стопку конусных диаграмм|
|Cone100PercentStacked|Представляет 100% стопку конусных диаграмм|
|ConicalBar|Представляет коническую столбчатую диаграмму|
|ConicalBarStacked|Представляет стопку конических столбчатых диаграмм|
|ConicalBar100PercentStacked|Представляет 100% стопку конических столбчатых диаграмм|
|ConicalColumn3D|Представляет 3D коническую колонную диаграмму|
|Pyramid|Представляет пирамидальную диаграмму|
|PyramidStacked|Представляет стопку пирамидальных диаграмм|
|Pyramid100PercentStacked|Представляет 100% стопку пирамидальных диаграмм|
|PyramidBar|Представляет стопку пирамидальных столбчатых диаграмм|
|PyramidBarStacked|Представляет стопку пирамидальных столбчатых диаграмм|
|PyramidBar100PercentStacked|Представляет 100% стопку пирамидальных столбчатых диаграмм|
|PyramidColumn3D|Представляет 3D пирамидальную колонную диаграмму|

{{% alert color="primary" %}}

При назначении диапазона ячеек в качестве источника данных можно установить только диапазон сверху влево до нижнего правого. Например, "A1:C3" - допустимо, а "C3:A1" - недопустимо.

{{% /alert %}}

#### **Пирамидальная диаграмма**

При выполнении примерного кода на листе добавляется пирамидальная диаграмма.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Chart and Download</h1>
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

            // If a file is provided, load it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Pyramid, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and chart added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **Линейная диаграмма**

В приведенном выше примере, просто изменив [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) на *Line*, создается линейная диаграмма. Полный источник приведен ниже. После выполнения кода, на лист добавится линейная диаграмма.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Chart</title>
    </head>
    <body>
        <h1>Add Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **Пузырьковая диаграмма**

Чтобы создать пузырьковую диаграмму, необходимо установить [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) в [**ChartType.Bubble**](https://reference.aspose.com/cells/javascript-cpp/charttype), а также задать несколько дополнительных свойств, таких как BubbleSizes, Values и XValues. После выполнения следующего кода, на лист добавится пузырьковая диаграмма.

#### **Диаграмма линии с маркерами данных**

Чтобы создать линию с маркером данных, [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) должен быть установлен в *ChartType.LineWithDataMarkers*, а также задать дополнительные свойства, такие как фон, маркеры серии, Values и XValues. После выполнения следующего кода, на лист добавится диаграмма с линией и маркером данных.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Line With Data Marker Chart</title>
    </head>
    <body>
        <h1>Line With Data Marker Chart Example</h1>
        <p>You may optionally select an existing Excel file to modify, or leave empty to create a new workbook.</p>
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
            if (fileInput.files.length === 0) {
                // Proceed with a new workbook if no file selected
            }

            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set columns title 
            worksheet.cells.get(0, 0).putValue("X");
            worksheet.cells.get(0, 1).putValue("Y");

            // Random data shall be used for generating the chart
            // Create random data and save in the cells
            for (let i = 1; i < 21; i++) {
                worksheet.cells.get(i, 0).putValue(i);
                worksheet.cells.get(i, 1).putValue(0.8);
            }

            for (let i = 21; i < 41; i++) {
                worksheet.cells.get(i, 0).putValue(i - 20);
                worksheet.cells.get(i, 1).putValue(0.9);
            }

            // Add a chart to the worksheet
            const idx = worksheet.charts.add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

            // Access the newly created chart
            const chart = worksheet.charts.get(idx);

            // Set chart style
            chart.style = 3;

            // Set autoscaling value to true
            chart.autoScaling = true;

            // Set foreground color white
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;

            // Set Properties of chart title
            chart.title.text = "Sample Chart";

            // Set chart type
            chart.type = AsposeCells.ChartType.LineWithDataMarkers;

            // Set Properties of categoryaxis title
            chart.categoryAxis.title.text = "Units";

            //Set Properties of nseries
            const s2_idx = chart.nSeries.add("A2:A2", true);
            const s3_idx = chart.nSeries.add("A22:A22", true);

            // Set IsColorVaried to true for varied points color
            chart.nSeries.isColorVaried = true;

            // Set properties of background area and series markers
            const series2 = chart.nSeries.get(s2_idx);
            series2.area.formatting = AsposeCells.FormattingType.Custom;
            series2.marker.area.foregroundColor = AsposeCells.Color.Yellow;
            series2.marker.border.isVisible = false;

            // Set X and Y values of series chart
            series2.xValues = "A2:A21";
            series2.values = "B2:B21";

            // Set properties of background area and series markers for series3
            const series3 = chart.nSeries.get(s3_idx);
            series3.area.formatting = AsposeCells.FormattingType.Custom;
            series3.marker.area.foregroundColor = AsposeCells.Color.Green;
            series3.marker.border.isVisible = false;

            // Set X and Y values of series chart
            series3.xValues = "A22:A41";
            series3.values = "B22:B41";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'LineWithDataMarkerChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Чтение и манипулирование диаграммами Excel 2016](/cells/ru/javascript-cpp/read-and-manipulate-excel-2016-charts/)
- [Управление осями диаграмм Excel](/cells/ru/javascript-cpp/chart-axes/)
- [Настройка внешнего вида диаграммы](/cells/ru/javascript-cpp/setting-chart-appearance/)
- [Типы диаграмм](/cells/ru/javascript-cpp/chart-types/)
- [Настройка диаграмм](/cells/ru/javascript-cpp/customizing-charts/)
- [Установить источник данных для диаграммы](/cells/ru/javascript-cpp/data-formatting-in-charts/)
- [Управление подписями данных диаграмм Excel](/cells/ru/javascript-cpp/insert-datalabels-to-chart/)
- [Получить лист диаграммы](/cells/ru/javascript-cpp/get-worksheet-of-the-chart/)
- [Управление легендой диаграмм Excel](/cells/ru/javascript-cpp/chart-legend/)
- [Управление позицией, размером и дизайном диаграммы](/cells/ru/javascript-cpp/manipulate-position-size-and-designer-chart/)
- [Создание круговой диаграммы с линиями](/cells/ru/javascript-cpp/creating-pie-chart-with-leader-lines/)
- [Фигуры в диаграммах](/cells/ru/javascript-cpp/controls-in-charts/)
- [Управление заголовками диаграмм Excel](/cells/ru/javascript-cpp/chart-and-axis-titles/)
- [Отображение диаграммы](/cells/ru/javascript-cpp/chart-rendering/)
- [Получить текст уравнения линии тренда диаграммы](/cells/ru/javascript-cpp/get-equation-text-of-chart-trendline/)
