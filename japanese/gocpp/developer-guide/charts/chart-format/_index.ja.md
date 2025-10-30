---
title: GolangをC++経由で使用した場合のチャートの外観設定
linktitle: チャートの形式
description: Aspose.Cells for C++でグラフの外観を設定する方法を学びます。レイアウト、色、フォント、エフェクトのカスタマイズ方法を紹介し、望ましいビジュアルスタイルを実現し、ワークシートを向上させます。
keywords: Aspose.Cells for C++、グラフ作成、グラフの外観、レイアウト、色、フォント、エフェクト、ワークシート
type: docs
weight: 20
url: /ja/go-cpp/setting-chart-appearance/
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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat.go" >}}
### **チャートラインの設定**
[SeriesCollection](https://reference.aspose.com/cells/go-cpp/seriescollection/)のラインやデータマーカーに対してさまざまなスタイルを適用できます。以下のコードスニペットは、Aspose.Cells APIを使用してチャートラインを設定する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-1.go" >}}
### **Microsoft Excel 2007/2010のテーマをチャートに適用**
開発者はまた、[SeriesCollection](https://reference.aspose.com/cells/go-cpp/seriescollection/)や他のチャートオブジェクトに対してMicrosoft Excelのテーマや色を適用できます。以下の例に示す方法です。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-2.go" >}}
### **チャートや軸のタイトルの設定**
Microsoft Excelを使用して、チャートと軸のタイトルをWYSIWYG環境で設定できます。Aspose.Cellsはまた、開発者がチャートと軸のタイトルを実行時に設定できるようにします。すべてのチャートとその軸には [Title](https://reference.aspose.com/cells/go-cpp/title/) プロパティがあり、これを使用してタイトルを設定できます。例を以下に示します。

次のコードスニペットは、チャートや軸にタイトルを設定する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-3.go" >}}
### **主な目盛りの操作**
主な目盛りの外観をカスタマイズできます。目盛りを非表示にしたり表示したり、その色やその他の設定を定義できます。以下では、目盛りを非表示にする方法と色を変更する方法を説明します。

#### **メジャーグリッドラインの非表示**
開発者は、[Line](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/line/) オブジェクトの [IsVisible](https://reference.aspose.com/cells/go-cpp/line/isvisible/) プロパティを **true** または **false** に設定することで、主要なグリッド線の可視性を制御できます。

次のコードスニペットは、メジャーグリッド線を非表示にする方法を示しています。メジャーグリッド線を非表示にした後、ワークシートに列のチャートが追加され、グリッド線がありません。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-4.go" >}}
#### **メジャーグリッドラインの設定変更**
開発者は、メジャーグリッド線の可視性だけでなく、色などの他のプロパティも制御できます。

次のコードスニペットは、メジャーグリッド線の色を変更する方法を示しています。メジャーグリッド線の色を設定した後、ワークシートに変更されたグリッド線を持つ列チャートが追加されます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-5.go" >}}
## **高度なトピック**
- [チャートシリーズの値の形式コードを設定する](/cells/ja/cpp/set-the-values-format-code-of-chart-series/)
- [グラフの背景に画像を設定する](/cells/ja/cpp/set-picture-as-background-fill-in-the-chart/)
