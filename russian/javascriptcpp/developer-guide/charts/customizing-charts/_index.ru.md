---
title: Настройка графиков с помощью JavaScript через C++
linktitle: Настройка диаграмм
description: Узнайте, как настраивать графики в Aspose.Cells for JavaScript на C++. Наше руководство покажет, как изменять макеты графиков, добавлять и форматировать серии данных, настраивать оси и применять различные параметры форматирования для улучшения внешнего вида и удобства использования ваших графиков.
keywords: Aspose.Cells for JavaScript на C++, построение графиков, настройка, макеты, серии данных, оси, форматирование, внешний вид, удобство использования.
type: docs
weight: 40
url: /ru/javascript-cpp/customizing-charts/
---

## **Создание настраиваемых диаграмм**  

До настоящего времени, когда мы говорили о графиках, мы рассматривали стандартные графики с их стандартными настройками форматирования. Мы просто задаём источник данных, устанавливаем несколько свойств, и график создаётся с настройками по умолчанию. Но API Aspose.Cells поддерживает также создание пользовательских графиков, позволяющих разработчикам создавать графики с собственными настройками форматирования.  

Разработчики могут создавать пользовательские графики во время выполнения с использованием Aspose.Cells.  

График состоит из серии данных. Каждая серия данных в Aspose.Cells представлена объектом [**Series**](https://reference.aspose.com/cells/javascript-cpp/series), тогда как объект [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection) служит коллекцией [**Series**](https://reference.aspose.com/cells/javascript-cpp/series) объектов. При создании пользовательского графика разработчики имеют возможность использовать разные типы графиков для разных серий данных (собранных в объекте [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection)).  

Приведенный ниже пример кода демонстрирует, как создать пользовательские графики. В этом примере мы собираемся использовать столбчатую диаграмму для первой серии данных и линейную диаграмму для второй серии. Результатом будет добавление столбчатой диаграммы, объединенной с линейной диаграммой, на лист.  

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
            // Ensure Aspose.Cells is initialized
            await readyPromise;

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("A4").value = 110;
            worksheet.cells.get("B1").value = 260;
            worksheet.cells.get("B2").value = 12;
            worksheet.cells.get("B3").value = 50;
            worksheet.cells.get("B4").value = 100;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.nSeries.add("A1:B4", true);

            // Setting the chart type of 2nd NSeries to display as line chart
            chart.nSeries.get(1).type = ChartType.Line;

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

{{% alert color="primary" %}}  

В настоящее время Aspose.Cells поддерживает только пользовательские графики, сочетающие диаграммы типа pie, line, column и column stack, однако в будущих версиях будет поддержано больше типов графиков.  

{{% /alert %}}
