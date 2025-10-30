---
title: Gestionar los ejes de los gráficos de Excel con JavaScript mediante C++
description: Aprende cómo configurar los ejes de gráficos en Aspose.Cells for JavaScript mediante C++. Nuestra guía te mostrará cómo ajustar los ejes primarios y secundarios, establecer sus rangos y modificar sus propiedades para mejorar tus gráficos.
keywords: Aspose.Cells for JavaScript vía C++, ejes del gráfico, configuración, ejes primarios, ejes secundarios, rango, propiedades.
linktitle: Ejes
type: docs
weight: 50
url: /es/javascript-cpp/chart-axes/
---

{{% alert color="primary" %}}  

En los gráficos de Excel, hay 3 tipos de ejes:  
1. Eje Horizontal (Categoría): Eje X  
1. Eje Vertical (Valor): Eje Y  
1. Eje de Profundidad (Serie): Eje Z  

{{% /alert %}}  

## **Opciones del Eje**  
Aspose.Cells for JavaScript vía C++ también te permite gestionar los ejes del gráfico en tiempo de ejecución. Con el objeto [Axis](https://reference.aspose.com/cells/javascript-cpp/axis/), puedes cambiar todas las opciones del Eje como se hace en Excel.  

|![todo:image_alt_text](chart_axes.png)|  

## **Administrar Ejes X e Y**  
En los gráficos de Excel, los ejes horizontal y vertical son los dos ejes más populares para usar.  

El siguiente fragmento de código demuestra cómo establecer las opciones de los ejes X e Y.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Chart Axes</title>
    </head>
    <body>
        <h1>Chart Axes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = "Series1";
            worksheet.cells.get("A2").value = 50;
            worksheet.cells.get("A3").value = 100;
            worksheet.cells.get("A4").value = 150;
            worksheet.cells.get("B1").value = "Series2";
            worksheet.cells.get("B2").value = 60;
            worksheet.cells.get("B3").value = 32;
            worksheet.cells.get("B4").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.chartDataRange = ["A1:B4", true];

            // Hiding X axis
            chart.categoryAxis.isVisible = false;

            // Setting max value of Y axis
            chart.valueAxis.maxValue = 200;
            // Setting major unit
            chart.valueAxis.majorUnit = 50;

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_axes.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```  

## **Temas avanzados**  
- [Cambiar la dirección de la etiqueta del eje](/cells/es/javascript-cpp/change-tick-label-direction/)  
- [Determinar qué Eje existe en el Gráfico](/cells/es/javascript-cpp/determine-which-axis-exists-in-the-chart/)  
- [Manejar Unidades Automáticas del Eje del Gráfico como Microsoft Excel](/cells/es/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [Leer etiquetas del eje después de calcular el gráfico](/cells/es/javascript-cpp/read-axis-labels-after-calculating-the-chart/)  
- [Cómo establecer el Eje de Categoría en el Gráfico de Excel](/cells/es/javascript-cpp/how-to-set-category-axis/)
