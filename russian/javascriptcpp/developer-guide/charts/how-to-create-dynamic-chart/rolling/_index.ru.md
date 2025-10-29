---
title: Как создать динамическую скользящую диаграмму с помощью JavaScript через C++
linktitle: Как создать динамическую катящуюся диаграмму
description: Узнайте, как создать динамическую скользящую диаграмму с помощью Aspose.Cells for JavaScript через C++. Наше руководство покажет, как реализовать плавные переходы данных и скользящие средние на вашей диаграмме для непрерывного и обновляемого отображения.
keywords: Aspose.Cells for JavaScript через C++, Динамическая скользящая диаграмма, Переходы данных, Плавные средние, Непрерывное отображение, Обновление визуализации.
type: docs
weight: 74
url: /ru/javascript-cpp/create-dynamic-rolling-chart/
---

## **Возможные сценарии использования**
Динамическая катящаяся диаграмма относится к графическому представлению данных, которое постоянно смещается и обновляется с течением времени. Это тип диаграммы, который постоянно обновляется, показывая катящееся окно последних данных, отбрасывая старые данные по мере поступления новых.

Динамические катящиеся диаграммы часто используются для визуализации тенденций и закономерностей в реальном времени или потоковых данных. Они особенно полезны в сценариях, где временные аспекты и изменения со временем критичны, таких как анализ фондового рынка, мониторинг погоды или отслеживание живой производительности.

Эти диаграммы обычно используют анимацию или автоматическую прокрутку, чтобы обеспечить обновление наиболее актуальной информации. Длина катящегося окна может быть настроена для отображения определенного временного периода, такого как последний час, день или неделя.

В заключение, динамическая катящаяся диаграмма представляет собой непрерывно обновляемое графическое представление, отображающее последние данные и отбрасывающее старые, что позволяет пользователям наблюдать тенденции и закономерности в реальном времени.

## **Используйте Aspose Cells для создания динамической катящейся диаграммы**
В следующих абзацах мы покажем вам, как создать динамическую катящуюся диаграмму с использованием Aspose.Cells. Мы покажем вам код для примера, а также созданный этим кодом файл Excel.

## **Образец кода**
Приведенный ниже образец кода сгенерирует файл [Динамической Карты Прокрутки](DynamicRollingChart.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Rolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Utils } = AsposeCells;

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
            // Create a new workbook and access the first worksheet.
            const workbook = new Workbook();
            const sheets = workbook.worksheets;
            const sheet = sheets.get(0);

            // Populate the data for the chart. Add values to cells and set series names.
            sheet.cells.get("A1").value = "Month";
            sheet.cells.get("A2").value = 1;
            sheet.cells.get("A3").value = 2;
            sheet.cells.get("A4").value = 3;
            sheet.cells.get("A5").value = 4;
            sheet.cells.get("A6").value = 5;
            sheet.cells.get("A7").value = 6;
            sheet.cells.get("A8").value = 7;

            sheet.cells.get("B1").value = "Sales";
            sheet.cells.get("B2").value = 50;
            sheet.cells.get("B3").value = 45;
            sheet.cells.get("B4").value = 55;
            sheet.cells.get("B5").value = 60;
            sheet.cells.get("B6").value = 55;
            sheet.cells.get("B7").value = 65;
            sheet.cells.get("B8").value = 70;

            // Set the dynamic range for the chart's data source.
            let index = sheets.names.add("Sheet1!ChtData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)";

            // Set the dynamic range for the chart's data labels.
            index = sheets.names.add("Sheet1!ChtLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 10, 3, 25, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicRollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Примечания**
В сгенерированном файле вы можете продолжать добавлять данные в столбцах A и B, в то время как диаграмма динамически подсчитывает последние 5 наборов данных. Это делается с использованием формулы "СМЕЩЕНИЕ" в образцовом коде:
