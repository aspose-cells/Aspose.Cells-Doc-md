---
title: 通过 JavaScript 及 C++ 将图表转换为图片
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 转换图表为图片格式，如 JPEG 或 PNG。我们将演示如何从 Microsoft Excel 导出图表并将其保存为独立的图片，以便后续使用和处理。
keywords: 通过 C++ 使用 Aspose.Cells for JavaScript，图表转图片，Microsoft Excel，图像转换，导出，独立图片。
linktitle: 图表转为图像
type: docs
weight: 46
url: /zh/javascript-cpp/chart-to-image/
---

## **渲染图表**

Aspose.Cells API支持将Excel图表转换成图片格式，无需额外工具或应用程序。为了支持渲染，[**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart)类提供了[**toImage(string)**](https://reference.aspose.com/cells/javascript-cpp/chart/#toImage-string-)方法及多种重载以满足不同应用需求。

### **将图表渲染为图像**

[**Chart.toImage(string)**](https://reference.aspose.com/cells/javascript-cpp/chart/#toImage-string-) 方法具有多种重载，以支持简单和高级渲染。如果应用需求是在默认尺寸中渲染图表，建议使用如下 [**Chart.toImage(string)**](https://reference.aspose.com/cells/javascript-cpp/chart/#toImage-string-) 方法：

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

也可以使用高级设置将图表渲染为图片。Aspose.Cells API提供了[**Chart.toImage(string)**](https://reference.aspose.com/cells/javascript-cpp/chart/#toImage-string-)方法的重载版本，接受[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions)实例，同时允许设置分辨率、平滑模式、图片格式等参数。

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

## **支持的图表类型的渲染**

目前有一些不支持渲染的图表类型。这些图表类型在下表的**Supported**列中包含**N**。

|图表类型|图表子类型|支持  
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
如果尝试将不受支持的图表类型渲染为图像或PDF，则可能会得到大小为0的图像或空白PDF。  
{{% /alert %}}  

## **高级主题**  
- [将图表转换为PDF](/cells/zh/javascript-cpp/chart-to-pdf/)
