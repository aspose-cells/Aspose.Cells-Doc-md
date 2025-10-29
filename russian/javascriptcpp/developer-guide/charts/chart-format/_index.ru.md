---
title: Настройка внешнего вида графика с помощью JavaScript через C++
description: Узнайте, как настраивать внешний вид графиков в Aspose.Cells for JavaScript на C++. Наше руководство покажет вам, как изменять макеты графиков, цвета, шрифты и эффекты для достижения желаемого визуального стиля и улучшения ваших таблиц.
keywords: Aspose.Cells for JavaScript на C++, построение графиков, внешний вид графика, макеты, цвета, шрифты, эффекты, таблицы.
linktitle: Формат графика
type: docs
weight: 20
url: /ru/javascript-cpp/setting-chart-appearance/
---

## **Настройка внешнего вида диаграммы**
В статье Как создать график мы дали краткое введение в типы графиков и объекты построения предлагаемые Aspose.Cells и описали, как создать их. В этой статье рассматривается, как настроить внешний вид графиков путем установки их свойств:

- Установка области графика.
- Установка линий графика.
- Применение тем.
- Установка заголовков для графиков и осей.
Работа с линиями сетки.

### **Установка области диаграммы**
В диаграмме существуют различные виды областей, и Aspose.Cells предоставляет гибкость для изменения внешнего вида каждой области. Разработчики могут применять различные настройки форматирования к области, изменяя ее передний план, задний план и формат заливки и т. д.

В приведенном ниже примере мы применили различные настройки форматирования к различным видам областей диаграммы. Эти области включают:

- Область построения
- Область диаграммы
- Область коллекции серий
- Область одной точки в коллекции серий

В следующем фрагменте кода демонстрируется, как установить область диаграммы.

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
            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

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
            chart.plotArea.area.foregroundColor = new AsposeCells.Color(0, 0, 255);

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = new AsposeCells.Color(255, 255, 0);

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = new AsposeCells.Color(255, 0, 0);

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = new AsposeCells.Color(0, 255, 255);

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient = [new AsposeCells.Color(0, 255, 0), 1, AsposeCells.GradientStyleType.Horizontal, 1];

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```

### **Установка линий диаграммы**
Разработчики также могут применять различные стили к линиям или маркерам данных в [SeriesCollection](https://reference.aspose.com/cells/javascript-cpp/seriescollection/). Следующий пример показывает, как установить линии графика с помощью API Aspose.Cells.

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
            // Instantiating a Workbook object
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

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = AsposeCells.Color.Blue;

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = AsposeCells.Color.Red;

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = AsposeCells.Color.Cyan;

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient = [AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1];

            // Applying a dotted line style on the lines of a SeriesCollection
            chart.nSeries.get(0).border.style = AsposeCells.LineType.Dot;

            // Applying a triangular marker style on the data markers of a SeriesCollection
            chart.nSeries.get(0).marker.markerStyle = AsposeCells.ChartMarkerType.Triangle;

            // Setting the weight of all lines in a SeriesCollection to medium
            chart.nSeries.get(1).border.weight = AsposeCells.WeightType.MediumLine;

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

### **Применение тем Microsoft Excel 2007/2010 к диаграммам**
Разработчики могут применять различные темы/цвета Microsoft Excel к [SeriesCollection](https://reference.aspose.com/cells/javascript-cpp/seriescollection/) или другим объектам графика, как показано ниже в примере.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update Chart Series Fill Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FillType, ThemeColor, ThemeColorType } = AsposeCells;

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

            // Loads the workbook containing the chart
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the first chart in the sheet
            const chart = worksheet.charts.get(0);

            // Specify the FillFormat's type to Solid Fill of the first series
            const series = chart.nSeries.get(0);
            series.area.fillFormat.fillType = FillType.Solid;

            // Get the CellsColor of SolidFill
            const cc = series.area.fillFormat.solidFill.cellsColor;

            // Create a theme in Accent style
            cc.themeColor = new ThemeColor(ThemeColorType.Accent6, 0.6);

            // Apply the theme to the series
            series.area.fillFormat.solidFill.cellsColor = cc;

            // Save the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart series fill updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Настройка заголовков диаграмм или осей**
Вы можете использовать Microsoft Excel для установки заголовков графика и его осей в среде WYSIWYG. Aspose.Cells также позволяет разработчикам назначать заголовки графика и его осей во время выполнения. Все графики и их оси содержат свойство [Title](https://reference.aspose.com/cells/javascript-cpp/title/), которое можно использовать для установки их заголовков, как показано в примере ниже.

 Следующий фрагмент кода демонстрирует, как задавать названия диаграмм и осей.

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
        const { Workbook, SaveFormat, ChartType, GradientStyleType, Color } = AsposeCells;

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
            // Creating a new Workbook object
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
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = Color.Blue;

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = Color.Yellow;

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = Color.Red;

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = Color.Cyan;

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient = [Color.Lime, 1, GradientStyleType.Horizontal, 1];

            // Setting the title of a chart
            chart.title.text = "Title";

            // Setting the font color of the chart title to blue
            chart.title.font.color = Color.Blue;

            // Setting the title of category axis of the chart
            chart.categoryAxis.title.text = "Category";

            // Setting the title of value axis of the chart
            chart.valueAxis.title.text = "Value";

            // Saving the Excel file and creating a download link
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

### **Работа с основными линиями сетки**
Есть возможность настраивать внешний вид основных линий сетки. Скрыть или показать линии сетки или определить их цвет и другие настройки. Ниже показано, как скрыть линии сетки и как изменить их цвет.

#### **Скрытие основных линий сетки**
Разработчики могут управлять видимостью основных линий сетки, устанавливая свойство [isVisible()](https://reference.aspose.com/cells/javascript-cpp/line/#isVisible--) объекта [Line](https://reference.aspose.com/cells/javascript-cpp/line/) в **true** или **false**.

Следующий фрагмент кода показывает, как скрыть основные линии сетки. После скрытия основных линий сетки, в рабочий лист будет добавлена столбцовая диаграмма без линий сетки.

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

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = AsposeCells.Color.Blue;

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = AsposeCells.Color.Red;

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = AsposeCells.Color.Cyan;

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient = [AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1];

            // Hiding the major gridlines of Category Axis
            chart.categoryAxis.majorGridLines.isVisible = false;

            // Hiding the major gridlines of Value Axis
            chart.valueAxis.majorGridLines.isVisible = false;

            // Saving the Excel file and preparing download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **Изменение настроек основных линий сетки**
Разработчики могут не только контролировать видимость основных линий сетки, но и другие свойства, включая их цвет и т.д.

Следующий фрагмент кода демонстрирует, как изменить цвет основных линий сетки. После установки цвета основных линий сетки, будет добавлена столбцовая диаграмма с изменёнными линиями сетки.

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

            document.getElementById('runExample').addEventListener('click', async () => {
                // Creating a new Workbook object
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
                chart.nSeries.get(1).area.fillFormat.oneColorGradient = [AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1];

                // Setting the color of Category Axis' major gridlines to silver
                chart.categoryAxis.majorGridLines.color = AsposeCells.Color.Silver;

                // Setting the color of Value Axis' major gridlines to red
                chart.valueAxis.majorGridLines.color = AsposeCells.Color.Red;

                // Saving the Excel file and creating download link
                const outputData = workbook.save(SaveFormat.Excel97To2003);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'book1.out.xls';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
            });
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Установить код формата значений серии графика](/cells/ru/javascript-cpp/set-the-values-format-code-of-chart-series/)
- [Установите изображение в качестве фона в диаграмме](/cells/ru/javascript-cpp/set-picture-as-background-fill-in-the-chart/)
