---
title: チャートの外観の設定
linktitle: チャート形式
type: docs
weight: 20
url: /ja/net/setting-chart-appearance/
---
## **チャートの外観の設定**
チャートの作成方法では、Aspose.Cells が提供するチャートとチャート オブジェクトの種類を簡単に紹介し、作成方法を説明しました。この記事では、プロパティを設定してグラフの外観をカスタマイズする方法について説明します。

- チャートエリアの設定。
- チャート ラインの設定。
- テーマの適用。
- チャートと軸にタイトルを設定します。
- グリッド線の操作。
### **チャートエリアの設定**
グラフにはさまざまな種類の領域があり、Aspose.Cells では各領域の外観を柔軟に変更できます。開発者は、前景色、背景色、塗りつぶし形式などを変更して、領域にさまざまな書式設定を適用できます。

以下の例では、グラフのさまざまな種類の領域にさまざまな書式設定を適用しています。これらの分野は次のとおりです。

- プロットエリア
- チャートエリア
- シリーズコレクションエリア
- SeriesCollection の単一点の面積

次のコード スニペットは、グラフ エリアを設定する方法を示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
### **チャート ラインの設定**
開発者は、さまざまな種類のスタイルをラインまたはデータ マーカーに適用することもできます。[シリーズコレクション](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection).次のコード スニペットは、Aspose.Cells API を使用してチャート ラインを設定する方法を示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
### **Microsoft Excel 2007/2010 テーマをグラフに適用する**
開発者は、さまざまな Microsoft Excel テーマ/色を適用できます[シリーズコレクション](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)または以下の例に示すような他のチャート オブジェクト。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
### **チャートまたは軸のタイトルの設定**
Microsoft Excel を使用して、グラフのタイトルとその軸を WYSIWYG 環境で設定できます。 Aspose.Cells を使用すると、開発者はチャートのタイトルとその軸を実行時に設定することもできます。すべてのグラフとその軸には、[題名](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title)以下の例に示すように、タイトルを設定するために使用できるプロパティ。

次のコード スニペットは、チャートと軸にタイトルを設定する方法を示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
### **主目盛線の操作**
主なグリッド線の外観をカスタマイズすることができます。グリッド線を非表示または表示するか、色やその他の設定を定義します。以下に、グリッド線を非表示にする方法とその色を変更する方法を示します。
#### **主目盛線を非表示にする**
開発者は、[可視](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible)のプロパティ[ライン](https://reference.aspose.com/cells/net/aspose.cells.drawing/line)異議を唱える**真実**また**間違い**.

次のコード スニペットは、主要なグリッド線を非表示にする方法を示しています。主なグリッド線を非表示にした後、縦棒グラフがワークシートに追加され、グリッド線がなくなります。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
#### **主目盛線の設定を変更する**
開発者は、主要なグリッド線の可視性だけでなく、色などの他のプロパティも制御できます。

次のコード スニペットは、主要なグリッド線の色を変更する方法を示しています。主なグリッド線の色を設定すると、グリッド線が変更されたワークシートに縦棒グラフが追加されます。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

## **先行トピック**
- [チャート シリーズの値のフォーマット コードを設定する](/cells/ja/net/set-the-values-format-code-of-chart-series/)
- [チャートの背景塗りつぶしとして画像を設定する](/cells/ja/net/set-picture-as-background-fill-in-the-chart/)
