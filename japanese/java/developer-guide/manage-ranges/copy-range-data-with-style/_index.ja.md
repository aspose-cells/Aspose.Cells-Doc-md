---
title: スタイル付きの範囲データをコピー
type: docs
weight: 340
url: /ja/java/copy-range-data-with-style/
---
{{% alert color="primary" %}} 

[範囲データのみをコピー](/cells/ja/java/copy-range-data-only/)セルの範囲から別の範囲にデータをコピーする方法を説明しました。 Aspose.Cells は、書式を設定した範囲をコピーすることもできます。この記事では、その方法について説明します。

{{% /alert %}} 
## **スタイル付きの範囲データをコピー**
Aspose.Cells は、範囲を操作するためのさまざまなクラスとメソッドを提供します。たとえば、[createRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), [スタイルフラグ](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), [applyStyle()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle\(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag\)）など

この例:

1. ワークブックを作成します。
1. 最初のワークシートの多数のセルにデータを入力します。
1. 範囲を作成します。
1. 指定されたフォーマット属性を持つスタイル オブジェクトを作成します。
1. スタイルをデータ範囲に適用します。
1. セルの 2 番目の範囲を作成します。
1. 最初の範囲から 2 番目の範囲に書式設定されたデータをコピーします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

