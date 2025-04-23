---
title: チャートの外観を設定する
description: Aspose.Cells for .NETでチャートの外観を構成する方法を学ぶ。私たちのガイドでは、望むビジュアルスタイルを実現し、ワークシートを強化するためにチャートのレイアウト、色、フォント、効果を変更する方法を示します。
keywords: Aspose.Cells for .NET, チャート作成, チャート外観, レイアウト, 色, フォント, 効果, ワークシート。
linktitle: チャートの形式
type: docs
weight: 20
url: /ja/net/setting-chart-appearance/
---

## **グラフの外観設定**
チャートの作成方法では、Aspose.Cellsが提供するチャートの種類やオブジェクトについて簡単に紹介し、それらの作成方法について説明しました。この記事では、プロパティを設定してチャートの外観をカスタマイズする方法について説明します。

- チャートエリアの設定。
- チャートラインの設定。
- テーマの適用。
- チャートと軸のタイトルの設定。
- グリッド線の操作。
### **チャートエリアの設定**
チャートには異なる種類のエリアがあり、Aspose.Cellsは各エリアの外観を変更する柔軟性を提供します。開発者は、前景色、背景色、塗りつぶし形式などの異なる書式設定をエリアに適用して、その外観を変更できます。

以下の例では、チャートの異なる種類のエリアに異なる書式設定を適用しました。

- プロットエリア
- チャートエリア
- SeriesCollectionエリア
- SeriesCollection内の単一のポイントのエリア

以下のコードスニペットは、チャートエリアを設定する方法を示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
### **チャートラインの設定**
開発者は、Aspose.Cells APIを使用して、[SeriesCollection](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)のラインやデータマーカーに異なるスタイルを適用することもできます。以下のコードスニペットは、Aspose.Cells APIを使用してチャートラインを設定する方法を示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
### **Microsoft Excel 2007/2010のテーマをチャートに適用**
開発者は、[SeriesCollection](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) やその他のチャートオブジェクトに異なるMicrosoft Excelのテーマ/色を適用できます。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
### **チャートや軸のタイトルの設定**
Microsoft Excelを使用してチャートおよびその軸のタイトルをWYSIWYG環境で設定することができます。Aspose.Cellsでは、開発者がランタイムでチャートおよびその軸のタイトルを設定することも可能です。すべてのチャートおよびその軸には、タイトルを設定するために使用できる[Title](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title)プロパティが含まれています。以下に示すように、以下はそれを示す一例です。

次のコードスニペットは、チャートや軸にタイトルを設定する方法を示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
### **主な目盛りの操作**
主な目盛りの外観をカスタマイズできます。目盛りを非表示にしたり表示したり、その色やその他の設定を定義できます。以下では、目盛りを非表示にする方法と色を変更する方法を説明します。
#### **メジャーグリッドラインの非表示**
開発者は、[Line](https://reference.aspose.com/cells/net/aspose.cells.drawing/line) オブジェクトの[IsVisible](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) プロパティを**true**または**false**に設定することで、主な目盛りの表示/非表示を制御できます。

次のコードスニペットは、メジャーグリッド線を非表示にする方法を示しています。メジャーグリッド線を非表示にした後、ワークシートに列のチャートが追加され、グリッド線がありません。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
#### **メジャーグリッドラインの設定変更**
開発者は、メジャーグリッド線の可視性だけでなく、色などの他のプロパティも制御できます。

次のコードスニペットは、メジャーグリッド線の色を変更する方法を示しています。メジャーグリッド線の色を設定した後、ワークシートに変更されたグリッド線を持つ列チャートが追加されます。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

## **高度なトピック**
- [チャートシリーズの値の形式コードを設定する](/cells/ja/net/set-the-values-format-code-of-chart-series/)
- [グラフの背景に画像を設定する](/cells/ja/net/set-picture-as-background-fill-in-the-chart/)
{{< app/cells/assistant language="csharp" >}}
