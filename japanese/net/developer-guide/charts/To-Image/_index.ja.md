---
title: グラフをイメージに変換する
description: Aspose.Cells for .NETを使用して、Microsoft Excelからグラフをエクスポートし、JPEGやPNGなどの画像形式に保存する方法を学びます。当ガイドでは、Microsoft Excelからグラフをエクスポートし、独立した画像として保存する手順を示します。
keywords: Aspose.Cells for .NET, グラフをイメージ, Microsoft Excel, 画像変換, エクスポート, スタンドアロン イメージ
linktitle: グラフをイメージに変換する
type: docs
weight: 46
url: /ja/net/chart-to-image/
---

## **チャートのレンダリング**

Aspose.CellsのAPIは、追加のツールやアプリケーションを必要とせずにExcelのチャートをイメージ形式に変換するサポートを提供しています。描画サポートを提供するため、[**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) クラスは、アプリケーションの要件に最も適したオーバーロードを備えた [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) メソッドを公開しています。

### **画像へのチャートのレンダリング**

このメソッドには、シンプルな描画から高度な描画までをサポートする多くのオーバーロードがあります。アプリケーション要件がチャートをデフォルトの寸法で描画することである場合、[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) メソッドをご利用いただくことをお勧めします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

また、高度な設定でのチャートをイメージに描画することも可能です。Aspose.CellsのAPIは、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) のインスタンスを受け入れるオーバーロードバージョンのメソッドを公開しており、解像度、スムージングモード、画像形式などのパラメータを指定できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

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
- [グラフをPDFに変換する](/cells/ja/net/chart-to-pdf/)
{{< app/cells/assistant language="csharp" >}}
