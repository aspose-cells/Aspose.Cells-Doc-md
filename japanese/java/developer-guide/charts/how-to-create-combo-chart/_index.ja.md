---
title: コンボチャートの作成方法
type: docs
weight: 73
url: /ja/java/create-combo-chart/
description: コンボチャートの作成方法、ラインチャートに株価チャートを追加する方法、コンボチャートの生成方法。
keywords: コンボチャートを追加、ラインチャートで株価チャートを作成、コンボチャートを生成、ラインチャートに株価チャートを追加。
---

## **可能な使用シナリオ**
Excelのコンボチャートを使用すると、データを理解しやすくするために複数のチャートタイプを簡単に組み合わせることができます。コンボチャートは、価格と数量などのさまざまな種類のデータを含む場合に便利です。また、データの数値が系列ごとに大幅に変動する場合にもコンボチャートが有効です。
次のデータセットを例に取ると、これらのデータは[**VHCL**](https://docs.aspose.com/cells/java/create-volume-high-low-close-stock-chart/)で言及されたデータに非常に類似していることがわかります。"総収入"に対応するseries0をラインチャートとして可視化したい場合は、どのように進めればよいでしょうか？

![todo:image_alt_text](sample.png)
## **コンボチャート**
以下のコードを実行すると、以下に示すようにコンボチャートが表示されます。

![todo:image_alt_text](result.png)
## **サンプルコード**
以下のサンプルコードは、[サンプルExcelファイル](combo.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-add-combo-chart.java" >}}
{{< app/cells/assistant language="java" >}}
