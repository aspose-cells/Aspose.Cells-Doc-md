---
title: チャートの書式設定
type: docs
weight: 20
url: /ja/java/chart-formatting/
---

## **グラフの外観設定**

Aspose.Cellsが提供する[チャートの種類](/cells/ja/java/chart-types/)では、提供される各種チャートやチャートオブジェクトについて簡単に紹介しました。

この記事では、次の異なるプロパティを設定することで、チャートの外観をカスタマイズする方法について説明します:

- [チャートエリアの設定](/cells/ja/java/chart-formatting/#setting-chart-area)。
- [チャートラインの設定](/cells/ja/java/chart-formatting/#setting-chart-lines)。
- [テーマの適用](/cells/ja/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts)。
- [チャートおよび軸のタイトルの設定](/cells/ja/java/chart-formatting/#setting-the-titles-of-charts-or-axes)。
- [グリッド線の操作](/cells/ja/java/chart-formatting/#setting-major-gridlines)。
- [背面および側壁の境界線の設定](/cells/ja/java/chart-formatting/#setting-borders-for-back-and-side-walls)。

### **チャートエリアの設定**

チャートにはさまざまな種類のエリアがあり、Aspose.Cellsでは各エリアの外観を変更する柔軟性を提供しています。開発者は、前景色、背景色、塗りつぶし形式などを変更することで、エリアに異なる書式設定を適用できます。

以下の例では、チャートの異なる種類のエリアに異なる書式設定を適用しました。

- プロットエリア
- チャートエリア
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) エリア
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) の単一ポイントのエリア

例のコードを実行すると、以下のようにワークシートに列のチャートが追加されます:

**塗りつぶされたエリアのある列チャート** 

![todo:image_alt_text](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **チャートラインの設定**

開発者は、以下の例で示すように、[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) のラインやデータマーカーにさまざまなスタイルを適用できます。例のコードを実行すると、ワークシートに列のチャートが追加されます:

**ラインスタイルを適用した列チャート** 

![todo:image_alt_text](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **Microsoft Excel 2007/2010のテーマをチャートに適用**

開発者は、以下の例で示すように、[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) やその他のチャートオブジェクトに異なるMicrosoft Excelテーマと色を適用できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **チャートや軸のタイトルの設定**

Microsoft Excelを使用して、チャートとその軸のタイトルをWYSIWYG環境で設定できます（以下のように表示されます）。

Microsoft Excelを使用してチャートとその軸のタイトルを設定する方法 

![todo:image_alt_text](chart-formatting_3.png)

また、Aspose.Cellsは開発者がランタイムでチャートとその軸のタイトルを設定することも可能です。すべてのチャートとその軸には、以下の例に示すようにタイトルを設定するために使用できる [**Title.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text) メソッドが含まれています。例のコードを実行した後、ワークシートに列のチャートが以下のように追加されます。

タイトルを設定した列のチャート 

![todo:image_alt_text](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **メジャーグリッドラインの設定**

#### **メジャーグリッドラインの非表示**

開発者は、[**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line) オブジェクトの [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible) メソッドを使用してメジャーグリッドラインの表示を制御できます。メジャーグリッドラインを非表示にした後、ワークシートに追加された列のチャートは以下の外観になります。

メジャーグリッドラインが非表示の列のチャート 

![todo:image_alt_text](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **メジャーグリッドラインの設定変更**

開発者はメジャーグリッドラインの表示だけでなく、色などのその他のプロパティも制御できます。メジャーグリッドラインの色を設定した後、ワークシートに追加された列のチャートは以下の外観になります。

色付きメジャーグリッドラインを持つ列のチャート 

![todo:image_alt_text](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **背面と側面の壁の境界線の設定**

Microsoft Excel 2007のリリース以来、3Dチャートの壁は側壁と背面をそれぞれ表す2つの[**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls)オブジェクトがあります。これらは別々に表され、[**Chart.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall)と[**Chart.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall)を使用してアクセスできます。

チャートの位置とサイズの変更

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **チャートの位置とサイズの変更**

時々、ワークシート内の新しいまたは既存のチャートの位置やサイズを変更したいことがあります。Aspose.Cellsはこれを達成するために [**Chart.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject) プロパティを提供しています。新しい**高さ**や**幅**でチャートを再サイズしたり、新しい**X**や**Y**座標でチャートの再配置を行うためにそのサブプロパティを使用できます。

### **チャートの位置とサイズの変更**

チャートの位置（X、Y座標）とサイズ（高さ、幅）を変更するには、以下のプロパティを使用します。

1. [**Chart.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Chart.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Chart.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Chart.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

以下の例では、上記のプロパティの使用方法について説明しています。既存のワークブックを読み込み、最初のワークシートにチャートが含まれている場合、そのチャートのサイズを変更し、位置を移動させてからワークブックを保存します。

サンプルコードの実行前のソースファイルは以下のようになります。

サンプルコードの実行前のチャートのサイズと位置 

![todo:image_alt_text](chart-formatting_7.png)

サンプルコードの実行後、出力ファイルは以下のようになります。

サンプルコードの実行後のチャートのサイズと位置 

![todo:image_alt_text](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **デザイナーチャートの操作**

デザイナーテンプレートファイルでチャートを操作または修正する必要がある場合があります。Aspose.Cellsは、その内容や要素とともにデザイナーチャートの操作を完全にサポートしています。データ、チャートの内容、背景画像、および書式設定を正確に保存できます。

### **テンプレートファイルでのデザイナーチャートの操作**

テンプレートファイルでのデザイナーチャートを操作するには、チャート関連のすべてのAPI呼び出しを使用します。たとえば、テンプレートファイル内の既存のチャートコレクションを取得するために [**Worksheet.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts) プロパティを使用します。

#### **チャートの作成**

以下の例では、円グラフの作成方法を示しています。後でこのチャートを操作します。以下の出力は、コードによって生成されます。

入力された円グラフ 

![todo:image_alt_text](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **チャートの操作**

以下の例は、既存のチャートを操作する方法を示しています。この例では、上記で作成したチャートを変更します。以下は、コードによって生成された出力です。チャートタイトルの色が青から黒に変更され、'England 30000' が 'United Kingdom, 30K' に変更されていることに注意してください。

**パイチャートが変更されました** 

![todo:image_alt_text](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **デザイナーテンプレート内の折れ線グラフの操作**

この例では、折れ線グラフを操作します。既存のチャートにいくつかのデータシリーズを追加し、それらの線の色を変更します。

まず、デザイナーの折れ線グラフを見てみましょう。

**入力折れ線グラフ** 

![todo:image_alt_text](chart-formatting_11.png)

今、以下のコードを使用して折れ線グラフ（**linechart.xls** ファイルに含まれている）を操作します。以下は、コードによって生成された出力です。

**操作された折れ線グラフ** 

![todo:image_alt_text](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **スパークラインの使用**

Microsoft Excel 2010では、これまで以上に情報をさまざまな方法で分析できます。新しいデータ分析および可視化ツールを使用して重要なデータトレンドを追跡および強調することができます。スパークラインは、表内に配置してデータとグラフを同時に表示できるミニチャートです。スパークラインを適切に使用すると、データ分析が迅速かつ的確になります。また、情報のシンプルな表示を提供し、多くの複雑なチャートでワークシートが過度に混雑するのを避けることもできます。

Aspose.Cellsは、スプレッドシート内のスパークラインを操作するためのAPIを提供しています。

### **Microsoft Excelでのスパークライン**

Microsoft Excel 2010にスパークラインを挿入するには:

1. スパークラインが表示されるセルを選択します。視覚的にわかりやすくするため、データの横のセルを選択します。
1. リボンの**挿入**を選択し、**スパークライン**グループで**列**を選択します。

![todo:image_alt_text](chart-formatting_13.png)

1. ソースデータを含むワークシートのセル範囲を選択または入力します。
   これにより、チャートが表示されます。

スパークラインを使用すると、トレンドやソフトボールリーグの勝敗記録などの傾向を把握することができます。 スパークラインは、リーグ内の各チームのシーズン全体をまとめることさえできます。

![todo:image_alt_text](chart-formatting_14.png)

### **Aspose.Cellsを使用したスパークライン**

開発者は、Aspose.Cells が提供する API を使用して、テンプレートファイル内のスパークライン（を作成、削除、または読み取ることができます。特定のデータ範囲に異なるタイプの小さなチャートを追加することができます。

以下の例は、スパークライン機能を示しています。この例では次のことを示しています:

1. 簡単なテンプレートファイルを開きます。
1. ワークシートのスパークライン情報を読み取ります。
1.指定されたデータ範囲に新しいスパークラインをセル領域に追加します。
1. Excel ファイルをディスクに保存します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **チャートに 3D フォーマットを適用する**

シナリオに適した 3D チャートスタイルを取得できるかもしれません。 Aspose.Cells API は、この記事で示されているように、Microsoft Excel 2007 の 3D 書式設定を適用するための関連する API を提供しています。

### **チャートに 3D フォーマットを設定する**

以下に、チャートを作成し、Microsoft Excel 2007 の 3D 書式を適用する方法を示す完全な例があります。上記の例コードを実行した後、ワークシートに 3D 効果のある列のチャートが追加されます。

**3Dフォーマットを使用した縦型棒グラフ**

![todo:image_alt_text](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

サポートされている2Dおよび3Dチャートの完全なリストについては、[チャートのレンダリングにサポートされているチャートの種類](/cells/ja/java/chart-rendering/#supported-chart-types-for-rendering)を参照してください。

{{% /alert %}}

## **高度なトピック**
- [グラフの背景に画像を設定する](/cells/ja/java/set-picture-as-background-fill-in-the-chart/)
{{< app/cells/assistant language="java" >}}
