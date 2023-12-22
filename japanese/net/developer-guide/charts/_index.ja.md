---
title: グラフの作成と管理
description: Aspose.Cells for .NET を使用して Microsoft Excel でグラフを作成する方法を学びます。このガイドでは、作成できるさまざまな種類のグラフと、その外観と書式をカスタマイズする方法を説明します。
keywords: Aspose.Cells for .NET, Chart Creation, Microsoft Excel, Chart Types, Customization, Appearance, Formatting.
linktitle: チャート
type: docs
weight: 130
url: /ja/net/creating-charts/
description: CSharp で Excel および ODS ファイル用のグラフを作成します。
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

Aspose.Cells を使用すると、さまざまなグラフをスプレッドシートに追加できます。Aspose.Cells は、多くの柔軟なグラフ オブジェクトを提供します。このトピックでは、Aspose.Cells' グラフ作成オブジェクトについて説明します。

{{% /alert %}}

##  **チャートの作成**

###  **単純にグラフを作成する**
次のコード例を使用すると、Aspose.Cells のグラフを簡単に作成できます。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

###  **グラフを作成するために知っておくべきこと**

グラフを作成する前に、Aspose.Cells を使用してグラフを作成するときに役立ついくつかの基本概念を理解することが重要です。

####  **オブジェクトのグラフ化**

Aspose.Cells は、特別なクラスのセットを提供します。[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts)Aspose.Cells でサポートされるグラフを作成するために使用される名前空間。これらのクラスは、グラフの構成要素として機能する *グラフ オブジェクト** を作成するために使用されます。グラフ作成オブジェクトを以下に示します。

- シリーズ。グラフ内の単一のデータ系列。
- 軸、チャートの軸。
- グラフ、単一の Excel グラフ。
- ChartArea、ワークシート内のグラフ領域。
- ChartDataTable、グラフ データ テーブル。
- ChartFrame、チャート内のフレーム オブジェクト。
- ChartPoint: チャート内の一連の単一ポイント。
- ChartPointCollection。1 つの系列内のすべてのポイントを含むコレクション。
- Charts、Chart オブジェクトのコレクション。
- DataLabels。指定されたシリーズのすべての DataLabel オブジェクトのコレクション。
- FillFormat、形状の塗りつぶし形式。
- Floor、3D チャートのフロア。
- レジェンド、チャートのレジェンド。
- ライン、チャートの線。
- SeriesCollection、Series オブジェクトのコレクション。
- TickLabels、チャート軸上の目盛りに関連付けられた目盛りラベル。
- タイトル、チャートまたは軸のタイトル。
- トレンドライン、チャート内のトレンドライン。
- TrendlineCollection は、指定されたデータ シリーズのすべての Trendline オブジェクトのコレクションです。
- 壁、3D チャートの壁。

####  **チャートオブジェクトの使用**

前述したように、すべてのグラフ オブジェクトはそれぞれのクラスのインスタンスであり、特定のタスクを実行するための特定のプロパティとメソッドを提供します。グラフオブジェクトを使用してグラフを作成します。

を使用して、任意のタイプのグラフをワークシートに追加します。[**チャート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts)コレクション。の各項目[**チャート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts)コレクションは、[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)物体。あ[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)object は、チャートの外観をカスタマイズするために必要な他のすべてのチャート オブジェクトをカプセル化します。次のセクションでは、いくつかの基本的なグラフ オブジェクトを使用して単純なグラフを作成する方法を示します。

###  **Aspose.Cellsを使用してグラフを作成**

**手順:**

1. 次のコマンドを使用して、ワークシートのセルにデータを追加します。[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)オブジェクトの[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法。
これはグラフのデータ ソースとして使用されます。
1. を呼び出して、ワークシートにグラフを追加します。[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)コレクションの[**追加**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add)メソッドにカプセル化されている[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)物体。
1. チャートの種類を指定します。[**グラフの種類**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)列挙。
たとえば、以下の例では、[**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)グラフの種類として値を指定します。
1. 新しいものにアクセスする[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)からのオブジェクト[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)インデックスを渡すことによってコレクションを作成します。
1. にカプセル化されたグラフ オブジェクトのいずれかを使用します。[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)チャートを管理するオブジェクト。
以下の例では、[**シリーズコレクション**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)チャート オブジェクトを使用してチャートのデータ ソースを指定します。

ソース データをグラフに追加する場合、データ ソースはセル範囲 (「A1:C3」など)、連続しない一連のセル (「A1、A3、A5」など)、または一連のセルにすることができます。値 (「1、2、3」など)。

これらの一般的な手順により、あらゆるタイプのグラフを作成できます。さまざまなグラフ オブジェクトを使用して、さまざまなグラフを作成します。

Aspose.Cells を使用して、さまざまな種類のグラフを作成できます。Aspose.Cells でサポートされるすべての標準グラフは、という名前の列挙で事前定義されています。[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

事前定義されたグラフのタイプは次のとおりです。

|**グラフの種類**|**説明**|
| :- | :- |
|カラム|集合縦棒グラフを表します|
|列積み上げ|積み上げ縦棒グラフを表します|
|列100パーセント積み上げ|100% 積み上げ縦棒グラフを表します|
|列3Dクラスター化|3D 集合縦棒グラフを表します|
|列 3D 積み上げ|3D 積み上げ縦棒グラフを表します|
|列 3D100 パーセント積み上げ|3D 100% 積み上げ縦棒グラフを表します|
|コラム3D|3D 縦棒グラフを表します|
|バー|集合棒グラフを表します|
|バー積み上げ|積み上げ棒グラフを表します|
|バー100パーセント積み上げ|100% 積み上げ棒グラフを表します|
|バー3Dクラスター化|3D 集合棒グラフを表します|
|Bar3D積み上げ|3D 積み上げ棒グラフを表します|
|Bar3D100パーセント積み上げ|3D 100% 積み上げ棒グラフを表します|
|ライン|折れ線グラフを表します|
|ラインスタック|積み上げ折れ線グラフを表します|
|線100パーセント積み上げ|100% 積み上げ折れ線グラフを表します|
|LineWithDataMarkers|データマーカーを使用して折れ線グラフを表します|
|LineStackedWithDataMarkers|データ マーカーを使用して積み上げ折れ線グラフを表します|
|Line100PercentStackedWithDataMarkers|データ マーカー付きの 100% 積み上げ折れ線グラフを表します|
|ライン3D|3D 折れ線グラフを表します|
|パイ|円グラフを表します|
|パイ3D|3D 円グラフを表します|
|パイパイ|円グラフを表す|
|パイ爆発|展開円グラフを表します|
|パイ3D分解|3D 分解円グラフを表します|
|パイバー|円グラフの棒グラフを表します|
|散布|散布図を表します|
|ScatterConnectedByCurvesWithDataMarker|データ マーカーを使用して曲線で接続された散布図を表します|
|データマーカーなしの曲線による散乱接続|データ マーカーのない、曲線で接続された散布図を表します。|
|ScatterConnectedByLinesWithDataMarker|データ マーカーを使用して線で接続された散布図を表します|
|ScatterConnectedByLinesWithoutDataMarker|データマーカーのない、線で結ばれた散布図を表します。|
|エリア|面グラフを表します|
|積み上げられたエリア|積み上げ面グラフを表します|
|面積100パーセント積み上げ|100% 積み上げ面グラフを表します|
|エリア3D|3D 面グラフを表します|
|エリア3D積み上げ|3D 積み上げ面グラフを表します|
|エリア3D100パーセント積み上げ|3D 100% 積み上げ面グラフを表します|
|ドーナツ|ドーナツ チャートを表します|
|ドーナツ爆発|展開されたドーナツ グラフを表します|
|レーダー|レーダーチャートを表します|
|レーダーとデータマーカー|レーダー チャートをデータ マーカーで表します|
|レーダー充填済み|塗りつぶされたレーダー チャートを表します|
|表面3D|3D 平面図を表します|
|表面ワイヤーフレーム3D|ワイヤーフレーム 3D 曲面チャートを表します|
|表面輪郭|等高線図を表します|
|表面輪郭ワイヤーフレーム|ワイヤーフレーム等高線チャートを表します|
|バブル|バブルチャートを表します|
|バブル3D|3D バブル チャートを表します|
|シリンダー|円柱グラフを表します|
|シリンダー積み上げ|積み上げ円柱グラフを表します|
|シリンダー100パーセント積み上げ|100% 積み上げ円柱グラフを表します|
|円筒形バー|円柱棒グラフを表します。|
|円筒形バー積み上げ|積み上げ円筒棒グラフを表します|
|円柱バー100パーセント積み上げ|100% 積み上げ円筒棒グラフを表します|
|円柱柱3D|3D 円柱柱グラフを表します|
|円錐|円錐グラフを表します|
|コーン積み上げ|積み上げ円錐グラフを表します|
|コーン100パーセント積み上げ|100% 積み上げ円錐グラフを表します|
|コニカルバー|円錐棒グラフを表します|
|円錐形バー積み上げ|積み上げ円錐棒グラフを表します|
|円錐バー100パーセント積み上げ|100% 積み上げ円錐棒グラフを表します|
|円錐柱3D|3D 円錐縦棒グラフを表します|
|ピラミッド|ピラミッドチャートを表します|
|ピラミッド積み上げ|積み上げピラミッド チャートを表します|
|ピラミッド100パーセント積み上げ|100% 積み上げピラミッド チャートを表します|
|ピラミッドバー|ピラミッド棒グラフを表します|
|ピラミッドバー積み上げ|積み上げピラミッド棒グラフを表します|
|ピラミッドバー100パーセント積み上げ|100% 積み上げピラミッド棒グラフを表します|
|ピラミッド柱3D|3D ピラミッド縦棒グラフを表します|
{{% alert color="primary" %}}

セル範囲をデータ ソースとして割り当てる場合は、左上から右下までの範囲のみを設定できます。たとえば、「A1:C3」は有効ですが、「C3:A1」は無効です。

{{% /alert %}}

####  **ピラミッドチャート**

サンプル コードを実行すると、ピラミッド グラフがワークシートに追加されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

####  **折れ線グラフ**

上記の例では、単純に[**グラフの種類**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)に*ライン*折れ線グラフを作成します。完全なソースは以下に提供されます。コードが実行されると、折れ線グラフがワークシートに追加されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

####  **バブルチャート**

バブル チャートを作成するには、[**グラフの種類**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)に設定する必要があります[**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)それに応じて、BubbleSizes、Values、XValues などのいくつかの追加プロパティを設定する必要があります。次のコードを実行すると、バブル チャートがワークシートに追加されます。

####  **データマーカー付き折れ線グラフ**

データマーカーチャートでラインを作成するには、[**グラフの種類**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)に設定する必要があります*ChartType.LineWithDataMarkers*それに応じて、背景領域、シリーズ マーカー、値、XValue などのいくつかの追加プロパティを設定する必要があります。次のコードを実行すると、データ マーカー グラフを含む行がワークシートに追加されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

##  **アドバンストトピック**
- [Excel 2016 グラフの読み取りと操作](/cells/ja/net/read-and-manipulate-excel-2016-charts/)
- [Excel グラフの軸を管理する](/cells/ja/net/chart-axes/)
- [チャートの外観の設定](/cells/ja/net/setting-chart-appearance/)
- [グラフの種類](/cells/ja/net/chart-types/)
- [グラフのカスタマイズ](/cells/ja/net/customizing-charts/)
- [グラフのデータソースを設定する](/cells/ja/net/data-formatting-in-charts/)
- [Excel グラフのデータラベルを管理する](/cells/ja/net/insert-datalabels-to-chart/)
- [スマートマーカーを処理してチャートを生成](/cells/ja/net/generate-chart-by-processing-smart-markers/)
- [チャートのワークシートを取得する](/cells/ja/net/get-worksheet-of-the-chart/)
- [Excel グラフの凡例の管理](/cells/ja/net/chart-legend/)
- [ポジションサイズとデザイナーチャートの操作](/cells/ja/net/manipulate-position-size-and-designer-chart/)
- [引き出し線付きの円グラフの作成](/cells/ja/net/creating-pie-chart-with-leader-lines/)
- [グラフの形状](/cells/ja/net/controls-in-charts/)
- [Excel グラフのタイトルを管理する](/cells/ja/net/chart-and-axis-titles/)
- [チャートのレンダリング](/cells/ja/net/chart-rendering/)
- [チャート近似曲線の数式テキストを取得](/cells/ja/net/get-equation-text-of-chart-trendline/)
