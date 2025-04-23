---
title: スタイル付きの範囲のデータをコピーします。
type: docs
weight: 340
url: /ja/java/copy-range-data-with-style/
---

{{% alert color="primary" %}} 

[Copy Range Data Only](/cells/ja/java/copy-range-data-only/)では、セル範囲から別の範囲にデータをコピーする方法について説明しています。Aspose.Cellsでは、書式を含めた範囲をコピーすることもできます。この記事ではその方法を説明します。

{{% /alert %}} 
## **スタイルで範囲データをコピー**
Aspose.Cellsは、範囲を操作するためのさまざまなクラスとメソッドを提供します。例として、[createRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-)、[StyleFlag](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)、[applyStyle()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-)などがあります。

この例:

1. ワークブックを作成します。
1. 最初のワークシートのいくつかのセルにデータを入力します。
1. 範囲を作成します。
1. 指定された書式属性を持つスタイルオブジェクトを作成します。
1. データ範囲にスタイルを適用します。
1. 別のセルの範囲を作成します。
1. 最初の範囲から2番目の範囲にデータと書式をコピーします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

{{< app/cells/assistant language="java" >}}
