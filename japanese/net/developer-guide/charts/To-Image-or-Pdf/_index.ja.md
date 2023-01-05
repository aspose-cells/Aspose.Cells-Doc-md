---
title: チャートのレンダリング
linktitle: 画像またはPDFへ
type: docs
weight: 45
url: /ja/net/chart-rendering/
---
## **チャートのレンダリング**

 Aspose.Cells API は、Excel チャートを画像や PDF 形式に変換することをサポートしており、追加のツールやアプリケーションは必要ありません。レンダリングのサポートを提供するために、[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)クラスが暴露した[**イメージへ**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**PDFへ**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)アプリケーションの要件に最も適したオーバーロードの真実性を持つメソッド。

### **グラフを画像にレンダリングする**

の[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**PDFへ**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)メソッドには、単純なレンダリングだけでなく高度なレンダリングもサポートするための多数のオーバーロードがあります。アプリケーション要件がグラフをデフォルトの寸法でレンダリングすることである場合は、[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)方法は以下の通り。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

詳細設定を使用して、グラフを画像にレンダリングすることもできます。 Aspose.Cells API がオーバーロード バージョンを公開しました[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)のインスタンスを受け入れることができるメソッド[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)、解像度、スムージング モード、画像形式などのパラメータを指定できるようにします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

### **PDF へのレンダリング チャート**

グラフを PDF 形式でレンダリングするために、Aspose.Cells API は[**Chart.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)結果の PDF をディスク パスまたはストリームに格納する機能を備えたメソッド。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

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
- [グラフを目的のページ サイズで PDF に変換する](/cells/ja/net/chart-to-pdf/)
