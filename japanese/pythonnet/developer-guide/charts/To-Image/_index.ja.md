---
title: グラフをイメージに変換する
description: Aspose.Cells for Python via .NETを使ってチャートを画像形式（JPEGやPNGなど）に変換する方法を学びましょう。ガイドでは、Microsoft Excelからチャートをエクスポートし、スタンドアロンの画像として保存し、追加の利用や操作を行う方法を示します。
keywords: Aspose.Cells for Python via .NET、チャートを画像に変換、Microsoft Excel、画像変換、エクスポート、スタンドアロン画像。
linktitle: グラフをイメージに変換する
type: docs
weight: 46
url: /ja/python-net/chart-to-image/
---

## **チャートのレンダリング**

Aspose.Cells for Python via .NET APIは、追加のツールやアプリケーションを必要とせずにExcelのチャートを画像形式に変換することをサポートしています。レンダリングサポートを提供するために、[**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart)クラスは、アプリケーションの要件に最適な様々なオーバーロードを持つ[**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image)メソッドを公開しています。

### **画像へのチャートのレンダリング**

このメソッドには、シンプルな描画から高度な描画までをサポートする多くのオーバーロードがあります。アプリケーション要件がチャートをデフォルトの寸法で描画することである場合、[**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) メソッドをご利用いただくことをお勧めします。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRendering-ChartRenderingChartToImage.py" >}}

高度な設定を用いてチャートを画像にレンダリングすることも可能です。Aspose.Cells for Python via .NET APIは、[**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image)メソッドのオーバーロードバージョンを公開しており、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/)のインスタンスを受け入れつつ、解像度、スムージングモード、画像フォーマットなどのパラメータを指定できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.py" >}}

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
- [グラフをPDFに変換する](/cells/ja/python-net/chart-to-pdf/)
