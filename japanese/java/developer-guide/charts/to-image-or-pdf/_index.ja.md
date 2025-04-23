---
title: チャートのレンダリング
linktitle: 画像またはPDFへの変換
type: docs
weight: 40
url: /ja/java/chart-rendering/
---

## **チャートの作成**

Aspose.CellsのAPIは、[Creating & Customizing Excel Charts](/cells/ja/java/creating-and-customizing-charts/)で詳細に説明されているように、さまざまな種類のExcelチャートの作成をサポートしています。Aspose.CellsのAPIを使用してチャートを画像やPDF形式にレンダリングする方法を示すために、以下のスニペットに従って列のタイプのチャートを作成します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **チャートのレンダリング**

Aspose.CellsのAPIは、追加のツールやアプリケーションを必要とせずにExcelチャートを画像やPDF形式に変換することをサポートしています。レンダリングのサポートを提供するために、[**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)クラスはさまざまなオーバーロードを持つ[**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-)および[**toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf-java.io.OutputStream-)メソッドを公開しています。これにより、アプリケーションの要件に最適なオーバーロードを使用できます。

### **画像へのチャートのレンダリング**

[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-)メソッドは、シンプルな操作から高度なレンダリングまでをサポートするさまざまなオーバーロードを備えています。チャートをデフォルトのサイズでレンダリングする必要がある場合は、次のように[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-)メソッドを使用することをお勧めします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

また、高度な設定でチャートを画像にレンダリングすることも可能です。Aspose.CellsのAPIでは、インスタンスを受け入れて解像度、レンダリングヒント、画像フォーマットなどのパラメータを指定できる[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-)メソッドのオーバーロードバージョンを公開しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **PDFへのチャートのレンダリング**

チャートをPDF形式にレンダリングするために、Aspose.CellsのAPIはディスクパスに結果のPDFを保存する能力を持つ[**Chart.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf-java.io.OutputStream-)メソッドを公開しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **レンダリングにサポートされているチャートの種類**

現在レンダリングをサポートしていないチャートのタイプもいくつかあります。そのようなチャートタイプには、以下の表の**Supported**列に**N**が含まれています。

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
- [SVG形式でチャートを画像に変換](/cells/ja/java/converting-chart-to-image-in-svg-format/)
- [希望のページサイズでチャートPDFを作成](/cells/ja/java/create-chart-pdf-with-desired-page-size/)
- [viewBox属性を使用してチャートをSVGにエクスポート](/cells/ja/java/export-chart-to-svg-with-viewbox-attribute/)
{{< app/cells/assistant language="java" >}}
