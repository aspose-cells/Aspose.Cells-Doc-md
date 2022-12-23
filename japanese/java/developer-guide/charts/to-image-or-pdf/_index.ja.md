---
title: チャートのレンダリング
linktitle: 画像またはPDFへ
type: docs
weight: 40
url: /ja/java/chart-rendering/
---
## **チャートの作成**

Aspose.Cells API は、トピックで詳述されているように、Excel チャートの真正性を作成することをサポートします[Excel チャートの作成とカスタマイズ](/cells/ja/java/creating-and-customizing-charts/)Aspose.Cells API を使用して画像と PDF 形式でグラフをレンダリングする方法を示すために、次のスニペットに従って列タイプのグラフを作成します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **チャートのレンダリング**

 Aspose.Cells API は、Excel チャートを画像や PDF 形式に変換することをサポートしており、追加のツールやアプリケーションは必要ありません。レンダリングのサポートを提供するために、[**チャート**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)クラスが暴露した[**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) & [**PDFへ**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)アプリケーションの要件に最適なオーバーロードの真正性を備えたメソッド。

### **グラフを画像にレンダリングする**

の[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) メソッドには、単純なレンダリングだけでなく高度なレンダリングもサポートするためのオーバーロードが多数あります。アプリケーション要件がグラフをデフォルトの寸法でレンダリングすることである場合は、[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) 方法は次のとおりです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

詳細設定を使用して、グラフを画像にレンダリングすることもできます。 Aspose.Cells API がオーバーロード バージョンを公開しました[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions) のインスタンスを受け入れることができるメソッド[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)解像度、レンダリングのヒント、画像形式などのパラメータを指定できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **PDF へのレンダリング チャート**

グラフを PDF 形式でレンダリングするために、Aspose.Cells API は[**Chart.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) メソッドを使用して、結果の PDF をディスク パスまたは OutputStream のインスタンスに格納できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **レンダリングでサポートされているグラフの種類**

現在、レンダリングがサポートされていないチャート タイプがいくつかあります。このようなチャート タイプには、次のものが含まれます。** N** の**下表の**列をサポート。

|**グラフの種類**|**チャートのサブタイプ**|**対応**|
|:- |:- |:- |
|**桁**|桁|**はい**|
||積み上げ列|**はい**|
||Column100PercentStacked|**はい**|
||列 3DClustered|**はい**|
||Column3D積み上げ|**はい**|
||Column3D100PercentStacked|**はい**|
||列 3D|**はい**|
|**バー**|バー|**はい**|
||棒積み上げ|**はい**|
||Bar100Percent積み上げ|**はい**|
||Bar3DClustered|**はい**|
||Bar3D積み上げ|**はい**|
||Bar3D100PercentStacked|**はい**|
|**ライン**|ライン|**はい**|
||LineStacked|**はい**|
||Line100PercentStacked|**はい**|
||LineWithDataMarkers|**はい**|
||LineStackedWithDataMarkers|**はい**|
||Line100PercentStackedWithDataMarkers|**はい**|
||Line3D|**はい**|
|**パイ**|パイ|**はい**|
||Pie3D|**はい**|
||パイパイ|**はい**|
||パイ爆発|**はい**|
||Pie3DExploded|**はい**|
||パイバー|**はい**|
|**散布**|散布|**はい**|
||ScatterConnectedByCurvesWithDataMarker|**はい**|
||ScatterConnectedByCurvesWithoutDataMarker|**はい**|
||ScatterConnectedByLinesWithDataMarker|**はい**|
||ScatterConnectedByLinesWithoutDataMarker|**はい**|
|**範囲**|範囲|**はい**|
||エリア積み上げ|**はい**|
||Area100PercentStacked|**はい**|
||エリア3D|**はい**|
||Area3D積み上げ|**はい**|
||Area3D100PercentStacked|**はい**|
|**ドーナツ**|ドーナツ|**はい**|
||ドーナツ爆発|**はい**|
|**レーダー**|レーダー|**はい**|
||RadarWithDataMarkers|**はい**|
||レーダーいっぱい|**はい**|
|**水面**|Surface3D|N|
||SurfaceWireframe3D|N|
||表面輪郭|N|
||SurfaceContourWireframe|N|
|**バブル**|バブル|**はい**|
||バブル3D|N|
|**ストック**|株価高低終値|**はい**|
||株式オープン高低クローズ|**はい**|
||在庫高低終値|**はい**|
||在庫量OpenHighLowClose|**はい**|
|**シリンダー**|シリンダー|**はい**|
||円柱積み上げ|**はい**|
||円柱 100%積み上げ|**はい**|
||円柱棒|**はい**|
||円柱棒積み上げ|**はい**|
||CylindricalBar100PercentStacked|**はい**|
||円筒柱 3D|**はい**|
|**円錐**|円錐|**はい**|
||円錐積み上げ|**はい**|
||円錐 100% 積み上げ|**はい**|
||円錐バー|**はい**|
||円錐棒積み上げ|**はい**|
||ConicalBar100PercentStacked|**はい**|
||ConicalColumn3D|**はい**|
|**ピラミッド**|ピラミッド|**はい**|
||ピラミッド積み上げ|**はい**|
||Pyramid100PercentStacked|**はい**|
||ピラミッドバー|**はい**|
||ピラミッド棒積み上げ|**はい**|
||PyramidBar100PercentStacked|**はい**|
||PyramidColumn3D|**はい**|
|**箱ひげ**|箱ひげ|よ|
|**漏斗**|漏斗|**はい**|
|**パレートライン**|パレートライン|**はい**|
|**サンバースト**|サンバースト|**はい**|
|**ツリーマップ**|ツリーマップ|**はい**|
|**滝**|滝|**はい**|
|**ヒストグラム**|ヒストグラム|よ|
|**地図**|地図|**な**|

{{% alert color="primary" %}}

サポートされていないチャート タイプを画像または PDF にレンダリングしようとすると、サイズが 0 の画像または空白の PDF になる可能性があります。

{{% /alert %}}


## **先行トピック**
- [チャートを SVG 形式の画像に変換する](/cells/ja/java/converting-chart-to-image-in-svg-format/)
- [目的のページ サイズでグラフ PDF を作成する](/cells/ja/java/create-chart-pdf-with-desired-page-size/)
- [viewBox属性を使用してグラフをSVGにエクスポートします](/cells/ja/java/export-chart-to-svg-with-viewbox-attribute/)
