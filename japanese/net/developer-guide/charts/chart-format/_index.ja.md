---
title: チャートの外観の設定
description: Aspose.Cells for .NET でグラフの外観を構成する方法を学習します。このガイドでは、グラフのレイアウト、色、フォント、効果を変更して、目的の視覚スタイルを実現し、ワークシートを強化する方法を説明します。
keywords: Aspose.Cells for .NET, charting, chart appearance, layouts, colors, fonts, effects, worksheets.
linktitle: グラフの形式
type: docs
weight: 20
url: /ja/net/setting-chart-appearance/
---
##  **チャートの外観の設定**
「チャートの作成方法」では、Aspose.Cells が提供するチャートとチャート オブジェクトの種類を簡単に紹介し、その作成方法について説明しました。この記事では、プロパティを設定してグラフの外観をカスタマイズする方法について説明します。

- チャートエリアの設定。
- チャートの線を設定します。
- テーマの適用。
- グラフと軸にタイトルを設定します。
- グリッド線の操作。
###  **チャートエリアの設定**
グラフにはさまざまな種類の領域があり、Aspose.Cells を使用すると、各領域の外観を柔軟に変更できます。開発者は、前景色、背景色、塗りつぶし形式などを変更することで、領域にさまざまな書式設定を適用できます。

以下の例では、グラフのさまざまな種類の領域にさまざまな書式設定を適用しています。これらの領域には次のものが含まれます。

- プロットエリア
- チャートエリア
- シリーズコレクションエリア
- SeriesCollection 内の単一点の面積

次のコード スニペットは、グラフ領域を設定する方法を示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
###  **チャートの線の設定**
開発者は、ラインやデータ マーカーにさまざまな種類のスタイルを適用することもできます。[シリーズコレクション](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)。次のコード スニペットは、Aspose.Cells API を使用してグラフの線を設定する方法を示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
###  **Microsoft Excel 2007/2010 テーマをグラフに適用する**
開発者は、さまざまな Microsoft Excel テーマ/色を適用できます。[シリーズコレクション](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)または、以下の例に示すような他のチャート オブジェクト。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
###  **グラフまたは軸のタイトルの設定**
Microsoft Excel を使用して、WYSIWYG 環境でグラフのタイトルとその軸を設定できます。 Aspose.Cells を使用すると、開発者は実行時にグラフのタイトルとその軸を設定できます。すべてのグラフとその軸には、[タイトル](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title)以下の例に示すように、タイトルを設定するために使用できるプロパティ。

次のコード スニペットは、グラフと軸にタイトルを設定する方法を示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
###  **主なグリッド線の操作**
主要なグリッド線の外観をカスタマイズすることができます。グリッド線を表示または非表示にしたり、その色やその他の設定を定義したりできます。以下に、グリッド線を非表示にする方法とその色を変更する方法を示します。
####  **主なグリッド線を非表示にする**
開発者は、主要なグリッド線の表示を制御できます。[見える](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible)の財産[ライン](https://reference.aspose.com/cells/net/aspose.cells.drawing/line)に反対する**真実**または *偽**。

次のコード スニペットは、主グリッド線を非表示にする方法を示しています。主グリッド線を非表示にすると、グリッド線のない縦棒グラフがワークシートに追加されます。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
####  **大グリッド線の設定を変更する**
開発者は、主要グリッド線の表示設定だけでなく、その色などの他のプロパティも制御できます。

次のコード スニペットは、主グリッド線の色を変更する方法を示しています。主グリッド線の色を設定すると、グリッド線が変更された縦棒グラフがワークシートに追加されます。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

##  **アドバンストトピック**
- [グラフシリーズの値フォーマットコードを設定する](/cells/ja/net/set-the-values-format-code-of-chart-series/)
- [画像を背景として設定する グラフに記入する](/cells/ja/net/set-picture-as-background-fill-in-the-chart/)
