---
title: チャートの作成と管理
description: Aspose.Cells for Python via .NETを使用してMicrosoft Excelでチャートを作成する方法を学びましょう。ガイドでは、作成可能なさまざまな種類のチャートと、その外観や書式のカスタマイズ方法を示します。
keywords: Aspose.Cells for Python via .NET、チャート作成、Microsoft Excel、チャートタイプ、カスタマイズ、外観、書式設定。
linktitle: チャート
type: docs
weight: 130
url: /ja/python-net/creating-charts/
description: ExcelおよびODSファイルのCSharpでチャートを作成します。
keywords: チャートを作成し、グラフを作成します 
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETを使用すると、さまざまなタイプのチャートをスプレッドシートに追加できます。Aspose.Cells for Python via .NETは、多くの柔軟なチャートオブジェクトを提供します。このトピックでは、Aspose.Cellsのチャートオブジェクトについて説明します。

{{% /alert %}}

## **チャートの作成**

### **単純なチャートの作成**
以下の例コードを使用して、Aspose.Cells for Python via .NETでチャートを簡単に作成できます：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateColumnChart-1.py" >}}

### **チャート作成のための注意事項**

チャートを作成する前に、Aspose.Cells for Python via .NETを使用したチャート作成時に役立つ基本的な概念を理解することが重要です。

#### **チャートオブジェクト**

Aspose.Cells for Python via .NETは、Aspose.Cells for Python via .NETがサポートするチャートを作成するために使用される[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/python-net/aspose.cells.charts)名前空間内の特殊なクラスセットを提供します。これらのクラスは、**チャート作成オブジェクト**を作成するために使用され、これらはチャートの構成要素として機能します。チャート作成オブジェクトは以下の通りです：

- シリーズ、チャート内の単一のデータシリーズ。
- 軸、チャートの軸。
- Chart, 単一のExcelグラフ。
- ChartArea, ワークシート内のグラフエリア。
- ChartDataTable, グラフデータテーブル。
- ChartFrame, グラフ内のフレームオブジェクト。
- ChartPoint, グラフ内のシリーズの単一のポイント。
- ChartPointCollection, 1つのシリーズ内のすべてのポイントを含むコレクション。
- Charts, Chartオブジェクトのコレクション。
- DataLabels, 指定されたシリーズのすべてのDataLabelオブジェクトのコレクション。
- FillFormat, シェイプの塗りつぶし形式。
- Floor, 3Dグラフの床。
- Legend, グラフの凡例。
- Line, グラフの線。
- SeriesCollection, Seriesオブジェクトのコレクション。
- TickLabels, グラフ軸の目盛りのラベル。
- Title, グラフまたは軸のタイトル。
- Trendline, グラフ内のトレンドライン。
- TrendlineCollection, 指定されたデータシリーズのすべてのTrendlineオブジェクトのコレクション。
- Walls, 3Dグラフの壁。

#### **Chartingオブジェクトの使用**

上記のように、すべてのチャートオブジェクトはそれぞれのクラスのインスタンスであり、特定のタスクを実行するための特定のプロパティとメソッドを提供します。チャートオブジェクトを使用して、チャートを作成します。

ワークシートに任意の種類のチャートを追加するには、[**charts**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/charts)のコレクションを使用します。[**charts**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/charts)のコレクション内の各アイテムは[**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart)オブジェクトを表します。[**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart)オブジェクトはグラフの外観をカスタマイズするために必要な他のすべてのチャートオブジェクトをカプセル化します。次のセクションでは、いくつかの基本的なチャートオブジェクトを使用して、単純なチャートを作成する方法を示します。

### **Aspose.Cells for Python via .NETを使用したチャートの作成**

**手順:**

1. [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)オブジェクトの[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value)メソッドを使用してワークシートセルにデータを追加します。
   これはグラフのデータソースとして使用されます。
1. [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartcollection)コレクションの[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartcollection/add)メソッドを呼び出してワークシートにチャートを追加します。これは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)オブジェクトにカプセル化されています。
1. [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype)列挙型を使用してチャートのタイプを指定します。
   たとえば、以下の例では、[**ChartType.PYRAMID**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype/)値をチャートの種類として使用しています。
1. インデックスを渡して[**charts**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartcollection)コレクションから新しい[**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart)オブジェクトをアクセスします。
1. [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart)オブジェクトにカプセル化されたチャートの管理に使用できるいずれかのチャートオブジェクトを使用します。
   以下の例では、[**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)チャートオブジェクトを使用して、チャートのデータソースを指定します。

チャートにソースデータを追加する場合、データソースはセルの範囲（"A1:C3"など）、非連続セルのシーケンス（"A1, A3, A5"など）、値のシーケンス（"1,2,3"など）のいずれかです。

これらの一般的な手順を使用すると、任意のタイプのチャートを作成できます。異なるチャートオブジェクトを使用して、異なるチャートを作成します。

Aspose.Cells for Python via .NETを使用すると、多種多様なチャートを作成できます。Aspose.Cells for Python via .NETがサポートするすべての標準チャートは、[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype)と呼ばれる列挙体に事前定義されています。

事前定義されたチャートの種類は:

|**チャートの種類**|**説明**|
| :- | :- |
|Column| クラスタ化された列チャートを表します。
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
|Scatter| 散布図を表します|
|ScatterConnectedByCurvesWithDataMarker| データマーカー付きの曲線で接続された散布図を表します|
|ScatterConnectedByCurvesWithoutDataMarker| データマーカーなしの曲線で接続された散布図を表します|
|ScatterConnectedByLinesWithDataMarker| データマーカー付きの線で接続された散布図を表します|
|ScatterConnectedByLinesWithoutDataMarker| データマーカーなしの線で接続された散布図を表します|
|Area| エリアチャートを表します|
|AreaStacked| 積み上げエリアチャートを表します|
|Area100PercentStacked| 100% 積み上げエリアチャートを表します|
|Area3D| 3Dエリアチャートを表します|
|Area3DStacked| 3D積み上げエリアチャートを表します|
|Area3D100PercentStacked| 3D 100% 積み上げエリアチャートを表します|
|Doughnut| ドーナツチャートを表します|
|DoughnutExploded| 分裂したドーナツチャートを表します|
|Radar| レーダーチャートを表します|
|RadarWithDataMarkers| データマーカー付きのレーダーチャートを表します|
|RadarFilled| 塗りつぶしのレーダーチャートを表します|
|Surface3D| 3Dサーフェスチャートを表します|
|SurfaceWireframe3D| ワイヤーフレーム3Dサーフェスチャートを表します|
|SurfaceContour| 等高線チャートを表します|
|SurfaceContourWireframe| ワイヤーフレーム等高線チャートを表します|
|Bubble| バブルチャートを表します|
|Bubble3D| 3Dバブルチャートを表します|
|Cylinder| シリンダーチャートを表します|
|CylinderStacked| 積み上げシリンダーチャートを表します|
|Cylinder100PercentStacked| 100% 積み上げシリンダーチャートを表します|
|CylindericalBar| 円柱形バーチャートを表します|
|CylindericalBarStacked| 積み上げ円柱形バーチャートを表します|
|CylindericalBar100PercentStacked| 100% 積み上げ円柱形バーチャートを表します|
|CylindericalColumn3D| 3D円柱チャートを表します
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
|PyramidBar| ピラミッドバーチャートを表します
|PyramidBarStacked| 積み重ねピラミッドバーチャートを表します
|PyramidBar100PercentStacked| 100% 積み重ねピラミッドバーチャートを表します
|PyramidColumn3D| 3Dピラミッド柱チャートを表します
{{% alert color="primary" %}}

セルの範囲をデータソースとして割り当てると、左上から右下までの範囲を設定できます。例えば、"A1:C3"は有効ですが、"C3:A1"は無効です。

{{% /alert %}}

#### **ピラミッドチャート**

例のコードを実行すると、ワークシートにピラミッドチャートが追加されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreatePyramidChart-1.py" >}}

#### **折れ線グラフ**

上記の例では、[**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype)を*Line*に変更するだけで、折れ線グラフが作成されます。完全なソースは以下に提供されています。コードを実行すると、ワークシートに折れ線グラフが追加されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateLineChart-1.py" >}}

#### **バブルチャート**

バブルチャートを作成するには、[**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype)を[**ChartType.BUBBLE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype)に設定し、BubbleSizes、Values、XValuesなどの追加のプロパティを適切に設定する必要があります。次のコードを実行すると、ワークシートにバブルチャートが追加されます。

#### **データマーカー付きラインチャート**

データマーカー付きラインチャートを作成するには、[**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype)を*ChartType.LineWithDataMarkers*に設定し、バックグラウンドエリア、シリーズマーカー、Values、XValuesなどの追加のプロパティを適切に設定する必要があります。次のコードを実行すると、ワークシートにデータマーカー付きラインチャートが追加されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateLineWithDataMarkerChart-1.py" >}}

## **高度なトピック**
- [Excel 2016のチャートの読み込みと操作](/cells/ja/python-net/read-and-manipulate-excel-2016-charts/)
- [Excelチャートの軸の管理](/cells/ja/python-net/chart-axes/)
- [グラフの外観設定](/cells/ja/python-net/setting-chart-appearance/)
- [チャートタイプ](/cells/ja/python-net/chart-types/)
- [チャートのカスタマイズ](/cells/ja/python-net/customizing-charts/)
- [チャートのデータソースを設定する](/cells/ja/python-net/data-formatting-in-charts/)
- [Excelチャートのデータラベルの管理](/cells/ja/python-net/insert-datalabels-to-chart/)
- [スマートマーカーの処理によるチャートの生成](/cells/ja/python-net/generate-chart-by-processing-smart-markers/)
- [チャートのワークシートを取得する](/cells/ja/python-net/get-worksheet-of-the-chart/)
- [Excelチャートの凡例の管理](/cells/ja/python-net/chart-legend/)
- [チャートの位置、サイズ、デザインの操作](/cells/ja/python-net/manipulate-position-size-and-designer-chart/)
- [リーダーライン付き円グラフの作成](/cells/ja/python-net/creating-pie-chart-with-leader-lines/)
- [グラフ内の図形](/cells/ja/python-net/controls-in-charts/)
- [Excelグラフのタイトルの管理](/cells/ja/python-net/chart-and-axis-titles/)
- [グラフのレンダリング](/cells/ja/python-net/chart-rendering/)
- [グラフトレンドラインの方程式テキストを取得](/cells/ja/python-net/get-equation-text-of-chart-trendline/)
