---
title: チャートから画像へ
description: Aspose.Cells for .NET を使用してグラフを JPEG や PNG などの画像形式に変換する方法について説明します。ガイドでは、Microsoft Excel からグラフをエクスポートし、さらに使用したり操作したりできるようにスタンドアロン画像として保存する方法を説明します。
keywords: Aspose.Cells for .NET, Chart to Image, Microsoft Excel, Image Conversion, Export, Standalone Image.
linktitle: チャートから画像へ
type: docs
weight: 46
url: /ja/net/chart-to-image/
---
##  **レンダリングチャート**

 Aspose.Cells API は、追加のツールやアプリケーションを必要とせずに、Excel グラフを画像形式に変換することをサポートしています。レンダリングのサポートを提供するために、[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)クラスが暴露した[**画像へ**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)アプリケーション要件に最適な多数のオーバーロードを備えたメソッド。

###  **チャートを画像にレンダリングする**

の[**チャート.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)メソッドには、単純なレンダリングだけでなく高度なレンダリングもサポートする多数のオーバーロードがあります。アプリケーションの要件がデフォルトの寸法でグラフをレンダリングすることである場合は、[**チャート.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)以下のような方法で。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

高度な設定を使用してチャートを画像にレンダリングすることもできます。 Aspose.Cells API は、次のオーバーロード バージョンを公開しました。[**チャート.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)のインスタンスを受け入れることができるメソッド[**画像または印刷オプション**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)、解像度、スムージングモード、画像形式などのパラメータを指定できるようにします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

##  **レンダリングでサポートされているグラフの種類**

現在レンダリングがサポートされていないグラフの種類がいくつかあります。このようなグラフの種類には次のものがあります。**** の N** サポートされています**下の表の列。

|**グラフの種類**|**グラフのサブタイプ**|**サポートされています**|
| :- | :- | :- |
|**カラム**|カラム|*はい**|
| |列積み上げ|*はい**|
| |列100パーセント積み上げ|*はい**|
| |列3Dクラスター化|*はい**|
| |列 3D 積み上げ|*はい**|
| |列 3D100 パーセント積み上げ|*はい**|
| |コラム3D|*はい**|
|**バー**|バー|*はい**|
| |バー積み上げ|*はい**|
| |バー100パーセント積み上げ|*はい**|
| |バー3Dクラスター化|*はい**|
| |Bar3D積み上げ|*はい**|
| |Bar3D100パーセント積み上げ|*はい**|
|**ライン**|ライン|*はい**|
| |ラインスタック|*はい**|
| |線100パーセント積み上げ|*はい**|
| |LineWithDataMarkers|*はい**|
| |LineStackedWithDataMarkers|*はい**|
| |Line100PercentStackedWithDataMarkers|*はい**|
| |ライン3D|*はい**|
|**パイ**|パイ|*はい**|
| |パイ3D|*はい**|
| |パイパイ|*はい**|
| |パイ爆発|*はい**|
| |パイ3D分解|*はい**|
| |パイバー|*はい**|
|**散布**|散布|*はい**|
| |ScatterConnectedByCurvesWithDataMarker|*はい**|
| |データマーカーなしの曲線による散乱接続|*はい**|
| |ScatterConnectedByLinesWithDataMarker|*はい**|
| |ScatterConnectedByLinesWithoutDataMarker|*はい**|
|**エリア**|エリア|*はい**|
| |積み上げられたエリア|*はい**|
| |面積100パーセント積み上げ|*はい**|
| |エリア3D|*はい**|
| |エリア3D積み上げ|*はい**|
| |エリア3D100パーセント積み上げ|*はい**|
|**ドーナツ**|ドーナツ|*はい**|
| |ドーナツ爆発|*はい**|
|**レーダー**|レーダー|*はい**|
| |レーダーとデータマーカー|*はい**|
| |レーダー充填済み|*はい**|
|**表面**|表面3D|N|
| |表面ワイヤーフレーム3D|N|
| |表面輪郭|N|
| |表面輪郭ワイヤーフレーム|N|
|**バブル**|バブル|*はい**|
| |バブル3D|N|
|**ストック**|株価高安値終値|*はい**|
| |株価オープン高値安値クローズ|*はい**|
| |株価出来高高安値終値|*はい**|
| |株価出来高オープン高値安値クローズ|*はい**|
|**シリンダー**|シリンダー|*はい**|
| |シリンダー積み上げ|*はい**|
| |シリンダー100パーセント積み上げ|*はい**|
| |円筒形バー|*はい**|
| |円筒形バー積み上げ|*はい**|
| |円柱バー100パーセント積み上げ|*はい**|
| |円柱柱3D|*はい**|
|**円錐**|円錐|*はい**|
| |コーン積み上げ|*はい**|
| |コーン100パーセント積み上げ|*はい**|
| |コニカルバー|*はい**|
| |円錐形バー積み上げ|*はい**|
| |円錐バー100パーセント積み上げ|*はい**|
| |円錐柱3D|*はい**|
|**ピラミッド**|ピラミッド|*はい**|
| |ピラミッド積み上げ|*はい**|
| |ピラミッド100パーセント積み上げ|*はい**|
| |ピラミッドバー|*はい**|
| |ピラミッドバー積み上げ|*はい**|
| |ピラミッドバー100パーセント積み上げ|*はい**|
| |ピラミッド柱3D|*はい**|
|**ボックスウィスカー**|ボックスウィスカー|Y|
|**漏斗**|漏斗|*はい**|
|**パレートライン**|パレートライン|*はい**|
|**サンバースト**|サンバースト|*はい**|
|**ツリーマップ**|ツリーマップ|*はい**|
|**滝**|滝|*はい**|
|**ヒストグラム**|ヒストグラム|Y|
|**地図**|地図|*N**|

{{% alert color="primary" %}}

サポートされていないグラフ タイプを画像または PDF にレンダリングしようとすると、サイズが 0 の画像または空白の PDF が表示される可能性があります。

{{% /alert %}}

##  **アドバンストトピック**
- [チャートを PDF に変換](/cells/ja/net/chart-to-pdf/)
