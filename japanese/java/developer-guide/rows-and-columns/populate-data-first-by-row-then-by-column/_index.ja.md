---
title: 最初に行、次に列ごとにデータを埋めます
type: docs
weight: 10
url: /ja/java/populate-data-first-by-row-then-by-column/
---

{{% alert color="primary" %}}

スプレッドシートにデータを最初に行ごと、次に列ごとに埋めると、全体のパフォーマンスが向上します。

{{% /alert %}}

## 最初に行、次に列ごとにデータを埋める

A1、B1、A2、B2の順にデータを入れることは、A1、A2、B1、B2の順よりも速くなります。ワークシートに多くのセルがある場合、データを行ごとに入力する場合、このヒントはプログラムをはるかに高速化できます。

## 行ごとに先に、次に列ごとにデータを埋めるためのJavaコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PopulateDatabyRowthenColumn-PopulateDatabyRowthenColumn.java" >}}
