---
title: グラフの作成とカスタマイズ
type: docs
weight: 10
url: /ja/cpp/creating-and-customizing-charts/
---
##  **考えられる使用シナリオ**

チャートは情報を視覚的に表示したものです。 Aspose.Cells を使用すると、開発者は Microsoft Excel と同じように情報をグラフで視覚化できます。情報をグラフで表示することは、意思決定者が迅速かつタイムリーな意思決定を行うのに常に役立ちます。生の数値よりもグラフを使用すると、データの比較、パターン、傾向をすぐに確認するのが簡単になります。スプレッドシート内のデータに基づいて実行時にグラフを作成することは、Aspose.Cells の便利な機能の 1 つです。 Aspose.Cells は、標準グラフとカスタマイズされたグラフの両方の作成をサポートしています。以下では、Aspose.Cells API を使用していくつかの一般的な MS-Excel グラフ タイプを作成する方法について、サンプル ファイルを使用していくつかの例を示します。

##  **ピラミッドチャート**

サンプル コードを実行すると、ピラミッド グラフがワークシートに追加されます。をご覧ください。[Excelファイルを出力](66519068.xlsx)以下のサンプルコードです。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

##  **折れ線グラフ**

上記の例では、単純に[**グラフの種類**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)に**`ChartType::Line`**折れ線グラフを作成します。完全なソースは以下に提供されます。コードが実行されると、折れ線グラフがワークシートに追加されます。をご覧ください。[Excelファイルを出力](66519069.xlsx)以下のサンプルコードです。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

##  **バブルチャート**

バブル チャートを作成するには、[**グラフの種類**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)に設定する必要があります**`チャートタイプ_バブル`**そしていくつかの追加のプロパティ[**バブルサイズの設定**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/) & [**SetXValues**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/)それに応じて設定する必要があります。次のコードを実行すると、バブル チャートがワークシートに追加されます。をご覧ください。[Excelファイルを出力](66519070.xlsx)以下のサンプルコードです。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

##  **カスタムチャートの作成**

これまでグラフについて説明してきたとき、独自の標準書式設定を持つ標準グラフを見てきました。データ ソースを定義し、いくつかのプロパティを設定するだけで、デフォルトの形式設定でグラフが作成されます。ただし、Aspose.Cells API は、開発者が独自の形式設定でグラフを作成できるカスタム グラフの作成もサポートしています。開発者は、Aspose.Cells を使用して実行時にカスタム グラフを作成できます。

チャートはデータ系列で構成されます。カスタム グラフを作成する場合、開発者はさまざまなデータ シリーズに対してさまざまなタイプのグラフを自由に使用できます。

以下のコード例は、カスタム グラフの作成方法を示しています。この例では、最初のデータ系列に縦棒グラフを使用し、2 番目のデータ系列に折れ線グラフを使用します。その結果、折れ線グラフと組み合わせた縦棒グラフがワークシートに追加されます。をご覧ください。[Excelファイルを出力](66519071.xlsx)以下のサンプルコードです。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
