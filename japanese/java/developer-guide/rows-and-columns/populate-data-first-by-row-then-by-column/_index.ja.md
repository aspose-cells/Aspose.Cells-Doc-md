---
title: 最初に行ごと、次に列ごとにデータを入力
type: docs
weight: 10
url: /ja/java/populate-data-first-by-row-then-by-column/
---
{{% alert color="primary" %}}

最初に行ごと、次に列ごとにスプレッドシートにデータを入力すると、全体的なパフォーマンスが向上します。

{{% /alert %}}

## 最初に行ごと、次に列ごとにデータを入力

A1、B1、A2、B2 の順序でデータを配置する方が、A1、A2、B1、B2 よりも高速です。ワークシートに多数のセルがあり、2 番目の手順に従う場合、つまり行ごとにデータを入力する場合、このヒントを使用すると、プログラムを大幅に高速化できます。

## Java 最初に行ごと、次に列ごとにデータを入力するコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PopulateDatabyRowthenColumn-PopulateDatabyRowthenColumn.java" >}}
