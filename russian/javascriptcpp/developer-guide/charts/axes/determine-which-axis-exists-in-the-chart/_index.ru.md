---
title: Определите, какая ось существует на графике с помощью JavaScript через C++
linktitle: Определите, какая ось существует в диаграмме
description: Узнайте, как определить, какая ось существует на графике, созданном с помощью Aspose.Cells for JavaScript через C++. Наш гид поможет вам идентифицировать и получать доступ к различным осям на графике, включая категориальные, значенческие и вторичные оси.
keywords: Aspose.Cells for JavaScript через C++, график, ось, существование, категория, значение, вторичная.
type: docs
weight: 140
url: /ru/javascript-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}  
Иногда пользователю нужно знать, существует ли конкретная ось в Диаграмме. Например, он хочет узнать, существует ли Вторая Значительная Ось внутри диаграммы или нет. Некоторые диаграммы, такие как Круговая, Взрывная круговая, Пирог, Бар-Пирог, 3D-Пирог, 3D-взрывной Пирог, Бублик, Взрывной бублик и т.д., не имеют оси.  

В следующем образце кода демонстрируется использование [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/javascript-cpp/chart/#hasAxis-AxisType-boolean-) для определения, имеет ли образецная диаграмма основную и вторичную категориальные и числовые оси.  
{{% /alert %}}  

Следующий пример кода демонстрирует использование [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/javascript-cpp/chart/#hasAxis-AxisType-boolean-) для определения наличия в образцовой диаграмме Первичной и Вторичной Категориальной и Значительной Оси.  

## Код JavaScript для определения существования оси на графике

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Chart Axes Example</h1>
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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Check if there are any charts before accessing
            const charts = worksheet.charts;
            if (charts.count === 0) {
                resultDiv.innerHTML = '<p>No charts found in the worksheet.</p>';
                return;
            }

            // Access the chart
            const chart = charts.get(0);

            // Determine which axis exists in chart
            let outputs = [];
            let ret = chart.hasAxis(AsposeCells.AxisType.Category, true);
            outputs.push("Has Primary Category Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Category, false);
            outputs.push("Has Secondary Category Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Value, true);
            outputs.push("Has Primary Value Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Value, false);
            outputs.push("Has Secondary Value Axis: " + ret);

            resultDiv.innerHTML = '<p>' + outputs.join('</p><p>') + '</p>';
        });
    </script>
</html>
```

## Консольный вывод, сгенерированный образцовым кодом

Вывод консоли этого кода показан ниже, он показывает true для Первичной Категориальной и Значительной Оси и false для Вторичной Категориальной и Значительной Оси.  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}
