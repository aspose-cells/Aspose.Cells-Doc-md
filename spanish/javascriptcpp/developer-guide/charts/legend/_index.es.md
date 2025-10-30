---
title: Gestionar la leyenda de gráficos de Excel con JavaScript vía C++
description: Aprende cómo utilizar Aspose.Cells for JavaScript vía C++ para aprovechar y personalizar eficazmente las leyendas de gráficos en Microsoft Excel. Nuestra guía completa explica la funcionalidad de la leyenda, cómo acceder y modificarla, así como cómo mejorar la visualización y comprensión de datos con las leyendas.
keywords: Aspose.Cells for JavaScript vía C++, Leyendas de gráficos, Microsoft Excel, Visualización, Comprensión de datos.
linktitle: Leyenda
type: docs
weight: 50
url: /es/javascript-cpp/chart-legend/
---

## **Opciones de Leyenda**
Aspose.Cells for JavaScript vía C++ también permite gestionar la leyenda de un gráfico en tiempo de ejecución. El objeto [Legend](https://reference.aspose.com/cells/javascript-cpp/legend/) puede ser movido, actualizado y formateado.

|![todo:image_alt_text](chart_legend.png)|

## **Establecimiento de la Leyenda del Gráfico**
Es fácil gestionar la leyenda del gráfico con Aspose.Cells [Legend](https://reference.aspose.com/cells/javascript-cpp/legend/).

El siguiente fragmento de código muestra cómo gestionar la leyenda:


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Legend Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Color, LegendPositionType } = AsposeCells;

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
                // No file selected - a new workbook will be created
            }

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(50);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("B1").putValue(60);
            worksheet.cells.get("B2").putValue(32);
            worksheet.cells.get("B3").putValue(50);

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the title of a chart
            chart.title.text = "Title";

            // Setting the font color of the chart title to blue
            chart.title.font.color = Color.Blue;

            // Move the legend to left
            chart.legend.position = LegendPositionType.Left;

            // Set font color of the legend
            chart.legend.font.color = Color.Blue;

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_legend.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart with legend created successfully! Click the download link to get the workbook.</p>';
        });
    </script>
</html>
```

## **Temas avanzados**
- [Establecer el texto de relleno de entrada de leyenda del gráfico a ninguno usando Aspose.Cells](/cells/es/javascript-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
