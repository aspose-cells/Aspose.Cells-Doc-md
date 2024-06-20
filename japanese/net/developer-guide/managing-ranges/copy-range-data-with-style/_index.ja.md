---
title: スタイル付きの範囲のデータをコピーします。
type: docs
weight: 610
url: /ja/net/copy-range-data-with-style/
---

{{% alert color="primary" %}}

[Copy Range Data Only](/cells/ja/net/copy-range-data-only/)は、セルの範囲から別の範囲にデータをコピーする方法について説明しており、具体的には新しいスタイルセットをコピーしたセルに適用しました。Aspose.Cellsは書式付きで範囲をコピーすることもできます。この記事ではその方法について説明します。

{{% /alert %}}

Aspose.Cellsは、範囲を操作するためのさまざまなクラスやメソッドを提供しています。例えば、[**CreateRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index)、[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)、[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle)などがあります。

この例:

1. ワークブックを作成します。
1. 最初のワークシートのいくつかのセルにデータを入力します。
1. [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)を作成します。
1. 指定した書式属性で[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトを作成します。
1. データ範囲にスタイルを適用します。
1. 別のセルの範囲を作成します。
1. 最初の範囲から2番目の範囲にデータと書式をコピーします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
