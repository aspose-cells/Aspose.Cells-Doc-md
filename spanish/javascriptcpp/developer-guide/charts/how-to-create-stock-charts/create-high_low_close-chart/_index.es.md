---
title: Crear Gráfico de Acciones High Low Close (HLC) con JavaScript vía C++
linktitle: Crear Gráfico de Cotizaciones Altas Bajas Cierre (HLC)
description: Aprenda cómo crear un gráfico de acciones high low close utilizando Aspose.Cells for JavaScript vía C++. Nuestra guía paso a paso demostrará cómo graficar datos del mercado de valores, incluyendo los precios máximo, mínimo y de cierre, para un mejor análisis y visualización.
keywords: Aspose.Cells for JavaScript vía C++, Gráfico de Acciones High Low Close, Datos del Mercado de Valores, Análisis, Visualización.
type: docs
weight: 181
url: /es/javascript-cpp/create-high-low-close-stock-chart/
---

## **Escenarios de uso posibles**  
El gráfico de acciones Máximo-Mínimo-Cierre (HLC) usa cuatro columnas de datos. La primera columna es una categoría, generalmente una fecha, aunque también pueden usarse nombres de acciones. Las siguientes tres columnas en orden son para precios máximos, mínimos y de cierre. El rango de precios para cada categoría se indica con una línea vertical de mínimo a máximo, y el precio de cierre se muestra con una marca en forma de tick extendiéndose a la derecha de esta línea.  

![todo:image_alt_text](sample.png)  
## **Mejoras de visibilidad en el gráfico**  
A veces, para que el gráfico luzca más intuitivo, podemos modificar la apariencia del marcador (cierre), o hacer que se muestre en el eje secundario.  

![todo:image_alt_text](sample2.png)  
## **Código de muestra**  
El siguiente código de ejemplo carga el [archivo de Excel de muestra](High-Low-Close.xlsx) y genera el [archivo de Excel de salida](out.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>High-Low-Close Stock Chart Example</h1>
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

            // Create an instance of Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockHighLowClose, 5, 6, 20, 12);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);

            // Set the legend can be showed
            chart.showLegend = true;

            // Set the chart title name 
            chart.title.text = "High-Low-Close Stock";

            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set data range (range and orientation)
            chart.chartDataRange = ["A1:D9", true];

            // Set category data 
            chart.nSeries.categoryData = "A2:A9";

            // Set the marker with the built-in data for the 3rd series (index 2)
            const series2 = chart.nSeries.get(2);
            const marker = series2.marker;
            marker.markerStyle = AsposeCells.ChartMarkerType.Dash;
            marker.markerSize = 20;
            marker.area.formatting = AsposeCells.FormattingType.Custom;
            marker.area.foregroundColor = AsposeCells.Color.Maroon;

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
