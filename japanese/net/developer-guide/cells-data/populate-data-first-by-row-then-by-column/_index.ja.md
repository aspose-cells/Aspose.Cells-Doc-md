---
title: 最初に行ごと、次に列ごとにデータを入力
type: docs
weight: 1000
url: /ja/net/populate-data-first-by-row-then-by-column/
---
{{% alert color="primary" %}} 

最初に行ごと、次に列ごとにスプレッドシートにデータを入力すると、全体的なパフォーマンスが向上します。

{{% /alert %}} 

A1、B1、A2、B2 の順序でデータを配置する方が、A1、A2、B1、B2 よりも高速です。ワークシートに多数のセルがあり、2 番目の手順に従う場合、つまり行ごとにデータを入力する場合、このヒントを使用すると、プログラムを大幅に高速化できます。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-PopulateDataEfficiently-PopulateDataFirstByRowThenColumns.cs" >}}
