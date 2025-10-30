---
title: Crear Gráfico de Acciones Open High Low Close (OHLC) con JavaScript vía C++
description: Aprenda cómo crear un gráfico de acciones open high low close usando Aspose.Cells for JavaScript vía C++. Nuestra guía demostrará cómo graficar datos del mercado, incluyendo precio de apertura, máximo, mínimo y cierre en un gráfico para mejor análisis y visualización.
keywords: Aspose.Cells for JavaScript vía C++, Gráfico de Acciones Open High Low Close, Datos del Mercado de Valores, Análisis, Visualización.
type: docs
weight: 182
url: /es/javascript-cpp/create-open-high-low-close-stock-chart/
---

## **Escenarios de uso posibles**
El gráfico de cotizaciones apertura-alta-baja-cierre (OHLC) utiliza cinco columnas de datos, en orden: categoría, apertura, alta, baja y cierre. El rango de precios en cada categoría nuevamente se indica con una línea vertical, mientras que el rango entre la apertura y el cierre se muestra con una barra flotante más ancha; si el precio aumenta en la categoría (el cierre es mayor que la apertura), la barra se llena de un color, mientras que si el precio disminuye, la barra se llena de otro. Este tipo de gráfico a menudo se llama gráfico de velas.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Mejoras de visibilidad en el gráfico**
A menudo usamos colores en lugar de blanco y negro para indicar precios en aumento y en disminución. En el primer conjunto de velas abajo, el rojo muestra precios en aumento y el verde en disminución.

![todo:image_alt_text](sample2.png)
## **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de ejemplo](Open-High-Low-Close.xlsx) y genera el [archivo de Excel de salida](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open-High-Low-Close Stock Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Accessing the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockOpenHighLowClose, 5, 6, 20, 12);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);

            // Set the legend can be showed
            chart.showLegend = true;

            // Set the chart title name 
            chart.title.text = "Open-High-Low-Close Stock";

            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set data range
            chart.chartDataRange = ["A1:E9", true];

            // Set category data 
            chart.nSeries.categoryData = "A2:A9";

            // Set the DownBars and UpBars with different color
            chart.nSeries.get(0).downBars.area.foregroundColor = AsposeCells.Color.Green;
            chart.nSeries.get(0).upBars.area.foregroundColor = AsposeCells.Color.Red;

            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
