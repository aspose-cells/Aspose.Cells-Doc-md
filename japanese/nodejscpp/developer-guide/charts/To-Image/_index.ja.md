---  
title: Node.js via C++によるチャートを画像に変換  
description: Aspose.Cells for Node.js via C++を使ってチャートをJPEGやPNGなどの画像フォーマットに変換する方法を学びます。Microsoft Excelからチャートをエクスポートして、独立した画像として保存し、さらなる利用や操作が可能です。  
keywords: Aspose.Cells for Node.js via C++、チャートを画像に変換、Microsoft Excel、画像変換、エクスポート、スタンドアロン画像。  
linktitle: グラフをイメージに変換する  
type: docs  
weight: 46  
url: /ja/nodejs-cpp/chart-to-image/  
---  

## **チャートのレンダリング**

Aspose.Cells APIは、追加のツールやアプリケーションを必要とせずにExcelチャートを画像フォーマットに変換することをサポートします。レンダリングサポートを提供するために、[**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart)クラスはさまざまなオーバーロードを持つ[**toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-)メソッドを公開し、アプリケーションの要件に最適な形で対応します。

### **画像へのチャートのレンダリング**

[**Chart.toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-) メソッドには、シンプルなレンダリングから高度なレンダリングをサポートするためのさまざまなオーバーロードがあります。アプリケーションの要件がチャートをデフォルトの寸法でレンダリングする場合は、次のように [**Chart.toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-) メソッドを使用することをお勧めします。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Adding a new worksheet to the Workbook
const sheetIndex = workbook.getWorksheets().add();
// Obtaining the reference of the newly added worksheet by passing its index to WorksheetCollection
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);
// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Converting chart to image
chart.toImage(path.join(dataDir, "chartEMF_out.emf"), AsposeCells.ImageType.Emf);

// Converting chart to Bitmap
chart.toImage(path.join(dataDir, "chartBMP_out.bmp"), AsposeCells.ImageType.Bmp);
```

高度な設定を使用してチャートを画像にレンダリングすることも可能です。Aspose.Cells APIs は、[**Chart.toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-) メソッドのオーバーロードバージョンを公開しており、ここでは [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions) のインスタンスを受け入れつつ、解像度やスムージングモード、画像フォーマットなどのパラメータを指定できます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Adding a new worksheet to the Workbook
const sheetIndex = workbook.getWorksheets().add();
// Obtaining the reference of the newly added worksheet by passing its index to WorksheetCollection
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);
// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Create an instance of ImageOrPrintOptions and set a few properties
const options = new AsposeCells.ImageOrPrintOptions();
options.setVerticalResolution(300);
options.setHorizontalResolution(300);

// Convert chart to image with additional settings
chart.toImage(path.join(dataDir, "chartPNG_out.png"), options);
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
- [グラフをPDFに変換する](/cells/ja/nodejs-cpp/chart-to-pdf/)  

