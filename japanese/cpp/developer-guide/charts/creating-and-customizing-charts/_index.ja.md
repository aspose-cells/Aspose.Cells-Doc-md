---
title: チャートの作成とカスタマイズ
type: docs
weight: 10
url: /ja/cpp/creating-and-customizing-charts/
---

## **可能な使用シナリオ**

チャートは情報を視覚的に表示するものです。Aspose.Cellsを使用すると、Microsoft Excelと同様にチャートを使用して情報を視覚化することができます。情報をチャートで表現することは、意思決定者が迅速かつタイムリーな決定を下すのに役立ちます。チャートを使用すると、生の数字よりも比較やパターン、データの傾向を素早く把握することができます。スプレッドシートのデータに基づいてランタイムでチャートを作成することは、Aspose.Cellsの有用な機能の1つです。Aspose.Cellsは、標準チャートとカスタマイズされたチャートの両方を作成することをサポートしています。以下では、Aspose.Cells APIを使用して一般的なMS-Excelのチャートの作成方法についていくつかの例を示します。

## **ピラミッドチャート**

例のコードを実行すると、ワークシートにピラミッドチャートが追加されます。次のサンプルコードの出力Excelファイル(66519068.xlsx)を参照してください。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

## **折れ線グラフ**

上記の例では、[**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)を**`ChartType::Line`**に変更すると折れ線グラフが作成されます。完全なソースは以下に示します。コードを実行すると、折れ線グラフがワークシートに追加されます。次のサンプルコードの出力Excelファイル(66519069.xlsx)を参照してください。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

## **バブルチャート**

バブルチャートを作成するには、[**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)を**`ChartType_Bubble`**に設定し、[**SetBubbleSizes**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/)と[**SetXValues**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/)などの追加のプロパティを適切に設定する必要があります。以下のコードを実行すると、バブルチャートがワークシートに追加されます。次のサンプルコードの出力Excelファイル(66519070.xlsx)を参照してください。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

## **カスタムチャートの作成**

これまでに標準チャートについて見てきましたが、標準のフォーマット設定があるチャートです。データソースを定義し、いくつかのプロパティを設定するだけで、チャートはデフォルトのフォーマット設定で作成されます。しかし、Aspose.Cells APIは、開発者が独自のフォーマット設定でチャートを作成できるカスタムチャートもサポートしています。Aspose.Cellsを使用して、開発者は独自のフォーマット設定でランタイムでカスタムチャートを作成することができます。

チャートはデータシリーズから構成されています。カスタムチャートを作成するとき、開発者は異なる種類のチャートを異なるデータシリーズに使用する自由があります。

以下の例のコードは、カスタムチャートの作成方法を示しています。この例では、最初のデータシリーズには列チャート、2番目のシリーズには折れ線グラフを使用します。その結果、ワークシートには列チャートと折れ線グラフが組み合わされたチャートが追加されます。以下のサンプルコードの出力Excelファイル(66519071.xlsx)を参照してください。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
