---
title: Establecer el texto de la entrada de leyenda del gráfico a ninguno usando Aspose.Cells for JavaScript vía C++
linktitle: Establecer el texto de relleno de entrada de leyenda del gráfico a ninguno usando Aspose.Cells
description: Aprende a usar Aspose.Cells for JavaScript vía C++ para establecer que el relleno de una entrada de leyenda de gráfico sea ninguno. Esta guía demostrará cómo modificar el color de relleno de las entradas de leyenda en gráficos de Microsoft Excel para una mejor visualización y personalización.
keywords: Aspose.Cells for JavaScript vía C++, Relleno de entradas de leyenda de gráfico, Microsoft Excel, Visualización, Personalización.
type: docs
weight: 320
url: /es/javascript-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Si deseas configurar el texto del relleno de la entrada de la leyenda del gráfico a ninguno para que no se muestre dentro de la leyenda del gráfico, establece [**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/javascript-cpp/legendentry/#isTextNoFill--) en **true**.

{{% /alert %}}

El siguiente código de muestra establece el texto del relleno de la segunda entrada de leyenda del gráfico en ninguno. Descargue el [archivo de Excel de muestra](5115219.xlsx) utilizado en este código y el [archivo de Excel de salida](5115217.xlsx) generado por él para su referencia.

La siguiente captura de pantalla resalta el efecto de este código en el archivo de Excel de muestra (5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Legend Entry Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the first chart inside the sheet
            const chart = sheet.charts.get(0);

            // Set text of second legend entry fill to none
            const legendEntry = chart.legend.legendEntries.get(1);
            legendEntry.isTextNoFill = true;

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ChartLegendEntry_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
