---
title: Agregar marca de agua WordArt al gráfico con JavaScript vía C++
linktitle: Agregar marca de agua WordArt al gráfico
description: Aprende a usar Aspose.Cells for JavaScript vía C++ para añadir una marca de agua WordArt en un gráfico en Microsoft Excel. Nuestra guía demostrará cómo crear y posicionar una marca de agua WordArt para mejorar el atractivo visual y la unicidad de tu gráfico.
keywords: Aspose.Cells for JavaScript, Marca de agua WordArt, Marca de agua del gráfico, Microsoft Excel, Atracción visual, Unicidad del gráfico.
type: docs
weight: 50
url: /es/javascript-cpp/add-wordart-watermark-to-chart/
---

{{% alert color="primary" %}}  

Puede usar WordArt para agregar efectos especiales de texto a las hojas de cálculo. Por ejemplo, estirar un título, decorar texto, hacer que el texto se ajuste a una forma preestablecida o aplicar el texto afectado al área de trazado de un gráfico como marca de agua. El WordArt se convierte en un objeto que puede mover o posicionar en sus hojas de cálculo para agregar decoración.  

El siguiente ejemplo muestra cómo agregar una forma de WordArt como marca de agua para el área de trazado del gráfico.  

{{% /alert %}}  

El siguiente ejemplo muestra cómo agregar una forma de WordArt como marca de agua para el área de trazado de un gráfico existente.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add WordArt Watermark to Chart</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet's first chart
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Add a WordArt watermark (shape) to the chart's plot area
            const wordart = chart.shapes.addTextEffectInChart(AsposeCells.MsoPresetTextEffect.TextEffect2,
                "CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

            // Get the shape's fill format and set transparency
            const wordArtFormat = wordart.fill;
            wordArtFormat.transparency = 0.9;

            // Get the line format and set weight to invisible (0.0)
            const lineFormat = wordart.line;
            lineFormat.weight = 0.0;

            // Save the modified workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">WordArt watermark added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
