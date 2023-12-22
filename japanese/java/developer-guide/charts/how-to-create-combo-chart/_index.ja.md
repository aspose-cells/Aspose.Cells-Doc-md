---
title: コンボチャートの作成方法
type: docs
weight: 73
url: /ja/java/create-combo-chart/
description: コンボ チャートの作成方法、折れ線グラフを含む株価チャートの追加方法、コンボ チャートの生成方法。
keywords: Add combo chart, Create stock chart with line chart, Generate combo chart, add stock chart with line chart.
---
##  **考えられる使用シナリオ**
Excel の複合グラフでは、2 つ以上のグラフの種類を簡単に組み合わせてデータを理解しやすくできるため、このオプションを利用できます。コンボ チャートは、データに価格や出来高などの複数の種類の値が含まれている場合に役立ちます。さらに、データ数値が系列ごとに大きく変化する場合にも、コンボ チャートが可能です。
次のデータセットを例にとると、これらのデータは、次のデータセットで説明したデータと非常に似ていることがわかります。[**VHCL**](https://docs.aspose.com/cells/java/create-volume-high-low-close-stock-chart/)。 「Total Revenue」に相当する series0 を折れ線グラフとして視覚化したい場合、どうすればよいでしょうか?

![todo:image_alt_text](sample.png)
##  **コンボチャート**
以下のコードを実行すると、以下に示すようなコンボ チャートが表示されます。

![todo:image_alt_text](result.png)
##  **サンプルコード**
次のサンプルコードは、[サンプル Excel ファイル](combo.xlsx)そして、[Excelファイルを出力](out.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-add-combo-chart.java" >}}
