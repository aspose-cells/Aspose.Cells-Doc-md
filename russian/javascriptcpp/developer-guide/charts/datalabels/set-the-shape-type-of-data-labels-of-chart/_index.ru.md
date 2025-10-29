---
title: Установить тип фигуры меток данных графика с помощью JavaScript через C++
linktitle: Установка формы меток данных диаграммы
description: Узнайте, как установить тип фигуры меток данных на графиках с помощью Aspose.Cells for JavaScript через C++. В нашем руководстве объясняются доступные типы фигур и как выбрать подходящую форму для ваших меток данных для улучшения презентации и удобства использования.
keywords: Aspose.Cells for JavaScript с помощью C++, построение графиков, метки данных, типы фигур, презентация, удобство использования.
type: docs
weight: 110
url: /ru/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Возможные сценарии использования**
Вы можете изменить тип формы метки данных диаграммы, используя свойство `DataLabels.shapeType`. Оно принимает значение перечисления `DataLabelShapeType` и соответственно меняет тип формы метки данных. Некоторые из его значений:

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **Установка типа формы меток данных диаграммы**
Следующий пример кода изменяет тип формы меток данных диаграммы на `DataLabelShapeType.WedgeEllipseCallout`. Обратите внимание на [пример файла Excel](60489778.xlsx), используемый в этом коде, и на [сгенерированный файл Excel](60489779.xlsx). Скриншот показывает эффект от кода на примере файла Excel.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Образец кода**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Shape Type of Data Labels of Chart Example</title>
    </head>
    <body>
        <h1>Set Shape Type of Data Labels of Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart
            const chart = worksheet.charts.get(0);

            // Accessing the first series
            const series = chart.nSeries.get(0);

            // Set the shape type of data labels i.e. Speech Bubble Oval
            series.dataLabels.shapeType = AsposeCells.DataLabelShapeType.WedgeEllipseCallout;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSetShapeTypeOfDataLabelsOfChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape type set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
