---
title: スタイル オブジェクトの再利用
type: docs
weight: 3000
url: /ja/net/reusing-style-objects/
---
{{% alert color="primary" %}}

スタイル オブジェクトを再利用すると、メモリを節約し、プログラムを高速化できます。

{{% /alert %}}

ワークシート内の広範囲のセルに書式を適用するには:

1. スタイル オブジェクトを作成します。
1. 属性を指定します。
1. 範囲内のセルにスタイルを適用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

なぜなら[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)古い Cell.Style プロパティは不要なメモリを大量に消費していましたが、Aspose.Cells 7.1.0 のリリースで削除されました。

{{% /alert %}}
