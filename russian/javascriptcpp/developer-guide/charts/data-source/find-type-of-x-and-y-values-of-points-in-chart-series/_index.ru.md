---
title: Определите тип XY значений точек в серии диаграмм с помощью JavaScript через C++
linktitle: Найдите тип значений X и Y точек в серии графика
description: Узнайте, как определить тип XY значений в точках серии диаграмм, используя Aspose.Cells for JavaScript через C++. В этом руководстве объясняются типы данных и способы доступа к ним для работы с ними в ваших диаграммах.
keywords: Aspose.Cells for JavaScript через C++, создание диаграмм, X значения, Y значения, типы данных, доступ, работа с, серия диаграмм.
type: docs
weight: 150
url: /ru/javascript-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Возможные сценарии использования**  
Иногда бывает полезно узнать тип XY-значений точек диаграммы в серии. Aspose.Cells for JavaScript через C++ предоставляет свойства `ChartPoint.XValueType` и `ChartPoint.YValueType`, которые можно использовать для этой цели. Обратите внимание, что перед использованием этих свойств необходимо вызвать метод `Chart.calculate()`, чтобы данные были актуальными.  

## **Найдите тип значений X и Y точек в серии графика**  
Следующий пример кода загружает [пробный файл Excel](64716905.xlsx) и получает доступ к первой диаграмме внутри первого листа. Затем он вызывает метод `Chart.calculate()` и определяет типы X и Y значений первой точки диаграммы, выводя их в консоль. См. вывод в консоли ниже для справки.  

## **Образец кода**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Find Type Of X and Y Values Of Points In Chart Series</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first chart.
            const chart = worksheet.charts.get(0);

            // Calculate chart data.
            chart.calculate();

            // Access first chart point in the first series.
            const point = chart.nSeries.get(0).points.get(0);

            // Get the types of X and Y values of chart point.
            const xValueType = point.xValueType;
            const yValueType = point.yValueType;

            // Display results
            document.getElementById('result').innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <p>X Value Type: ${xValueType}</p>
                <p>Y Value Type: ${yValueType}</p>
            `;
        });
    </script>
</html>
```  

## **Вывод в консоль**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}
