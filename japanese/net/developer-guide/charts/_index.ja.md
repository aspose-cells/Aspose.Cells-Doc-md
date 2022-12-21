---
title: チャートの作成と管理
linktitle: チャート
type: docs
weight: 130
url: /ja/net/creating-charts/
description: CSharp で Excel および ODS ファイル用のグラフを作成します。
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

Aspose.Cells を使用して、さまざまなチャートをスプレッドシートに追加することができます。Aspose.Cells は、多くの柔軟なチャート オブジェクトを提供します。このトピックでは、Aspose.Cells' チャート オブジェクトについて説明します。

{{% /alert %}}

## **チャートの作成**

### **単純なチャートの作成**
次のコード例を使用して、Aspose.Cells のグラフを簡単に作成できます。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **グラフを作成するための注意事項**

グラフを作成する前に、Aspose.Cells を使用してグラフを作成するときに役立ついくつかの基本概念を理解することが重要です。

#### **グラフ オブジェクト**

Aspose.Cells は、[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts) Aspose.Cells でサポートされているチャートを作成するために使用される名前空間。これらのクラスは、**グラフ オブジェクト**、チャートの構成要素として機能します。チャート オブジェクトは次のとおりです。

- シリーズ、グラフ内の単一のデータ シリーズ。
- 軸、グラフの軸。
- グラフ、単一の Excel グラフ。
- ChartArea、ワークシートのグラフ エリア。
- ChartDataTable、グラフ データ テーブル。
- ChartFrame、チャート内のフレーム オブジェクト。
- ChartPoint は、チャートの系列の単一ポイントです。
- ChartPointCollection は、1 つのシリーズのすべてのポイントを含むコレクションです。
- Charts、Chart オブジェクトのコレクション。
- DataLabels、指定されたシリーズのすべての DataLabel オブジェクトのコレクション。
- FillFormat、形状の塗りつぶし形式。
- フロア、3D チャートのフロア。
- 凡例、チャートの凡例。
- 線、チャート ライン。
- SeriesCollection、Series オブジェクトのコレクション。
- TickLabels、チャート軸の目盛りに関連付けられた目盛りラベル。
- タイトル、グラフまたは軸のタイトル。
- トレンドライン、チャートのトレンドライン。
- 指定されたデータ系列のすべての Trendline オブジェクトのコレクションです。
- 壁、3D チャートの壁。

#### **チャート オブジェクトの使用**

前述のように、すべてのチャート オブジェクトはそれぞれのクラスのインスタンスであり、特定のタスクを実行するための特定のプロパティとメソッドを提供します。チャート オブジェクトを使用してチャートを作成します。

を使用して、任意の種類のグラフをワークシートに追加します。[**チャート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts)コレクション。の各項目[**チャート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts)コレクションは[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)物体。あ[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)オブジェクトは、チャートの外観をカスタマイズするために必要な他のすべてのチャート オブジェクトをカプセル化します。次のセクションでは、いくつかの基本的なチャート オブジェクトを使用して単純なチャートを作成する方法を示します。

### **Aspose.Cells を使用してチャートを作成**

**手順:**

1. を使用して、ワークシートのセルにデータを追加します。[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)オブジェクトの[**プットバリュー**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法。
これは、グラフのデータ ソースとして使用されます。
1. を呼び出して、ワークシートにグラフを追加します。[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)コレクションの[**追加**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add)にカプセル化されたメソッド[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)物体。
1. でグラフの種類を指定します[**グラフの種類**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)列挙。
たとえば、以下の例では、[**ChartType.ピラミッド**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)値をグラフ タイプとして指定します。
1. 新しい[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)からのオブジェクト[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)インデックスを渡すことによってコレクション。
1. にカプセル化されたチャート オブジェクトのいずれかを使用します。[**チャート**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)チャートを管理するオブジェクト。
以下の例では、[**シリーズコレクション**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)charting オブジェクトを使用して、チャートのデータ ソースを指定します。

ソース データをグラフに追加する場合、データ ソースはセルの範囲 (「A1:C3」など)、連続していないセルのシーケンス (「A1、A3、A5」など)、または一連のセルのいずれかです。値 (「1,2,3」など)。

これらの一般的な手順により、あらゆる種類のグラフを作成できます。さまざまなチャート オブジェクトを使用して、さまざまなチャートを作成します。

Aspose.Cells を使用して、さまざまな種類のチャートを作成できます。Aspose.Cells でサポートされているすべての標準チャートは、列挙型で事前に定義されています。[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

定義済みのグラフの種類は次のとおりです。

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
|ScatterConnectedByLinesWithoutDataMarker|線で結ばれた散布図を表します。データ マーカーはありません。|
|範囲|面グラフを表します|
|エリア積み上げ|積み上げ面グラフを表します|
|Area100PercentStacked|100% 積み上げ面グラフを表します|
|エリア3D|3D 面グラフを表します|
|Area3D積み上げ|3D 積み上げ面グラフを表します|
|Area3D100PercentStacked|3D 100% 積み上げ面グラフを表します|
|ドーナツ|ドーナツ チャートを表します|
|ドーナツ爆発|展開されたドーナツ グラフを表します|
|レーダー|レーダー チャートを表します|
|RadarWithDataMarkers|データ マーカー付きのレーダー チャートを表します|
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
|CylindericalBar100PercentStacked|100% 積み上げ円柱棒グラフを表します|
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
{{% alert color="primary" %}}

セルの範囲をデータ ソースとして割り当てる場合、範囲は左上から右下までしか設定できません。たとえば、「A1:C3」は有効ですが、「C3:A1」は無効です。

{{% /alert %}}

#### **ピラミッドチャート**

サンプル コードを実行すると、ピラミッド チャートがワークシートに追加されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **折れ線グラフ**

上記の例では、単純に[**グラフの種類**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)に*ライン*折れ線グラフを作成します。完全なソースを以下に示します。コードが実行されると、折れ線グラフがワークシートに追加されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **バブル チャート**

バブル チャートを作成するには、[**グラフの種類**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)に設定する必要があります[**ChartType.バブル**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)それに応じて、BubbleSizes、Values、XValues などのいくつかの追加プロパティを設定する必要があります。次のコードを実行すると、バブル チャートがワークシートに追加されます。

#### **データ マーカー付き折れ線グラフ**

データ マーカー チャートで線を作成するには、[**グラフの種類**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)に設定する必要があります*ChartType.LineWithDataMarkers*また、背景領域、シリーズ マーカー、Values & XValues などのいくつかの追加プロパティを適宜設定する必要があります。次のコードを実行すると、データ マーカー チャートを含む行がワークシートに追加されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **先行トピック**
- [Excel 2016 グラフの読み取りと操作](/cells/ja/net/read-and-manipulate-excel-2016-charts/)
- [Excel チャートの軸の管理](/cells/ja/net/chart-axes/)
- [チャートの外観の設定](/cells/ja/net/setting-chart-appearance/)
- [グラフの種類](/cells/ja/net/chart-types/)
- [チャートのカスタマイズ](/cells/ja/net/customizing-charts/)
- [グラフのデータ ソースを設定する](/cells/ja/net/data-formatting-in-charts/)
- [Excel チャートの DataLabels の管理](/cells/ja/net/insert-datalabels-to-chart/)
- [スマート マーカーを処理してチャートを生成する](/cells/ja/net/generate-chart-by-processing-smart-markers/)
- [チャートのワークシートを取得](/cells/ja/net/get-worksheet-of-the-chart/)
- [Excel チャートの凡例の管理](/cells/ja/net/chart-legend/)
- [ポジション サイズとデザイナー チャートの操作](/cells/ja/net/manipulate-position-size-and-designer-chart/)
- [引出線付き円グラフの作成](/cells/ja/net/creating-pie-chart-with-leader-lines/)
- [チャートの形状](/cells/ja/net/controls-in-charts/)
- [Excel チャートのタイトルを管理する](/cells/ja/net/chart-and-axis-titles/)
- [チャートのレンダリング](/cells/ja/net/chart-rendering/)
- [チャート トレンドラインの数式テキストを取得する](/cells/ja/net/get-equation-text-of-chart-trendline/)
