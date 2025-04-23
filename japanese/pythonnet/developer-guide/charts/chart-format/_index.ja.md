---
title: チャートの外観を設定する
description: Aspose.Cells for Python via .NETでのチャートの外観の設定方法について学びます。チャートのレイアウト、色、フォント、エフェクトを変更して、望ましいビジュアルスタイルを実現し、ワークシートを強化します。
keywords: Aspose.Cells for Python via .NET、チャート作成、外観、レイアウト、色、フォント、エフェクト、ワークシート。
linktitle: チャートの形式
type: docs
weight: 20
url: /ja/python-net/setting-chart-appearance/
---

## **グラフの外観設定**
「チャートの作成方法」では、Aspose.Cells for Python via .NETが提供するチャートタイプの概要と、それらを作成・カスタマイズしてワークシートを強化する方法について説明しました。この記事では、これらのプロパティを設定してチャートの外観をカスタマイズする方法について詳述します。

- チャートエリアの設定。
- チャートラインの設定。
- テーマの適用。
- チャートと軸のタイトルの設定。
- グリッド線の操作。
### **チャートエリアの設定**
チャートにはさまざまな種類があり、Aspose.Cells for Python via .NETは各種の外観を変更する柔軟性を提供します。開発者は、前景色、背景色、塗りつぶし形式などを変更することで、それぞれのエリアの書式設定を適用できます。

以下の例では、チャートの異なる種類のエリアに異なる書式設定を適用しました。

- プロットエリア
- チャートエリア
- SeriesCollectionエリア
- SeriesCollection内の単一のポイントのエリア

以下のコードスニペットは、チャートエリアを設定する方法を示しています。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingChartArea-1.py" >}}

### **チャートラインの設定**
開発者はまた、[SeriesCollection](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)の線やデータマーカーに異なるスタイルを適用することも可能です。以下のコードスニペットは、Aspose.Cells for Python via .NET APIを使用してチャートの線を設定する方法を示しています。


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingChartLines-1.py" >}}

### **Microsoft Excel 2007/2010のテーマをチャートに適用**
開発者は、[SeriesCollection](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)や他のチャートオブジェクトにMicrosoft Excelのテーマや色を適用できます。以下の例に示す通りです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-ApplyingThemes-1.py" >}}

### **チャートや軸のタイトルの設定**
Microsoft Excelを使って、チャートや軸のタイトルをWYSIWYG環境で設定できます。Aspose.Cells for Python via .NETでは、開発者が実行時にチャートや軸のタイトルを設定することも可能です。すべてのチャートと軸は [Chart.title](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/title) プロパティを持ち、それを使用してタイトルを設定できます。例を次に示します。

次のコードスニペットは、チャートや軸にタイトルを設定する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingTitlesAxes-1.py" >}}

### **主な目盛りの操作**
主な目盛りの外観をカスタマイズできます。目盛りを非表示にしたり表示したり、その色やその他の設定を定義できます。以下では、目盛りを非表示にする方法と色を変更する方法を説明します。

#### **メジャーグリッドラインの非表示**
開発者は、[Line](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/line) オブジェクトの [is_visible](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/line/is_visible) プロパティを **true** または **false** に設定して、主要なグリッド線の表示/非表示を制御できます。

次のコードスニペットは、メジャーグリッド線を非表示にする方法を示しています。メジャーグリッド線を非表示にした後、ワークシートに列のチャートが追加され、グリッド線がありません。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-MajorGridlines-1.py" >}}

#### **メジャーグリッドラインの設定変更**
開発者は、メジャーグリッド線の可視性だけでなく、色などの他のプロパティも制御できます。

次のコードスニペットは、メジャーグリッド線の色を変更する方法を示しています。メジャーグリッド線の色を設定した後、ワークシートに変更されたグリッド線を持つ列チャートが追加されます。


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-ChangingMajorGridlines-1.py" >}}

## **高度なトピック**
- [チャートシリーズの値の形式コードを設定する](/cells/ja/python-net/set-the-values-format-code-of-chart-series/)
- [グラフの背景に画像を設定する](/cells/ja/python-net/set-picture-as-background-fill-in-the-chart/)
