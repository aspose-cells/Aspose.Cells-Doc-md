---
title: スタイル付きの範囲データをコピー
type: docs
weight: 610
url: /ja/net/copy-range-data-with-style/
---
{{% alert color="primary" %}}

[範囲データのみをコピー](/cells/ja/net/copy-range-data-only/)セルの範囲から別の範囲にデータをコピーする方法を説明しました。具体的には、コピーしたセルに新しいスタイル セットを適用しました。 Aspose.Cells は、書式を設定した範囲をコピーすることもできます。この記事では、その方法について説明します。

{{% /alert %}}

Aspose.Cells は、範囲を操作するためのさまざまなクラスとメソッドを提供します。たとえば、[**CreateRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**スタイルフラグ**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)と[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

この例:

1. ワークブックを作成します。
1. 最初のワークシートの多数のセルにデータを入力します。
1. を作成します[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. を作成します[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)指定されたフォーマット属性を持つオブジェクト。
1. スタイルをデータ範囲に適用します。
1. セルの 2 番目の範囲を作成します。
1. 最初の範囲から 2 番目の範囲に書式設定されたデータをコピーします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
