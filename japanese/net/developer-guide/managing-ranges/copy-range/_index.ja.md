---
title: Excel の範囲をコピーする
linktitle: 範囲をコピーする
type: docs
weight: 105
url: /ja/net/copy-ranges-of-Excel/
---

## **紹介**

Excel では、範囲を選択し、範囲をコピーし、その後、同じワークシート、他のワークシート、または他のファイルに特定のオプションで貼り付けることができます。

## **Aspose.Cells を使用して範囲をコピーする**

Aspose.Cells はいくつかのオーバーロード [Range.Copy](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy) メソッドを提供しています
および [Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/) は範囲のコピーにスタイルのみ; [Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/) は範囲の値のみをコピーします

## **範囲をコピー**

ソース範囲、ターゲット範囲を作成し、その後、Range.Copy メソッドを使用してソース範囲をターゲット範囲にコピーします。

以下のコードを参照してください:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **オプションで範囲を貼り付ける**

Aspose.Cells は特定のタイプで範囲を貼り付ける機能をサポートしています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **範囲のデータのみのコピー**
次のコードのようにRange.CopyDataメソッドを使用してデータをコピーすることもできます:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **高度なトピック**
- [ソース範囲の行の高さを宛先範囲にコピーします。](/cells/ja/net/copy-row-heights-of-source-range-to-destination-range/)


