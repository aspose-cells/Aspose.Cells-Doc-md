---
title: Использование Sparklines и настроек 3D форматирования с помощью JavaScript через C++
linktitle: Использование мини графиков и настройки 3D формата
type: docs
weight: 40
url: /ru/javascript-cpp/using-sparklines-and-settings-3d-format/
description: Узнайте, как использовать sparklines и применять 3D форматирование в файлах Excel с помощью Aspose.Cells for JavaScript через C++. 
---

## **Использование мини-графиков**
Microsoft Excel 2010 позволяет анализировать информацию более чем когда-либо прежде. С его помощью пользователи могут отслеживать и выделять важные тенденции данных с помощью новых средств анализа и визуализации. Мини-графики - это миниатюрные графики, которые можно разместить внутри ячеек, чтобы одновременно просматривать данные и диаграмму на одной и той же таблице. При правильном использовании мини-графиков анализ данных становится более быстрым и точным. Они также обеспечивают простой просмотр информации, избегая переполненных листов с множеством занятых диаграмм.

Aspose.Cells for JavaScript через C++ предоставляет API для манипулирования sparklines в таблицах.
### **Мини-графики в Microsoft Excel**
Для вставки мини-графиков в Microsoft Excel 2010:

1. Выберите ячейки, где вы хотите разместить мини-графики. Чтобы упростить их просмотр, выберите ячейки сбоку от данных.
1. Нажмите **Вставка** на ленте и затем выберите **столбец** в группе **Мини-графики**.
1. Выберите или введите диапазон ячеек на листе, который содержит исходные данные. Диаграммы появятся.

Мини-графики помогают видеть тенденции, например, победы или поражения в лиге по софтболу. Мини-графики могут даже подвести итоги всего сезона каждой команды в лиге.
### **Sparklines с использованием Aspose.Cells for JavaScript через C++**
Разработчики могут создавать, удалять или читать sparklines (в шаблонных файлах) с помощью API Aspose.Cells for JavaScript через C++. Классы, управляющие sparklines, содержатся в модуле [SparklineGroupCollection](https://reference.aspose.com/cells/javascript-cpp/sparklinegroupcollection/), поэтому перед использованием этих функций необходимо подключить этот модуль.

Добавляя пользовательские графики для определенного диапазона данных, разработчики имеют возможность добавлять различные типы маленьких диаграмм в выбранные области ячеек.

Приведенный ниже пример демонстрирует функцию мини-графиков. Пример показывает, как:

1. Открыть простой файл шаблона.
1. Прочитать информацию о мини-графиках для листа.
1. Добавьте новые искры для определенного диапазона данных в область ячейки.
1. Сохраните файл Excel на диск.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sparkline Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sparkline Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, SparklineType, Color } = AsposeCells;

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

            // Instantiate a Workbook by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Read the Sparklines from the worksheet (if any)
            const sparklinesCount = sheet.sparklineGroups.count;
            let logHtml = '';
            for (let i = 0; i < sparklinesCount; i++) {
                const group = sheet.sparklineGroups.get(i);
                logHtml += `sparkline group: type:${group.type}, sparkline items count:${group.sparklines.count}<br/>`;
                const sparklineCount = group.sparklines.count;
                for (let j = 0; j < sparklineCount; j++) {
                    const sparkline = group.sparklines.get(j);
                    logHtml += `sparkline: row:${sparkline.row}, col:${sparkline.column}, dataRange:${sparkline.dataRange}<br/>`;
                }
            }

            // Add Sparklines
            // Define the CellArea D2:D10 (rows and columns are zero-based: D is column 4 -> index 4)
            const ca = CellArea.createCellArea(1, 4, 7, 4);
            // Add new Sparklines for a data range to a cell area
            const idx = sheet.sparklineGroups.add(SparklineType.Column, "Sheet1!B2:D8", false, ca);
            const newGroup = sheet.sparklineGroups.get(idx);
            // Create CellsColor and set color
            const clr = workbook.createCellsColor();
            clr.color = Color.Orange;
            newGroup.seriesColor = clr;

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p><div>' + logHtml + '</div>';
        });
    </script>
</html>
```
## **Настройка 3D формата**
Вам могут понадобиться стили 3D-графиков, чтобы получать только результаты для вашего сценария. Aspose.Cells for JavaScript через C++ действительно предоставляет соответствующий API для применения 3D-форматирования Microsoft Excel 2007.

Ниже приведен полный пример для демонстрации того, как создать диаграмму и применить форматирование 3D Microsoft Excel 2007. После выполнения примерного кода на листе будет добавлена столбчатая диаграмма (с 3D эффектами).


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>3D Chart Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Color, BevelPresetType, PresetMaterialType, LightRigType } = AsposeCells;

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
            // Creating a new workbook
            const book = new Workbook();

            // Add a Data Worksheet
            const dataSheet = book.worksheets.add("DataSheet");

            // Add Chart Worksheet
            const sheet = book.worksheets.add("MyChart");

            // Put some values into the cells in the data worksheet
            dataSheet.cells.get("B1").value = 1;
            dataSheet.cells.get("B2").value = 2;
            dataSheet.cells.get("B3").value = 3;
            dataSheet.cells.get("A1").value = "A";
            dataSheet.cells.get("A2").value = "B";
            dataSheet.cells.get("A3").value = "C";

            // Define the Chart Collection
            const charts = sheet.charts;
            // Add a Column chart to the Chart Worksheet
            const chartSheetIdx = charts.add(ChartType.Column, 5, 0, 25, 15);

            // Get the newly added Chart
            const chart = book.worksheets.get(2).charts.get(0);

            // Set the background/foreground color for PlotArea/ChartArea
            chart.plotArea.area.backgroundColor = Color.White;
            chart.chartArea.area.backgroundColor = Color.White;
            chart.plotArea.area.foregroundColor = Color.White;
            chart.chartArea.area.foregroundColor = Color.White;

            // Hide the Legend
            chart.showLegend = false;

            // Add Data Series for the Chart
            chart.nSeries.add("DataSheet!B1:B3", true);
            // Specify the Category Data
            chart.nSeries.categoryData = "DataSheet!A1:A3";

            // Get the Data Series
            const ser = chart.nSeries.get(0);

            // Apply the 3-D formatting
            const spPr = ser.shapeProperties;
            const fmt3d = spPr.format3D;

            // Specify Bevel with its height/width
            const bevel = fmt3d.topBevel;
            bevel.type = BevelPresetType.Circle;
            bevel.height = 2;
            bevel.width = 5;

            // Specify Surface material type
            fmt3d.surfaceMaterialType = PresetMaterialType.WarmMatte;

            // Specify surface lighting type
            fmt3d.surfaceLightingType = LightRigType.ThreePoint;

            // Specify lighting angle
            fmt3d.lightingAngle = 20;

            // Specify Series background/foreground and line color
            ser.area.backgroundColor = Color.Maroon;
            ser.area.foregroundColor = Color.Maroon;
            ser.border.color = Color.Maroon;

            // Saving the modified Excel file and providing download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = '3d_format.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
