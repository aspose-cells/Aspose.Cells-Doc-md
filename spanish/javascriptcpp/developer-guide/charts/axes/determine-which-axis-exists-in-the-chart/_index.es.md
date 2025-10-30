---
title: Determina qué eje existe en el gráfico con JavaScript a través de C++
linktitle: Determinar qué eje existe en el gráfico
description: Aprende cómo determinar qué eje existe en un gráfico creado con Aspose.Cells for JavaScript mediante C++. Nuestra guía te ayudará a identificar y acceder a los diferentes ejes en un gráfico, incluidos los ejes de categoría, valor y secundarios.
keywords: Aspose.Cells for JavaScript mediante C++, gráfico, eje, existencia, categoría, valor, secundario.
type: docs
weight: 140
url: /es/javascript-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}  
A veces, el usuario necesita saber si un eje en particular existe en el Gráfico. Por ejemplo, quieren saber si un Eje de Valor Secundario existe dentro del gráfico o no. Algunos gráficos como Pastel, Pastel Explotado, Pastel Pastel, Pastel Barra, Pastel 3D, Pastel 3D Explotado, Rosquilla, Rosquilla Explotada, etc., no tienen eje.  

Aspose.Cells proporciona [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/javascript-cpp/chart/#hasAxis-AxisType-boolean-) método para determinar si el gráfico tiene un eje específico o no.  
{{% /alert %}}  

El siguiente código de ejemplo demuestra el uso de [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/javascript-cpp/chart/#hasAxis-AxisType-boolean-) para determinar si el gráfico de muestra tiene Ejes de Categoría y Valor Principales y Secundarios.  

## Código JavaScript para determinar qué eje existe en el gráfico

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

## Salida de consola generada por el código de ejemplo

La salida de la consola del código se muestra a continuación, que muestra verdadero para el Eje de Categoría y Valor Principal y falso para el Eje de Categoría y Valor Secundario.  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}
