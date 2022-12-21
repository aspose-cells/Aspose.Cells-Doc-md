---
title: チャートのカスタマイズ
type: docs
weight: 15
url: /ja/java/creating-and-customizing-charts/
---
## **チャートの作成**

Aspose.Cells を使用して、さまざまなチャートをスプレッドシートに追加することができます。Aspose.Cells は、多くの柔軟なチャート オブジェクトを提供します。このトピックでは、Aspose.Cells' チャート オブジェクトについて説明します。

### **単純なチャートの作成**

次のコード例を使用して、Aspose.Cells のグラフを簡単に作成できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **グラフを作成するための注意事項**

グラフを作成する前に、Aspose.Cells を使用してグラフを作成するときに役立ついくつかの基本概念を理解することが重要です。

#### **グラフ オブジェクト**

Aspose.Cells は、あらゆる種類のチャートを作成するために使用される特別なクラスのセットを提供します。これらのクラスは、作成するために使用されます**グラフ オブジェクト**、チャートの構成要素として機能します。チャート オブジェクトは次のとおりです。

- [**軸**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis)、グラフの軸。
- [**チャート**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)、単一の Excel グラフ。
- [**チャートエリア**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea)、ワークシートのグラフ領域。
- [**チャートデータテーブル**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable)、グラフ データ テーブル。
- [**ChartFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame)、チャート内のフレーム オブジェクト。
- [**チャートポイント**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)、チャートの系列の単一ポイント。
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection)、1 つのシリーズのすべてのポイントを含むコレクション。
- [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) 、のコレクション[**チャート**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)オブジェクト。
-  DataLabels、指定された DataLabels[**シリーズ**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**チャートポイント**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**トレンドライン**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)など
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat)、形状の塗りつぶし形式。
- [**床**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor)、3D チャートの下限。
- [**伝説**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend)、チャートの凡例。
- [**ライン**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)、チャート ライン。
- [**シリーズコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) 、のコレクション[**シリーズ**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)オブジェクト。
- [**シリーズ**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)は、グラフ内の単一のデータ シリーズを表します。
- [**目盛りラベル**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels)、チャート軸の目盛りに関連付けられた目盛りラベル。
- [**題名**](https://reference.aspose.com/cells/java/com.aspose.cells/Title)、チャートまたは軸のタイトル。
- [**トレンドライン**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)、チャートの傾向線。
- [**トレンドライン コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection)、指定されたデータ シリーズのすべての Trendline オブジェクトのコレクション。
- [**壁**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls)、3D グラフの壁。

#### **チャート オブジェクトの使用**

前述のように、すべてのチャート オブジェクトはそれぞれのクラスのインスタンスであり、特定のタスクを実行するための特定のプロパティとメソッドを提供します。チャート オブジェクトを使用してチャートを作成します。

を使用して、任意の種類のグラフをワークシートに追加します。[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)コレクション。の各項目[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)コレクションは[**チャート**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)物体。あ[**チャート**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)オブジェクトは、チャートの外観をカスタマイズするために必要なすべてのチャート オブジェクトをカプセル化します。次のセクションでは、いくつかの基本的なチャート オブジェクトを使用して単純なチャートを作成する方法を示します。

### **簡単なチャートの作成**

Aspose.Cells を使用して、さまざまな種類のチャートを作成できます。Aspose.Cells でサポートされているすべての標準チャートは、列挙型で事前に定義されています。[**グラフの種類**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType).定義済みのグラフの種類は次のとおりです。

|**グラフの種類**|**説明**|
|:- |:- |
|桁|集合縦棒グラフを表します|
|積み上げ列|積み上げ縦棒グラフを表します|
|Column100PercentStacked|100% 積み上げ縦棒グラフを表します|
|列 3DClustered|立体集合縦棒グラフを表します|
|Column3D積み上げ|3D 積み上げ縦棒グラフを表します|
|Column3D100PercentStacked|3D 100% 積み上げ縦棒グラフを表します|
|列 3D|3D 縦棒グラフを表します|
|バー|集合棒グラフを表します|
|棒積み上げ|積み上げ棒グラフを表します|
|Bar100Percent積み上げ|100% 積み上げ棒グラフを表します|
|Bar3DClustered|3D 集合棒グラフを表します|
|Bar3D積み上げ|3D 積み上げ棒グラフを表します|
|Bar3D100PercentStacked|3D 100% 積み上げ棒グラフを表します|
|ライン|折れ線グラフを表します|
|LineStacked|積み上げ折れ線グラフを表します|
|Line100PercentStacked|100% 積み上げ折れ線グラフを表します|
|LineWithDataMarkers|データ マーカー付きの折れ線グラフを表します|
|LineStackedWithDataMarkers|データ マーカー付きの積み上げ折れ線グラフを表します|
|Line100PercentStackedWithDataMarkers|データ マーカー付きの 100% 積み上げ折れ線グラフを表します|
|Line3D|3D 折れ線グラフを表します|
|パイ|円グラフを表します|
|Pie3D|3D 円グラフを表します|
|パイパイ|円グラフの円を表します|
|パイ爆発|分解円グラフを表します|
|Pie3DExploded|3D 分解円グラフを表します|
|パイバー|円グラフのバーを表します|
|散布|散布図を表します|
|ScatterConnectedByCurvesWithDataMarker|データ マーカー付きの曲線で接続された散布図を表します|
|ScatterConnectedByCurvesWithoutDataMarker|データ マーカーのない、曲線で接続された散布図を表します|
|ScatterConnectedByLinesWithDataMarker|データ マーカー付きの線で結ばれた散布図を表します|
|ScatterConnectedByLinesWithoutDataMarker|データ マーカーのない、線で結ばれた散布図を表します|
|範囲|面グラフを表します|
|エリア積み上げ|積み上げ面グラフを表します|
|Area100PercentStacked|100% 積み上げ面グラフを表します|
|エリア3D|3D 面グラフを表します|
|Area3D積み上げ|3D 積み上げ面グラフを表します|
|Area3D100PercentStacked|3D 100% 積み上げ面グラフを表します|
|ドーナツ|ドーナツ チャートを表します|
|ドーナツ爆発|展開されたドーナツ グラフを表します|
|レーダー|レーダー チャートを表します|
|RadarWithDataMarkers|レーダー チャートをデータ マーカーで表します|
|レーダーいっぱい|塗りつぶされたレーダー チャートを表します|
|Surface3D|3D 等高線図を表します|
|SurfaceWireframe3D|ワイヤーフレーム 3D 等高線図を表します|
|表面輪郭|等高線図を表します|
|SurfaceContourWireframe|ワイヤーフレーム等高線図を表します|
|バブル|バブル チャートを表します|
|バブル3D|3D バブル チャートを表します|
|シリンダー|円柱グラフを表します|
|円柱積み上げ|積み上げ円柱グラフを表します|
|円柱 100%積み上げ|100% 積み上げ円柱グラフを表します|
|円柱棒|円柱棒グラフを表します。|
|円柱棒積み上げ|積み上げ円筒棒グラフを表します|
|CylindricalBar100PercentStacked|100% 積み上げ円柱棒グラフを表します|
|円筒柱 3D|3D 円柱縦棒グラフを表します|
|円錐|コーン チャートを表します|
|円錐積み上げ|積み上げ円錐グラフを表します|
|円錐 100% 積み上げ|100% 積み上げ円錐グラフを表します|
|円錐バー|円錐棒グラフを表します|
|円錐棒積み上げ|積み上げ円錐棒グラフを表します|
|ConicalBar100PercentStacked|100% 積み上げ円錐棒グラフを表します|
|ConicalColumn3D|3D 円錐縦棒グラフを表します|
|ピラミッド|ピラミッド チャートを表します|
|ピラミッド積み上げ|積み上げピラミッド チャートを表します|
|Pyramid100PercentStacked|100% 積み上げピラミッド チャートを表します|
|ピラミッドバー|ピラミッド棒グラフを表します|
|ピラミッド棒積み上げ|積み上げピラミッド棒グラフを表します|
|PyramidBar100PercentStacked|100% 積み上げピラミッド棒グラフを表します|
|PyramidColumn3D|3D ピラミッド縦棒グラフを表します|
Aspose.Cells を使用してグラフを作成するには:

1. を使用して、ワークシートのセルにデータを追加します。[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)オブジェクトの[**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)方法。
これは、グラフのデータ ソースとして使用されます。
1. を呼び出して、ワークシートにグラフを追加します。[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)コレクションの[*追加*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int) メソッド、カプセル化された[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)物体。
1. でグラフの種類を指定します[**グラフの種類**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)列挙。
たとえば、この例では[**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)値をグラフ タイプとして指定します。
1. 新しい[**チャート**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)からのオブジェクト[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)インデックスを渡すことによってコレクション。
1. にカプセル化されたチャート オブジェクトのいずれかを使用します。[**チャート**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)チャートを管理するオブジェクト。
以下の例では、[**シリーズコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)charting オブジェクトを使用して、チャートのデータ ソースを指定します。

ソース データをグラフに追加する場合、データ ソースはセルの範囲 (「A1:C3」など)、連続していないセルのシーケンス (「A1、A3、A5」など)、または一連のセルのいずれかです。値 (「1,2,3」など)。

{{% alert color="primary" %}}

セルの範囲をデータ ソースとして割り当てる場合、左上から右下までの範囲のみを設定できます。たとえば、「A1:C3」は有効ですが、「C3:A1」は無効です。

{{% /alert %}}

これらの一般的な手順により、あらゆる種類のグラフを作成できます。さまざまなチャート オブジェクトを使用して、さまざまなチャートを作成します。

サンプル コードを実行すると、次のようにピラミッド チャートがワークシートに追加されます。

**ピラミッド チャートとそのデータ ソース**

![todo:画像_代替_文章](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

バブル チャートを作成するには、[**グラフの種類**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)に設定する必要があります[**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)それに応じて、BubbleSizes、Values、XValues などのいくつかの追加プロパティを設定する必要があります。次のコードを実行すると、以下に示すようにバブル チャートがワークシートに追加されます。

**バブル チャートとそのデータ ソース**

![todo:画像_代替_文章](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **データ マーカー付き折れ線グラフ**

データ マーカー チャートで線を作成するには、[**グラフの種類**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)に設定する必要があります[**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS)また、背景領域、シリーズ マーカー、値、X 値などのいくつかの追加プロパティを適宜設定する必要があります。次のコードを実行すると、データ マーカー グラフを含む行がワークシートに追加されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **カスタム グラフの作成**

これまでグラフについて説明してきたとき、標準の書式設定が設定された標準のグラフを見てきました。データ ソースを定義し、いくつかのプロパティを設定するだけで、チャートはデフォルトのフォーマット設定で作成されます。ただし、Aspose.Cells は、開発者が独自の形式設定でグラフを作成できるようにするカスタム グラフの作成もサポートしています。

### **カスタム グラフの作成**

開発者は、Aspose.Cells simple API を使用して実行時にカスタム チャートを作成できます。

グラフはデータ系列で構成されています。 Aspose.Cells の各データ系列は、[**シリーズ**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)オブジェクトに対して[**シリーズコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)オブジェクトはのコレクションとして機能します[**シリーズ**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)オブジェクト。カスタム グラフを作成する場合、開発者は、さまざまなデータ シリーズにさまざまな種類のグラフを自由に使用できます ([**シリーズコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)物体）。

{{% alert color="primary" %}}

現在、Aspose.Cells は、円グラフ、折れ線グラフ、縦棒グラフ、積み上げ縦棒グラフを組み合わせたカスタム グラフのみをサポートしていますが、今後のリリースではさらに多くのグラフがサポートされる予定です。 Aspose.Cells がサポートする標準チャートの完全なリストについては、[グラフの種類](/cells/ja/java/chart-types/)記事。

{{% /alert %}}

以下のコード例は、カスタム グラフを作成する方法を示しています。この例では、最初のデータ系列に縦棒グラフを使用し、2 番目の系列に折れ線グラフを使用します。その結果、折れ線グラフと組み合わせた縦棒グラフがワークシートに追加されます。

**縦棒グラフと折れ線グラフを組み合わせたカスタム グラフ**

![todo:画像_代替_文章](creating-and-customizing-charts_3.png)

**プログラミング例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

サポートされているチャート タイプのリストを確認するには、[グラフの種類](/cells/ja/java/chart-types/)記事。

{{% /alert %}}

