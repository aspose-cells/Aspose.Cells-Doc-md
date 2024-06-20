---
title: チャートのカスタマイズ
type: docs
weight: 15
url: /ja/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---

## **チャートの作成**

Aspose.Cellsでさまざまなチャートをスプレッドシートに追加できます。Aspose.Cellsは多くの柔軟なチャートオブジェクトを提供します。このトピックでは、Aspose.Cellsのチャートオブジェクトについて説明します。

### **単純なチャートの作成**

Aspose.Cellsを使用して、次のような例コードで簡単にグラフを作成できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **グラフの作成に関する事項**

Aspose.Cellsを使用してチャートを作成する際に役立ついくつかの基本的な概念を理解することが重要です。

#### **チャートオブジェクト**

Aspose.Cellsは、あらゆる種類のグラフを作成するために使用される特別なクラス群を提供しています。これらのクラスは **グラフオブジェクト** を作成するために使用され、グラフの構築ブロックとして機能します。以下にグラフオブジェクトがリストされています:

- [**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis)、グラフの軸。
- [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) 、単一のExcelグラフ。
- [**ChartArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea)、ワークシート内のグラフエリア。
- [**ChartDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable)、グラフデータテーブル。
- [**ChartFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame)、グラフ内の枠オブジェクト。
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)、グラフ内のシリーズ内の単一のポイント。
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection)、1つのシリーズ内のすべてのポイントを含むコレクション。
- [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)、[**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)のコレクション。
- DataLabels、指定された [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)、[**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)、[**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline) などのDataLabels。
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat)、形状の塗りつぶし形式。
- [**Floor**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor)、3Dグラフの床。
- [**Legend**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend)、グラフの凡例。
- [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)、グラフの線。
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)、[**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)のコレクション。
- [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)、グラフ内の単一のデータ系列を表します。
- [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels)、グラフ軸上の目盛りラベル。
- [**Title**](https://reference.aspose.com/cells/java/com.aspose.cells/Title)、グラフまたは軸のタイトル。
- [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)、グラフ内のトレンドライン。
- [**TrendlineCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection)、指定されたデータ系列のすべてのTrendlineオブジェクトのコレクション。
- [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls)、3Dグラフの壁。

#### **Chartingオブジェクトの使用**

上記のように、すべてのチャートオブジェクトはそれぞれのクラスのインスタンスであり、特定のタスクを実行するための特定のプロパティとメソッドを提供します。チャートオブジェクトを使用して、チャートを作成します。

Aspose.Cellsの[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)コレクションを使用してワークシートに任意の種類のグラフを追加できます。[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)コレクション内の各アイテムは[**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)オブジェクトを表します。[**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)オブジェクトは、グラフの外観をカスタマイズするために必要なグラフオブジェクトをカプセル化しています。次のセクションでは、いくつかの基本的なグラフオブジェクトを使用してシンプルなグラフを作成する方法を示します。

### **シンプルなグラフの作成**

Aspose.Cellsを使用して様々な種類のグラフを作成することができます。Aspose.Cellsでサポートされているすべての標準グラフは、[**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)という列挙型で事前定義されています。事前定義されたグラフの種類は次のとおりです:

|**チャートの種類**|**説明**|
| :- | :- |
|Column|クラスター化された縦棒グラフを表します|
|ColumnStacked| 積み上げ列チャートを表します。
|Column100PercentStacked| 100% 積み上げ列チャートを表します。
|Column3DClustered| 3D クラスタ化された列チャートを表します。
|Column3DStacked| 3D 積み上げ列チャートを表します。
|Column3D100PercentStacked| 3D 100% 積み上げ列チャートを表します。
|Column3D| 3D 列チャートを表します。
|Bar| クラスタ化された棒チャートを表します。
|BarStacked| 積み上げ棒チャートを表します。
|Bar100PercentStacked| 100% 積み上げ棒チャートを表します。
|Bar3DClustered| 3D クラスタ化された棒チャートを表します。
|Bar3DStacked| 3D 積み上げ棒チャートを表します。
|Bar3D100PercentStacked| 3D 100% 積み上げ棒チャートを表します。
|Line| 折れ線チャートを表します。
|LineStacked| 積み上げ折れ線チャートを表します。
|Line100PercentStacked| 100% 積み上げ折れ線チャートを表します。
|LineWithDataMarkers| データマーカー付きの折れ線チャートを表します。
|LineStackedWithDataMarkers| データマーカー付きの積み上げ折れ線チャートを表します。
|Line100PercentStackedWithDataMarkers| データマーカー付きの100% 積み上げ折れ線チャートを表します。
|Line3D| 3D 折れ線チャートを表します。
|Pie| 円グラフを表します。
|Pie3D| 3D 円グラフを表します。
|PiePie| パイ オブ パイ チャートを表します。
|PieExploded| 分解された円グラフを表します。
|Pie3DExploded| 3Dエクスプロード円グラフを表します|
|PieBar| パイチャートのバーを表します|
|Scatter|散布図を表します|
|ScatterConnectedByCurvesWithDataMarker|曲線で接続されたデータマーカー付きの散布図を表します|
|ScatterConnectedByCurvesWithoutDataMarker|曲線で接続された散布図を表します|
|ScatterConnectedByLinesWithDataMarker|データマーカーを使用した線でつながる散布図を表します。
|ScatterConnectedByLinesWithoutDataMarker|データマーカーを使用しない線でつながる散布図を表します。
|Area| エリアチャートを表します|
|AreaStacked| 積み上げエリアチャートを表します|
|Area100PercentStacked| 100% 積み上げエリアチャートを表します|
|Area3D| 3Dエリアチャートを表します|
|Area3DStacked| 3D積み上げエリアチャートを表します|
|Area3D100PercentStacked| 3D 100% 積み上げエリアチャートを表します|
|Doughnut| ドーナツチャートを表します|
|DoughnutExploded| 分裂したドーナツチャートを表します|
|Radar|レーダーチャートを表します。
|RadarWithDataMarkers|データマーカーを使用したレーダーチャートを表します。
|RadarFilled| 塗りつぶしのレーダーチャートを表します|
|Surface3D| 3Dサーフェスチャートを表します|
|SurfaceWireframe3D|3D ワイヤーフレーム 表面チャートを表します。
|SurfaceContour| 等高線チャートを表します|
|SurfaceContourWireframe| ワイヤーフレーム等高線チャートを表します|
|Bubble| バブルチャートを表します|
|Bubble3D| 3Dバブルチャートを表します|
|Cylinder| シリンダーチャートを表します|
|CylinderStacked| 積み上げシリンダーチャートを表します|
|Cylinder100PercentStacked| 100% 積み上げシリンダーチャートを表します|
|CylindricalBar|円柱型棒グラフを表します。
|CylindricalBarStacked|積み上げ円柱型棒グラフを表します。
|CylindricalBar100PercentStacked|100% 積み上げ円柱型棒グラフを表します。
|CylindricalColumn3D|3D 円柱型柱グラフを表します。
|Cone| 円錐チャートを表します
|ConeStacked| 積み重ね円錐チャートを表します
|Cone100PercentStacked| 100% 積み重ね円錐チャートを表します
|ConicalBar| 円錐バーチャートを表します
|ConicalBarStacked 積み重ね円錐バーチャートを表します
|ConicalBar100PercentStacked| 100% 積み重ね円錐バーチャートを表します
|ConicalColumn3D| 3D円錐柱チャートを表します
|Pyramid| ピラミッドチャートを表します
|PyramidStacked| 積み重ねピラミッドチャートを表します
|Pyramid100PercentStacked| 100% 積み重ねピラミッドチャートを表します
|PyramidBar|ピラミッド棒グラフを表す|
|PyramidBarStacked| 積み重ねピラミッドバーチャートを表します
|PyramidBar100PercentStacked| 100% 積み重ねピラミッドバーチャートを表します
|PyramidColumn3D| 3Dピラミッド柱チャートを表します
Aspose.Cellsを使用してグラフを作成するには：

1. [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)オブジェクトの[**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)メソッドを使用してワークシートセルにデータを追加します。
   これはグラフのデータソースとして使用されます。
1. [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)コレクションの[*add*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int))メソッドを呼び出してワークシートにグラフを追加します。
1. [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)列挙型を使用してチャートのタイプを指定します。
   たとえば、この例ではグラフの種類として[**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)値を使用します。
1. インデックスを渡して[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)コレクションから新しい[**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)オブジェクトをアクセスします。
1. [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)オブジェクトにカプセル化されたチャートの管理に使用できるいずれかのチャートオブジェクトを使用します。
   以下の例では、[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)チャートオブジェクトを使用して、チャートのデータソースを指定します。

チャートにソースデータを追加する場合、データソースはセルの範囲（"A1:C3"など）、非連続セルのシーケンス（"A1, A3, A5"など）、値のシーケンス（"1,2,3"など）のいずれかです。

{{% alert color="primary" %}}

セルの範囲をデータソースとして設定する場合、範囲を左上から右下に限定することができます。たとえば、「A1:C3」は有効であり、「C3:A1」は無効です。

{{% /alert %}}

これらの一般的な手順を使用すると、任意のタイプのチャートを作成できます。異なるチャートオブジェクトを使用して、異なるチャートを作成します。

例のコードを実行すると、以下に示すようにワークシートにピラミッドグラフが追加されます。

**データソースを持つピラミッドグラフ**

![todo:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

バブルチャートを作成するには、[**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)を[**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)に設定する必要があり、BubbleSizes、Values、およびXValuesなどのいくつかの追加プロパティを適切に設定する必要があります。次のコードを実行すると、以下に示すようにワークシートにバブルチャートが追加されます。

**データソースを持つバブルチャート**

![todo:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **データマーカー付きラインチャート**

データマーカー付き折れ線グラフを作成するには、[**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)を[**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS)に設定し、背景エリア、シリーズマーカー、値、およびXValuesなどの追加プロパティを適切に設定する必要があります。次のコードを実行すると、以下に示すようにワークシートにデータマーカー付き折れ線グラフが追加されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **カスタムチャートの作成**

これまでに、標準のフォーマット設定を持つ標準のチャートを見てきました。データソースを定義し、いくつかのプロパティを設定すると、デフォルトのフォーマット設定でグラフが作成されます。しかし、Aspose.Cellsは開発者が独自のフォーマット設定でグラフを作成できるカスタムチャートもサポートしています。

### **カスタムチャートの作成**

開発者は、Aspose.CellsのシンプルなAPIを使用して実行時にカスタムチャートを作成できます。

チャートはデータシリーズで構成されています。Aspose.Cellsの各データシリーズは[**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)オブジェクトで表され、[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)オブジェクトは[**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)オブジェクトのコレクションとして機能します。カスタムチャートの作成時、開発者は異なるタイプのチャートを異なるデータシリーズ（[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)オブジェクトで収集）に使用する自由があります。

{{% alert color="primary" %}}

現在、Aspose.Cellsはパイ、ライン、カラム、およびカラム積み上げチャートを組み合わせたカスタムチャートのみをサポートしていますが、将来のリリースでさらに多くのチャートがサポートされる予定です。Aspose.Cellsがサポートする標準チャートの完全なリストについては、[チャートの種類](/cells/ja/java/chart-types/)記事を参照してください。

{{% /alert %}}

以下の例コードは、カスタムチャートの作成方法を示しています。この例では、最初のデータ系列には列チャートを使用し、2番目のデータ系列には折れ線グラフを使用しています。その結果、ワークシートには列チャートと折れ線グラフが組み合わされたチャートが追加されます。

**カラムとラインチャートを組み合わせたカスタムチャート**

![todo:image_alt_text](creating-and-customizing-charts_3.png)

**プログラミング例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

サポートされているチャートの種類のリストを表示するには、[チャートの種類](/cells/ja/java/chart-types/)記事を参照してください。

{{% /alert %}}

