---
title: グラフのカスタマイズ
type: docs
weight: 15
url: /ja/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---
##  **チャートの作成**

Aspose.Cells を使用すると、さまざまなグラフをスプレッドシートに追加できます。Aspose.Cells は、多くの柔軟なグラフ オブジェクトを提供します。このトピックでは、Aspose.Cells' グラフ作成オブジェクトについて説明します。

###  **単純にグラフを作成する**

次のコード例を使用すると、Aspose.Cells のグラフを簡単に作成できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


###  **グラフを作成するために知っておくべきこと**

グラフを作成する前に、Aspose.Cells を使用してグラフを作成するときに役立ついくつかの基本概念を理解することが重要です。

####  **オブジェクトのグラフ化**

Aspose.Cells は、あらゆる種類のグラフの作成に使用される特別なクラスのセットを提供します。これらのクラスは、グラフの構成要素として機能する *グラフ オブジェクト** を作成するために使用されます。グラフ作成オブジェクトを以下に示します。

- [**軸**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis)、チャートの軸。
- [**チャート**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)、単一の Excel グラフ。
- [**チャートエリア**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea)、ワークシート内のグラフ領域。
- [**チャートデータテーブル**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable)、チャートデータテーブル。
- [**チャートフレーム**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame)、チャート内のフレーム オブジェクト。
- [**チャートポイント**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)、チャート内の一連の単一ポイント。
- [**チャートポイントコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection)、1つのシリーズのすべてのポイントを含むコレクション。
- [**チャートコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)、のコレクション[**チャート**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)オブジェクト。
-  DataLabels、指定されたデータラベル[**シリーズ**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**チャートポイント**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**トレンドライン**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)、など。
- [**フィルフォーマット**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat)、図形の塗りつぶし形式。
- [**床**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor)、3D チャートの床。
- [**伝説**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend)、チャートの凡例。
- [**ライン**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)、チャートの線。
- [**シリーズコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)、のコレクション[**シリーズ**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)オブジェクト。
- [**シリーズ**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)は、グラフ内の単一のデータ系列を表します。
- [**ティックラベル**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels)、グラフ軸上の目盛りに関連付けられた目盛りラベル。
- [**タイトル**](https://reference.aspose.com/cells/java/com.aspose.cells/Title)、グラフまたは軸のタイトル。
- [**トレンドライン**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)、チャート内のトレンドライン。
- [**トレンドラインコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection)、指定されたデータ系列のすべての Trendline オブジェクトのコレクション。
- [**壁**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls)、3D チャートの壁。

####  **チャートオブジェクトの使用**

前述したように、すべてのグラフ オブジェクトはそれぞれのクラスのインスタンスであり、特定のタスクを実行するための特定のプロパティとメソッドを提供します。グラフオブジェクトを使用してグラフを作成します。

を使用して、任意のタイプのグラフをワークシートに追加します。[**チャートコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)コレクション。の各項目[**チャートコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)コレクションは、[**チャート**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)物体。あ[**チャート**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)object は、チャートの外観をカスタマイズするために必要なすべてのチャート オブジェクトをカプセル化します。次のセクションでは、いくつかの基本的なグラフ オブジェクトを使用して単純なグラフを作成する方法を示します。

###  **単純なグラフの作成**

Aspose.Cells を使用して、さまざまな種類のグラフを作成できます。Aspose.Cells でサポートされるすべての標準グラフは、という名前の列挙で事前定義されています。[**グラフの種類**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)。事前定義されたグラフのタイプは次のとおりです。

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
|ScatterConnectedByCurvesWithDataMarker|データ マーカーを使用して曲線で接続された散布図を表します。|
|データマーカーなしの曲線による散乱接続|データ マーカーのない、曲線で接続された散布図を表します。|
|ScatterConnectedByLinesWithDataMarker|データ マーカーを使用して線で接続された散布図を表します|
|ScatterConnectedByLinesWithoutDataMarker|データ マーカーのない、線で接続された散布図を表します。|
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
Aspose.Cells を使用してグラフを作成するには:

1. 次のコマンドを使用して、ワークシートのセルにデータを追加します。[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)オブジェクトの[**セット値**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)方法。
これはグラフのデータ ソースとして使用されます。
1. を呼び出して、ワークシートにグラフを追加します。[**チャートコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)コレクションの[*追加*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int) メソッド。[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)物体。
1. チャートの種類を指定します。[**グラフの種類**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)列挙。
たとえば、この例では[**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)グラフの種類として値を指定します。
1. 新しいものにアクセスする[**チャート**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)からのオブジェクト[**チャートコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)インデックスを渡すことによってコレクションを作成します。
1. にカプセル化されたグラフ オブジェクトのいずれかを使用します。[**チャート**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)チャートを管理するオブジェクト。
以下の例では、[**シリーズコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)チャート オブジェクトを使用してチャートのデータ ソースを指定します。

ソース データをグラフに追加する場合、データ ソースはセル範囲 (「A1:C3」など)、連続しない一連のセル (「A1、A3、A5」など)、または一連のセルにすることができます。値 (「1、2、3」など)。

{{% alert color="primary" %}}

セル範囲をデータ ソースとして割り当てる場合は、左上から右下までの範囲のみを設定できます。たとえば、「A1:C3」は有効ですが、「C3:A1」は無効です。

{{% /alert %}}

これらの一般的な手順により、あらゆるタイプのグラフを作成できます。さまざまなグラフ オブジェクトを使用して、さまざまなグラフを作成します。

サンプルコードを実行すると、以下に示すようにピラミッド チャートがワークシートに追加されます。

**ピラミッド チャートとそのデータ ソース**

![todo:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

バブル チャートを作成するには、[**グラフの種類**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)に設定する必要があります[**チャートタイプ.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)それに応じて、BubbleSizes、Values、XValues などのいくつかの追加プロパティを設定する必要があります。次のコードを実行すると、以下に示すようにバブル チャートがワークシートに追加されます。

**バブル チャートとそのデータ ソース**

![todo:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

####  **データマーカー付き折れ線グラフ**

データ マーカー グラフを使用して線を作成するには、[**グラフの種類**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)に設定する必要があります[**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS)それに応じて、背景領域、シリーズ マーカー、値、XValue などのいくつかの追加プロパティを設定する必要があります。次のコードを実行すると、データ マーカー グラフを含む線がワークシートに追加されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

##  **カスタムチャートの作成**

これまでグラフについて説明してきたとき、標準の書式設定を持つ標準グラフを見てきました。データ ソースを定義し、いくつかのプロパティを設定するだけで、デフォルトの形式設定でグラフが作成されます。ただし、Aspose.Cells は、開発者が独自の形式設定でグラフを作成できるカスタム グラフの作成もサポートしています。

###  **カスタムチャートの作成**

開発者は、Aspose.Cells 単純な API を使用して、実行時にカスタム グラフを作成できます。

チャートはデータ系列で構成されます。 Aspose.Cells の各データ系列は、[**シリーズ**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)オブジェクトですが、[**シリーズコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)オブジェクトは、次のコレクションとして機能します。[**シリーズ**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)オブジェクト。カスタム グラフを作成する場合、開発者は、さまざまなデータ シリーズ ([**シリーズコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)物体）。

{{% alert color="primary" %}}

現在、Aspose.Cells は、円グラフ、折れ線グラフ、縦棒グラフ、縦棒積み上げグラフを組み合わせたカスタム グラフのみをサポートしていますが、将来のリリースではさらに多くのグラフがサポートされる予定です。 Aspose.Cells がサポートする標準チャートの完全なリストについては、[グラフの種類](/cells/ja/java/chart-types/)記事。

{{% /alert %}}

以下のコード例は、カスタム グラフの作成方法を示しています。この例では、最初のデータ系列に縦棒グラフを使用し、2 番目のデータ系列に折れ線グラフを使用します。その結果、折れ線グラフと組み合わせた縦棒グラフがワークシートに追加されます。

**縦棒グラフと折れ線グラフを組み合わせたカスタム グラフ**

![todo:image_alt_text](creating-and-customizing-charts_3.png)

**プログラミング例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

サポートされているグラフの種類のリストを確認するには、「[グラフの種類](/cells/ja/java/chart-types/)記事。

{{% /alert %}}

