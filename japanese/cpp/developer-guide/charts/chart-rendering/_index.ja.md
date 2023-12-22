---
title: チャートのレンダリング
type: docs
weight: 30
url: /ja/cpp/chart-rendering/
---
##  **チャートの作成**

Aspose.Cells API は、トピックで詳しく説明されているとおり、Excel グラフの作成をサポートします。[Excel グラフの作成とカスタマイズ](/cells/ja/cpp/creating-and-customizing-charts/)。 Aspose.Cells API を使用してグラフを画像および PDF 形式でレンダリングする方法を示すために、次のスニペットのように列タイプのグラフを作成します。

{{< highlight "cpp" >}}

Aspose::Cells::Startup();

// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");

// Create a new workbook
Workbook workbook;

// Get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// Adding sample values to cells
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"B1").PutValue(4);
worksheet.GetCells().Get(u"B2").PutValue(20);
worksheet.GetCells().Get(u"B3").PutValue(50);

// Adding a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);

// Accessing the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.GetNSeries().Add(u"A1:B3", true);

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";
chart.ToImage(outputChartImage, ImageType::Png);

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

Aspose::Cells::Cleanup();

{{< /highlight >}}

##  **レンダリングチャート**

Aspose.Cells API は、追加のツールやアプリケーションを必要とせずに、Excel グラフを画像および PDF 形式に変換することをサポートします。レンダリングのサポートを提供するために、Chart クラスは、アプリケーション要件に最適な多数のオーバーロードを備えた ToImage メソッドと ToPdf メソッドを公開しました。

###  **チャートを画像にレンダリングする**

Chart.toImage メソッドには、単純なレンダリングだけでなく高度なレンダリングもサポートする多数のオーバーロードがあります。アプリケーションの要件がデフォルトの寸法でグラフをレンダリングすることである場合は、次のように Chart.toImage メソッドを使用することをお勧めします。

{{< highlight "cpp" >}}

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";

// Saving the chart to image file
chart.ToImage(outputChartImage, ImageType::Png);

{{< /highlight >}}

###  **PDFまでのレンダリングチャート**

グラフを PDF 形式でレンダリングするために、Aspose.Cells API は、結果の PDF をディスク パスまたはストリームに保存する機能を備えた Chart.ToPdf メソッドを公開しました。

{{< highlight "cpp" >}}

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

{{< /highlight >}}

##  **レンダリングでサポートされているグラフの種類**

現在レンダリングがサポートされていないグラフの種類がいくつかあります。このようなグラフの種類には次のものがあります。**** の N** サポートされています**下の表の欄。

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
|ストック|株価高安値終値|*はい**|
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
