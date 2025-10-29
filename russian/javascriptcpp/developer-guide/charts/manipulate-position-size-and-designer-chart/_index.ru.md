---
title: Манипуляции с позициями, размером и дизайном диаграммы с помощью JavaScript через C++
linktitle: Управление позицией, размером и оформлением диаграммы
description: Узнайте, как использовать Script Aspose.Cells for Java через C++ для эффективного управления положением, размером и дизайном диаграммы в Microsoft Excel. Наш гид покажет, как настроить эти свойства для улучшения макета и визуализации.
keywords: Script Aspose.Cells for Java через C++, позиция, размер, дизайн диаграммы, Microsoft Excel, макет, визуализация.
type: docs
weight: 45
url: /ru/javascript-cpp/manipulate-position-size-and-designer-chart/
---

## **Позиция и размер диаграммы**
 Иногда нужно изменить позицию или размер новой или существующей диаграммы внутри листа. Aspose.Cells предоставляет свойство [Chart.chartObject](https://reference.aspose.com/cells/javascript-cpp/chart/#chartObject--) для этого. Вы можете использовать его дочерние свойства, чтобы изменить размер диаграммы с помощью новых **высоты** и **ширины** или переместить ее с помощью новых координат **X** и **Y**.

### **Управление позицией и размером диаграммы**
Чтобы изменить позицию диаграммы (координаты X, Y) или размер (высота, ширина), используйте эти свойства:

1. [Shape.x](https://reference.aspose.com/cells/javascript-cpp/shape/#x--)
1. [Shape.y](https://reference.aspose.com/cells/javascript-cpp/shape/#y--)
1. [Shape.height](https://reference.aspose.com/cells/javascript-cpp/shape/#height--)
1. [Shape.width](https://reference.aspose.com/cells/javascript-cpp/shape/#width--)

Следующий пример демонстрирует использование вышеуказанных API: он загружает существующую рабочую книгу с графиком на первом листе, затем изменяет размер и позицию графика с помощью Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Resize and Reposition Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the second worksheet in the Excel file (index 1)
            const worksheet = workbook.worksheets.get(1);

            // Load the chart from source worksheet (first chart)
            const chart = worksheet.charts.get(0);

            // Resize the chart
            chart.chartObject.width = 400;
            chart.chartObject.height = 300;

            // Reposition the chart
            chart.chartObject.x = 250;
            chart.chartObject.y = 150;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Chart resized and repositioned successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Манипулирование дизайнерскими диаграммами**
Иногда необходимо манипулировать или изменять графики в шаблонных файлах. Aspose.Cells полностью поддерживает работу с содержимым и элементами дизайнерских графиков. Данные, содержимое графика, фоновое изображение и форматирование можно сохранять с точностью.

### **Манипулирование дизайнерскими диаграммами в файле-шаблоне**
Для управления дизайнерскими графиками в шаблонных файлах используйте API, связанные с графиками. Например, можно использовать свойство Worksheet.charts для получения существующей коллекции графиков в шаблоне.

#### **Создание диаграммы**
В следующем примере показано, как создать пирамидальную диаграмму. Позже мы будем изменять эту диаграмму.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Create Workbook with Pyramid Chart</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            await readyPromise;

            // Instantiating a Workbook object
            const workbook = new Workbook();

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
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and chart added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **Изменение диаграммы**
В следующем примере показано, как изменить существующую диаграмму. В этом примере мы модифицируем созданную выше диаграмму. В полученном выводе обратите внимание, что метка даты одной точки данных установлена на 'Великобритания, 30K'.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pie Chart Data Label Update</title>
    </head>
    <body>
        <h1>Update Pie Chart Data Label Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the second sheet.
            const sheet = workbook.worksheets.get(1);
            const chart = sheet.charts.get(0);

            // Get the data labels in the data series of the third data point.
            const dataLabels = chart.nSeries.get(0).points.get(2).dataLabels;

            // Change the text of the label.
            dataLabels.text = "Unided Kingdom, 400K ";

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Data label updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **Изменение линейной диаграммы в шаблоне конструктора**
В этом примере мы будем изменять линейную диаграмму. Мы добавим несколько рядов данных к существующей диаграмме и изменим цвета их линий.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Series Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const chart = worksheet.charts.get(0);

            // Add the third data series to it.
            chart.nSeries.add("{60, 80, 10}", true);

            // Add another data series (fourth) to it.
            chart.nSeries.add("{0.3, 0.7, 1.2}", true);

            // Plot the fourth data series on the second axis.
            chart.nSeries.get(3).plotOnSecondAxis = true;

            // Change the Border color of the second data series.
            chart.nSeries.get(1).border.color = AsposeCells.Color.Green;

            // Change the Border color of the third data series.
            chart.nSeries.get(2).border.color = AsposeCells.Color.Red;

            // Make the second value axis visible.
            chart.secondValueAxis.isVisible = true;

            // Save the excel file and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
