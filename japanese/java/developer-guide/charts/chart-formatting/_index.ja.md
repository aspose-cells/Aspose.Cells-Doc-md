---
title: チャートの書式設定
type: docs
weight: 20
url: /ja/java/chart-formatting/
---
## **チャートの外観の設定**

の[グラフの種類](/cells/ja/java/chart-types/)で、Aspose.Cells が提供するチャートとチャート オブジェクトの種類を簡単に紹介しました。

この記事では、さまざまなプロパティを設定してチャートの外観をカスタマイズする方法について説明します。

- [チャートエリアの設定](/cells/ja/java/chart-formatting/#setting-chart-area).
- [チャートラインの設定](/cells/ja/java/chart-formatting/#setting-chart-lines).
- [テーマの適用](/cells/ja/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts).
- [チャートと軸にタイトルを設定する](/cells/ja/java/chart-formatting/#setting-the-titles-of-charts-or-axes).
- [グリッド線の操作](/cells/ja/java/chart-formatting/#setting-major-gridlines).
- [背面と側面の壁の境界の設定](/cells/ja/java/chart-formatting/#setting-borders-for-back-and-side-walls).

### **チャートエリアの設定**

グラフにはさまざまな種類の領域があり、Aspose.Cells では各領域の外観を柔軟に変更できます。開発者は、前景色、背景色、塗りつぶし形式などを変更して、領域にさまざまな書式設定を適用できます。

以下の例では、グラフのさまざまな種類の領域にさまざまな書式設定を適用しています。これらの分野は次のとおりです。

- プロットエリア
- チャートエリア
- [**シリーズコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)範囲
- の 1 点の面積[**シリーズコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

サンプル コードを実行すると、次のように縦棒グラフがワークシートに追加されます。

**領域が塗りつぶされた縦棒グラフ** 

![todo:画像_代替_文章](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **チャート ラインの設定**

開発者は、さまざまな種類のスタイルをラインまたはデータ マーカーに適用することもできます。[**シリーズコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)以下の例のように。サンプル コードを実行すると、以下に示すように縦棒グラフがワークシートに追加されます。

**線のスタイルを適用した後の縦棒グラフ** 

![todo:画像_代替_文章](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **Microsoft Excel 2007/2010 テーマをグラフに適用する**

開発者は、さまざまな Microsoft Excel のテーマと色を[**シリーズコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)または以下の例に示すように、他のチャート オブジェクト。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **チャートまたは軸のタイトルの設定**

以下に示すように、Microsoft Excel を使用して、WYSIWYG 環境でグラフのタイトルとその軸を設定できます。

**Microsoft Excel を使用してグラフとその軸のタイトルを設定する** 

![todo:画像_代替_文章](chart-formatting_3.png)

Aspose.Cells を使用すると、開発者はチャートのタイトルとその軸を実行時に設定することもできます。すべてのグラフとその軸には、[**Title.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text)以下の例に示すように、タイトルを設定するために使用できるメソッド。サンプル コードを実行すると、次のように縦棒グラフがワークシートに追加されます。

**タイトル設定後の縦棒グラフ** 

![todo:画像_代替_文章](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **主目盛線の設定**

#### **主目盛線を非表示にする**

開発者は、[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible)の方法[**ライン**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)物体。主なグリッド線を非表示にした後、ワークシートに追加された縦棒グラフは次のように表示されます。

**主なグリッド線が隠れている縦棒グラフ** 

![todo:画像_代替_文章](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **主目盛線の設定を変更する**

開発者は、主要なグリッド線の表示だけでなく、色などの他のプロパティも制御できます。主要なグリッド線の色を設定すると、ワークシートに追加された縦棒グラフは次のように表示されます。

**主なグリッド線が色付きの縦棒グラフ** 

![todo:画像_代替_文章](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **背面と側面の壁の境界の設定**

Microsoft Excel 2007 のリリース以降、3D グラフの壁は 2 つの部分 (側壁と後壁) に分割されているため、2 つの部分を使用する必要があります。[**壁**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls)オブジェクトはそれらを個別に表し、次を使用してアクセスできます[**Chart.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall)と[**Chart.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall).

以下の例は、さまざまな属性を使用してサイドウォールの境界を設定する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **グラフの位置とサイズを変更する**

ワークシート内の新規または既存のグラフの位置またはサイズを変更したい場合があります。 Aspose.Cells は[**Chart.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject)これを達成するためのプロパティ。そのサブプロパティを使用して、チャートのサイズを変更できます**身長**と**幅**または新しいもので再配置します**X** と**Y** 座標。

### **チャートの位置とサイズの変更**

グラフの位置 (X、Y 座標) とサイズ (高さ、幅) を変更するには、次のプロパティを使用します。

1. [**Chart.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Chart.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Chart.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Chart.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

次の例は、上記のプロパティの使用法を説明しています。最初のワークシートにグラフを含む既存のワークブックを読み込みます。次に、グラフのサイズと位置を変更し、ワークブックを保存します。

サンプル コードを実行する前のソース ファイルは次のようになります。

**サンプルコード実行前のチャートのサイズと位置** 

![todo:画像_代替_文章](chart-formatting_7.png)

実行後、出力ファイルは次のようになります。

**サンプルコード実行後のチャートのサイズと位置** 

![todo:画像_代替_文章](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **デザイナー チャートの操作**

デザイナー テンプレート ファイル内のグラフを操作または変更する必要がある場合があります。 Aspose.Cells は、デザイナー チャートのコンテンツと要素の操作を完全にサポートします。データ、グラフの内容、背景画像、および書式設定を正確に保持できます。

### **テンプレート ファイルでデザイナー チャートを操作する**

テンプレート ファイルでデザイナー チャートを操作するには、すべてのチャート関連の API 呼び出しを使用します。たとえば、[**Worksheet.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts)プロパティを使用して、テンプレート ファイル内の既存のチャート コレクションを取得します。

#### **チャートの作成**

次の例は、円グラフを作成する方法を示しています。このチャートは後で操作します。次の出力は、コードによって生成されます。

**入力円グラフ** 

![todo:画像_代替_文章](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **チャートの操作**

次の例は、既存のグラフを操作する方法を示しています。この例では、上で作成したチャートを変更します。次の出力は、コードによって生成されます。チャートのタイトルの色が青から黒に変わり、「イングランド 30000」が「英国、30K」に変更されていることに注意してください。

**円グラフが変更されました** 

![todo:画像_代替_文章](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **Designer テンプレートでの折れ線グラフの操作**

この例では、折れ線グラフを操作します。既存のチャートにいくつかのデータ シリーズを追加し、線の色を変更します。

まず、デザイナーの折れ線グラフを見てください。

**入力折れ線グラフ** 

![todo:画像_代替_文章](chart-formatting_11.png)

次に、折れ線グラフを操作します (これは、**折れ線グラフ.xls**ファイル) 次のコードを使用します。次の出力は、コードによって生成されます。

**操作された折れ線グラフ** 

![todo:画像_代替_文章](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **スパークラインの使用**

Microsoft Excel 2010 では、これまで以上にさまざまな方法で情報を分析できます。ユーザーは、新しいデータ分析および視覚化ツールを使用して、重要なデータの傾向を追跡および強調できます。スパークラインは、同じテーブルでデータとグラフを表示できるように、セル内に配置できるミニ グラフです。スパークラインを適切に使用すると、データ分析がより迅速になり、より的確になります。また、情報のシンプルなビューを提供し、多くのビジーなチャートでワークシートが過密になるのを防ぎます。

Aspose.Cells は、スプレッドシートでスパークラインを操作するための API を提供します。

### **Microsoft Excel のスパークライン**

Microsoft Excel 2010 でスパークラインを挿入するには:

1. スパークラインを表示するセルを選択します。見やすくするには、データの横にあるセルを選択します。
1. クリック**入れる**リボンで選択します**桁**の中に**スパークライン**グループ。

![todo:画像_代替_文章](chart-formatting_13.png)

1. ソース データを含むワークシートのセル範囲を選択または入力します。
グラフが表示されます。

スパークラインは、たとえばソフトボール リーグの勝敗記録などの傾向を確認するのに役立ちます。スパークラインは、リーグの各チームのシーズン全体を合計することもできます。

![todo:画像_代替_文章](chart-formatting_14.png)

### **Aspose.Cells を使用したスパークライン**

開発者は、Aspose.Cells が提供する API を使用して、スパークライン (テンプレート ファイル内) を作成、削除、または読み取ることができます。特定のデータ範囲にカスタム グラフィックを追加することにより、開発者は選択したセル領域にさまざまな種類の小さなグラフを自由に追加できます。

以下の例は、スパークライン機能を示しています。この例は、次の方法を示しています。

1. シンプルなテンプレート ファイルを開きます。
1. ワークシートのスパークライン情報を読み取ります。
1. 特定のデータ範囲の新しいスパークラインをセル領域に追加します。
1. Excel ファイルをディスクに保存します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **チャートへの 3D フォーマットの適用**

シナリオの結果だけを取得できるように、3D チャート スタイルが必要になる場合があります。 Aspose.Cells API は、この記事で説明されているように、Microsoft Excel 2007 3D 書式設定を適用するための関連する API を提供します。

### **チャートに 3D フォーマットを設定する**

グラフを作成して Microsoft Excel 2007 3D フォーマットを適用する方法を示す完全な例を以下に示します。上記のコード例を実行すると、以下に示すように、縦棒グラフ (3D 効果付き) がワークシートに追加されます。

**3D フォーマットの縦棒グラフ**

![todo:画像_代替_文章](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

サポートされている 2D チャートと 3D チャートの完全なリストについては、次を参照してください。[レンダリングでサポートされているグラフの種類](/cells/ja/java/chart-rendering/#supported-chart-types-for-rendering).

{{% /alert %}}

## **先行トピック**
- [チャートの背景塗りつぶしとして画像を設定する](/cells/ja/java/set-picture-as-background-fill-in-the-chart/)
