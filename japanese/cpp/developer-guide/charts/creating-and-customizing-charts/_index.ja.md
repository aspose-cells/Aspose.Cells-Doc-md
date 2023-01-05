---
title: グラフの作成とカスタマイズ
type: docs
weight: 10
url: /ja/cpp/creating-and-customizing-charts/
---
## **考えられる使用シナリオ**

チャートは、情報を視覚的に表示するものです。 Aspose.Cells を使用すると、開発者は Microsoft Excel と同じようにチャートで情報を視覚化できます。チャートで情報を提示することは、意思決定者が迅速かつタイムリーに意思決定を行うのに常に役立ちます。生の数値よりもグラフを使用すると、データの比較、パターン、および傾向をすばやく確認するのが簡単になります。スプレッドシートのデータに基づいて実行時にグラフを作成することは、Aspose.Cells' の便利な機能の 1 つです。 Aspose.Cells は、標準チャートとカスタマイズ チャートの両方の作成をサポートします。以下に、Aspose.Cells API を使用していくつかの一般的な MS-Excel グラフ タイプを作成する方法について、サンプル ファイルを使用していくつかの例を示します。

## **ピラミッドチャート**

サンプル コードを実行すると、ピラミッド チャートがワークシートに追加されます。をご覧ください[出力エクセルファイル](66519068.xlsx)以下のサンプルコードの.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart.cpp" >}}

## **折れ線グラフ**

上記の例では、単純に[**グラフの種類**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70)に[**ChartType_Line**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70ad12ff1561ab1424a0c3095b6dc07ac25)折れ線グラフを作成します。完全なソースを以下に示します。コードが実行されると、折れ線グラフがワークシートに追加されます。をご覧ください[出力エクセルファイル](66519069.xlsx)以下のサンプルコードの.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart.cpp" >}}

## **バブル チャート**

バブル チャートを作成するには、[**グラフの種類**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70)に設定する必要があります[**ChartType_Bubble**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70a5efa533b454f9415e4497dbb2ab28b3d)および次のようないくつかの追加プロパティ[**SetBubbleSizes**](https://reference.aspose.com/cells/cpp/class/aspose.cells.charts.i_series#a00cf890ba7ab419d31a522ab52b02e9d) & [**SetXValues**](https://reference.aspose.com/cells/cpp/class/aspose.cells.charts.i_series#a788ff4aa51dbf9bed5327298af93a6db)それに応じて設定する必要があります。次のコードを実行すると、バブル チャートがワークシートに追加されます。をご覧ください[出力エクセルファイル](66519070.xlsx)以下のサンプルコードの.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart.cpp" >}}

## **カスタム グラフの作成**

これまでグラフについて説明してきたとき、独自の標準書式設定を持つ標準グラフを見てきました。データ ソースを定義し、いくつかのプロパティを設定するだけで、チャートはデフォルトのフォーマット設定で作成されます。ただし、Aspose.Cells API は、開発者が独自の形式設定でチャートを作成できるようにするカスタム チャートの作成もサポートしています。開発者は、実行時に Aspose.Cells を使用してカスタム グラフを作成できます。

グラフはデータ系列で構成されています。カスタム グラフを作成する場合、開発者はさまざまなデータ シリーズにさまざまな種類のグラフを自由に使用できます。

以下のコード例は、カスタム グラフを作成する方法を示しています。この例では、最初のデータ系列に縦棒グラフを使用し、2 番目の系列に折れ線グラフを使用します。その結果、折れ線グラフと組み合わせた縦棒グラフがワークシートに追加されます。をご覧ください[出力エクセルファイル](66519071.xlsx)以下のサンプルコードの.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart.cpp" >}}
