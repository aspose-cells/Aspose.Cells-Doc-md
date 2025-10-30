---
title: Gráfico a Imagen con JavaScript vía C++
description: Aprenda cómo usar Aspose.Cells for JavaScript vía C++ para convertir un gráfico en un formato de imagen, como JPEG o PNG. Nuestra guía demostrará cómo exportar un gráfico de Microsoft Excel y guardarlo como una imagen independiente para su posterior uso y manipulación.
keywords: Aspose.Cells for JavaScript vía C++, gráfico a imagen, Microsoft Excel, conversión de imágenes, exportación, imagen independiente.
linktitle: Gráfico a Imagen
type: docs
weight: 46
url: /es/javascript-cpp/chart-to-image/
---

## **Renderización de Gráficos**

Las API de Aspose.Cells admiten convertir gráficos de Excel a formatos de imagen sin necesidad de herramientas o aplicaciones adicionales. Para proporcionar soporte de renderizado, la clase [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart) expone métodos [**toImage(string)**](https://reference.aspose.com/cells/javascript-cpp/chart/#toImage-string-) con varias sobrecargas para adaptarse mejor a los requisitos de la aplicación.

### **Renderizar Gráficos a Imágenes**

El método [**Chart.toImage(string)**](https://reference.aspose.com/cells/javascript-cpp/chart/#toImage-string-) tiene varias sobrecargas para soportar renderizado simple y avanzado. Si el requisito de la aplicación es renderizar el gráfico en sus dimensiones predeterminadas, sugerimos usar el método [**Chart.toImage(string)**](https://reference.aspose.com/cells/javascript-cpp/chart/#toImage-string-) de la siguiente manera.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <br/><br/>
        <a id="downloadLinkEMF" style="display: none; margin-right: 10px;">Download EMF Image</a>
        <a id="downloadLinkBMP" style="display: none;">Download BMP Image</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, ImageType } = AsposeCells;

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
            // This example does not require an input file; an empty workbook is created as in the original JavaScript example.

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its index to WorksheetCollection
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Converting chart to image (EMF)
            const emfData = chart.toImage(ImageType.Emf);
            const emfBlob = new Blob([emfData], { type: "image/emf" });
            const downloadLinkEMF = document.getElementById('downloadLinkEMF');
            downloadLinkEMF.href = URL.createObjectURL(emfBlob);
            downloadLinkEMF.download = 'chartEMF_out.emf';
            downloadLinkEMF.style.display = 'inline-block';
            downloadLinkEMF.textContent = 'Download EMF Image';

            // Converting chart to Bitmap (BMP)
            const bmpData = chart.toImage(ImageType.Bmp);
            const bmpBlob = new Blob([bmpData], { type: "image/bmp" });
            const downloadLinkBMP = document.getElementById('downloadLinkBMP');
            downloadLinkBMP.href = URL.createObjectURL(bmpBlob);
            downloadLinkBMP.download = 'chartBMP_out.bmp';
            downloadLinkBMP.style.display = 'inline-block';
            downloadLinkBMP.textContent = 'Download BMP Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart images created. Click the download links to save them.</p>';
        });
    </script>
</html>
```

También es posible renderizar gráficos en imágenes con configuraciones avanzadas. Las API de Aspose.Cells han expuesto una versión sobrecargada del método [**Chart.toImage(string)**](https://reference.aspose.com/cells/javascript-cpp/chart/#toImage-string-) que acepta una instancia de [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions), permitiendo además especificar parámetros como resolución, modo de suavizado, formato de imagen, etc.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Chart and Export as PNG</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, ImageOrPrintOptions, ImageFormat } = AsposeCells;

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
            // Creating a new Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook
            const sheetIndex = workbook.worksheets.add();
            // Obtaining the reference of the newly added worksheet by passing its index to WorksheetCollection
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);
            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);
            // Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Create an instance of ImageOrPrintOptions and set a few properties
            const options = new ImageOrPrintOptions();
            options.verticalResolution = 300;
            options.horizontalResolution = 300;
            options.imageFormat = ImageFormat.Png;

            // Convert chart to image with additional settings
            const imageData = chart.toImage(options);
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chartPNG_out.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart PNG';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart exported successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```

## **Tipos de Gráficos Soportados para Renderizado**

Hay algunos tipos de gráficos que actualmente no están soportados para el renderizado. Dichos tipos de gráficos contienen **N** en la columna **Soportado** de la siguiente tabla.

|**Tipo de Gráfico**|**Subtipo de Gráfico**|**Soportado**|  
| :- | :- | :- |  
|**Column**|Column|**Y**|  
| |ColumnStacked|**Y**|  
| |Column100PercentStacked|**Y**|  
| |Column3DClustered|**Y**|  
| |Column3DStacked|**Y**|  
| |Column3D100PercentStacked|**Y**|  
| |Column3D|**Y**|  
|**Bar**|Bar|**Y**|  
| |BarStacked|**Y**|  
| |Bar100PercentStacked|**Y**|  
| |Bar3DClustered|**Y**|  
| |Bar3DStacked|**Y**|  
| |Bar3D100PercentStacked|**Y**|  
|**Line**|Line|**Y**|  
| |LineStacked|**Y**|  
| |Line100PercentStacked|**Y**|  
| |LineWithDataMarkers|**Y**|  
| |LineStackedWithDataMarkers|**Y**|  
| |Line100PercentStackedWithDataMarkers|**Y**|  
| |Line3D|**Y**|  
|**Pie**|Pie|**Y**|  
| |Pie3D|**Y**|  
| |PiePie|**Y**|  
| |PieExploded|**Y**|  
| |Pie3DExploded|**Y**|  
| |PieBar|**Y**|  
|**Scatter**|Scatter|**Y**|  
| |ScatterConnectedByCurvesWithDataMarker|**Y**|  
| |ScatterConnectedByCurvesWithoutDataMarker|**Y**|  
| |ScatterConnectedByLinesWithDataMarker|**Y**|  
| |ScatterConnectedByLinesWithoutDataMarker|**Y**|  
|**Area**|Area|**Y**|  
| |AreaStacked|**Y**|  
| |Area100PercentStacked|**Y**|  
| |Area3D|**Y**|  
| |Area3DStacked|**Y**|  
| |Area3D100PercentStacked|**Y**|  
|**Doughnut**|Doughnut|**Y**|  
| |DoughnutExploded|**Y**|  
|**Radar**|Radar|**Y**|  
| |RadarWithDataMarkers|**Y**|  
| |RadarFilled|**Y**|  
|**Surface**|Surface3D|N|  
| |SurfaceWireframe3D|N|  
| |SurfaceContour|N|  
| |SurfaceContourWireframe|N|  
|**Bubble**|Bubble|**Y**|  
| |Bubble3D|N|  
|**Stock**|StockHighLowClose|**Y**|  
| |StockOpenHighLowClose|**Y**|  
| |StockVolumeHighLowClose|**Y**|  
| |StockVolumeOpenHighLowClose|**Y**|  
|**Cylinder**|Cylinder|**Y**|  
| |CylinderStacked|**Y**|  
| |Cylinder100PercentStacked|**Y**|  
| |CylindricalBar|**Y**|  
| |CylindricalBarStacked|**Y**|  
| |CylindricalBar100PercentStacked|**Y**|  
| |CylindricalColumn3D|**Y**|  
|**Cone**|Cone|**Y**|  
| |ConeStacked|**Y**|  
| |Cone100PercentStacked|**Y**|  
| |ConicalBar|**Y**|  
| |ConicalBarStacked|**Y**|  
| |ConicalBar100PercentStacked|**Y**|  
| |ConicalColumn3D|**Y**|  
|**Pyramid**|Pyramid|**Y**|  
| |PyramidStacked|**Y**|  
| |Pyramid100PercentStacked|**Y**|  
| |PyramidBar|**Y**|  
| |PyramidBarStacked|**Y**|  
| |PyramidBar100PercentStacked|**Y**|  
| |PyramidColumn3D|**Y**|  
|**BoxWhisker**|BoxWhisker|Y|  
|**Funnel**|Funnel|**Y**|  
|**ParetoLine**|ParetoLine|**Y**|  
|**Sunburst**|Sunburst|**Y**|  
|**Treemap**|Treemap|**Y**|  
|**Waterfall**|Waterfall|**Y**|  
|**Histogram**|Histogram|Y|  
|**Map**|Map|**N**|  

{{% alert color="primary" %}}  
En caso de intentar renderizar los tipos de gráficos no soportados a imagen o PDF, es posible que se obtengan imágenes de tamaño 0 o PDF en blanco.  
{{% /alert %}}  

## **Temas avanzados**  
- [Convertir Gráfico a PDF](/cells/es/javascript-cpp/chart-to-pdf/)
