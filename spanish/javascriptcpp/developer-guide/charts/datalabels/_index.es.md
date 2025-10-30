---
title: Gestiona las etiquetas de datos de gráficos de Excel con JavaScript a través de C++
description: Aprende cómo gestionar eficazmente las etiquetas de datos en gráficos de Excel usando Aspose.Cells for JavaScript via C++. Esta guía completa cubre varias tareas de gestión, incluyendo añadir, quitar y modificar etiquetas para mejorar la legibilidad y usabilidad del gráfico.
keywords: Aspose.Cells for JavaScript, gráficos de Excel, etiquetas de datos, gestión, legibilidad, usabilidad, añadir, eliminar, modificar.
linktitle: Etiquetas de datos
type: docs
weight: 50
url: /es/javascript-cpp/insert-datalabels-to-chart/
---

{{% alert color="primary" %}}  

Las etiquetas de datos son una parte importante de un gráfico.  
Podemos conocer fácilmente el valor, el porcentaje, etc. de cada serie  

{{% /alert %}}  

## **Opciones de etiquetas de datos**  
Aspose.Cells for JavaScript via C++ también permite gestionar las etiquetas de datos del gráfico en tiempo de ejecución, con el objeto [DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/), es sencillo mover, actualizar y formatear las etiquetas del gráfico.  

|![todo:image_alt_text](chart_datalabels.png)|  

## **Administrar las etiquetas de datos del gráfico**  
Es sencillo gestionar las etiquetas de datos del gráfico con Aspose.Cells [DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/).  

El siguiente fragmento de código demuestra cómo gestionar DataLabels.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Data Labels Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        let asposeReady = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeReady = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');
            if (!asposeReady) {
                resultDiv.innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            // Instantiate a new Workbook object
            const workbook = new Workbook();

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
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Show value labels
            chart.nSeries.get(0).dataLabels.showValue = true;
            // Show series name labels
            chart.nSeries.get(1).dataLabels.showSeriesName = true;
            // Move labels to center
            chart.nSeries.get(1).dataLabels.position = AsposeCells.LabelPositionType.Center;

            // Save the file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_datalabels.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Temas avanzados**  
- [Agregar etiquetas personalizadas a los puntos de datos en la serie del gráfico](/cells/es/javascript-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [Deshabilitar el ajuste de texto para las etiquetas de datos del gráfico](/cells/es/javascript-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [Redimensionar la forma de la etiqueta de datos del gráfico para que se ajuste al texto](/cells/es/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [Etiqueta de datos personalizada de texto enriquecido del punto del gráfico](/cells/es/javascript-cpp/rich-text-custom-data-label-of-chart-point/)  
- [Establecer el tipo de forma de las etiquetas de datos del gráfico](/cells/es/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [Mostrar el rango de celdas como las etiquetas de datos](/cells/es/javascript-cpp/showing-cell-range-as-the-data-labels/)
