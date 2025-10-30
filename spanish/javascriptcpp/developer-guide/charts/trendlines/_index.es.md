---
title: Obtener texto de la ecuación de la línea de tendencia del gráfico con JavaScript vía C++
description: Aprende cómo usar Aspose.Cells for JavaScript a través de C++ para recuperar el texto de la ecuación de una línea de tendencia en un gráfico creado en Microsoft Excel. Nuestra guía demostrará cómo acceder y extraer la ecuación de una línea de tendencia para un análisis o visualización posterior.
keywords: Aspose.Cells for JavaScript a través de C++, Línea de tendencia del gráfico, Texto de la ecuación, Microsoft Excel, Análisis de datos, Visualización.
linktitle: Líneas de tendencia
type: docs
weight: 110
url: /es/javascript-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

 Puedes recuperar el Texto de la Ecuación de la Línea de tendencia del gráfico usando Aspose.Cells for JavaScript vía C++. Aspose.Cells proporciona la propiedad [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--) que devuelve el Texto de la Ecuación de la línea de tendencia del gráfico. Para usar esta propiedad, primero deberás llamar al método [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--).

{{% /alert %}}

La siguiente captura muestra el gráfico con una línea de tendencia y su texto de ecuación en color rojo. Nosotros recuperaremos este texto usando la propiedad [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--) en el siguiente ejemplo de código.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Código en JavaScript para obtener el texto de la ecuación de la línea de tendencia del gráfico

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Trendline Equation Example</h1>
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

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Calculate the Chart to get the Equation Text of Trendline
            chart.calculate();

            // Access the Trendline
            const trendLine = chart.nSeries.get(0).trendLines.get(0);

            // Read the Equation Text of Trendline
            const equationText = trendLine.dataLabels.text;

            document.getElementById('result').innerHTML = `<p>Equation Text: ${equationText}</p>`;
        });
    </script>
</html>
```

Resultado generado por el código de ejemplo

Este es el resultado de consola del código de ejemplo anterior.

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
