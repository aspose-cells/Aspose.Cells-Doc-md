---
title: JavaScript を使用したチャートの画像変換（C++ 経由）
description: C++ で Aspose.Cells for JavaScript を使用してチャートを JPEG や PNG などの画像形式に変換する方法を学びます。Microsoft Excel からのチャートのエクスポートと、別の画像として保存し、さらなる操作に使用する方法を示します。
keywords: C++ での Aspose.Cells for JavaScript、チャートから画像へ、Microsoft Excel、画像変換、エクスポート、単独画像
linktitle: グラフをイメージに変換する
type: docs
weight: 46
url: /ja/javascript-cpp/chart-to-image/
---

## **チャートのレンダリング**

Aspose.Cells APIは、追加のツールやアプリケーションを必要とせずにExcelチャートを画像フォーマットに変換することをサポートします。レンダリングサポートを提供するために、[**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart)クラスはさまざまなオーバーロードを持つ[**toImage(string)**](https://reference.aspose.com/cells/javascript-cpp/chart/#toImage-string-)メソッドを公開し、アプリケーションの要件に最適な形で対応します。

### **画像へのチャートのレンダリング**

[**Chart.toImage(string)**](https://reference.aspose.com/cells/javascript-cpp/chart/#toImage-string-) メソッドには、シンプルなレンダリングから高度なレンダリングをサポートするためのさまざまなオーバーロードがあります。アプリケーションの要件がチャートをデフォルトの寸法でレンダリングする場合は、次のように [**Chart.toImage(string)**](https://reference.aspose.com/cells/javascript-cpp/chart/#toImage-string-) メソッドを使用することをお勧めします。

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

高度な設定を使用してチャートを画像にレンダリングすることも可能です。Aspose.Cells APIs は、[**Chart.toImage(string)**](https://reference.aspose.com/cells/javascript-cpp/chart/#toImage-string-) メソッドのオーバーロードバージョンを公開しており、ここでは [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions) のインスタンスを受け入れつつ、解像度やスムージングモード、画像フォーマットなどのパラメータを指定できます。

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

## **レンダリングにサポートされているチャートの種類**

現在は描画に対応していないチャートタイプもいくつかあります。そうしたチャートタイプには、以下の表の**サポート**列に**N**が含まれています。

|チャートタイプ|チャートサブタイプ|サポートされているかどうか|  
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
レンダリングでサポートされていないチャートタイプを画像やPDFにレンダリングしようとすると、サイズが0の画像や空白のPDFができる可能性があります。  
{{% /alert %}}  

## **高度なトピック**  
- [グラフをPDFに変換する](/cells/ja/javascript-cpp/chart-to-pdf/)
